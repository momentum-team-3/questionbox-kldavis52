# Generated by Django 3.1.1 on 2020-09-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0016_auto_20200914_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
