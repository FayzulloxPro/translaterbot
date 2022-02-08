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

list_states = ["uztranslation", "en_translation", "ar_translation", "tr_translation", "de_translation"
               , "fr_translation", "ru_translation", "it_translation", "ja_translation",
               "es_translation", "ko_translation", "hi_translation", "zh-cn_translation", "zh-tw_translation",
               "id_translation"]


@dp.message_handler(Command("status"), state="uztranslation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Uzbek\n\n"
                         "🇺🇿Tanlangan til : O'zbek\n\n"
                         "🇷🇺Выбранный язык : Узбекский")


@dp.message_handler(Command("status"), state="en_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : English\n\n"
                         "🇺🇿Tanlangan til : Ingliz\n\n"
                         "🇷🇺Выбранный язык : Английский")


@dp.message_handler(Command("status"), state="ar_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Arabic\n\n"
                         "🇺🇿Tanlangan til : Arab\n\n"
                         "🇷🇺Выбранный язык : Арабский")


@dp.message_handler(Command("status"), state="tr_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Turkish\n\n"
                         "🇺🇿Tanlangan til : Turk\n\n"
                         "🇷🇺Выбранный язык : Турецкий")



@dp.message_handler(Command("status"), state="de_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : German\n\n"
                         "🇺🇿Tanlangan til : Nemis\n\n"
                         "🇷🇺Выбранный язык : Немецкий")



@dp.message_handler(Command("status"), state="fr_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : French\n\n"
                         "🇺🇿Tanlangan til : Fransuz\n\n"
                         "🇷🇺Выбранный язык : Французский")



@dp.message_handler(Command("status"), state="ru_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Russian\n\n"
                         "🇺🇿Tanlangan til : Rus\n\n"
                         "🇷🇺Выбранный язык : Русский")



@dp.message_handler(Command("status"), state="it_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Italian\n\n"
                         "🇺🇿Tanlangan til : Italyan\n\n"
                         "🇷🇺Выбранный язык : Итальянский")



@dp.message_handler(Command("status"), state="ja_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Japanese\n\n"
                         "🇺🇿Tanlangan til : Yapon\n\n"
                         "🇷🇺Выбранный язык : Японский")


@dp.message_handler(Command("status"), state="es_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Spanish\n\n"
                         "🇺🇿Tanlangan til : Ispan\n\n"
                         "🇷🇺Выбранный язык : Испанский")



@dp.message_handler(Command("status"), state="ko_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Korean\n\n"
                         "🇺🇿Tanlangan til : Koreys\n\n"
                         "🇷🇺Выбранный язык : Корейский")



@dp.message_handler(Command("status"), state="hi_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Hindi\n\n"
                         "🇺🇿Tanlangan til : Hind\n\n"
                         "🇷🇺Выбранный язык : Индийский")



@dp.message_handler(Command("status"), state="zh-cn_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Chinses (simplified)\n\n"
                         "🇺🇿Tanlangan til : Xitoy (soddalashgan)\n\n"
                         "🇷🇺Выбранный язык : Китайский (упрощенный)")



@dp.message_handler(Command("status"), state="zh-tw_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Chinses (traditional)\n\n"
                         "🇺🇿Tanlangan til : Xitoy (an'anaviy)\n\n"
                         "🇷🇺Выбранный язык : Китайский (традиционный)")




@dp.message_handler(Command("status"), state="id_translation")
async def send_status(message: Message):
    await message.answer("🇬🇧Selected language : Indonesian\n\n"
                         "🇺🇿Tanlangan til : Indonez\n\n"
                         "🇷🇺Выбранный язык : индонезийский")

