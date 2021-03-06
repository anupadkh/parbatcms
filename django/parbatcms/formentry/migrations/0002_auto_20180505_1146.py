# Generated by Django 2.0.4 on 2018-05-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formentry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='markers',
        ),
        migrations.AddField(
            model_name='formvalue',
            name='markers',
            field=models.IntegerField(default=1, verbose_name='Total Markers (प्राप्ताङ्कको जम्मा सङ्ख्या)'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='marks',
            field=models.FloatField(default=10, verbose_name='Marks'),
        ),
    ]
