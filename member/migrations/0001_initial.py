# Generated by Django 2.2.5 on 2022-01-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False, unique=True)),
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('agree', models.BooleanField()),
                ('file_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='%Y/%m/%d')),
            ],
        ),
    ]
