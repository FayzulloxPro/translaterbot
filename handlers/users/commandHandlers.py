import googletrans, logging, typing, time
from googletrans import LANGUAGES, Translator
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ContentTypes, ReplyKeyboardRemove
from keyboards.inline.listofLanguages import list_languages_top, list_languages1, list_languages2, list_languages3
from aiogram.types import Message, CallbackQuery

@dp.message_handler(Command("changelan"), state=None)
async def send_message(message: Message, state: FSMContext):
    await message.answer("🇬🇧Which language do you want to change the main language to?"
                         "\n\n🇺🇿Asosiy tilni qaysi tilga o'zgartirmoqchisiz?"
                         "\n\n🇷🇺На какой язык вы хотите изменить язык по умолчанию?", reply_markup=list_languages_top)
    await state.finish()


@dp.callback_query_handler(text="delete")
async def send_callback(call: CallbackQuery):
    await call.message.delete()


list_states = ["uztranslation", "en_translation", "ar_translation", "tr_translation", "de_translation"
               , "fr_translation", "ru_translation", "it_translation", "ja_translation",
               "es_translation", "ko_translation", "hi_translation", "zh-cn_translation", "zh-tw_translation",
               "id_translation"]

for get_state in list_states:
    @dp.message_handler(Command("help"), state=get_state)
    async def release_state(message: Message, state: FSMContext):
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
        await state.finish()


for get_start in list_states:
    @dp.message_handler(Command("start"), state=get_start)
    async def release_start(message: Message, state: FSMContext):
        await message.answer(
            f"🇺🇿Assalomu alaykum {message.from_user.full_name}! \nGoogle tarjimonning telegramdagi norasmiy botiga xush kelibsiz! "
            f"\n \n🇬🇧Hello {message.from_user.full_name}! Welcome to an unofficial bot of Google translater in telegram! "
            f"\n \n🇷🇺Привет {message.from_user.full_name}!Добро пожаловать в неофициальный бот переводчика Google в телеграме!")
        await dp.bot.send_message(912429653,
                                  f"{message.from_user.get_mention(as_html=True)} botga start buyrug'ini yubordi.")
        await state.finish()


for get_languages in list_states:
    @dp.message_handler(Command("changelan"), state=get_languages)
    async def send_message(message: Message, state: FSMContext):
        await message.answer("🇬🇧Which language do you want to change the main language to?"
                             "\n\n🇺🇿Asosiy tilni qaysi tilga o'zgartirmoqchisiz?"
                             "\n\n🇷🇺На какой язык вы хотите изменить язык по умолчанию?",
                             reply_markup=list_languages_top)
        await state.finish()





@dp.message_handler(Command("status"), state="uztranslation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Uzbek\n\n"
                         "🇺🇿Tanlangan til : O'zbek\n\n"
                         "🇷🇺Выбранный язык : Узбекский")

