# Generated by Django 5.1 on 2024-11-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.PositiveSmallIntegerField(max_length=60, primary_key=True, serialize=False),
        ),
    ]
