import datetime

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class MediumWebsite(CMSPlugin):
    """
    Website powerered by Medium
    """
    url = models.URLField(
        _("blog address"),
        help_text=_("URL of medium blog website"),
    )

    posts = models.PositiveSmallIntegerField(
        _("Maximum number of posts to display"),
        default=10,
    )
    
    cache = models.DurationField(
        _("Frequency to which check for new blog posts"),
        default=datetime.timedelta(minutes=10),
    )

    class Meta:
        verbose_name = _('Medium website')
        verbose_name_plural = _('Medium websites')

    def __unicode__(self):
        return self.url

    @property
    def rss_url(self):
        return self.url.rstrip("/") + "/feed"