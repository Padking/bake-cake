from typing import Optional

from aiogram import Dispatcher
from django.apps import AppConfig


def register(dp: Optional[Dispatcher] = None) -> None:
    """
    The function registers the app.

    :param dp:
        If Dispatcher is not None — register bots modules.
    """
    from .models import register_models

    register_models()

    if dp is not None:
        from .bot.handlers.proba_handler import register_handlers

        register_handlers(dp)


class Core(AppConfig):
    """Django App Config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    verbose_name = "core"

    def ready(self):
        from .web import admin  # type: ignore
