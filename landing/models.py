from django.db import models
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

class LanguageRedirectionPage(Page):

    def serve(self, request):
        language = translation.get_language_from_request(request)
        return HttpResponseRedirect(self.url + language + '/')

class LandingPageSection(Orderable, models.Model):
    page = ParentalKey('LandingPage', related_name='sections')
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=50)
    body = RichTextField()

    panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('short_title'),
        FieldPanel('body', classname="full"),
    ]

class LandingPage(Page):
    language = models.CharField(max_length=10, null=False, blank=False,
            choices=settings.LANGUAGES)
    display_title = models.CharField(max_length=255)
    tag_line = models.CharField(max_length=255, null=False, blank=False)
    notification = RichTextField(blank=True, default="")
    footer_content = RichTextField()

LandingPage.content_panels = [
    FieldPanel('language'),
    FieldPanel('title'),
    FieldPanel('display_title'),
    InlinePanel(LandingPage, 'sections', label="Sections"),
    FieldPanel('tag_line'),
    FieldPanel('notification'),
    FieldPanel('footer_content', classname="full"),
]

@register_snippet
class Partner(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField(default="", null=False, blank=True)
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True,
            on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        ImageChooserPanel('logo')
    ]
