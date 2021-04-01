from django.contrib import admin
from .models import Task

# Register your models here.
class TenInstanceAdminMixin(object):
    """Hides the "Add" button when there are 10 instances."""
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 10:
            return False
        return super(TenInstanceAdminMixin, self).has_add_permission(request)

class TaskAdmin(TenInstanceAdminMixin, admin.ModelAdmin):
     model = Task

admin.site.register(Task, TaskAdmin)