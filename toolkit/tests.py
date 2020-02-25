from django.test import SimpleTestCase

from .templatetags import toolkit


class ToolkitTestCase(SimpleTestCase):

    def test_spacer(self):
        self.assertEqual(toolkit.spacer('X'), ' X')
        self.assertEqual(toolkit.spacer(''), '')
        self.assertEqual(toolkit.spacer(None), '')
        self.assertEqual(toolkit.spacer(False), '')
        self.assertEqual(toolkit.spacer(True), ' True')
