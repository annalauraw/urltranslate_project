from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    # path(_("welcome"), views.translate_url, name="welcome"),
    path(_("welcome"), views.translate_url),
]
