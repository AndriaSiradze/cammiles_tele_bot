from aiogram import types
from create_bot import bot, dp
from data import write_db, show_names, get_ids

caption = None  # need to always have caption because some message ==  caption is none
GALLERY_ID = -624404815
file_ids = {}


@dp.message_handler(commands=['start', 'help'])
async def start_com(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Hello it's Camilles galley bot \nYou need to type hashtag and i will send you photos from "
                           "Camilles gallery\n"
                           "If you wanna see what we have in gallery type /show")


@dp.message_handler(lambda message: message.chat.id == GALLERY_ID,
                    content_types='photo')
async def get_img(message):
    """
    сохраняет file_id чтобы в будущем пересылать фотографии.
    if message.caption:
    если есть caption != None значи что это новая группа фотографий
    caption = Ключь к id в data base
    """
    global caption  # need to always have caption because some message caption is none
    file_id = dict(message.photo[0])['file_id']
    if message.caption:
        caption = message.caption
    # making dict where keys is hashtags and values is file ids
    if caption in file_ids.keys():
        file_ids[caption].append(file_id)
    else:
        file_ids[caption] = [file_id]
    write_db(file_ids)  # writing in data base
    file_ids.clear()


@dp.message_handler(commands=['show'])
async def show_gallery(message: types.Message):
    """
    Проказывает альбомы которые есть в галерее
    """
    gallery = "\n".join(show_names())
    text = f"""Hello type #hashtag which one you wanna see and i will send you gallery \n
    This is what we have :  
    {gallery}
"""
    await bot.send_message(message.from_user.id, text)


@dp.message_handler(lambda message: message.text and "#" in message.text, content_types=['text'])
async def give_photo(message: types.Message):
    """
    Здесь будет отправлять фото по запросу пользователя
    """
    gallery = show_names()
    if message.text in gallery:
        photo_ids = get_ids(message.text)
        for photo in photo_ids:
            await bot.send_photo(message.from_user.id, photo)
    else:
        bot.send_message(message.from_user.id, "Sorry it's wrong hashtag")
