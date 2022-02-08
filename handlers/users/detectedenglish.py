import googletrans, logging, typing, time
from googletrans import LANGUAGES, Translator
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ContentTypes, ReplyKeyboardRemove
from googletrans import Translator
from aiogram.dispatcher.filters.state import StatesGroup, State
translater = Translator()
ADMINS = [912429653]

######################################
            #UZBEK
@dp.callback_query_handler(text="uz")
async def send_callback(call: CallbackQuery, state: FSMContext):
    await call.message.answer("O'zbek tiliga o'girish uchun xabarni yuboring")
    await state.set_state("uztranslation")
    await call.answer("🇬🇧Main language: Uzbek\n\n"
                      "🇺🇿Asosiy til: O'zbek\n\n"
                      "🇷🇺Главный язык: Узбэкский", show_alert=True)
    await call.message.delete()


@dp.message_handler(state="uztranslation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="uz")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")

########################################
            #ENGLISH...


@dp.callback_query_handler(text="en")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into English")
    await state.set_state("en_translation")
    await call.answer("🇬🇧Main language: English\n\n"
                      "🇺🇿Asosiy til: Ingliz\n\n"
                      "🇷🇺Главный язык: Англиский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="en_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="en")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


###################################
            #ARABIC

@dp.callback_query_handler(text="ar")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Arabic")
    await state.set_state("ar_translation")
    await call.answer("🇬🇧Main language: Arabic\n\n"
                      "🇺🇿Asosiy til: Arab\n\n"
                      "🇷🇺Главный язык: Арабский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="ar_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="ar")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")
####################
                #TURKISH


@dp.callback_query_handler(text="tr")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Turkish")
    await state.set_state("tr_translation")
    await call.answer("🇬🇧Main language: Turkish\n\n"
                      "🇺🇿Asosiy til: Turk\n\n"
                      "🇷🇺Главный язык: Туретский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="tr_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="tr")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")

################################
                #GERMAN

@dp.callback_query_handler(text="de")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into German")
    await state.set_state("de_translation")
    await call.answer("🇬🇧Main language: German\n\n"
                      "🇺🇿Asosiy til: Nemis\n\n"
                      "🇷🇺Главный язык: Немецкий", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="de_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="de")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


#####################################
                #FRENCH

@dp.callback_query_handler(text="fr")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into French")
    await state.set_state("fr_translation")
    await call.answer("🇬🇧Main language: French\n\n"
                      "🇺🇿Asosiy til: Fransuz\n\n"
                      "🇷🇺Главный язык: Французский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="fr_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="fr")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")

########################################
                #RUSSIAN
@dp.callback_query_handler(text="ru")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Russian")
    await state.set_state("ru_translation")
    await call.answer("🇬🇧Main language: Russian\n\n"
                      "🇺🇿Asosiy til: Rus\n\n"
                      "🇷🇺Главный язык: Русский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="ru_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="ru")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


#########################################
                    #ITALIAN

@dp.callback_query_handler(text="it")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Italian language")
    await state.set_state("it_translation")
    await call.answer("🇬🇧Main language: Italian\n\n"
                      "🇺🇿Asosiy til: Italyan\n\n"
                      "🇷🇺Главный язык: Итальянский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="it_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="it")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


#########################################
                #JAPANESE

@dp.callback_query_handler(text="ja")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Japanese")
    await state.set_state("ja_translation")
    await call.answer("🇬🇧Main language: Japanese\n\n"
                      "🇺🇿Asosiy til: Yapon\n\n"
                      "🇷🇺Главный язык: Японский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="ja_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="ja")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


########################################
                #SPANISH
@dp.callback_query_handler(text="es")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Spanish")
    await state.set_state("es_translation")
    await call.answer("🇬🇧Main language: Spanish\n\n"
                      "🇺🇿Asosiy til: Ispan\n\n"
                      "🇷🇺Главный язык: Испанский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="es_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="es")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


########################################
                #KOREAN

@dp.callback_query_handler(text="ko")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Korean language")
    await state.set_state("ko_translation")
    await call.answer("🇬🇧Main language: Korean\n\n"
                      "🇺🇿Asosiy til: Koreys\n\n"
                      "🇷🇺Главный язык: Корейскский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="ko_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="ko")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


#######################################
                #HINDI

@dp.callback_query_handler(text="hi")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Hindi")
    await state.set_state("hi_translation")
    await call.answer("🇬🇧Main language: Indian\n\n"
                      "🇺🇿Asosiy til: Hindcha\n\n"
                      "🇷🇺Главный язык: Хинди", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="hi_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="hi")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")

#################################################
                    #CHINESE(SIMPLIFIED)
@dp.callback_query_handler(text="zh-cn")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Chinese (simplified)")
    await state.set_state("zh-cn_translation")
    await call.answer("🇬🇧Main language: Chinese (simplified)\n\n"
                      "🇺🇿Asosiy til: Xitoycha (soddalashgan)\n\n"
                      "🇷🇺Главный язык: Китайский (упрощенный)", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="zh-cn_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="zh-cn")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")


##################################
                #CHINESE TRADITIONAL
@dp.callback_query_handler(text="zh-tw")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Chinesw (traditional)")
    await state.set_state("zh-tw_translation")
    await call.answer("🇬🇧Main language: Chinese (traditional)\n\n"
                      "🇺🇿Asosiy til: Xitoy (an'anaviy)\n\n"
                      "🇷🇺Главный язык: Китайский (традиционный)", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="zh-tw_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="zh-tw")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")

########################################
                #INDONESIAN
@dp.callback_query_handler(text="id")
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your message to translate into Indonesian language")
    await state.set_state("id_translation")
    await call.answer("🇬🇧Main language: Indonesian\n\n"
                      "🇺🇿Asosiy til: Indonez\n\n"
                      "🇷🇺Главный язык: Индонезийский", show_alert=True)
    await call.message.delete()
@dp.message_handler(state="id_translation")
async def send_message(message: Message):
    try:
        detection = translater.detect(message.text)
        det_make_str = str(detection)
        pos = det_make_str.find(",")
        source = det_make_str[14 : pos]
        translation = translater.translate(message.text, src=source, dest="id")
        make_str = str(translation)
        pos_1 = make_str.find("text=") + 5
        pos_2 = make_str.find("pronunciation=") - 2
        translated_text = make_str[pos_1 : pos_2]
        await message.answer(translated_text)
    except:
        await message.answer("🇬🇧Language not defined\n\n"
                             "🇺🇿Til aniqlanmadi!\n\n"
                             "🇷🇺Язык не определен")