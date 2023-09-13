from django.urls import path
from contactslist.views import *

urlpatterns = [
    path("contactslist/", display, name="display"),
]
