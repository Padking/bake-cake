from os import getenv

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from ..helpers.bot_helper import (
    get_keyboard,
)
from ..states import RegisterUser, CreateCake

from ..constants import (
    scenario_code_to_scenario_name,
    state_code_to_text_message,
)

from ... import (
    db_filler,
    models,
)


async def start_cmd(message: Message, state: FSMContext):
    user_optional_fields = {
        "first_name": message.from_user.first_name,
        "tg_username": message.from_user.username,
        "last_name": message.from_user.last_name,
    }

    user, is_created = await (models.User.
                              get_or_create(defaults=user_optional_fields,
                                            tg_user_id=message.from_user.id))

    user_status = user.status
    if user_status == "anonymous":
        await RegisterUser.start_registration.set()

    menu = get_keyboard(user_status)
    await message.answer(state_code_to_text_message["1"],
                         reply_markup=menu)

    if is_created or user_status == "anonymous":
        await message.answer(state_code_to_text_message["1.1"])


async def fill_db_cmd(message: Message):
    """Технологическая команда.
       Использовать только для пустой БД!

    """

    await db_filler.create_one_to_many_relation_records()
    await db_filler.create_single_tables_records()


async def reset_tmp_storage(message: Message, state: FSMContext):
    """Технологическая команда."""

    await state.finish()

    await message.reply('Состояния и привязанные к ним данные сброшены!')


async def cmd_cancel(message: Message, state: FSMContext):
    await state.reset_state(with_data=False)

    user = await (models.User.get(tg_user_id=message.from_user.id))
    menu = get_keyboard(user.status)

    await message.answer(state_code_to_text_message["1.2"],
                         reply_markup=menu)


async def send_help_message(message: Message):
    photo_obj = open(getenv("HELP_PHOTO_FILEPATH"), "rb")
    await message.answer_photo(photo_obj,
                               caption=state_code_to_text_message["help"])
    photo_obj.close()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start_cmd,
                                commands=["start"],
                                state="*")
    dp.register_message_handler(fill_db_cmd,
                                commands=["fill_db"],
                                state="*")
    dp.register_message_handler(reset_tmp_storage,
                                commands=["reset"],
                                state="*")
    dp.register_message_handler(cmd_cancel,
                                Text(equals=scenario_code_to_scenario_name["1"]),
                                state="*")
    dp.register_message_handler(send_help_message,
                                state=[
                                    CreateCake,
                                    RegisterUser.pd_approval
                                ])
