# Generated by Django 5.0.5 on 2024-05-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_alter_items_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.DateField(null=True),
        ),
    ]