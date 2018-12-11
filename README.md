# Django CMS Medium Plugin

[Django CMS](https://www.django-cms.org) plugin that show the lasts posts of a Medium blog.

## Setup

Add `cmsmedium` to `INSTALLED_APPS`.

## Entries

Example of data available in every entry


```python
{
    'title': 'ERC-1400: Evolution of a Security Token Standard',
    'link': 'https://blog.polymath.network/erc-1400-evolution-of-a-security-token-standard-1e25d12b9261?source=rss----5f051a102000---4',
    'id': 'https://medium.com/p/1e25d12b9261',
    'image': 'https://cdn-images-1.medium.com/max/1024/1*9lYIZdgqrX2e2giKMHlt6g.png',
    'tags': [
        {
            'term': 'ethereum',
            'scheme': None,
            'label': None
        },
        {
            'term': 'polymath',
            'scheme': None,
            'label': None
        }
    ],
    'author': 'Adam Dossa',
    'published_parsed': time.struct_time(tm_year=2018, tm_mon=12, tm_mday=10, tm_hour=21, tm_min=33, tm_sec=35, tm_wday=0, tm_yday=344, tm_isdst=0),
    'updated_parsed': time.struct_time(tm_year=2018, tm_mon=12, tm_mday=10, tm_hour=21, tm_min=33, tm_sec=35, tm_wday=0, tm_yday=344, tm_isdst=0),
    'content': '<figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*9lYIZdgqrX2e2giKMHlt6g.png" /></figure><p>The team at <a href="https://polymath.network">Polymath</a>, along with external contributors, published <a href="https://github.com/ethereum/EIPs/issues/1411">ERC-1400</a> around two months ago, following an extensive discussion and <a href="https://blog.polymath.network/security-token-roundtable-recap-30e7d371cf14">round\xa0table</a>.</p><p>Since then we’ve had a huge amount of interest and discussion on the GitHub...</p>'
 }
 ```