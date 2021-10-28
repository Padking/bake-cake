import asyncio
from orm_converter.tortoise_to_django import ConvertedModel
from tortoise import Tortoise, fields
from tortoise.models import Model

from config import DatabaseConfig


class User(Model, ConvertedModel):
    tg_user_id = fields.BigIntField(pk=True,
                                    description="ID в Telegram")
    first_name = fields.CharField(max_length=64,
                                  description="Имя в Telegram")

    tg_username = fields.CharField(max_length=64,
                                   description="Юзернейм в Telegram",
                                   null=True)
    last_name = fields.CharField(max_length=64,
                                 description="Фамилия в Telegram",
                                 null=True)
    contact_phone = fields.CharField(max_length=15,
                                     description="Контактный телефон",
                                     null=True)
    status = fields.CharField(max_length=64,
                              default="anonymous",
                              description="Статус в ИС")

    orders: fields.ReverseRelation["Order"]
    cakes = fields.ManyToManyField("core.Cake",
                                   related_name="user_cakes",
                                   on_delete=fields.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.tg_user_id}"

    class Meta:
        table = "user"


class Shape(Model, ConvertedModel):
    name = fields.CharField(max_length=64,
                            description="Название")

    price = fields.FloatField(description="Цена")

    # cakes: fields.ReverseRelation["Cake"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "shape"


class Layer(Model, ConvertedModel):
    name = fields.CharField(max_length=64,
                            description="Название")

    price = fields.FloatField(description="Цена")

    # cakes: fields.ReverseRelation["Cake"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "layer"


class Cake(Model, ConvertedModel):
    basis = fields.CharField(max_length=64, description="Основа")
    shape = fields.CharField(max_length=64, description="Форма")
    layers_count = fields.IntField(description="Кол-во слоёв")

    name = fields.CharField(max_length=64,
                            description="Название разновидности",
                            null=True)
    affiliation = fields.CharField(max_length=64,
                                   description="Принадлежность к торговой площадке",
                                   null=True)

    shape = fields.ForeignKeyField("core.Shape",
                                   related_name="cakes_per_shape")
    layer = fields.ForeignKeyField("core.Layer",
                                   related_name="cakes_per_layer")

    users: fields.ManyToManyRelation[User]
    toppings = fields.ManyToManyField("core.Topping",
                                      related_name="cake_toppings",
                                      on_delete=fields.CASCADE)

    def __str__(self) -> str:
        return f"{self.shape} на основе: {self.basis}"

    class Meta:
        table = "cake"


class ToppingType(Model, ConvertedModel):
    name = fields.CharField(max_length=64,
                            description="Название разновидности")

    toppings: fields.ReverseRelation["Topping"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "topping_type"


class Topping(Model, ConvertedModel):
    name = fields.CharField(max_length=64,
                            description="Название топпинга")

    price = fields.FloatField(description="Цена")

    cakes: fields.ManyToManyRelation[Cake]
    topping_type = fields.ForeignKeyField("core.ToppingType",
                                          related_name="toppings")

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "topping"


class Order(Model, ConvertedModel):
    formation_at = fields.DatetimeField(auto_now_add=True,
                                        description="Дата и время формирования")
    delivery_address = fields.CharField(max_length=255,
                                        description="Адрес доставки",
                                        index=True)

    delivery_at = fields.DatetimeField(description="Дата и время доставки")
    amount = fields.FloatField(description="Сумма")
    status = fields.CharField(max_length=64,
                              description="Статус")

    customer = fields.ForeignKeyField("core.User",
                                      related_name="orders")

    def __str__(self) -> str:
        return f"Дата и время формирования: {self.formation_at}"

    class Meta:
        table = "order"


class Comment(Model, ConvertedModel):
    order = fields.OneToOneField("core.Order",
                                 related_name="comment",
                                 pk=True)
    content = fields.TextField(description="Содержание",
                               null=True)

    def __str__(self) -> str:
        return self.content[:10]

    class Meta:
        table = "comment"


class PromoCode(Model, ConvertedModel):
    order = fields.OneToOneField("core.Order",
                                 related_name="promo_code",
                                 pk=True)
    c_value = fields.CharField(max_length=16,
                               description="Значение",
                               null=True)

    def __str__(self) -> str:
        return f"Промокод к заказу: {self.c_value}"

    class Meta:
        table = "promo_code"


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.core.models"],
        app_label="core",
        _init_relations=True,
    )
