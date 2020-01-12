# Generated by Django 3.0.1 on 2020-01-08 19:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('address_1', models.TimeField()),
                ('address_2', models.TimeField()),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=12)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(default='http://lorempixel.com/output/animals-q-c-640-480-4.jpg', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('s', 'Small'), ('m', 'Medium'), ('l', 'Large')], default='s', max_length=6)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='ecommerce.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_price', models.IntegerField(default=1000)),
                ('shipping_price', models.IntegerField(default=499)),
                ('total_price', models.IntegerField(default=1499)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to='ecommerce.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_product', to='ecommerce.Product')),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_product_details', to='ecommerce.Product')),
            ],
        ),
    ]