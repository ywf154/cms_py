from django.contrib import admin

from repair_records.models import RepairRecord


class RepairRecordAdmin(admin.ModelAdmin):
    list_display = ('RecordName', 'work_time', 'price_per_hour', 'finish_time','cost')
    exclude = ['add_time']


admin.site.register(RepairRecord, RepairRecordAdmin)
