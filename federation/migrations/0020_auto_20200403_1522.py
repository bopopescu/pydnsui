# Generated by Django 3.0.4 on 2020-04-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('federation', '0019_auto_20200403_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote',
            name='auth_token',
            field=models.CharField(blank=True, help_text='The token this remote should use for pulling zone information.', max_length=255, unique=True, verbose_name='Authorization token'),
        ),
    ]