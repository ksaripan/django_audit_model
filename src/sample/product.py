from django.db import models

from django_audit_model import AuditModel


class Product(AuditModel):
    barcode = models.CharField(max_length=20, unique=True, default='')
    name = models.CharField(max_length=100)
