"""Common admin utils"""
from django.contrib.admin.widgets import AdminTextInputWidget
from django.urls import reverse
from django.utils.html import format_html


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return "-"
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


def override_text_area_admin_factory(base_class: type):
    """Used to display an input instead of a textarea for desired fields"""

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.override_textarea_input:
            kwargs["widget"] = AdminTextInputWidget
        return base_class.formfield_for_dbfield(self, db_field, **kwargs)

    return type(
        "OverrideTextAreaInput" + base_class.__name__,
        (base_class,),
        {
            "formfield_for_dbfield": formfield_for_dbfield,
            "override_textarea_input": [],
        },
    )
