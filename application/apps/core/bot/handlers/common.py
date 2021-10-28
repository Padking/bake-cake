from aiogram import Dispatcher
from aiogram.types import Message

from ... import services, db_filler


async def start(message: Message):
    user, is_created = await services.add_user(
        tg_user_id=message.from_user.id,
        first_name=message.from_user.first_name,
    )
    
    if is_created:
        await message.answer("You have successfully registered in the bot!")
    else:
        await message.answer("You are already registered in the bot!")


async def fill_db_cmd(message: Message):
    """Технологическая команда.
       Использовать только для пустой БД!

    """

    await db_filler.create_one_to_many_relation_records()
    await db_filler.create_single_tables_records()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])

    dp.register_message_handler(fill_db_cmd, commands=["fill_db"])
