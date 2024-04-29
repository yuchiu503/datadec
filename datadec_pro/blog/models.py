from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# add this:
from wagtail.search import index

# keep the definition of BlogIndexPage model, and add the BlogPage model:

