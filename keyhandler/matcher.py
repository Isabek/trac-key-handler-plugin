import re

from trac.core import Component, implements
from trac.web import IRequestHandler
from trac.web.chrome import add_script, ITemplateProvider


class KeyHandlerModule(Component):
    implements(IRequestHandler, ITemplateProvider)

    def match_request(self, req):
        if re.match(r'/newticket', req.path_info):
            add_script(req, 'keyhandler/js/main.js')
        return False

    def process_request(self, req):
        req.send_response(200)
        content = 'Hello world!'
        req.send_header('Content-Type', 'text/plain')
        req.send_header('Content-length', str(len(content)))
        req.end_headers()
        req.write(content)

    def get_templates_dirs(self):
        pass

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename

        return [('keyhandler', resource_filename(__name__, 'htdocs'))]