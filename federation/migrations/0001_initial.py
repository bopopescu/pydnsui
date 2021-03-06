# Generated by Django 3.0.4 on 2020-04-09 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Unique identifier for this remote. Maybe the FQDN?', max_length=255, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Remote is enabled')),
                ('auth_token', models.CharField(blank=True, help_text='The token this remote should use for pulling zone information.', max_length=255, unique=True, verbose_name='Authorization token')),
                ('pull_url', models.URLField(blank=True, help_text='URL to pull zone information from this remote.', verbose_name='Pull URL')),
                ('pull_token', models.CharField(blank=True, help_text='The token used for pulling zone information, should correspond to the authorization token on this remote.', max_length=255, verbose_name='Pull Token')),
                ('pull_last', models.DateTimeField(blank=True, help_text='Last successful pull from this remote.', null=True, verbose_name='Last pull')),
                ('owners', models.ManyToManyField(help_text='Users that are allowed to modify this object. Staff users can modify all objects.', related_name='owned_federation_remote', to=settings.AUTH_USER_MODEL, verbose_name='Owners')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Unique identifier for this server. Maybe the FQDN?', max_length=255, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Server is enabled')),
                ('ipv4', models.GenericIPAddressField(help_text='IPv4 address of the nameserver for the bind query settings.', protocol='IPv4', verbose_name='IPv4 address')),
                ('ipv6', models.GenericIPAddressField(help_text='IPv6 address of the nameserver for the bind query settings.', protocol='IPv6', verbose_name='IPv6 address')),
                ('nameserver', models.CharField(help_text='Proper FQDN of the nameserver for the NS entries.', max_length=255, verbose_name='Nameserver')),
                ('owners', models.ManyToManyField(help_text='Users that are allowed to modify this object. Staff users can modify all objects.', related_name='owned_federation_server', to=settings.AUTH_USER_MODEL, verbose_name='Owners')),
                ('remote', models.ForeignKey(help_text='Remote that introduced this server', null=True, on_delete=django.db.models.deletion.CASCADE, to='federation.Remote', verbose_name='Responsible remote')),
            ],
            options={
                'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('remote'), nulls_last=False), 'name'],
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Zone is enabled')),
                ('slaves_all', models.BooleanField(default=True, verbose_name='All servers are slaves')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zones_master', to='federation.Server', verbose_name='Master server')),
                ('owners', models.ManyToManyField(help_text='Users that are allowed to modify this object. Staff users can modify all objects.', related_name='owned_federation_zone', to=settings.AUTH_USER_MODEL, verbose_name='Owners')),
                ('slaves', models.ManyToManyField(blank=True, related_name='zones_slave', to='federation.Server', verbose_name='Slave servers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
