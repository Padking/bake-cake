from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterUser(StatesGroup):
    pd_approval = State()
    phone_number = State()
    address = State()


class CreateCake(StatesGroup):
    levels_number = State()
    shape = State()
    topping = State()
    berries = State()
    decor = State()
    title = State()
    post_title = State()  # New
    comment = State()
    address = State()
    date = State()
    time = State()
