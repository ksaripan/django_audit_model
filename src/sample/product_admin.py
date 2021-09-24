from django.contrib import admin

from django_audit_model import AuditModelAdmin
from .product import Product

@admin.register(Product)
class ProductAdmin(AuditModelAdmin):
    list_display = (...)
    list_display_links = (...)
    search_fields = (...)
    readonly_fields = (...)
    list_filter = (...)
