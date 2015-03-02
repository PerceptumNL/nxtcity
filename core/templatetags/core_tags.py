from django import template

register = template.Library()

def has_menu_children(page):
    return page.get_children().live().in_menu().exists()

@register.assignment_tag(takes_context=True)
def get_site_root(context, current_page):
    """Return the root of this site.
    In case the root is a LanguageRedirectionPage, the returned page is the
    child under root that is also an ancestor of current_page.
    """
    root_page = context['request'].site.root_page
    try:
        root_page.languageredirectionpage
    except root.RelatedObjectDoesNotExist:
        return root_page
    else:
        page_ptr = current_page
        while page_ptr.get_parent() != root_page:
            page_ptr = page_ptr.get_parent()
        return page_ptr

@register.assignment_tag(takes_context=True)
def get_site_language(context, current_page):
    """Return the language of this site.
    In case the site's root page is a LanguageRedirectionPage,
      the language of its LandingPage child is returned.
    Else the output of Django's translation.get_language is used.
    """
    #TODO: Generalize this function to remove LandingPage specifics.
    root_page = get_site_root(context, current_page)
    try:
        landing_page = root_page.landingpage
    except root_page.RelatedObjectDoesNotExist:
        from django.utils import translation
        return translation.get_language()
    else:
        return landing_page.language

@register.inclusion_tag('core/tags/navbar.html', takes_context=True)
def navbar(context, parent, calling_page=None):
    menuitems = parent.get_children().filter(
        live=True,
        show_in_menus=True
    )
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

