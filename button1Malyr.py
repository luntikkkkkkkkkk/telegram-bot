import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

logging.basicConfig(level=logging.INFO)

bot = Bot("7241614496:AAHElnPsH_Qovm6GXN1A3VO6cnvxZ4MoxMk")

dp = Dispatcher()

@dp.message(F.text.lower() == "товары для маляров")
async def goods_for_painters(message: types.Message):
    
    
    
    
    
    
    await message.reply("Внизу представлен каталог товаров для маляров")


