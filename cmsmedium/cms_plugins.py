__version__ = "0.1"

"""
Django CMS plugin that render posts of medium
"""

import logging
from html.parser import HTMLParser

import feedparser
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from django.utils import timezone

from .models import MediumWebsite


LOGGER = logging.getLogger(__name__)


class firstImageParser(HTMLParser):
    image = None

    def handle_starttag(self, tag, attrs):
        if self.image is not None:
            return
        if tag != "img":
            return
        for attr, value in attrs:
            if attr == 'src':
                self.image = value


class MediumPlugin(CMSPluginBase):
    """
    Plugin that render template with medium posts information
    """
    cache = False
    module = _('Medium blog posts')
    model = MediumWebsite
    render_template = "cmsmedium/entries.html"


    def render(self, context, instance, placeholder):
        context = CMSPluginBase.render(self, context, instance, placeholder)
        cache_key = "%s-%s-%d-%d" % (self.__class__.__name__, instance.url,
                        instance.cache.seconds, instance.posts)
        entries = cache.get(cache_key)
        if entries is None:
            LOGGER.debug("Parse RSS feed %s", instance.rss_url)
            output = feedparser.parse(instance.rss_url)
            entries = output['entries'][0:instance.posts]
            for i in range(0, len(entries)):
                entries[i]['content'] = entries[i]['summary']
                for key in ('summary', 'title_detail', 'links', 'guidislink', 'authors',
                            'author_detail', 'published', 'updated'):
                    del entries[i][key]
                parser = firstImageParser()
                parser.feed(entries[i]['content'])
                entries[i]['image'] = parser.image
                entries[i]['published_parsed'] =  timezone.make_aware(
                    timezone.datetime(*entries[i]['published_parsed'][:-3]),
                    timezone.get_default_timezone()
                )
            cache.set(cache_key, entries, timeout=instance.cache.seconds)
            LOGGER.debug("Parsed RSS feed %s: %d entries", instance.url, len(output['entries']))
        else:
            LOGGER.debug("Cached value")
        context['medium_entries'] = entries
        context['medium_url'] = instance.url
        return context


plugin_pool.register_plugin(MediumPlugin)