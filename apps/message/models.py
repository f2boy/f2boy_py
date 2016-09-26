from django.db import models
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    def __str__(self):
        return self.message_content + '-' + self.user_nick

    message_content = models.CharField(max_length=200, null=False, blank=False)
    user_nick = models.CharField(max_length=32, null=False, blank=False)
    create_time = models.DateTimeField('添加时间', default=timezone.now())
    paper_no = models.IntegerField(default=0)
