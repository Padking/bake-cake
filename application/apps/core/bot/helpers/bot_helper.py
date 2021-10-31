from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from tortoise.queryset import QuerySet

from ..constants import (
    button_label_template,
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


def update_button_properties(records: QuerySet,
                             step: str,
                             base_structure=scenario_step_to_labels_callback_data,
                             template=button_label_template) -> None:

    for record in records:
        record_name = record.name
        layer_label = template.format(record_name, int(record.price))
        record_c_data = record_name
        base_structure[step].update({layer_label: record_c_data})
