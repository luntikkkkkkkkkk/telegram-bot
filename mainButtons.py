import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7241614496:AAHElnPsH_Qovm6GXN1A3VO6cnvxZ4MoxMk")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Товары для маляров")],
        [types.KeyboardButton(text="Саморезы, винты, гайки, шурупы")],
        [types.KeyboardButton(text="Электроника")]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard = kb,
        resize_keyboard = True,
        input_field_placeholder = "Выберите категорию товаров"
    )
    
    
    
    
    await message.answer("Привет! Я бот- маркет с хозтоварами. Выбери внизу нужную категорию.", reply_markup=keyboard)











async def main():
    await dp.start_polling(bot)

if __name__== "__main__":
    asyncio.run(main())
