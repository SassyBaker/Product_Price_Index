# Generated by Django 5.0.4 on 2024-04-27 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('weight_unit', models.CharField(choices=[('g', 'Grams'), ('kg', 'Kilos'), ('oz', 'OZ'), ('ml', 'mL')], default='g', max_length=64)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updates_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costco_products.product')),
            ],
        ),
    ]
