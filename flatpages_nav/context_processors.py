from flatpages_nav.models import FlatpagesNav


def nav_flatpages(request):
    """Adds 2 lists (one each for main/footer nav) of flatpages to the template context."""
    d = {}
    d['main_nav_flatpages'] = map(lambda x: x.flatpage, FlatpagesNav.objects.filter(active=True, in_main_nav=True))
    d['footer_nav_flatpages'] = map(lambda x: x.flatpage, FlatpagesNav.objects.filter(active=True, in_footer_nav=True))
    return d
