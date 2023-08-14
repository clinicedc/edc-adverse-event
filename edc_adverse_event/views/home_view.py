from django.conf import settings
from django.views.generic import TemplateView
from edc_dashboard.url_names import url_names
from edc_dashboard.view_mixins import EdcViewMixin, UrlRequestContextMixin
from edc_navbar import NavbarViewMixin

from ..constants import ADVERSE_EVENT_ADMIN_SITE
from ..utils import get_adverse_event_app_label


class AeHomeView(UrlRequestContextMixin, EdcViewMixin, NavbarViewMixin, TemplateView):
    ae_listboard_url = "ae_listboard_url"
    death_report_listboard_url = "death_report_listboard_url"
    navbar_selected_item = "ae_home"
    template_name = f"edc_adverse_event/bootstrap{settings.EDC_BOOTSTRAP}/ae/ae_home.html"
    url_name = "ae_home_url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context = self.add_url_to_context(
            new_key="ae_home_url", existing_key=self.url_name, context=context
        )
        context.update(ADVERSE_EVENT_ADMIN_SITE=get_adverse_event_app_label())
        context.update(ADVERSE_EVENT_APP_LABEL=get_adverse_event_app_label())
        app_list_url = f"{ADVERSE_EVENT_ADMIN_SITE}:app_list"
        ae_listboard_url = url_names.get(self.ae_listboard_url)
        death_report_listboard_url = url_names.get(self.death_report_listboard_url)
        context.update(
            app_list_url=app_list_url,
            ae_listboard_url=ae_listboard_url,
            death_report_listboard_url=death_report_listboard_url,
        )
        return context
