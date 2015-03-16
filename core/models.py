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

"""
Class for creating a separate page for every blog entry
"""
class BlogPage(Page):
    page = ParentalKey('FullBlogPage', related_name = 'blog_entries', null=True, blank=True, on_delete = models.SET_NULL)
    body = RichTextField()
    author = models.CharField(default = '', blank = True, null = True, max_length = 255)
    date = models.DateField("Post date")
    search_name = "Blog Page"

    indexed_fields = ('body', )
    
    """
    We want to order the entries on the index page from newest to oldest
    """
    class Meta:
        ordering = ['-date']

BlogPage.content_panels = [
    FieldPanel('page'),
    FieldPanel('title', classname = "full title"),
    FieldPanel('date'),
    FieldPanel('body', classname = "full"),
    FieldPanel('author')
]

"""
Class to display every blog entry on a single page
"""
class FullBlogPage(Page):
    body = RichTextField()

FullBlogPage.content_panels = [
    FieldPanel('title', classname = "full title"),
    FieldPanel('body')
]


