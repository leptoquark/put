Schema Allegato articolo 4 bis
==============================

Schemi di pubblicazione
-----------------------
Gli schemi rappresentano informazioni da pubblicare ex-novo nella Sezione “Amministrazione Trasparente” del sito istituzionale dell’amministrazione, sotto-sezione di primo livello “Pagamenti dell’amministrazione” e sotto-sezione di secondo livello “Dati sui pagamenti”.

Scarica lo Schema JSON
----------------------

Per facilitare l'implementazione e la verifica del JSON conforme ai requisiti dell'amministrazione pubblica, mettiamo a disposizione il JSON Schema completo. Puoi scaricare lo schema dal link sottostante per utilizzarlo nei tuoi progetti o per ulteriori test e validazioni.


.. raw:: html

    <a href="https://raw.githubusercontent.com/leptoquark/put/refs/heads/main/schemi/art4-bis-v1.0.0.schema.json" class="btn float-right" title="Download schema" >Scarica il JSON Schema<span class="fa fa-download"></span></a>




Questa documentazione fornisce una guida dettagliata su come strutturare i dati finanziari secondo il JSON Schema "art4-bis-v1.0.0", facilitando l'interoperabilità e la standardizzazione dei dati per le amministrazioni pubbliche.

Questo schema organizza e standardizza la pubblicazione delle informazioni finanziarie relative ai pagamenti effettuati dalle amministrazioni pubbliche.

Il diagramma seguente fornisce una rappresentazione visiva della struttura e delle relazioni tra i vari componenti del JSON Schema "art4-bis-v1.0.0". Questo schema è utilizzato per documentare e standardizzare la pubblicazione dei dati finanziari delle amministrazioni pubbliche, in particolare i dettagli dei pagamenti effettuati.

Il diagramma delle classi aiuta a visualizzare come i dati sono organizzati e come interagiscono tra loro, fornendo una chiara comprensione delle relazioni tra le diverse parti del schema. È uno strumento essenziale per gli sviluppatori che implementano questo schema nei loro sistemi e per gli analisti che devono comprendere la struttura dei dati.

Visualizzando le classi e le loro connessioni, gli utenti possono facilmente identificare quali dati sono necessari, come sono collegati e quali informazioni sono obbligatorie o opzionali.

.. image:: ../media/art.4-bis-v1.0.0.png
   :alt: Diagramma delle classi per lo schema dell'articolo 4 bis
   :align: center

Il diagramma mostra:

- **Intestazione**: Include informazioni identificative dell'amministrazione come il codice fiscale, la denominazione e l'ambito di pubblicazione.
- **Ambito Temporale di Riferimento**: Definisce l'anno e il trimestre di riferimento dei dati finanziari pubblicati.
- **Sintesi Pagamenti**: Array di oggetti che descrive i dettagli dei pagamenti, con possibilità di specificare se la spesa è corrente o in conto capitale, oltre all'importo e al beneficiario dei pagamenti.

Questo schema visivo è integrato nella documentazione per offrire un accesso immediato alla comprensione della struttura dei dati senza la necessità di analizzare il codice del JSON Schema.

Di seguito vengono mostrati i dettagli specifici di ciascun campo un esempio di come popolare il JSON seguendo questo schema.

Dettagli dei Campi
------------------
 
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| Campo                         | Tipo                  | Descrizione                                                                                                    |
+===============================+=======================+================================================================================================================+
| **Intestazione**              | Oggetto Obbligatorio  | Contiene i dati identificativi dell'amministrazione.                                                           |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| amministrazione               | Oggetto               | Dettagli dell'ente amministrativo.                                                                             |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| codiceFiscale                 | Stringa               | Codice fiscale dell'amministrazione (11 cifre numeriche).                                                      |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| denominazione                 | Stringa               | Nome formale dell'amministrazione (max 256 caratteri).                                                         |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| ambito                        | Enumerazione          | Specifica l'obbligo di pubblicazione ("Soggetto tenuto all'obbligo di pubblicazione", etc.).                   |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| dataPubblicazione             | Stringa               | Data di pubblicazione dei dati (formato GG/MM/AAAA).                                                           |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+

+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| Campo                         | Tipo                  | Descrizione                                                                                                    |
+===============================+=======================+================================================================================================================+
| **Ambito Temporale**          | Oggetto Obbligatorio  | Contiene l'ambito temporale di riferimento                                                                     |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| anno                          | Intero                | Anno di riferimento dei dati (min 2000, max 9999).                                                             |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| trimestre                     | Intero                | Trimestre dell'anno di riferimento (min 1, max 4).                                                             |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+

+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| Campo                         | Tipo                  | Descrizione                                                                                                    |
+===============================+=======================+================================================================================================================+
| **Sintesi Pagamenti**         | Array di Oggetti      | Elenco dettagliato dei pagamenti effettuati.                                                                   |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| uscitaCorrente                | Enumerazione          | Tipo di spesa corrente (opzionale, esclusivo con uscitaInContoCapitale).                                       |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| uscitaInContoCapitale         | Enumerazione          | Tipo di spesa di capitale (opzionale, esclusivo con uscitaCorrente).                                           |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| importo                       | Numero                | Ammontare del pagamento (minimo 0.01).                                                                         |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
| beneficiario                  | Stringa               | Identificativo del beneficiario ("Soggetto privato" o codice fiscale di 11 cifre).                             |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+

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
