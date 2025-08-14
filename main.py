import asyncio
import logging
from aiogram import Bot
from db import create_table
from handlers import dp

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
API_TOKEN = # "Ваш токен бота"
bot = Bot(token=API_TOKEN)


async def main():
    # Создаем таблицу в базе данных, если она еще не существует
    await create_table()
    # Запускаем процесс опроса (polling) для обработки входящих сообщений
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
