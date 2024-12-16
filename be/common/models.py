"""Common modeling logic"""
import uuid

from django.db import models


class BaseModel(models.Model):
    """Contains fields and logic needed for all DB models"""

    ##########
    # Fields #
    ##########

    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Activity info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def sguid(self):
        """Short GUID to display on admin"""
        return f"{str(self.guid)[:2]}...{str(self.guid)[-2:]}"

    class Meta:
        abstract = True
