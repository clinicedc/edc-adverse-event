from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from django.utils.translation import gettext as _
from edc_subject_dashboard.view_utils import ModelButton

if TYPE_CHECKING:
    from edc_model.models import BaseUuidModel

    from edc_adverse_event.model_mixins import (
        AeFollowupModelMixin,
        AeInitialModelMixin,
        DeathReportModelMixin,
        DeathReportTmgModelMixin,
    )

    class AeInitialModel(AeInitialModelMixin, BaseUuidModel): ...

    class AeFollowupModel(AeFollowupModelMixin, BaseUuidModel): ...

    class DeathReportTmgModel(DeathReportTmgModelMixin, BaseUuidModel): ...

    class DeathReportModel(DeathReportModelMixin, BaseUuidModel): ...


@dataclass
class TmgButton(ModelButton):
    model_obj: DeathReportTmgModel | DeathReportModel | AeFollowupModel | AeInitialModel = None
    next_url_name: str = "open_tmg_ae_listboard_url"
    only_user_created_may_access: bool | None = None
    forloop_counter: int | None = None
    colors: tuple[str, str, str] = field(default=("warning", "success", "success"))
    titles: tuple[str, str, str] = field(default=(_("Add"), _("Change"), _("View")))

    disable_all: bool = False

    @property
    def disabled(self) -> str:
        if self.disable_all:
            disabled = "disabled"
        else:
            disabled = super().disabled
            if (
                self.only_user_created_may_access
                and self.model_obj.user_created != self.user.username
            ):
                disabled = "disabled"
        return disabled

    @property
    def fa_icon(self) -> str:
        if self.disabled:
            return "fa-eye-slash"
        return super().fa_icon

    @property
    def btn_id(self) -> str:
        if self.forloop_counter is not None:
            return str(self.forloop_counter)
        return super().btn_id

    @property
    def title(self) -> str:
        if (
            self.model_obj
            and self.only_user_created_may_access
            and self.model_obj.user_created != self.user.username
        ):
            title = _("May only be edited by %(user)s") % {"user": self.model_obj.user_created}
            if self.model_obj.site.id != self.request.site.id:
                title = _("%(title)s when logged into site %(site)s") % {
                    "title": title,
                    "site": self.model_obj.site.id,
                }
        else:
            title = super().title
        return title

    @property
    def label(self) -> str:
        if (
            self.model_obj
            and self.only_user_created_may_access
            and self.model_obj.user_created != self.user.username
        ):
            return _("View")
        return _(super().label)
