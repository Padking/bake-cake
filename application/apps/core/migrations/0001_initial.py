# Generated by Django 3.2.8 on 2021-10-28 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Название разновидности')),
                ('affiliation', models.CharField(blank=True, max_length=64, null=True, verbose_name='Принадлежность к торговой площадке')),
            ],
            options={
                'db_table': 'cake',
            },
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'db_table': 'layer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время формирования')),
                ('delivery_address', models.CharField(max_length=255, verbose_name='Адрес доставки')),
                ('delivery_at', models.DateTimeField(verbose_name='Дата и время доставки')),
                ('amount', models.FloatField(verbose_name='Сумма')),
                ('status', models.CharField(max_length=64, verbose_name='Статус')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'db_table': 'shape',
            },
        ),
        migrations.CreateModel(
            name='ToppingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название разновидности')),
            ],
            options={
                'db_table': 'topping_type',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.order')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержание')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.order')),
                ('c_value', models.CharField(blank=True, max_length=16, null=True, verbose_name='Значение')),
            ],
            options={
                'db_table': 'promo_code',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('tg_user_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID в Telegram')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя в Telegram')),
                ('tg_username', models.CharField(blank=True, max_length=64, null=True, verbose_name='Юзернейм в Telegram')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Фамилия в Telegram')),
                ('contact_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Контактный телефон')),
                ('status', models.CharField(default='anonymous', max_length=64, verbose_name='Статус в ИС')),
                ('cakes', models.ManyToManyField(related_name='user_cakes', to='core.Cake')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название топпинга')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('topping_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='core.toppingtype')),
            ],
            options={
                'db_table': 'topping',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.user'),
        ),
        migrations.AddField(
            model_name='cake',
            name='layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakes_per_layer', to='core.layer'),
        ),
        migrations.AddField(
            model_name='cake',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakes_per_shape', to='core.shape'),
        ),
        migrations.AddField(
            model_name='cake',
            name='toppings',
            field=models.ManyToManyField(related_name='cake_toppings', to='core.Topping'),
        ),
    ]
