# Generated by Django 4.1.1 on 2023-01-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app8', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=10)),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.CharField(max_length=10)),
                ('product_offer', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]