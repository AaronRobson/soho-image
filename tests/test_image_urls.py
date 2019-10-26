import unittest

import soho_image as si

BASE_URL = 'https://sohowww.nascom.nasa.gov'


class TestImageUrls(unittest.TestCase):
    def test_static_large(self):
        expected = BASE_URL + '/data/realtime/%s/1024/latest.jpg'
        actual = si.ImagePathMask(animated=False, small=False)
        self.assertEqual(expected, actual)

    def test_static_small(self):
        expected = BASE_URL + '/data/realtime/%s/512/latest.jpg'
        actual = si.ImagePathMask(animated=False, small=True)
        self.assertEqual(expected, actual)

    def test_animated_large(self):
        expected = BASE_URL + '/data/LATEST/current_%s.gif'
        actual = si.ImagePathMask(animated=True, small=False)
        self.assertEqual(expected, actual)

    def test_animated_small(self):
        expected = BASE_URL + '/data/LATEST/current_%ssmall.gif'
        actual = si.ImagePathMask(animated=True, small=True)
        self.assertEqual(expected, actual)
