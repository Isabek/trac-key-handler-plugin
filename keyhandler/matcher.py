import re
from trac.core import Component, implements
from trac.web import IRequestHandler


class KeyHandlerModule(Component):
    implements(IRequestHandler)

    def match_request(self, req):
        if re.match(r'/newticket', req.path_info):
            return True

    def process_request(self, req):
        return None

    def get_templates_dir(self):
        pass

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename

        return [('trac', resource_filename(__name__, 'htdocs'))]