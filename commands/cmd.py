import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode


logging.basicConfig(level=logging.INFO)

bot = Bot("7080348418:AAErQoWem3850SAEd43T2r5f-beJP3_kbkg")

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, Hello, <b> {message.from_user.full_name} </b>"
                         "! Это бот, который ты можешь добавить в чат и соревноваться там у кого будут длиннее волосы."
                         "Все просто: ты должен каждый день заходить в чат и прописывать команду /grow и твои волосы вырастут."
                         "Но может быть так, что твои волосы сократятся и ты будешь лохом. Также вы можете оформить подписку,"
                         "тогда ежедневно ваши отращенные волосы будут удвоены, а еще вы будете закреплены в описании бота."
                         "Если вы заметили баги и тп, то пишите лунтику, тоесть мне."
                         "На админа денег нет, если кто-то купит подписку, то открою вакансию админа-поддержки.", parse_mode=ParseMode.HTML
                         )



@dp.message(Command('grow'))
async def cmd_grow(message: types.Message):
    itog = 0
    if itog == 0:
       size = random.randint(1, 10)
    else:
        size = random.randint(-10, 10)
    itog += size
    await message.answer(f"Ваши волосы выросли на {size} см. Теперь ваши волосы {itog} см. Следующая попытка завтра. ")










async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())