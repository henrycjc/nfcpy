# -*- coding: latin-1 -*-
# -----------------------------------------------------------------------------
# Copyright 2013-2014 Stephen Tiedemann <stephen.tiedemann@gmail.com>
#
# Licensed under the EUPL, Version 1.1 or - as soon they 
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# http://www.osor.eu/eupl
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
# -----------------------------------------------------------------------------

import logging
log = logging.getLogger(__name__)

from tag import activate, emulate

class Tag(object):
    @property
    def type(self):
        return self.TYPE

    @property
    def product(self):
        return self._product if hasattr(self, "_product") else self.type

    @property
    def identifier(self):
        return str(self.uid if hasattr(self, "uid") else self.idm)

    def __str__(self):
        try: s = self.type + ' ' + repr(self._product)
        except AttributeError: s = self.type
        return s + ' ID=' + self.identifier.encode("hex").upper()

class Error: pass
class AccessError(Error): pass
class CapacityError(Error): pass
