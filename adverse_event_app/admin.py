from django.contrib import admin
from edc_model_admin.history import SimpleHistoryAdmin

from edc_adverse_event.forms import AeFollowupForm, AeInitialForm
from edc_adverse_event.modeladmin_mixins import (
    AeFollowupModelAdminMixin,
    AeInitialModelAdminMixin,
)

from .models import AeFollowup, AeInitial


@admin.register(AeInitial)
class AeInitialAdmin(AeInitialModelAdminMixin, SimpleHistoryAdmin):
    form = AeInitialForm


@admin.register(AeFollowup)
class AeFollowupAdmin(AeFollowupModelAdminMixin, SimpleHistoryAdmin):
    form = AeFollowupForm
