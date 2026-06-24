from django.db import models
from django.contrib.auth.models import User


class InterviewSession(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job_title = models.CharField(max_length=255)

    experience_years = models.IntegerField()

    job_description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Question(models.Model):
    session = models.ForeignKey(
        InterviewSession,
        on_delete=models.CASCADE
    )

    question = models.TextField()

    question_type = models.CharField(
        max_length=50
    )


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    answer = models.TextField()

    score = models.FloatField(
        null=True,
        blank=True
    )

    feedback = models.TextField(
        blank=True
    )