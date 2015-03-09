from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField

from modelcluster.fields import ParentalKey


class HomePage(Page):
    pass

class BlankPage(Page):
    body = RichTextField()

BlankPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('body')
]

class BlogPage(Page):
    page = ParentalKey('FullBlogPage', related_name = 'blog_entries', null=True, blank=True, on_delete = models.SET_NULL)
    body = RichTextField()
    date = models.DateField("Post date")
    search_name = "Blog Page"

    indexed_fields = ('body', )

    class Meta:
        ordering = ['-date']

BlogPage.content_panels = [
    FieldPanel('page'),
    FieldPanel('title', classname = "full title"),
    FieldPanel('date'),
    FieldPanel('body', classname = "full"),
]


class FullBlogPage(Page):
    body = RichTextField()

FullBlogPage.content_panels = [
    FieldPanel('title', classname = "full title"),
    FieldPanel('body')
]


