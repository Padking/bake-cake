
from datetime import datetime, date, time

from aiogram import (
    Dispatcher,
    types,
)
from aiogram.dispatcher.filters import Text

from ... import (
    models,
)


async def create_order(user_id):
    user = await models.User.get(tg_user_id=user_id)
    d_f = date(2021, 10, 31)
    t_f = time(15, 10)
    d_d = date(2021, 11, 15)
    t_d = time(14, 0)
    await models.Order.create(
        formation_at=datetime.combine(d_f, t_f),
        delivery_address='Советская, 7, 123',
        delivery_at=datetime.combine(d_d, t_d),
        amount=1234,
        status='Готов',
        customer=user
    )


async def show_user_orders(message: types.Message):
    # await create_order(message.from_user.id) # Создает заказ для пользователя (для отладки)
    user = await models.User.filter(
        tg_user_id=message.from_user.id
    ).first().prefetch_related('orders')
    for order in user.orders:
        delivery_at = order.delivery_at.strftime("%d %B %Y %H:%M")
        message_text = f'Номер заказа: {order.id}\n' \
                       f'Стоимость торта: {int(order.amount)}\n' \
                       f'Дата и время заказа: {delivery_at}\n' \
                       f'Статус заказа: {order.status}'
        await message.answer(message_text)


def register_handlers_viewing_orders(dp: Dispatcher):
    dp.register_message_handler(show_user_orders,
                                Text(equals="История заказов"),
                                state="*")
