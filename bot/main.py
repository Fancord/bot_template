import asyncio
import logging
import sys

from aiogram import (
	Bot,  # What commands
	Dispatcher,  # Take updates
	types,  # Load the bot and execute a functions
)
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from dotenv import dotenv_values

config = dotenv_values("./config/.env")

API_TOKEN = config["API_TOKEN"]

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
	await message.answer(f"Здароў! {hbold(message.from_user.full_name)}")


@dp.message()
async def echo_handler(message: types.Message) -> None:
	try:
		await message.send_copy(chat_id=message.chat.id)
	except TypeError:
		await message.answer("Ня дурна!")


async def main() -> None:
	bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
	await dp.start_polling(bot)



if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	asyncio.run(main())