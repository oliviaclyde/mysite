from django.db import models
# from django.utils.timezone import now

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(default='', max_length=200)
#     pub_date = models.DateTimeField('date published', null=True)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, default='')
#     choice_text = models.CharField(default='', max_length=200)
#     votes = models.IntegerField(default=0)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)