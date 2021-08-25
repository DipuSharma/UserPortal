from django.db import models
from django.contrib.auth.models import User

@property
def total_user(self):
    return self.username, self.Data.user

class Data(models.Model):
    user = models.ForeignKey(User, verbose_name="username", on_delete=models.CASCADE, null=True, blank=True)
    Sample_received = models.IntegerField()
    Sequence_last = models.IntegerField()
    Sample_pending = models.IntegerField(null=True, blank=True)
    Sample_rejected = models.IntegerField(null=True, blank=True)
    Reason = models.CharField(max_length=200, blank=True)
    Remark = models.CharField(max_length=200, blank=True)
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    @property
    def total_pending(self):
        for d in Data:
            print(d.Sample_pending)
        return self.username, self.Data.user
