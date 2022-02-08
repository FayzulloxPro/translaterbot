from aiogram import types

from loader import dp


#Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("🇬🇧Status : language not selected \nSend command /help to get list of commands of the bot"
                         "\n\n🇺🇿Holat : til tanlanmagan\nBot buyruqlarini olsih uchun /help buyrug'ini yuboring"
                         "\n\n🇷🇺Статус : язык не выбран\nЧтобы получить команды бота, отправьте команду /help")
