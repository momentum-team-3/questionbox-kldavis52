# Generated by Django 3.1.1 on 2020-09-14 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0009_auto_20200914_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='qanda.question'),
        ),
    ]