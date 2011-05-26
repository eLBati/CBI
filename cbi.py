# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Lorenzo Battistini (<lorenzo.battistini@domsense.com>).
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

# This module helps handling CBI files
# (see http://www.cbi-org.eu for standard)
# See README for more info

# Struttura del record di testa - codice fisso "IM"
IM = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 8, 'mittente'),
    (9, 13, 'ricevente'),
    (14, 19, 'data_creazione'),
    (20, 39, 'nome_supporto'),
    (40, 45, 'campo_a_disposizione'),
    (46, 104, 'filler2'),
    (105, 105, 'tipo_flusso'),
    (106, 106, 'qualificatore_flusso'),
    (107, 111, 'soggetto_veicolatore'),
    (112, 113, 'filler3'),
    (114, 114, 'codice_divisa'),
    (115, 115, 'filler4'),
    (116, 120, 'campo_non_disponibile'),
    ]

# Struttura del record di coda - codice fisso "EF"
EF = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 8, 'mittente'),
    (9, 13, 'ricevente'),
    (14, 19, 'data_creazione'),
    (20, 39, 'nome_supporto'),
    (40, 45, 'campo_a_disposizione'),
    (46, 52, 'numero_disposizioni'),
    (53, 67, 'tot_importi_negativi'),
    (68, 82, 'tot_importi_positivi'),
    (83, 89, 'numero_record'),
    (90, 113, 'filler2'),
    (114, 114, 'codice_divisa'),
    (115, 120, 'campo_non_disponibile'),
    ]

# Struttura del record - codice fisso “14”
XIV = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 22, 'filler2'),
    (23, 28, 'data_pagamento'),
    (29, 33, 'causale'),
    (34, 46, 'importo'),
    (47, 47, 'segno'),
    (48, 52, 'codice_abi_banca'),
    (53, 57, 'cab_banca'),
    (58, 69, 'conto'),
    (70, 91, 'filler3'),
    (92, 96, 'codice_azienda'),
    (97, 97, 'tipo_codice'),
    (98, 113, 'codice_cliente_debitore'),
    (114, 119, 'filler4'),
    (120, 120, 'codice_divisa'),
    ]

# Tipo record 16 (coordinate ordinante)
XVI = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 12, 'codice_paese'),
    (13, 14, 'check_digit'),
    (15, 15, 'cin'),
    (16, 20, 'codice_abi'),
    (21, 25, 'codice_cab'),
    (26, 37, 'numero_conto'),
    (38, 44, 'filler2'),
    (45, 120, 'filler3'),
    ]

# Struttura del record - codice fisso “20”
XX = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 34, '1_segmento'),
    (35, 58, '2_segmento'),
    (59, 82, '3_segmento'),
    (83, 106, '4_segmento'),
    (107, 120, 'filler2'),
    ]

# Struttura del record - codice fisso “30”
XXX = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 40, '1_segmento'),
    (41, 70, '2_segmento'),
    (71, 86, 'codice_fiscale_cliente'),
    (87, 120, 'filler2'),
    ]

# Struttura del record - codice fisso “40”
XL = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 40, 'indirizzo'),
    (41, 45, 'cap'),
    (46, 70, 'comune_e_sigla_provincia'),
    (71, 98, 'completamento_indirizzo'),
    (99, 100, 'codice_paese'),
    (101, 120, 'filler2'),
    ]

# Struttura del record - codice fisso “50”
L = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 50, '1_segmento'),
    (51, 90, '2_segmento'),
    (91, 120, 'filler2'),
    ]

# Struttura del record - codice fisso “51”
LI = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 20, 'numero_disposizione'),
    (21, 74, 'filler2'),
    (75, 86, 'codice_identificativo_univoco'),
    (87, 120, 'filler3'),
    ]

# Struttura del record - codice fisso “59”
LIX = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 65, '1_segmento'),
    (66, 120, '2_segmento'),
    ]

# Struttura del record - codice fisso “70”
LXX = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 93, 'filler2'),
    (94, 94, 'tipo_bollettino'),
    (95, 95, 'filler3'),
    (96, 100, 'campo_a_disposizione'),
    (101, 120, 'chiavi_di_controllo'),
    ]

# Struttura del record di testa - codice fisso “IB”
IB = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 8, 'mittente'),
    (9, 13, 'ricevente'),
    (14, 19, 'data_creazione'),
    (20, 39, 'nome_supporto'),
    (40, 45, 'campo_a_disposizione'),
    (46, 104, 'filler2'),
    (105, 105, 'tipo_flusso'),
    (106, 106, 'qualificatore_flusso'),
    (107, 111, 'soggetto_veicolatore'),
    (112, 113, 'filler3'),
    (114, 114, 'codice_divisa'),
    (115, 115, 'filler4'),
    (116, 120, 'campo_non_disponibile'),
    ]

RECORD_MAPPING = {
    'IM': IM,
    'EF': EF,
    '14': XIV,
    '16': XVI,
    '20': XX,
    '30': XXX,
    '40': XL,
    '50': L,
    '51': LI,
    '59': LIX,
    '70': LXX,
    'IB': IB,
    }


#TODO add fields validation as specified in standard
class Field(object):

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


class Record(object):

    #we create EF record structure by default
    def __init__(self, rawrecord='EF'):
        self.fields = []
        if len(rawrecord) == 2:
            code = rawrecord
        elif len(rawrecord) == 120:
            code = rawrecord[1:3]
        else:
            raise TypeError('String (%s) must contain 2 or 120 chars'
                % rawrecord)
        if code not in RECORD_MAPPING:
            raise IndexError('Unknown record type %s' % code)
        for field_args in RECORD_MAPPING[code]:
            newfield = Field(*field_args)
            if field_args[2] == 'tipo_record':
                newfield.content = code
            self.appendfield(newfield)
        if len(rawrecord) == 120:
            self.readrawrecord(rawrecord)

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
                    return field.content.strip() # strip o non strip?
            raise IndexError('Impossible to find field with key %s' % key)
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
            raise IndexError('Impossible to find field with position %i, %i'
                % (key.start, key.stop))
        elif isinstance(key, str):
            for field in self.fields:
                if field.name == key:
                    if len(item) > field.length():
                        raise BufferError(
                            'Specified field value (%i) passes field capacity'
                            % len(item))
                    else:
                        field.content = item.ljust(field.length())
                        return
            raise IndexError('Impossible to find field with key %s' % key)
        else:
            raise TypeError(
                'You must use slice or string to access fields list')

    def appendfield(self, field):
        if not isinstance(field, Field):
            raise TypeError('You can only append Field objects')
        if field.name in [f.name for f in self.fields]:
            raise IndexError('Field name %s already present' % field.name)
        self.fields.append(field)

    def readrawrecord(self, rawrecord):
        for field in self.fields:
            field.content = rawrecord[
                (field.fromposition - 1):field.toposition]


class Disposal(object):

    def __init__(self, records=[]):
        self.records = records

    def __getitem__(self, key):
        """Overloading in order to retrieve content by record code"""
        if isinstance(key, str):
            for record in self.records:
                if record['tipo_record'] == key:
                    return record
            raise IndexError('Impossible to find record %s' % key)
        else:
            raise TypeError('Key must be string')

    def __setitem__(self, key, item):
        """Overloading in order to write content by record code"""
        if not isinstance(item, Record):
            raise TypeError('You can only write Record objects')
        if isinstance(key, str):
            for record in self.records:
                if record['tipo_record'] == key:
                    record = item
            raise IndexError('Impossible to find field with key %s' % key)
        else:
            raise TypeError('Key must be string')


class Flow(object):

    def __init__(self, header=None, footer=None, disposals=[]):
        self.header = header
        self.footer = footer
        self.disposals = disposals

    def readfile(self, fileobj, lastrecordidentifier='70'):
        rows = []
        for line in fileobj:
            rows.append(line.replace('\r', '').replace('\n', ''))
        if len(rows) < 3:
            raise TypeError('Insufficient number of rows')
        self.header = Record(rows[0])
        self.footer = Record(rows[len(rows) - 1])
        self.disposals = []
        currentdisposal = Disposal()
        for row in rows[1:len(rows) - 1]:
            record = Record(row)
            currentdisposal.records.append(record)
            if record['tipo_record'] == lastrecordidentifier:
                self.disposals.append(currentdisposal)
                currentdisposal = Disposal()
        lastrecordfound = False
        for disposal in self.disposals:
            if lastrecordidentifier in [r['tipo_record']
                for r in disposal.records]:
                lastrecordfound = True
        if not lastrecordfound:
            self.disposals = []
            raise IndexError(
                'Last record identifier %s for disposals not found'
                % lastrecordidentifier)

    def writefile(self, filepath):  # TODO
        f = open(filepath, 'w')
