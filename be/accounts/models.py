"""Accounts, users and companies models"""

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class User(AbstractUser, BaseModel):
    """User model"""

    # Relations

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
