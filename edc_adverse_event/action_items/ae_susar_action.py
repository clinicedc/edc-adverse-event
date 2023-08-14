from edc_action_item.action_with_notification import ActionWithNotification
from edc_constants.constants import HIGH_PRIORITY

from ..constants import ADVERSE_EVENT_ADMIN_SITE, AE_INITIAL_ACTION, AE_SUSAR_ACTION
from ..utils import get_adverse_event_app_label


class AeSusarAction(ActionWithNotification):
    name = AE_SUSAR_ACTION
    display_name = "Submit AE SUSAR Report"
    notification_display_name = "AE SUSAR Report"
    parent_action_names = [AE_INITIAL_ACTION]
    reference_model = f"{get_adverse_event_app_label()}.aesusar"
    related_reference_model = f"{get_adverse_event_app_label()}.aeinitial"
    related_reference_fk_attr = "ae_initial"
    create_by_user = False
    show_link_to_changelist = True
    admin_site_name = ADVERSE_EVENT_ADMIN_SITE
    instructions = "Complete the AE SUSAR report"
    priority = HIGH_PRIORITY
