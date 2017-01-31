from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.IntegerField()

    def __str__(self):
        return '%s(%d)' % (self.name, self.user_id)


class Problem(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    problem_id = models.IntegerField()

    def __str__(self):
        return '%s[id=%d, %dpt]' % (self.name, self.problem_id, self.points)


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Submission time')
    submission_id = models.IntegerField()
    verdict = models.IntegerField()
    lang = models.CharField(max_length=15)

    def __str__(self):
        res = '%s: %s' % (str(self.user), str(self.problem))
        res += ' (%s/%s) %d' % (self.verdict, self.lang, self.submission_id)
        return res


class Contest(models.Model):
    start_time = models.DateTimeField('Contest start time')
    end_time = models.DateTimeField('Contest end time')
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)
    problems = models.ManyToManyField(Problem)

    def __str__(self):
        return self.name
