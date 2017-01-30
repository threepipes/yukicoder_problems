from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.IntegerField()


class Problem(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    problem_id = models.IntegerField()


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Submission time')
    submission_id = models.IntegerField()
    verdict = models.IntegerField()
    lang = models.CharField(max_length=15)


class Contest(models.Model):
    start_time = models.DateTimeField('Contest start time')
    end_time = models.DateTimeField('Contest end time')
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)
    problems = models.ManyToManyField(Problem)
