from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=150)

class Variant(models.Model):
    name = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='variants')

class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)