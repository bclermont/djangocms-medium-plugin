import datetime
import urllib.parse

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

_URL_PATH_SEPARATOR = '/'
_URL_NETLOC = 'medium.com'
_URL_ROOT_MEDIUM = 'https://%s/' % _URL_NETLOC
_PATH_FEED = 'feed'

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
        parsed = urllib.parse.urlparse(self.url)
        if parsed.netloc == _URL_NETLOC:
            username = parsed.path.lstrip(_URL_PATH_SEPARATOR).rstrip(_URL_PATH_SEPARATOR)
            return _URL_ROOT_MEDIUM + _PATH_FEED + _URL_PATH_SEPARATOR + username
        return self.url.rstrip(_URL_PATH_SEPARATOR) + _URL_PATH_SEPARATOR + _PATH_FEED