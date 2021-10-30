from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from ..constants import (
    user_status_to_button_labels_for_menu_keyboard,
    project_scenario_to_labels_callback_data,
)


def get_keyboard(user_status: str,
                 b_labels=user_status_to_button_labels_for_menu_keyboard,
                 buttons=None) -> ReplyKeyboardMarkup:

    buttons = buttons or []
    labels = b_labels[user_status]

    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2,
                                   resize_keyboard=True, )
    keyboard.add(*labels)

    return keyboard


def get_inline_keyboard(scenario_name: str,
                        b_labels=project_scenario_to_labels_callback_data,
                        buttons=None):

    buttons = buttons or []
    labels = b_labels[scenario_name]

    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=btn_label, callback_data=btn_c_data)
               for btn_label, btn_c_data in labels.items()]

    keyboard.add(*buttons)

    return keyboard
