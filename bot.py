from aiogram import executor
from handlers import admin, client, other
from create_bot import dp


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
