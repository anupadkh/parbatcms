from django.db import models
from django.utils.timezone import *
import datetime

class formValue(models.Model):
    formName = models.TextField('Form Name (फारमको नाम)')
    markers = models.IntegerField('Total Markers (प्राप्ताङ्कको जम्मा सङ्ख्या)', default=1)
    def __str__(self):
        return self.formName;

class headings(models.Model):
    formID = models.ForeignKey(formValue, on_delete=models.CASCADE)
    tableName = models.TextField('Table Name')
    def __str__(self):
        return self.tableName;

class questions(models.Model):
    simpletext = 'st'
    multiplechoices = 'mc'
    selectchoices = 'sc'
    numberValue = 'nv'
    answerChoices = ((simpletext, 'Simple Text'),
        (multiplechoices, 'Multiple Choices'),
        (selectchoices, 'Select Choices'),
        (numberValue, 'Number Value')
    )
    tableID = models.ForeignKey(headings, on_delete=models.CASCADE)
    question = models.TextField('Question (प्रश्न)')
    answerType = models.CharField(
        max_length=2,
        choices=answerChoices,
        default=simpletext,
    )
    marks = models.FloatField('Marks', default=10)
    mandatory=((False,'Yes (खाली छोडे पनि हुने)'), (True, 'No (भर्नै पर्ने)'))
    unanswering = models.BooleanField('Unanswering is Allowed?', default=0,
        choices=mandatory
    )
    description = models.TextField('Description(विवरण)', null=True, default=' ')
    def __str__(self):
        return self.question;

class QuestionChoice (models.Model):
    questionID = models.ForeignKey(questions, on_delete=models.CASCADE)
    choiceDescription = models.TextField('Choice')
    choiceMarks = models.TextField('Choice Marks')
    def __str__(self):
        return self.choiceDescription;
