from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("🇬🇧Commands:"
            "\n/start - run the bot"
            "\n/help - get list of commands"
            "\n/changelan - choose or change translation language"
            "\n/status - current translation language",
            "\n\n🇺🇿Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - buyruqlar ro'yxatini olish",
            "/changelan - Tilni tanlash yoki o'zgartirish",
            "/status - Tarjima tili"
            "\n\n🇷🇺Команды:"
            "\n/start - Запустить бота"
            "\n/changelan - Выбрать или изменить язык"
            "\n/start - Запустить бота"
            "\n/status - Язык перевода")
    await message.answer("\n".join(text))
