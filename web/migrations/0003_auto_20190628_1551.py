# Generated by Django 2.2.1 on 2019-06-28 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190627_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinedetails',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Onlinelist'),
        ),
    ]
