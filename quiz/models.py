from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
# from notes.models import Signup

# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length=1255)

    def __str__(self):
        return self.name

class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=CASCADE, null=True, blank=True)
    # chapter_num = models.IntegerField(default=1)
    score = models.IntegerField(default=4)
    ques_text = models.TextField()

    def __str__(self):
        return "question"+str(self.id)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    option_num = models.CharField(max_length=20,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D','D')
        ],
        default='A',
    )

    def __str__(self):
        opt = self.option_num
        ques = self.question.pk
        return (str(ques)+opt)


class Attempt(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=CASCADE)
    # Question = models.ForeignKey(Question, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    total_score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str: return self.pk

class User_Answer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=CASCADE)
    question = models.ForeignKey(Question, on_delete=CASCADE)
    user_ans = models.ForeignKey(Option, on_delete=CASCADE, null=True)
