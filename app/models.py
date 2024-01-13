from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, null=True, blank=True)
    Sample_received = models.IntegerField()
    Sequence_last = models.IntegerField()
    Sample_pending = models.IntegerField(null=True, blank=True)
    Sample_rejected = models.IntegerField(null=True, blank=True)
    Reason = models.CharField(max_length=200, blank=True)
    Remark = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="last_login")

    def __str__(self):
        return self.Any_collaboration

    def save(self, *args, **kwargs):
        self.Sample_pending = (self.Sample_received - self.Sequence_last) - self.Sample_rejected
        if self.Sample_pending < 0:
            raise ValueError('Sample pending must be greater or equel to zero')
        super(Data, self).save(*args, **kwargs)

    
