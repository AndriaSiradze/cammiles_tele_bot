from aiogram import Bot, types, Dispatcher, executor
from data import write_db, check_data, read_db


"""
Task send photos with link 
"""
# creating a bot
GALLERY_ID = -624404815
TOKEN = "5285656641:AAFxlXEQQ8Q1YZtUKpICv95xjPsAn7a8yF0"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

file_ids = {}
caption = None


@dp.message_handler(commands=['start', 'help'])
async def start_com(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Hello it's cammiles galley bot you need to type hashtag and i will sen ypu photos from "
                           "camilles libray")


@dp.message_handler(lambda message: message.chat.id == GALLERY_ID,
                    content_types='photo')
async def get_img(message):
    """
    сохраняет file_id чтобы в будущем пересылать фотографии
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


@dp.message_handler(lambda message: message.text and "#" in message.text, content_types=['text'])
async def give_photo(message: types.Message):
    """
    Здесь будет отправлять фото по запросу пользователя
    """
    pass


@dp.message_handler(lambda message: message.text == 'check data')
async def check_id(message: types.Message):
    await bot.send_message(message.from_user.id, check_data())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
