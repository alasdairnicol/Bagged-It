from django.conf.urls.defaults import patterns, include, url

from piston.resource import Resource
from baggedit.api.handlers import MunroHandler, SectionHandler

munro_handler = Resource(MunroHandler)
section_handler = Resource(SectionHandler)

urlpatterns = patterns('',
   # Munros
   url(r'^munros/(?P<munro_id>\d+)/$', munro_handler),
   url(r'^munros/$', munro_handler),

   # Sections
   url(r'^sections/(?P<section_id>\d+)/$', section_handler),
   url(r'^sections/$', section_handler),
)
