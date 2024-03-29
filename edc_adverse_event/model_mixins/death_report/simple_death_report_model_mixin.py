from django.db import models
from edc_action_item.managers import (
    ActionIdentifierModelManager,
    ActionIdentifierSiteManager,
)
from edc_action_item.models import ActionModelMixin
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_model.validators import date_not_future, datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start
from edc_sites.model_mixins import SiteModelMixin
from edc_utils import get_utcnow

from ...constants import DEATH_REPORT_ACTION


class SimpleDeathReportModelMixin(
    UniqueSubjectIdentifierFieldMixin,
    SiteModelMixin,
    ActionModelMixin,
    models.Model,
):
    action_name = DEATH_REPORT_ACTION

    death_date_field = "death_date"

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[datetime_not_before_study_start, datetime_not_future],
        default=get_utcnow,
    )

    death_datetime = models.DateTimeField(
        validators=[datetime_not_future],
        verbose_name="Date and Time of Death",
        null=True,
        blank=False,
    )

    death_date = models.DateField(
        validators=[date_not_future],
        verbose_name="Date of Death",
        null=True,
        blank=False,
    )

    narrative = models.TextField(verbose_name="Narrative")

    objects = ActionIdentifierModelManager()

    on_site = ActionIdentifierSiteManager()

    def natural_key(self):
        return (self.action_identifier,)

    class Meta(ActionModelMixin.Meta):
        abstract = True
        verbose_name = "Death Report"
        verbose_name_plural = "Death Reports"
        indexes = ActionModelMixin.Meta.indexes + [
            models.Index(fields=["subject_identifier", "action_identifier", "site", "id"])
        ]
