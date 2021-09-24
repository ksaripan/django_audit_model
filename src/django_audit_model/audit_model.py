from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils import timezone


class AuditModel(models.Model):
    created_by = models.ForeignKey(User, related_name='create_%(class)s', editable=False)
    created_date = models.DateTimeField(editable=False)
    modified_by = models.ForeignKey(User, related_name='modify_%(class)s', editable=False)
    modified_date = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    @transaction.atomic()
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # On save, update timestamps
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        super(AuditModel, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u''
