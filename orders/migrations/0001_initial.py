# Generated by Django 4.0.2 on 2022-03-11 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_productmodel_long_description_en_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('country', models.CharField(max_length=30, verbose_name='country')),
                ('address1', models.CharField(max_length=255, verbose_name='address')),
                ('address2', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('state', models.CharField(max_length=30, verbose_name='state')),
                ('zip_code', models.CharField(max_length=30, verbose_name='zip code')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(to='shop.ProductModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
