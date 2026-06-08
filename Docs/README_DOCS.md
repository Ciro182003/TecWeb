<p align="center"><b>Stazione Meteo Didattica Open-Source</b></p>
<b>Obiettivo del Progetto:</b>
L'obiettivo principale è l'ingegnerizzazione di una stazione meteorologica modulare e replicabile in piccoli laboratori scolastici ed accademici. Il progetto è pensato come un kit didattico che unisce alcune macro discipline.
1. Meccanica: componenti struttirali ottimizzati per la stampa 3D( schermo solare,anemometro,pluviometro a cella di carico) con tolleranze ottimizzate per le più comuni stampanti in commercio.
2. Elettronica: Sviluppo del PCB su KICAD appositamente ingegnerizzato per la produzione autonoma tramite fresatura CNC da banco ( CNC3018 PRO) con piste opportunamente maggiorate e componenti THT per agevolare la saldatura.
3. Informatica: Firmware dei gestione dei sensori,calibrazione dei dati e trasmissione.
4. Uso dell'IA per agevolare compiti complessi di gestione e calibrazione:

* Manutenzione Predittiva dell'Hardware

* Ricerca Guasti (Anomaly Detection)

* Compensazione Dinamica del Vento sulla Cella di Carico:

* Autocalibrazione della Deriva Termica: 

* Previsione Meteo Locale (Nowcasting)

                                                                  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                Mappa della documentazione

I file contenuti in questa cartella seguono il flusso logico dell'ingegnerizzazione del prodotto e vanno letti nel seguente ordine:
01_macro_proposta.md:Definizione dell'idea e analisi delle necessità didattiche.
02_studio_di_fattibilità.md:Analisi limiti tecnologici (tolleranze per la stampa 3D,capacità di isolamento delle CNC, budget economico kit).
03_scelte_meccaniche.md:Relazione tecnica su disegni CAD di tutte le parti, sia in PARTI che in ASSIEMI ,completando l'opera con cartigli dettagliati.
04_scelte_elettroniche.md:Macro-schema a blocchi,schematico elettrico e regole di sbroglio (DRC) specifiche per l'incisione meccanica.
05_architettura_software.md:Diagrammi di flusso del FIRMWARE,gestione degli interrupt hardware e logiche di filtraggio del segnale.
## Mappa della Struttura del Repository

Per garantire la massima modularita ed evitare la sovrapposizione tra le diverse discipline (Meccanica, Elettronica, Informatica), il repository e strutturato secondo la seguente alberatura logica. Ciascuna cartella rappresenta uno specifico step della catena di ingegnerizzazione.

```text
├── .github/               # Template di gestione delle attivita e bug-tracking
├── docs/                  # Documentazione tecnica, analisi e studi di fattibilita
├── meccanica/             # Modelli CAD e file per la manifattura additiva (Stampa 3D)
├── elettronica/           # Progetti EDA, schemi elettrici e file di lavorazione CNC
└── software/              # Firmware del microcontrollore e script di intelligenza artificiale
