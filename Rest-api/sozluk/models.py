from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Word(models.Model):
    name = models.CharField(max_length=231)
    description = models.CharField(max_length=555)
    voice = models.CharField(max_length=252)
    partOfSpeech = models.CharField(max_length=77)
    example = models.CharField(max_length=567)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment", default=1)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="wordComment")
    content = models.CharField(max_length=255)
    commentDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.content
