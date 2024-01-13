from django.contrib import admin
from .models import Data

# Register your models here.

from .models import (
    Data
)


@admin.register(Data)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Sample_received', 'Sequence_last', 'Sample_pending',
                    'Sample_rejected', 'Reason', 'Remark', 'created_at', 'updated_at']
