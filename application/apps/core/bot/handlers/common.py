from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from ..helpers.bot_helper import (
    get_keyboard,
)

from ..constants import (
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
    menu = get_keyboard(user.status)
    await message.answer(state_code_to_text_message["1"],
                         reply_markup=menu)

    # Установка состояния/сохранение данных в него

    if is_created:
        await message.answer("Для начала вам нужно зарегистрироваться.\n"
                             "Нажмите на кнопку внизу экрана.")
    else:
        await message.answer("Вы уже зарегистрированы! Можете заказать торт")


async def fill_db_cmd(message: Message):
    """Технологическая команда.
       Использовать только для пустой БД!

    """

    await db_filler.create_one_to_many_relation_records()
    await db_filler.create_single_tables_records()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start_cmd,
                                commands=["start"],
                                state="*")

    dp.register_message_handler(fill_db_cmd, commands=["fill_db"])
