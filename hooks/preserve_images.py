"""Fail the build if a plugin removes images from rendered page content."""

from collections import Counter
from html.parser import HTMLParser

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority


class Images(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.sources = Counter()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            source = dict(attrs).get("src")
            if source:
                self.sources[source] += 1


_expected = {}


def on_pre_build(config, **kwargs):
    _expected.clear()


@event_priority(100)
def on_page_content(html, page, **kwargs):
    # Capture before the lightbox plugin transforms image elements.
    _expected[page.file.src_uri] = Images(html).sources


@event_priority(-100)
def on_post_page(output, page, **kwargs):
    missing = _expected.get(page.file.src_uri, Counter()) - Images(output).sources
    if missing:
        details = ", ".join(f"{source} ({count})" for source, count in sorted(missing.items()))
        raise PluginError(f"Images removed while rendering {page.file.src_uri}: {details}")
    return output
