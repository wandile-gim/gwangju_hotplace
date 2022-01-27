# Generated by Django 4.0.1 on 2022-01-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('agree', models.BooleanField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
