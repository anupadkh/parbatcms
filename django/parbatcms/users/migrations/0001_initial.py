# Generated by Django 2.0.4 on 2018-05-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Username')),
                ('password', models.CharField(max_length=70, verbose_name='Password')),
            ],
        ),
    ]
