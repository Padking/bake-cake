from typing import Tuple

from . import models


async def add_user(tg_user_id: int,
                   first_name: str) -> Tuple[models.User, bool]:

    return await models.User.get_or_create(tg_user_id=tg_user_id,
                                           first_name=first_name)
