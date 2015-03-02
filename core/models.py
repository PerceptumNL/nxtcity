from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField


class HomePage(Page):
    pass

class BlankPage(Page):
    body = RichTextField()

BlankPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('body')
]
