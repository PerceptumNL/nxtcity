from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

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



"""
Page for a single challenge
"""
class ChallengePage(Page):
    body = RichTextField()
    organization = models.CharField(default = '', blank = True, max_length = 255)
    picture = models.ForeignKey('wagtailimages.Image', null = True, blank = True,
        on_delete = models.SET_NULL, related_name = '+')  
    short_description = models.CharField(default = '', blank = True, max_length = 255)
 
    """
    Define ancestor
    """
    def challenge_index(self):
        return self.get_ancestors().type(ChallengeIndexPage).last()

ChallengePage.content_panels = [
    FieldPanel('title', classname = "full title"),
    FieldPanel('body'),
    FieldPanel('short_description'),
    FieldPanel('organization'),
    ImageChooserPanel('picture')
]

"""
Page for displaying all the challenges 
Only a picture and a short description for every challenge
"""
class ChallengeIndexPage(Page):
    subpage_types = ['ChallengePage'] #Possible descendants
    body = RichTextField()

    """
    Retrieve descendants
    """
    def challenges(self):
        challenges = ChallengePage.objects.live().descendant_of(self)
        return challenges

ChallengeIndexPage.content_panels = [
    FieldPanel('title', classname = "full title"),
    FieldPanel('body')
]


"""
Seperate section for every partner 
"""
class PartnerPageSection(Orderable, models.Model):
    page = ParentalKey('PartnerPage', related_name = 'partners')
    title = models.CharField(default = '', max_length = 255, null = True, blank = True)
    body = models.CharField(default = '', max_length = 255, null = True, blank = True)
    logo = models.ForeignKey('wagtailimages.Image', null = True, blank = True,
        on_delete = models.SET_NULL, related_name = '+') 


PartnerPageSection.content_panels = [
    FieldPanel('title', classname = "full title"),
    FieldPanel('body'),
    ImageChooserPanel('logo')
]


"""
Page for displaying all our partners and link to form
"""
class PartnerPage(Page):
    body = RichTextField()

PartnerPage.content_panels = [
    FieldPanel('title', classname = "full title"),
    FieldPanel('body'),
    InlinePanel(PartnerPage, 'partners', label = "Partner")
]






