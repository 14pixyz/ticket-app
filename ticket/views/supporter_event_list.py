from django.views.generic import TemplateView

class EventlistView(TemplateView):
    template_name = "supporter/event-list.html"