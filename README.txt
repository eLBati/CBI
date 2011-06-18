CBI Module
==========

Standard
--------

The Interbank Corporate Banking (<http://www.cbi-org.eu>), the Italian CBI, is
a telematic banking service allowing firms of all sizes to work directly,
through their computer, with all the banks they have relations with.

The CBI standards, defined by the Consortium, are aimed at a comprehensive
definition of Functions able to utterly satisfy Business requirements of both
Enterprises and Banks

The module
----------

The CBI module helps handling CBI records, letting you to write data within the
records or read data from the records

Example reading record:

$ python
>>> import cbi
>>> r = cbi.Record(' IM0123401234230311MIO NOME                                                                                      E      ')
>>> r['data_creazione']
'230311'
>>> r['nome_supporto']
'MIO NOME            '
>>> r['tipo_record']
'IM'

Example writing record:

>>> r = cbi.Record('IM')
>>> r['data_creazione'] = '300311'
>>> r['nome_supporto'] = 'MIO NOME BLA BLA BLA'
>>> r['codice_divisa'] = 'E'
>>> str(r)
' IM          300311MIO NOME BLA BLA BLA                                                                          E      '

It is possible to read/write by position too:

>>> r[14:19]
'300311'

Moreover, it is possibile to read the whole flow (file):

>>> flow = cbi.Flow()
>>> fileobj = open('MY_PATH/MY_FILE.txt')
>>> flow.readfile(fileobj)
>>> for disposal in flow.disposals:
...     print ('Codice: ' + disposal['51']['numero_disposizione']
...         + ' - importo: ' + str(float(disposal['14']['importo']) * 0.01)
...         + ' - Data: ' + disposal['14']['data_pagamento'])
... 
Codice: 4519 - importo: 145.0 - Data: 280209
Codice: 3059 - importo: 145.0 - Data: 280209
Codice: 18048 - importo: 160.0 - Data: 280211

Every flow is composed by N disposals and every disposal by N records.
