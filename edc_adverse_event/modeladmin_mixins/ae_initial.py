from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from edc_action_item import action_fieldset_tuple
from edc_action_item.modeladmin_mixins import ActionItemModelAdminMixin
from edc_constants.constants import DEAD
from edc_model_admin import audit_fieldset_tuple
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from edc_notification.utils import get_email_contacts

from ..forms import AeInitialForm
from ..get_ae_model import get_ae_model
from ..templatetags.edc_adverse_event_extras import (
    format_ae_description,
    select_description_template,
)
from .modeladmin_mixins import AdverseEventModelAdminMixin

fieldset_part_one = (
    "Part 1: Description",
    {
        "fields": (
            "ae_classification",
            "ae_classification_other",
            "ae_description",
            "ae_awareness_date",
            "ae_start_date",
            "ae_grade",
        )
    },
)

fieldset_part_two = (
    "Part 2: Cause and relationship to study",
    {
        "fields": (
            "ae_study_relation_possibility",
            "study_drug_relation",
            "ae_cause",
            "ae_cause_other",
        )
    },
)

fieldset_part_three = ("Part 3: Treatment", {"fields": ("ae_treatment",)})

fieldset_part_four = (
    "Part 4: SAE / SUSAR",
    {"fields": ("sae", "sae_reason", "susar", "susar_reported")},
)

default_radio_fields = {
    "ae_cause": admin.VERTICAL,
    "ae_classification": admin.VERTICAL,
    "ae_grade": admin.VERTICAL,
    "ae_study_relation_possibility": admin.VERTICAL,
    "study_drug_relation": admin.VERTICAL,
    "sae": admin.VERTICAL,
    "sae_reason": admin.VERTICAL,
    "susar": admin.VERTICAL,
    "susar_reported": admin.VERTICAL,
}


class AeInitialModelAdminMixin(
    AdverseEventModelAdminMixin,
    ModelAdminSubjectDashboardMixin,
    ActionItemModelAdminMixin,
):

    form = AeInitialForm

    email_contact = get_email_contacts("ae_reports")
    additional_instructions = format_html(  # nosec B308, B703
        "Complete the initial AE report and forward to the TMG. "
        'Email to <a href="mailto:{}">{}</a>',
        mark_safe(email_contact),  # nosec B308, B703
        mark_safe(email_contact),  # nosec B308, B703
    )

    fieldsets = (
        (None, {"fields": ("subject_identifier", "report_datetime")}),
        fieldset_part_one,
        fieldset_part_two,
        fieldset_part_three,
        fieldset_part_four,
        action_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = default_radio_fields

    ordering = ["-tracking_identifier"]

    list_display = [
        "identifier",
        "dashboard",
        "description",
        "follow_up_reports",
        "user",
    ]

    list_filter = [
        "ae_awareness_date",
        "ae_grade",
        "ae_classification",
        "sae",
        "sae_reason",
        "susar",
        "susar_reported",
    ]

    search_fields = ["subject_identifier", "action_identifier", "tracking_identifier"]

    def if_sae_reason(self, obj):
        """Returns the SAE reason.

        If DEATH, adds link to the death report.
        """
        if obj.sae_reason.name == DEAD:
            death_report_cls = get_ae_model("deathreport")
            try:
                death_report = death_report_cls.objects.get(
                    subject_identifier=obj.subject_identifier
                )
            except ObjectDoesNotExist:
                link = '<font color="red">Death report pending</font>'
            else:
                url_name = f"{settings.ADVERSE_EVENT_APP_LABEL}_deathreport"
                namespace = self.admin_site.name
                url = reverse(f"{namespace}:{url_name}_changelist")
                link = format_html(  # nosec B308, B703
                    'See report <a title="go to Death report"'
                    'href="{}?q={}"><span nowrap>{}</span></a>',
                    mark_safe(url),  # nosec B308, B703
                    death_report.subject_identifier,
                    death_report.identifier,
                )
            return mark_safe(f"{obj.sae_reason.name}.<BR>{link}.")
        return obj.get_sae_reason_display()

    if_sae_reason.short_description = "If SAE, reason"

    @staticmethod
    def description(obj):
        """Returns a formatted comprehensive description of the SAE
        combining multiple fields.
        """
        context = format_ae_description({}, obj, 50)
        return render_to_string(select_description_template("aeinitial"), context)
