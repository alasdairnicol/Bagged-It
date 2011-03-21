from piston.handler import AnonymousBaseHandler, BaseHandler
from munros.models import Munro, Section

class AnonymousMunroHandler(AnonymousBaseHandler):
    model = Munro
    fields = ('name', 'section', 'translation', 'height', 'summit_grid_ref',)

class MunroHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Munro
    anonymous = AnonymousMunroHandler
    fields = ('id', 'name', 'section', 'translation', 'height', 'summit_grid_ref',)


    def read(self, request, munro_id=None):
        """
        Returns a single munro is 'munro_id' is given,
        otherwise a subset
        """
        base = Munro.objects

        if munro_id:
            return base.get(pk=munro_id)
        else:
            return base.all()

class AnonymousSectionHandler(AnonymousBaseHandler):
    model = Section
    fields = ('name',)

class SectionHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Section
    anonymous = AnonymousSectionHandler
    fields = ('id', 'name',)

    def read(self, request, section_id=None):
        """
        Returns a single munro is 'section_id' is given,
        otherwise a subset
        """
        base = Section.objects

        if section_id:
            return base.get(pk=section_id)
        else:
            return base.all()
