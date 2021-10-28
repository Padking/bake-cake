from tortoise import Tortoise

from config import DatabaseConfig

from .db_constants import (
    topping_type_name_to_topping,

    layer_count_to_price,
    shape_name_to_price,
)

from .models import (
    Layer,
    Shape,
    Topping,
    ToppingType,
)


async def create_one_to_many_relation_records():
    await Tortoise.init(config=DatabaseConfig.get_tortoise_config())

    for t_type_name, topping in topping_type_name_to_topping.items():
        topping_type = ToppingType(name=t_type_name)
        await topping_type.save()
        for topping_name, topping_price in topping.items():
            await Topping(name=topping_name,
                          price=topping_price,
                          topping_type_id=topping_type.id).save()


async def create_single_tables_records(models=(Layer, Shape),
                                       features=(layer_count_to_price,
                                                 shape_name_to_price)):

    await Tortoise.init(config=DatabaseConfig.get_tortoise_config())

    for model, feature in zip(models, features):
        records = [model(name=name, price=price) for name, price in feature.items()]
        await model.bulk_create(records)
