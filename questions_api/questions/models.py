from django.db import models


class Questions(models.Model):
    jservice_id = models.IntegerField(unique=True, blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    question = models.TextField(blank=False, null=False)
    jservice_created_at = models.DateTimeField(auto_now=False, blank=False, null=False)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
