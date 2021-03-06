# Generated by Django 2.0.4 on 2018-05-05 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formName', models.TextField(verbose_name='Form Name (फारमको नाम)')),
            ],
        ),
        migrations.CreateModel(
            name='headings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableName', models.TextField(verbose_name='Table Name')),
                ('formID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formentry.formValue')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choiceDescription', models.TextField(verbose_name='Choice')),
                ('choiceMarks', models.TextField(verbose_name='Choice Marks')),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question (प्रश्न)')),
                ('answerType', models.CharField(choices=[('st', 'Simple Text'), ('mc', 'Multiple Choices'), ('sc', 'Select Choices'), ('nv', 'Number Value')], default='st', max_length=2)),
                ('marks', models.IntegerField(default=10, verbose_name='Marks')),
                ('unanswering', models.BooleanField(choices=[(False, 'Yes (खाली छोडे पनि हुने)'), (True, 'No (भर्नै पर्ने)')], default=0, verbose_name='Unanswering is Allowed?')),
                ('description', models.TextField(null=True, verbose_name='Description(विवरण)')),
                ('markers', models.IntegerField(default=1, verbose_name='Total Markers (प्राप्ताङ्कको जम्मा सङ्ख्या)')),
                ('tableID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formentry.headings')),
            ],
        ),
        migrations.AddField(
            model_name='questionchoice',
            name='questionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formentry.questions'),
        ),
    ]
