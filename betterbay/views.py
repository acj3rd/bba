# TODO: add copyright header

from django.views import View
from django.views.generic import TemplateView

import logging
import sys
import traceback as tb
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')


class AISView (TemplateView):
    """
    This class handles the display of the AIS page

    By default, it handles GET requests and renders the template based on the attribute "template_name".
    """
    template_name = "ais.html"

    def get(self, *args, **kwargs):
        """
        Handle the GET request for the AIS page
        :param args:
        :param kwargs:
        :return:
        """
        try:
            return render(self.request, self.template_name)

        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            logger.error(tb.format_exception(exc_type, exc_value, exc_tb))
