# Generated by Django 2.1.4 on 2019-04-29 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20190429_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinelist',
            name='Op_qz',
        ),
        migrations.RemoveField(
            model_name='onlinelist',
            name='Pm_qz',
        ),
        migrations.RemoveField(
            model_name='onlinelist',
            name='Test_qz',
        ),
        migrations.RemoveField(
            model_name='onlinelist',
            name='Ui_qz',
        ),
        migrations.RemoveField(
            model_name='onlinelist',
            name='Zj_qz',
        ),
        migrations.AddField(
            model_name='onlinelist',
            name='test',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo'),
        ),
        migrations.AlterField(
            model_name='script',
            name='interpreter',
            field=models.CharField(choices=[('py', 'python3'), ('sh', 'bash')], default='py', max_length=16, verbose_name='解释器'),
        ),
    ]