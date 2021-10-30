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
    layer_template,
    scenario_step_to_labels_callback_data,
    scenario_code_to_scenario_name,
    state_code_to_text_message,
)
from ..helpers.bot_helper import (
    get_inline_keyboard,
    get_keyboard,
)
from ... import (
    models,
)
from ..states import CreateCake


async def start_cake_collecting(message: types.Message, state: FSMContext):
    scenario_step = message.text
    layers = await models.Layer.all()
    for layer in layers:
        layer_name = layer.name
        layer_label = layer_template.format(layer_name, int(layer.price))
        layer_c_data = layer_name
        scenario_step_to_labels_callback_data[scenario_step].update({layer_label: layer_c_data})

    await CreateCake.levels_number.set()

    layer_markup = get_inline_keyboard(scenario_step, row_width=1)
    await message.answer(state_code_to_text_message["6"],
                         disable_notification=True,
                         reply_markup=layer_markup)


async def get_levels_number(callback_query: types.CallbackQuery,
                            state: FSMContext):

    choice = callback_query.data
    async with state.proxy() as cake:
        cake['levels_number'] = choice

    await callback_query.message.edit_text(text=f'Количество уровней: {choice}',
                                           reply_markup=None)

    await CreateCake.next()

    scenario_step = "Выбор формы"
    shapes = await models.Shape.all()
    for shape in shapes:
        shape_name = shape.name
        shape_label = layer_template.format(shape_name, int(shape.price))
        shape_c_data = shape_name
        scenario_step_to_labels_callback_data[scenario_step].update({shape_label: shape_c_data})

    shape_markup = get_inline_keyboard(scenario_step, row_width=1)
    await callback_query.message.answer(state_code_to_text_message["7"],
                                        disable_notification=True,
                                        reply_markup=shape_markup)


async def get_shape(callback_query: types.CallbackQuery,
                    state: FSMContext):

    choice = callback_query.data
    async with state.proxy() as cake:
        cake['shape'] = choice

    await callback_query.message.edit_text(text=f'Форма торта: {choice}',
                                           reply_markup=None)

    await CreateCake.next()

    scenario_step = "Выбор топпинга"
    type_of_topping = await models.ToppingType.get(name="Топпинг")
    toppings = await type_of_topping.toppings.all()
    for topping in toppings:
        topping_name = topping.name
        topping_label = layer_template.format(topping_name, int(topping.price))
        shape_c_data = topping_name
        scenario_step_to_labels_callback_data[scenario_step].update({topping_label: shape_c_data})

    topping_markup = get_inline_keyboard(scenario_step, row_width=1)
    await callback_query.message.answer(state_code_to_text_message["8"],
                                        disable_notification=True,
                                        reply_markup=topping_markup)


async def get_topping(callback_query: types.CallbackQuery,
                      state: FSMContext):

    choice = callback_query.data
    async with state.proxy() as cake:
        cake['topping'] = choice

    await callback_query.message.edit_text(text=f'Топпинг: {choice}',
                                           reply_markup=None)

    await CreateCake.next()

    scenario_step = "Выбор ягод"
    type_of_topping = await models.ToppingType.get(name="Ягоды")
    toppings = await type_of_topping.toppings.all()
    for topping in toppings:
        topping_name = topping.name
        topping_label = layer_template.format(topping_name, int(topping.price))
        shape_c_data = topping_name
        scenario_step_to_labels_callback_data[scenario_step].update({topping_label: shape_c_data})
    # Кнопка будет внизу, если раскомментировать
    # scenario_step_to_labels_callback_data[scenario_step].update({"Без ягод": "Без ягод"})

    topping_markup = get_inline_keyboard(scenario_step, row_width=1)
    await callback_query.message.answer(state_code_to_text_message["9"],
                                        disable_notification=True,
                                        reply_markup=topping_markup)


async def get_berries(callback_query: types.CallbackQuery,
                      state: FSMContext):

    choice = callback_query.data
    async with state.proxy() as cake:
        cake['berries'] = choice

    await callback_query.message.edit_text(text=f'Ягоды: {choice}',
                                           reply_markup=None)

    await CreateCake.next()

    scenario_step = "Выбор декора"
    type_of_topping = await models.ToppingType.get(name="Декор")
    toppings = await type_of_topping.toppings.all()
    for topping in toppings:
        topping_name = topping.name
        topping_label = layer_template.format(topping_name, int(topping.price))
        shape_c_data = topping_name
        scenario_step_to_labels_callback_data[scenario_step].update({topping_label: shape_c_data})

    topping_markup = get_inline_keyboard(scenario_step, row_width=1)
    await callback_query.message.answer(state_code_to_text_message["10"],
                                        disable_notification=True,
                                        reply_markup=topping_markup)


async def get_decor(callback_query: types.CallbackQuery,
                    state: FSMContext):

    choice = callback_query.data
    async with state.proxy() as cake:
        cake['decor'] = choice

    await callback_query.message.edit_text(text=f'Декор: {choice}',
                                           reply_markup=None)

    await CreateCake.next()

    scenario_step = "Выбор надписи"
    # type_of_topping = await models.ToppingType.get(name="Надпись")
    # toppings = await type_of_topping.toppings.all()
    # for topping in toppings:
    #     topping_name = topping.name
    #     topping_label = layer_template.format(topping_name, int(topping.price))
    #     shape_c_data = topping_name
    #     scenario_step_to_labels_callback_data[scenario_step].update({topping_label: shape_c_data})

    topping_markup = get_inline_keyboard(scenario_step, row_width=1)
    await callback_query.message.answer(state_code_to_text_message["11"],
                                        disable_notification=True,
                                        reply_markup=topping_markup)


async def get_title_from_button(callback_query: types.CallbackQuery,
                                state: FSMContext):

    choice = callback_query.data

    async with state.proxy() as cake:
        cake['title'] = choice

        await callback_query.message.edit_text(text="!",  # FIXME
                                               reply_markup=None)
        if choice == "Без надписи":

            await CreateCake.next()

            scenario_step = "Оставить комментарий"
            comment_markup = get_inline_keyboard(scenario_step, row_width=1)
            await callback_query.message.answer(state_code_to_text_message["13"],
                                                disable_notification=True,
                                                reply_markup=comment_markup)
        else:  # Пользователь желает добавить надпись
            await CreateCake.post_title.set()
            await callback_query.message.answer(state_code_to_text_message["12"],
                                                disable_notification=True)


async def get_title_from_stdout(message: types.Message, state: FSMContext):
    title = message.text
    async with state.proxy() as cake:
        cake['title'] = title

    await message.reply("Хорошо, сделаем такую надпись")

    await CreateCake.next()

    scenario_step = "Оставить комментарий"
    comment_markup = get_inline_keyboard(scenario_step, row_width=1)
    await message.answer(state_code_to_text_message["13"],
                         disable_notification=True,
                         reply_markup=comment_markup)


def register_handlers_cake_creation(dp: Dispatcher):
    dp.register_message_handler(start_cake_collecting,
                                Text(equals=scenario_code_to_scenario_name["3"]),
                                state="*")
    dp.register_callback_query_handler(get_levels_number,
                                       state=CreateCake.levels_number)
    dp.register_callback_query_handler(get_shape,
                                       state=CreateCake.shape)
    dp.register_callback_query_handler(get_topping,
                                       state=CreateCake.topping)
    dp.register_callback_query_handler(get_berries,
                                       state=CreateCake.berries)
    dp.register_callback_query_handler(get_decor,
                                       state=CreateCake.decor)
    dp.register_callback_query_handler(get_title_from_button,
                                       state=CreateCake.title)
    dp.register_message_handler(get_title_from_stdout,
                                state=CreateCake.post_title)
