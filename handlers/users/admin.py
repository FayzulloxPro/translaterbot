import time
from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def get_ad_from_admin(message: types.Message, state: FSMContext):
    await message.answer("Reklama uchun foto linkini yuboring")
    await state.set_state("get_advertisement")


@dp.message_handler(state="get_advertisement", chat_id=ADMINS)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    #advertisement_text=message.text
    get_advertisement_link = message.text
    await state.update_data(get_advertisement_link=get_advertisement_link)
    await message.reply("Endi reklama matnini yuboring")
    await state.set_state("get_advertisement_caption")

@dp.message_handler(state="get_advertisement_caption", chat_id=ADMINS)
async def get_ad_caption(message: types.Message, state: FSMContext):
    ad_caption = message.text
    await state.update_data(ad_caption=ad_caption)
    data = await state.get_data()
    get_advertisement_link =data.get("get_advertisement_link")

    users = db.select_all_users()
    try:
        for user in users:
            user_id = user[0]
            await bot.send_photo(chat_id=user_id, photo=get_advertisement_link, caption=ad_caption)
            time.sleep(1)

    except:
        await bot.send_message(chat_id=ADMINS, text="Xatolik yuz berdi")
    await state.finish()




# #admin_states = get_advertisement, get_advertisement_caption
#
# #for admin_state in admin_states:
# @dp.message_handler(user_id=ADMINS, text="/stoprek", state="get_advertisement")
# async def release_state(message: types.Message, state: FSMContext):
#     await state.finish()
#     await bot.send_message(chat_id=ADMINS, text="Reklama berish jarayoni yakunlandi")
#     await message.answer("Tugadi")
#
#
# @dp.message_handler(chat_id=ADMINS, text="/stoprek", state="get_advertisement_caption")
# async def release_state(message: types.Message, state: FSMContext):
#     await state.finish()
#     await bot.send_message(chat_id=ADMINS, text="Reklama berish jarayoni yakunlandi")
#     await message.answer("Tugadi")
