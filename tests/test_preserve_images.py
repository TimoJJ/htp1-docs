import unittest
from types import SimpleNamespace

from mkdocs.exceptions import PluginError

from hooks import preserve_images


class PreserveImagesTests(unittest.TestCase):
    def setUp(self):
        preserve_images.on_pre_build(None)
        self.page = SimpleNamespace(file=SimpleNamespace(src_uri="user-guide/example.md"))

    def capture(self, html):
        preserve_images.on_page_content(html, self.page)

    def test_lightbox_links_and_theme_images_are_allowed(self):
        self.capture('<p><img src="images/screen.png" alt="Screen"></p>')
        output = '<img src="logo.svg"><a class="glightbox"><img src="images/screen.png"></a>'
        self.assertEqual(preserve_images.on_post_page(output, self.page), output)

    def test_silent_image_removal_fails_with_page_and_source(self):
        self.capture('<p><img src="images/screen.png"></p>')
        with self.assertRaisesRegex(PluginError, r"user-guide/example.md: images/screen.png"):
            preserve_images.on_post_page('<p></p>', self.page)

    def test_removing_one_of_two_identical_images_fails(self):
        self.capture('<img src="screen.png"><img src="screen.png">')
        with self.assertRaisesRegex(PluginError, r"screen.png \(1\)"):
            preserve_images.on_post_page('<img src="screen.png">', self.page)

    def test_pages_and_builds_do_not_share_expected_images(self):
        self.capture('<img src="screen.png">')
        other = SimpleNamespace(file=SimpleNamespace(src_uri="other.md"))
        self.assertEqual(preserve_images.on_post_page('<p>Text</p>', other), '<p>Text</p>')
        preserve_images.on_pre_build(None)
        self.assertEqual(preserve_images.on_post_page('<p>Text</p>', self.page), '<p>Text</p>')
