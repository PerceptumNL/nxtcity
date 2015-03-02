from django.db import models
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

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
    """Creates a one-pager."""
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

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return unicode(self.name)

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')

class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    submit_text = models.CharField(max_length=255, default="Submit")

FormPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel(FormPage, 'form_fields', label="Form fields"),
    FieldPanel('submit_text', classname="full"),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
]
