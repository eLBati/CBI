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

# Struttura del record del flusso di ritorno - codice fisso “14”
XIV_IN = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 22, 'filler2'),
    (23, 28, 'data_pagamento'),
    (29, 33, 'causale'),
    (34, 46, 'importo'),
    (47, 47, 'segno'),
    (48, 52, 'codice_abi_esattrice'),
    (53, 57, 'cab_esattrice'),
    (58, 69, 'filler3'),
    (70, 74, 'codice_abi_assuntrice'),
    (75, 79, 'cab_assuntrice'),
    (80, 91, 'conto'),
    (92, 96, 'codice_azienda'),
    (97, 97, 'tipo_codice'),
    (98, 113, 'codice_cliente_debitore'),
    (114, 119, 'filler4'),
    (120, 120, 'codice_divisa'),
    ]

# Struttura del record del flusso di ritorno - codice fisso “51”
LI_IN = [
    (1, 1, 'filler1'),
    (2, 3, 'tipo_record'),
    (4, 10, 'numero_progressivo'),
    (11, 20, 'numero_disposizione'),
    (21, 74, 'filler2'),
    (75, 86, 'codice_identificativo_univoco'),
    (87, 91, 'importo'),
    (92, 97, 'valuta_di_addebito'),
    (98, 109, 'riferimento'),
    (110, 115, 'data_effettiva_di_pagamento'),
    ]

OUTPUT_RECORD_MAPPING = {
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

INPUT_RECORD_MAPPING = {
    'IM': IM,
    'EF': EF,
    '14': XIV_IN,
    '20': XX,
    '30': XXX,
    '40': XL,
    '50': L,
    '51': LI_IN,
    '59': LIX,
    '70': LXX,
    'IB': IB,
    }
