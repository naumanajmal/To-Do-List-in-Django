from django.contrib import admin
from .models import *
from django.db import models

from tinymce.widgets import TinyMCE

admin.site.register(Task)

# Register your models here.
