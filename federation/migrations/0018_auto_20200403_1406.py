# Generated by Django 3.0.4 on 2020-04-03 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('federation', '0017_auto_20200402_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='server',
            name='auth_token',
        ),
        migrations.RemoveField(
            model_name='server',
            name='configured_here',
        ),
        migrations.RemoveField(
            model_name='server',
            name='pull_enabled',
        ),
        migrations.RemoveField(
            model_name='server',
            name='pull_last',
        ),
        migrations.RemoveField(
            model_name='server',
            name='pull_servers',
        ),
        migrations.RemoveField(
            model_name='server',
            name='pull_token',
        ),
        migrations.RemoveField(
            model_name='server',
            name='pull_url',
        ),
        migrations.AlterField(
            model_name='server',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Server is enabled'),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipv4',
            field=models.GenericIPAddressField(help_text='IPv4 address of the nameserver for the bind query settings.', protocol='IPv4', verbose_name='IPv4 address'),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipv6',
            field=models.GenericIPAddressField(help_text='IPv6 address of the nameserver for the bind query settings.', protocol='IPv6', verbose_name='IPv6 address'),
        ),
        migrations.AlterField(
            model_name='server',
            name='nameserver',
            field=models.CharField(help_text='Proper FQDN of the nameserver for the NS entries.', max_length=255, verbose_name='Nameserver'),
        ),
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Unique identifier for this remote. Maybe the FQDN?', max_length=255, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Remote is enabled')),
                ('auth_token', models.CharField(blank=True, help_text='The token this remote should use for pulling zone information.', max_length=255, verbose_name='Authorization token')),
                ('pull_enabled', models.BooleanField(default=True, help_text='Whether we attempt to pull zone information from this remote.', verbose_name='Pull is enabled')),
                ('pull_url', models.URLField(blank=True, help_text='URL to pull zone information from this remote.', verbose_name='Pull URL')),
                ('pull_token', models.CharField(blank=True, help_text='The token used for pulling zone information, should correspond to the authorization token on this remote.', max_length=255, verbose_name='Pull Token')),
                ('pull_last', models.DateTimeField(blank=True, help_text='Last successful pull from this remote.', null=True, verbose_name='Last pull')),
                ('admins', models.ManyToManyField(help_text='Local users that may modify this remote.', to=settings.AUTH_USER_MODEL, verbose_name='Admin users')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='remote',
            field=models.ForeignKey(help_text='Remote that introduced this server', null=True, on_delete=django.db.models.deletion.CASCADE, to='federation.Remote', verbose_name='Responsible remote'),
        ),
    ]