from django.db import models

from wagtail.models import Page

import notebook.models


class HomePage(Page):
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['engagements'] = notebook.models.EngagementIndexPage.objects.live()
        return context
