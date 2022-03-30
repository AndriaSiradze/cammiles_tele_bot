from aiogram import Bot, types, Dispatcher, executor
from create_bot import bot, dp
from data import check_data


@dp.message_handler(lambda message: message.text == 'check data')
async def check_id(message: types.Message):
    """
    showing data with img urls
    """
    await bot.send_message(message.from_user.id, check_data())
