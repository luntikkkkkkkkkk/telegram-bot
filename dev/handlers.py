from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types

dp = Dispsatcher


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, Hello, <b> {message.from_user.full_name} </b>"
                         "! Это бот, который ты можешь добавить в чат и соревноваться там у кого будут длиннее волосы."
                         "Все просто: ты должен каждый день заходить в чат и прописывать команду /grow и твои волосы вырастут."
                         "Но может быть так, что твои волосы сократятся и ты будешь лохом. Также вы можете оформить подписку,"
                         "тогда ежедневно ваши отращенные волосы будут удвоены, а еще вы будете закреплены в описании бота."
                         "Если вы заметили баги и тп, то пишите лунтику, тоесть мне.", parse_mode=ParseMode.HTML
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


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer("пиши в лс @luuntikkkkk")


@dp.message(Command('error'))
async def cmd_error(message: types.Message):
    await message.answer_dice('🎯')
    await message.answer("вы выиграли! пиши лунтику за призом")
