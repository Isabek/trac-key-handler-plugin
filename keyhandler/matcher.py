import re
from trac.core import Component, implements
from trac.web import IRequestHandler
from trac.web.chrome import add_script


class KeyHandlerModule(Component):
    implements(IRequestHandler)

    def match_request(self, req):
        if re.match(r'/newticket', req.path_info):
            add_script(req, 'keyhandler/htdocs/js/main.js')
        return False

    def process_request(self, req):
        req.send_response(200)
        content = 'Hello world!'
        req.send_header('Content-Type', 'text/plain')
        req.send_header('Content-length', str(len(content)))
        req.end_headers()
        req.write(content)

    def get_templates_dir(self):
        pass

    def get_htdocs_dirs(self):
        pass