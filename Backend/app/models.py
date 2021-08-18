from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sample_rec = models.IntegerField()
    seq_last = models.IntegerField()
    sample_pen = models.IntegerField()
    sample_rejected = models.IntegerField()
    reason = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
