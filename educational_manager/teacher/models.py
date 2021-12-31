from django.db import models
from django.conf import settings


# Create your models here.
class Prep(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=20, choices=(("Math", "Math"),
                                                       ("Science", "Science"),
                                                       ("English", "English"),
                                                       ("Social Studies", "Social Studies"),
                                                       ("Elective", "Elective"),
                                                       ))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ScopeAndSequence(models.Model):
    subject = models.CharField(max_length=20, choices=(("Math", "Math"),
                                                       ("Science", "Science"),
                                                       ("English", "English"),
                                                       ("Social Studies", "Social Studies"),
                                                       ("Elective", "Elective"),
                                                       ))
    grade_level = models.CharField(max_length=200)
    content = models.JSONField()


class Course(models.Model):
    prep = models.ForeignKey(Prep, on_delete=models.CASCADE)
    period = models.IntegerField()


class Standard(models.Model):
    code = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    subject = models.CharField(max_length=20, choices=(("Math", "Math"),
                                                       ("Science", "Science"),
                                                       ("English", "English"),
                                                       ("Social Studies", "Social Studies"),
                                                       ("Elective", "Elective"),
                                                       ))

    def __str__(self):
        return self.code


class KnowShowChart(models.Model):
    content = models.JSONField()
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def get_assessments(self):
        return self.assessment_set.all()

    def __str__(self):
        return f'{self.standard} created by {self.creator} on {self.created}'


class Assessment(models.Model):
    know_show_chart = models.ForeignKey(KnowShowChart, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def get_standard(self):
        return self.know_show_chart.standard

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    satisfied = models.JSONField()
    text = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def get_standard(self):
        return self.assessment.know_show_chart.standard

    def get_answers(self):
        return self.answer_set.all()

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question}, answer: {self.text}, correct: {self.correct}"
