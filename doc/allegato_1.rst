Schema Allegato articolo 4 bis
==============================

Questa documentazione fornisce una guida dettagliata su come strutturare i dati finanziari secondo il JSON Schema "art4-bis-v1.0.0", facilitando l'interoperabilità e la standardizzazione dei dati per le amministrazioni pubbliche.

La norma

1. L'Agenzia per l'Italia digitale, d'intesa con il Ministero dell'economia e
delle finanze, al fine di promuovere l'accesso e migliorare la comprensione dei
dati relativi all'utilizzo delle risorse pubbliche, gestisce il sito internet
denominato "Soldi pubblici" che consente l'accesso ai dati dei pagamenti delle
pubbliche amministrazioni e ne permette la consultazione in relazione alla
tipologia di spesa sostenuta e alle amministrazioni che l'hanno effettuata, nonché
all'ambito temporale di riferimento.

2. Ciascuna amministrazione pubblica sul proprio sito istituzionale, in una parte
chiaramente identificabile della sezione "Amministrazione trasparente", i dati
sui propri pagamenti e ne permette la consultazione in relazione alla tipologia
di spesa sostenuta, all'ambito temporale di riferimento e ai beneficiari.

3. Per le spese in materia di personale si applica quanto previsto dagli articoli
da 15 a 20.

4. Dalle disposizioni di cui ai commi 1 e 2 non devono derivare nuovi o maggiori
oneri a carico della finanza pubblica. Le amministrazioni interessate provvedono
ai relativi adempimenti nell'ambito delle risorse umane, strumentali e finanziarie
disponibili a legislazione vigente.


Questo schema organizza e standardizza la pubblicazione delle informazioni finanziarie relative ai pagamenti effettuati dalle amministrazioni pubbliche.

.. image:: ../media/art.4-bis-v1.0.0.png

*Diagramma delle classi per lo schema dell'articolo 4 bis*

Schema: art4-bis-v1.0.0
Questo schema organizza e standardizza la pubblicazione delle informazioni finanziarie relative ai pagamenti effettuati dalle amministrazioni pubbliche.
Dettagli dei Campi

- Intestazione (Oggetto, Obbligatorio): Contiene le informazioni identificative dell'amministrazione pubblicatrice.
- Ambito Temporale di Riferimento (Oggetto, Obbligatorio): Indica il periodo di riferimento dei dati riportati.
- Sintesi Pagamenti (Array di Oggetti, Obbligatorio): Elenco dei pagamenti effettuati, classificati in categorie.

Dettagli dei Campi

Documentazione JSON Schema "art4-bis-v1.0.0"
============================================

Questo documento fornisce dettagli su come popolare il JSON basato sullo schema "art4-bis-v1.0.0", utilizzato per documentare i pagamenti delle amministrazioni pubbliche.

Definizioni Generali
---------------------

- **Intestazione** (Oggetto Obbligatorio)
  - ``amministrazione`` (Oggetto)
    - ``codiceFiscale``: Codice fiscale dell'amministrazione (Stringa, 11 cifre numeriche)
    - ``denominazione``: Nome formale dell'amministrazione (Stringa, max 256 caratteri)
    - ``ambito``: Campo enum che specifica l'obbligo di pubblicazione (Valori: "Soggetto tenuto all'obbligo di pubblicazione", "Soggetto tenuto parzialmente all'obbligo di pubblicazione", "Soggetto non tenuto all'obbligo di pubblicazione")
  - ``dataPubblicazione``: Data in cui i dati vengono pubblicati (Stringa, formato GG/MM/AAAA)

- **Ambito Temporale di Riferimento** (Oggetto Obbligatorio)
  - ``anno``: Anno di riferimento dei dati (Intero, minimo 2000, massimo 9999)
  - ``trimestre``: Trimestre dell'anno (Intero, minimo 1, massimo 4)

- **Sintesi Pagamenti** (Array di Oggetti Obbligatorio, minItems: 1)
  - Elementi dell'array (Oggetto):
    - ``uscitaCorrente``: Tipo di spesa corrente (Enum, opzionale, esclusivo con uscitaInContoCapitale)
    - ``uscitaInContoCapitale``: Tipo di spesa di capitale (Enum, opzionale, esclusivo con uscitaCorrente)
    - ``importo``: Ammontare del pagamento (Numero, minimo 0.01)
    - ``beneficiario``: Identificativo del beneficiario (Stringa, può essere "Soggetto privato" o un codice fiscale di 11 cifre)

Esempio di JSON
---------------

.. code-block:: json

    {
      "intestazione": {
        "amministrazione": {
          "codiceFiscale": "12345678901",
          "denominazione": "Comune di Esempio",
          "ambito": "Soggetto tenuto all'obbligo di pubblicazione"
        },
        "dataPubblicazione": "15/04/2025"
      },
      "ambitoTemporaleDiRiferimento": {
        "anno": 2025,
        "trimestre": 2
      },
      "sintesiPagamenti": [
        {
          "uscitaCorrente": "Acquisto di beni e di servizi",
          "importo": 15000.00,
          "beneficiario": "98765432109"
        },
        {
          "uscitaInContoCapitale": "Investimenti in beni materiali",
          "importo": 500000.00,
          "beneficiario": "Soggetto privato"
        }
      ]
    }

Procedure di Aggiornamento
--------------------------

Per garantire l'accuratezza e la tempestività delle informazioni, l'aggiornamento dei dati pubblicati attraverso questo schema deve essere eseguito seguendo una procedura specifica:

- **Aggiornamento Completo**: Non è sufficiente modificare singoli campi; piuttosto, è necessario fornire un nuovo documento JSON completo che rifletta tutte le informazioni aggiornate.
- **Data di Pubblicazione**: Ogni volta che i dati vengono aggiornati e pubblicati, la ``dataPubblicazione`` nell'intestazione deve essere aggiornata alla data corrente. Questo assicura che i lettori sappiano esattamente quando i dati sono stati rinnovati.

Esempio di Aggiornamento
------------------------

.. code-block:: json

    {
      "intestazione": {
        "amministrazione": {
          "codiceFiscale": "12345678901",
          "denominazione": "Comune di Esempio",
          "ambito": "Soggetto tenuto all'obbligo di pubblicazione"
        },
        "dataPubblicazione": "01/01/2026"  # Aggiornata alla data corrente di pubblicazione
      },
      "ambitoTemporaleDiRiferimento": {
        "anno": 2026,
        "trimestre": 1
      },
      "sintesiPagamenti": [
        {
          "uscitaCorrente": "Acquisto di beni e di servizi",
          "importo": 20000.00,  # Esempio di aggiornamento di un importo
          "beneficiario": "98765432109"
        },
        {
          "uscitaInContoCapitale": "Investimenti in beni immateriali",
          "importo": 750000.00,  # Aggiunto un nuovo pagamento
          "beneficiario": "Soggetto privato"
        }
      ]
    }

Raccomandazioni
---------------

Si raccomanda di verificare accuratamente i dati prima della loro pubblicazione per evitare la necessità di correzioni frequenti, che potrebbero minare la fiducia nelle informazioni diffuse.