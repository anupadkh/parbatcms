# Generated by Django 2.0.4 on 2018-05-05 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_auto_20180505_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headings',
            name='formID',
        ),
        migrations.RemoveField(
            model_name='questionchoice',
            name='questionID',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='tableID',
        ),
        migrations.DeleteModel(
            name='formValue',
        ),
        migrations.DeleteModel(
            name='headings',
        ),
        migrations.DeleteModel(
            name='QuestionChoice',
        ),
        migrations.DeleteModel(
            name='questions',
        ),
    ]