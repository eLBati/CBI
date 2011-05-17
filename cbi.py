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
            by position or field name as specified by CBI docs"""
        if isinstance(key, slice) and not key.step:
            return self.__str__()[key.start - 1:key.stop]
        elif isinstance(key, str):
            for field in self.fields:
                if field.name == key:
                    return field.content
            raise IndexError('Impossible to find field with that key')
        else:
            return self.__str__()[key]

    def __setitem__(self, key, item):
        """Overloading in order to write content
            by position or field name as specified by CBI docs"""
        if isinstance(key, slice) and not key.step:
            for field in self.fields:
                if (field.fromposition == key.start
                    and field.toposition == key.stop):
                    field.content = item
                    return
            raise IndexError('Impossible to find field with that position')
        elif isinstance(key, str):
            for field in self.fields:
                if field.name == key:
                    if len(item) > field.length():
                        raise BufferError(
                            'Specified field value passes field capacity')
                    else:
                        field.content = item.ljust(field.length())
                        return
            raise IndexError('Impossible to find field with that key')
        else:
            raise TypeError(
                'You must use slice or string to access fields list')

    def appendfield(self, field):
        if not isinstance(field, Field):
            raise TypeError('You can only append Field objects')
        if field.name in [f.name for f in self.fields]:
            raise IndexError('Field name already present')
        self.fields.append(field)

    def readrawrecord(self, rawrecord):
        for field in self.fields:
            field.content = rawrecord[
                (field.fromposition - 1):field.toposition]


class IMRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, 'IM')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 8, 'mittente'))
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
        if rawrecord:
            self.readrawrecord(rawrecord)


class EFRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, 'EF')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 8, 'mittente'))
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
        if rawrecord:
            self.readrawrecord(rawrecord)


class XIVRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '14')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 22, 'filler2'))
        self.appendfield(Field(23, 28, 'data_pagamento'))
        self.appendfield(Field(29, 33, 'causale'))
        self.appendfield(Field(34, 46, 'importo'))
        self.appendfield(Field(47, 47, 'segno'))
        self.appendfield(Field(48, 52, 'codice_abi_banca'))
        self.appendfield(Field(53, 57, 'cab_banca'))
        self.appendfield(Field(58, 69, 'conto'))
        self.appendfield(Field(70, 91, 'filler3'))
        self.appendfield(Field(92, 96, 'codice_azienda'))
        self.appendfield(Field(97, 97, 'tipo_codice'))
        self.appendfield(Field(98, 113, 'codice_cliente_debitore'))
        self.appendfield(Field(114, 119, 'filler4'))
        self.appendfield(Field(120, 120, 'codice_divisa'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class XVIRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '16')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 12, 'codice_paese'))
        self.appendfield(Field(13, 14, 'check_digit'))
        self.appendfield(Field(15, 15, 'cin'))
        self.appendfield(Field(16, 20, 'codice_abi'))
        self.appendfield(Field(21, 25, 'codice_cab'))
        self.appendfield(Field(26, 37, 'numero_conto'))
        self.appendfield(Field(38, 44, 'filler2'))
        self.appendfield(Field(45, 120, 'filler3'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class XXRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '20')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 34, '1_segmento'))
        self.appendfield(Field(35, 58, '2_segmento'))
        self.appendfield(Field(59, 82, '3_segmento'))
        self.appendfield(Field(83, 106, '4_segmento'))
        self.appendfield(Field(107, 120, 'filler2'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class XXXRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '30')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 40, '1_segmento'))
        self.appendfield(Field(41, 70, '2_segmento'))
        self.appendfield(Field(71, 86, 'codice_fiscale_cliente'))
        self.appendfield(Field(87, 120, 'filler2'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class XLRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '40')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 40, 'indirizzo'))
        self.appendfield(Field(41, 45, 'cap'))
        self.appendfield(Field(46, 70, 'comune_e_sigla_provincia'))
        self.appendfield(Field(71, 98, 'completamento_indirizzo'))
        self.appendfield(Field(99, 100, 'codice_paese'))
        self.appendfield(Field(101, 120, 'filler2'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class LRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '50')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 50, '1_segmento'))
        self.appendfield(Field(51, 90, '2_segmento'))
        self.appendfield(Field(91, 120, 'filler2'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class LIRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '51')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 20, 'numero_disposizione'))
        self.appendfield(Field(21, 74, 'filler2'))
        self.appendfield(Field(75, 86, 'codice_identificativo_univoco'))
        self.appendfield(Field(87, 120, 'filler3'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class LIXRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '59')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 65, '1_segmento'))
        self.appendfield(Field(66, 120, '2_segmento'))
        if rawrecord:
            self.readrawrecord(rawrecord)


class LXXRecord(Record):

    def __init__(self, rawrecord=''):
        Record.__init__(self, '70')
        self.appendfield(Field(1, 1, 'filler1'))
        self.appendfield(Field(2, 3, 'tipo_record', content=self.code))
        self.appendfield(Field(4, 10, 'numero_progressivo'))
        self.appendfield(Field(11, 93, 'filler2'))
        self.appendfield(Field(94, 94, 'tipo_bollettino'))
        self.appendfield(Field(95, 95, 'filler3'))
        self.appendfield(Field(96, 100, 'campo_a_disposizione'))
        self.appendfield(Field(101, 120, 'chiavi_di_controllo'))
        if rawrecord:
            self.readrawrecord(rawrecord)
