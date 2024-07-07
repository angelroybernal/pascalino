from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.search import index

class EngagementIndexPage(Page):
    target = RichTextField(blank=True)
    scope = RichTextField(blank=True)

    def get_context(self, request):
        context = super(EngagementIndexPage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['host_pages'] = self.get_children().type(HostPage)
        context['app_pages'] = self.get_children().type(ApplicationPage)
        context['network_pages'] = self.get_children().type(NetworkPage)
        context['identity_pages'] = self.get_children().type(IdentityPage)
        context['test_pages'] = self.get_children().type(TestPage)
        context['notes'] = self.get_children().type(NotePage)
        return context

    content_panels = Page.content_panels + [
        FieldPanel('target'),
        FieldPanel('scope')
    ]

class ApplicationPage(Page):
    description = models.TextField(blank=False)

    def get_context(self, request):
        context = super(ApplicationPage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['identity_pages'] = self.get_children().type(IdentityPage)
        context['host_pages'] = self.get_children().type(HostPage)
        context['notes'] = self.get_children().type(NotePage)
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]

class NetworkPage(Page):
    description = models.TextField(blank=False)
    ip_range = models.CharField(
        blank=False,
        max_length=255,
        help_text='E. 192.168.1.0/24, 192.168.1.1-192.168.1.10'
    )

    def get_context(self, request):
        context = super(NetworkPage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['host_pages'] = self.get_children().type(HostPage)
        context['notes'] = self.get_children().type(NotePage)
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('ip_range'),
    ]

class HostPage(Page):
    hostname = models.CharField(blank=True, max_length=128)
    ip_address = models.GenericIPAddressField(blank=False)
    operating_system = models.CharField(blank=True, max_length=128)

    def get_context(self, request):
        context = super(HostPage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['service_pages'] = self.get_children().type(ServicePage)
        context['notes'] = self.get_children().type(NotePage)
        return context

    content_panels = Page.content_panels + [
        FieldPanel('hostname'),
        FieldPanel('ip_address'),
        FieldPanel('operating_system')
    ]

class ServicePage(Page):
    SERVICE_STATUS = {
        'open':'Open',
        'closed': 'Closed',
    }
    PROTOCOLS = {
        'tcp': 'TCP',
        'udp': 'UDP',
    }
    description = models.TextField(blank=True)
    port = models.IntegerField()
    protocol = models.CharField(max_length=3, choices=PROTOCOLS)
    status = models.CharField(max_length=6, choices=SERVICE_STATUS)

    def get_context(self, request):
        context = super(ServicePage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['notes'] = self.get_children().type(NotePage)
        return context

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('port'),
        FieldPanel('protocol'),
        FieldPanel('status'),
    ]

class IdentityPage(Page):
    description = models.TextField(blank=False)
    username = models.CharField(blank=True, max_length=128)
    email_address = models.EmailField(blank=True)
    credentials_retrieved = models.BooleanField(default=False)

    def get_context(self, request):
        context = super(IdentityPage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['notes'] = self.get_children().type(NotePage)
        return context

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('username'),
        FieldPanel('email_address'),
        FieldPanel('credentials_retrieved'),
    ]

class TestPage(Page):
    TEST_STATUS = {
        'detected': 'Detected',
        'stopped': 'Stopped',
        'failed': 'Failed',
        'successful': 'Successful',
    }
    target = RichTextField(blank=False)
    test_execution = models.DateTimeField()
    expected_behavior = RichTextField(blank=False)
    real_behavior = RichTextField(blank=True)
    test_status = models.CharField(max_length=10, choices=TEST_STATUS)

    def get_context(self, request):
        context = super(TestPage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        context['notes'] = self.get_children().type(NotePage)
        return context

    content_panels = Page.content_panels + [
        FieldPanel('target'),
        FieldPanel('test_execution'),
        FieldPanel('expected_behavior'),
        FieldPanel('real_behavior'),
        FieldPanel('test_status'),
    ]

class NotePage(Page):
    detail = RichTextField(blank=False)

    def get_context(self, request):
        context = super(NotePage, self).get_context(request)
        context['engagements'] = EngagementIndexPage.objects.live()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('detail'),
    ]