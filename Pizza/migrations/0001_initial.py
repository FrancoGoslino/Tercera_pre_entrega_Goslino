# Generated by Django 4.1.7 on 2023-03-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_bebida', models.CharField(max_length=20)),
                ('precio_bebida', models.CharField(max_length=6)),
                ('marca_bebida', models.CharField(max_length=20)),
                ('litros_bebida', models.CharField(max_length=6)),
            ],
        ),
    ]
