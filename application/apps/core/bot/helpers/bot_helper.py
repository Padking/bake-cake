from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from ..constants import (
    user_status_to_button_labels_for_menu_keyboard,
    scenario_step_to_labels_callback_data,
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


def get_inline_keyboard(condition: str,
                        b_labels=scenario_step_to_labels_callback_data,
                        buttons=None,
                        row_width=2):

    buttons = buttons or []
    labels = b_labels[condition]

    keyboard = InlineKeyboardMarkup(row_width=row_width)
    buttons = [InlineKeyboardButton(text=btn_label, callback_data=btn_c_data)
               for btn_label, btn_c_data in labels.items()]

    keyboard.add(*buttons)

    return keyboard
