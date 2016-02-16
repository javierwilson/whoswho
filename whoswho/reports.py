from django.utils.translation import gettext as _

from model_report.report import reports, ReportAdmin
from model_report.utils import usd_format, avg_column, sum_column, count_column

from models import Event, Contact

class EventReport(ReportAdmin):
    title = _('Event')
    model = Event
    fields = [
        'name',
        'place',
        'start',
        'self.men',
        'self.women',
        'self.total',
    ]
    list_filter = ('start',)
    list_order_by = ('start',)
    report_totals = {
        'self.men': sum_column,
        'self.women': sum_column,
        'self.total': sum_column,
    }

class ContactReport(ReportAdmin):
    title = _('Contact')
    model = Contact
    fields = [
        'first_name',
        'last_name',
        'sex',
    ]
    list_filter = ('events__event', 'events__event__start', 'events__event__monitor')
    list_order_by = ('first_name', 'last_name')
    list_group_by = ('sex')
    group_totals = {
        'sex': count_column,
    }
    type = 'chart'
    chart_types = ('pie', 'column', 'line')
    list_serie_fields = ('sex',)

reports.register('event-report', EventReport)
reports.register('contact-report', ContactReport)
