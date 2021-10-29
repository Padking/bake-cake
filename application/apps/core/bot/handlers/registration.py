from os import getenv
from pathlib import Path

from aiogram import (
    Dispatcher,
    types,
)
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from dotenv import load_dotenv

from ..constants import (
    state_code_to_text_message,
    project_scenario_to_labels_callback_data,
)
from ..helpers.bot_helper import (
    get_inline_keyboard,
    get_keyboard,
)
from ... import (
    models,
)
from ..states import RegisterUser


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
load_dotenv(BASE_DIR / "config" / ".env")


async def send_help_message(message: types.Message, state: FSMContext):
    markup = get_inline_keyboard(message.text)
    f_obj = open(getenv("CONSENT_PD_FILEPATH"), "rb")
    await message.answer_document(f_obj,
                                  caption=state_code_to_text_message["2"],
                                  disable_notification=True,
                                  reply_markup=markup)
    f_obj.close()
    await RegisterUser.pd_approval.set()


async def get_user_consent(callback_query: types.CallbackQuery):
    await callback_query.message.edit_caption(
        caption='Согласен на обработку персональных данных',
        reply_markup=None
    )

    # Установка состояния/сохранение данных в него

    await callback_query.message.answer(state_code_to_text_message["3"])

    await RegisterUser.next()


async def get_phone_number(message: types.Message, state: FSMContext):
    # Если телефон валидный, обновить запись в PSQL
    async with state.proxy() as user:
        try:
            user['phone_number'] = message.contact.phone_number
        except AttributeError:
            # Здесь должна быть валидация
            user['phone_number'] = message.text
            # Если телефон невалидный, отправить картинку

    await message.answer(state_code_to_text_message["4"],
                         disable_notification=True,
                         reply_markup=None)

    await RegisterUser.next()


async def get_address(message: types.Message, state: FSMContext):
    # Если адрес доставки валидный, сохранить инфу в Redis
    async with state.proxy() as user:
        # Здесь должна быть валидация
        user['data'] = message.text
        # Если адрес доставки невалидный, отправить картинку

    # Обновить статус П-ля в PSQL
    # data = {}
    # user, _ = await (models.User.
    #                  update_from_dict(data=data)
    # menu = get_keyboard(user.status)

    await message.answer(state_code_to_text_message["5"])
                        #  reply_markup=menu)

    await state.finish()  # FIXME


def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(send_help_message,
                                Text(equals="Регистрация"),
                                state="*")
    dp.register_callback_query_handler(get_user_consent,
                                       Text(equals=(project_scenario_to_labels_callback_data
                                            ["Регистрация"]
                                            .values())),
                                       state=RegisterUser.pd_approval)
    dp.register_message_handler(get_phone_number,
                                Text(equals="+79631234567"),  # FIXME
                                state=RegisterUser.phone_number)
    dp.register_message_handler(get_address,
                                content_types=types.ContentTypes.TEXT,  # FIXME
                                state=RegisterUser.address)
