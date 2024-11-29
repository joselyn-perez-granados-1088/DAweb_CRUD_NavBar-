# Generated by Django 5.1.3 on 2024-11-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('codigo', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('productos', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.PositiveIntegerField()),
                ('frecuencia', models.CharField(max_length=60)),
                ('pagos', models.SmallIntegerField()),
            ],
        ),
    ]
