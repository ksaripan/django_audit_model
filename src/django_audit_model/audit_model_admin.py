from django.contrib import admin


class AuditModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        # Check if the object is newly created
        if obj.pk is None:
            obj.created_by = request.user
        super(AuditModelAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        return super(AuditModelAdmin, self).get_readonly_fields(request, obj) + \
               ('modified_by', 'created_by', 'created_date', 'modified_date')
