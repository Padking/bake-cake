from aiogram import Dispatcher
from aiogram.types import Message

from config.apps import INSTALLED_APPS


async def send_my_id(message: Message):
    await message.answer(
        f"User Id: <b>{message.from_user.id}</b>\n" f"Chat Id: <b>{message.chat.id}</b>"
    )

async def send_my_apps(message: Message):
    apps_names = ""
    for app in INSTALLED_APPS:
        apps_names += app.Config.name + "\n"

    await message.answer("Installed apps:\n" f"{apps_names}")


async def simple_handler(message: Message):
    await message.answer('Hello from "Core" app!')


def register_handlers_proba(dp: Dispatcher):
    dp.register_message_handler(send_my_id, commands=["id"])

    dp.register_message_handler(send_my_apps, commands=["apps"])

    dp.register_message_handler(simple_handler, commands=["core"])
