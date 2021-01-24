# TODO: Add correct copyright header

import django
import logging
import os
import sys

from django.test import SimpleTestCase, RequestFactory

logging.disable(logging.CRITICAL)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bba.settings')
django.setup()

scriptDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(scriptDir, "../"))

import views


class ViewTest_BetterBayAlliance(SimpleTestCase):
    """
    This class contains the unit tests for the view in the betterbay app.
    """

    def test_AIS_page_get(self):
        """
        Test the GET request to route bba/ais using the RequestFactory
        :return:
        """
        # Arrange
        status_code = 200
        view_class = views.AISView

        # Act
        request = RequestFactory().get('/bba/ais/')
        response = view_class.as_view()(request, *[], **{})

        # Assert
        self.assertEqual(response.status_code, status_code)
        self.assertTemplateUsed('ais.html')
        self.assertIn('https://www.vesselfinder.com/aismap.js', response.content.decode(), 'AIS url not found')

