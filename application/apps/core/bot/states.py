from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterUser(StatesGroup):
    pd_approval = State()
    phone_number = State()
    address = State()
