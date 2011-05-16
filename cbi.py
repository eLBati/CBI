# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Domsense s.r.l. (<http://www.domsense.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time

class Field():

    def __init__(self, fromposition, toposition, name, required=False, tp='an', check='N', desc=''):
        self.fromposition = fromposition
        self.toposition = toposition
        self.name = name
        self.required = required
        self.type = tp
        self.check = check
        self.desc = desc
        self.content = ''

    def __str__(self):
        return self.content

    def __getitem__(self, key):
        return self.content(key)

class Record():

    def __init__(self, code):
        self.code = code
        self.fields = []

class IMRecord(Record):

    def __init__(self):
        Record.__init__('IM')
