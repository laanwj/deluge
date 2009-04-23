#
# deluge/ui/web/webui.py
#
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
#   The Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor
#   Boston, MA    02110-1301, USA.
#

import server
from deluge.ui.ui import _UI, UI
from optparse import OptionGroup

class WebUI(UI):
    def __init__(self, args):
        import server
        deluge_web = server.DelugeWeb()
        deluge_web.start()

class Web(_UI):

    help = """Starts the Deluge web interface"""
    
    def __init__(self):
        super(Web, self).__init__("web")
        self.__server = server.DelugeWeb()
        
        group = OptionGroup(self.parser, "Web Options")
        group.add_option("-p", "--port", dest="port", type="int",
            help="Sets the port to be used for the webserver",
            action="store", default=None)
        self.parser.add_option_group(group)
    
    @property
    def server(self):
        return self.__server
    
    def start(self):
        super(Web, self).start()
        if self.options.port: self.server.port =  self.options.port
        self.server.start()

def start():
    web = Web()
    web.start()