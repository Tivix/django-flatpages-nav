from django.db import models
from django.contrib.flatpages.models import FlatPage


class FlatpagesNav(models.Model):
    """Defines whether a flatpage should appear in the main or footer nav and/or if this setting is currently active
    or not"""
    flatpage = models.ForeignKey(FlatPage)
    in_main_nav = models.BooleanField(default=False)
    in_footer_nav = models.BooleanField(default=False)
    order = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('order', )
    
    def __unicode__(self):
        return '%s (%s)' % (self.flatpage.title, 'Active' if self.active else 'Inactive')
