# Generated by Django 4.1.7 on 2023-04-23 02:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=25)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
            ],
            options={
                'db_table': 'USER',
                'managed': False,
            },
        ),
    ]
