# Generated by Django 3.0.4 on 2020-03-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('federation', '0003_auto_20200328_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='nameserver',
            field=models.CharField(default='', help_text='FQDN of the nameserver', max_length=255),
            preserve_default=False,
        ),
    ]
