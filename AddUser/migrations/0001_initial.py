# Generated by Django 2.2 on 2019-09-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=250)),
                ('LoginIDOrEmail', models.CharField(max_length=250)),
                ('Authority', models.PositiveIntegerField()),
                ('Password', models.CharField(max_length=250)),
                ('RetypePassword', models.CharField(max_length=250)),
            ],
        ),
    ]
