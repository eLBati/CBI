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

    def length(self):
        return (self.toposition - self.fromposition) + 1

    def __init__(self, fromposition, toposition, name, content=''):
        self.fromposition = fromposition
        self.toposition = toposition
        self.name = name
        if not content:
            self.content = ''.ljust(self.length())
        else:
            self.content = content

    def __str__(self):
        return self.content

class Record():

    def __init__(self, code):
        self.code = code
        self.fields = []

    def __str__(self):
        c = ''
        for field in self.fields:
            c = c + field.content
        return c

    def __getitem__(self, key):
        """Overloading in order to retrieve content
            by position or field name specified in CBI docs"""
        if isinstance(key, slice) and not key.step:
            return self[key.start-1:key.stop]
        elif isinstance(key, str):
            for field in self.fields:
                if field.name == key:
                    return field.content
            raise IndexError('Impossible to find field with that key')            
        else:
            return self[key]

    def __setitem__(self, key, item):
        """Overloading in order to write content
            by position or field name specified in CBI docs"""
        if isinstance(key, slice) and not key.step:
            for field in self.fields:
                if field.fromposition == key.start and field.toposition == key.stop:
                    field.content = item
                    return
            raise IndexError('Impossible to find field with that position')
        elif isinstance(key, str):
            for field in self.fields:
                if field.name == key:
                    if len(item) > field.length():
                        raise BufferError('Specified field value passes field capacity')
                    else:
                        field.content = item.ljust(field.length())
                        return
            raise IndexError('Impossible to find field with that key') 
        else:
            raise TypeError('You must use slice or string to access fields list')

    def appendfield(self, field):
        if not isinstance(key, Field):
            raise TypeError('You can only append Field objects')
        if field.name in [n for f.n in self.fields]:
            raise IndexError('Field name already present')
        self.fields.append(field)

class IMRecord(Record):

    def __init__(self):
        Record.__init__(self, 'IM')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content='IM'))
        self.appendfield(Field(4, 8, 'mittente')
        self.appendfield(Field(9, 13, 'ricevente'))
        self.appendfield(Field(14, 19, 'data_creazione'))
        self.appendfield(Field(20, 39, 'nome_supporto'))
        self.appendfield(Field(40, 45, 'campo_a_disposizione'))
        self.appendfield(Field(46, 104, 'filler2'))
        self.appendfield(Field(105, 105, 'tipo_flusso'))
        self.appendfield(Field(106, 106, 'qualificatore_flusso'))
        self.appendfield(Field(107, 111, 'soggetto_veicolatore'))
        self.appendfield(Field(112, 113, 'filler3'))
        self.appendfield(Field(114, 114, 'codice_divisa'))
        self.appendfield(Field(115, 115, 'filler4'))
        self.appendfield(Field(116, 120, 'campo_non_disponibile'))

class EFRecord(Record):

    def __init__(self):
        Record.__init__(self, 'IM')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content='EF'))
        self.appendfield(Field(4, 8, 'mittente')
        self.appendfield(Field(9, 13, 'ricevente'))
        self.appendfield(Field(14, 19, 'data_creazione'))
        self.appendfield(Field(20, 39, 'nome_supporto'))
        self.appendfield(Field(40, 45, 'campo_a_disposizione'))
        self.appendfield(Field(46, 52, 'numero_disposizioni'))
        self.appendfield(Field(53, 67, 'tot_importi_negativi'))
        self.appendfield(Field(68, 82, 'tot_importi_positivi'))
        self.appendfield(Field(83, 89, 'numero_record'))
        self.appendfield(Field(90, 113, 'filler2'))
        self.appendfield(Field(114, 114, 'codice_divisa'))
        self.appendfield(Field(115, 120, 'campo_non_disponibile'))


