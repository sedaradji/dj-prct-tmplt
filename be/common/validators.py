"""Validators"""
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

human_name_validator = RegexValidator(
    regex=r"^[a-zA-Z\-'\s]*$",
    message=_("Names should only contain letters, hyphens, apostrophes, or spaces."),
    code="invalid_name",
)
