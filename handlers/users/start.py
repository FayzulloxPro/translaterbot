import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    #Foydalanuvchilarni bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=912429653, text=err)
    count = db.count_users()[0]
    await message.answer(
        f"🇺🇿Assalomu alaykum {message.from_user.full_name}! \nGoogle tarjimonning telegramdagi norasmiy botiga xush kelibsiz! "
        f"\nBuyruqlar ro'yxatini olish uchun /help buyrug'ini yuboring"
        f"\n \n🇬🇧Hello {message.from_user.full_name}! Welcome to an unofficial bot of Google translater in telegram! "
        f"\nSend command /help to get list of commands"
        f"\n \n🇷🇺Привет {message.from_user.full_name}!Добро пожаловать в неофициальный бот переводчика Google в телеграме!"
        f"\nОтправьте команду /help, чтобы получить список команд")
    await dp.bot.send_message(912429653,
                              f"{message.from_user.get_mention(as_html=True)} botga start buyrug'ini yubordi.")
    msg = f"{message.from_user.full_name} bazaga qo'shildi. \nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=912429653, text=msg)