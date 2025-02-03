Schema Allegato articolo 4 bis
==============================

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


Schema per la definizione dell'allegato all'articolo 4 bis
==========================================================

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!

.. schema:: allegato_articolo_4_bis
    :title: Schema Allegato articolo 4 bis
    :description: Schema per la definizione dell'allegato all'articolo 4 bis

    :fields:
        - name: id
          type: integer
          description: Identificativo univoco dell'allegato
          required: true
          example: 1

        - name: name
          type: string
          description: Nome dell'allegato
          required: true
          example: "Allegato 1"

        - name: description
          type: string
          description: Descrizione dell'allegato
          required: false
          example: "Descrizione dell'allegato"

        - name: file
          type: string
          description: Percorso del file allegato
          required: true
          example: "/path/to/file.pdf"

        - name: created_at
          type: string
          description: Data di creazione dell'allegato
          required: true
          example: "2020-01-01T00:00:00Z"

        - name: updated_at
          type: string
          description: Data di ultima modifica dell'allegato
          required: true
          example: "2020-01-01T00:00:00Z"

        - name: deleted_at
          type: string
          description: Data di eliminazione dell'allegato
          required: false
          example: "2020-01-01T00:00:00Z"

        - name: article_id
          type: integer
          description: Identificativo dell'articolo a cui è allegato
          required: true
          example: 1

        - name: article
          type: object
          description: Articolo a cui è allegato
          required: true
          schema: articolo

        - name: created_by
          type: object
          description: Utente che ha creato l'allegato
          required: true
          schema: utente

        - name: updated_by
          type: object
          description: Utente che ha modificato l'allegato
          required: true
          schema: utente

        - name: deleted_by
          type: object