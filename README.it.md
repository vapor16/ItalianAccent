# ItalianAccent

**Artificial Intelligence. Authentic Italian Attitude.**

ItalianAccent è una [Agent Skill](https://agentskills.io) open source che fa parlare il tuo assistente AI come uno del
posto: napoletano, barese, catanese, romanesco, leccese e altre parlate, con grammatica e sintassi vere, lessico
locale, proverbi, modi di dire, ironia e parolacce **senza censura**.

Non è un traduttore e non è "italiano con una parola dialettale in cima": quando attivi una modalità, tutta la
conversazione — anche le spiegazioni tecniche e il debugging — viene ricostruita nella parlata scelta, mentre codice,
comandi e fatti tecnici restano esattamente corretti.

[Read in English](README.md)

> [!WARNING]
> **Linguaggio esplicito.** ItalianAccent contiene e genera parolacce, insulti, imprecazioni e (al livello massimo)
> bestemmie attestate nel parlato popolare. È una funzione volontaria: nulla cambia finché **tu** non attivi una
> modalità, e la volgarità si può abbassare fino a 0 in qualsiasi momento (`/italianaccent vulgarity 0`). Le regole di
> sicurezza del modello ospite, i rifiuti e gli avvisi necessari restano sempre validi: "senza censura" vale solo per
> espressioni linguistiche altrimenti consentite. Niente contenuti erotici, niente molestie, nessun aggiramento delle protezioni.

## Funzionalità

- **Dialetto vero, in tutta la risposta**: lessico, morfologia, verbi, sintassi, negazione e particelle del discorso,
  con 5 livelli di intensità.
- **Parolacce senza censura, configurabili 0–5**: 5 di default all'attivazione; contestuali (amichevoli o
  aggressive, sfogo, sorpresa, affetto), mai asterischi, mai avvertenze.
- **Proverbi e modi di dire** usati quando servono davvero, ognuno con fonte, significato e registro.
- **Umorismo e sarcasmo** costruiti con la lingua, non con stereotipi regionali.
- **Sicura per sviluppatori**: blocchi di codice, identificatori, SQL, comandi shell, percorsi ed errori non vengono mai alterati.
- **Base di conoscenza documentata**: voci validate con JSON Schema, ciascuna con provenienza e fonti.
- **Leggera e privata**: solo Markdown e JSON. Nessun server, nessuna API key, nessuna telemetria, nessuna rete a runtime.

## Modalità disponibili

<!-- CATALOG:START -->
| Mode | Variety | Region | Meaning of the mode name | Status |
|---|---|---|---|---|
| **Wallera** (`wallera`) | Napoletano | Campania | Neapolitan 'hernia / scrotum'; used in 'scassare 'a uallera' = to bust one's balls (commercial spelling of uallera) | experimental |
| **Daje** (`daje`) | Romanesco | Lazio | Roman 'come on! let's go!' | experimental |
| **Belin** (`belin`) | Genovese | Liguria | Genoese vulgar 'dick', all-purpose exclamation | experimental |
| **Pirla** (`pirla`) | Milanese | Lombardia | Milanese 'idiot, jerk' | experimental |
| **Potà** (`pota`) | Bergamasco | Lombardia | Bergamasque all-purpose interjection (originally vulgar 'female genitals') | experimental |
| **Mena** (`mena`) | Leccese — Salentino centrale | Puglia | Salentine 'come on / go on!' (from menare) | experimental |
| **Trimone** (`trimone`) | Barese | Puglia | Barese insult: 'idiot, dumbass' | experimental |
| **Mbare** (`mbare`) | Catanese | Sicilia | Sicilian vocative 'mate, buddy' (from 'cumpari/'mbari, godfather/companion) | experimental |
| **Minchia** (`minchia`) | Palermitano | Sicilia | Sicilian vulgar 'dick', used as all-purpose exclamation | experimental |
| **Bischero** (`bischero`) | Fiorentino | Toscana | Florentine 'fool, sucker' | experimental |
| **Boia dé** (`boiade`) | Livornese | Toscana | Livornese exclamation 'damn!, wow!' (boia = executioner, used as an intensifier, + the interjection dé) | experimental |

**11 available modes covering 7 of 20 regions** (Campania, Lazio, Liguria, Lombardia, Puglia, Sicilia, Toscana). 67 further varieties are listed as `planned` in [catalog.json](skills/italianaccent/references/catalog.json) and are not activatable yet.
<!-- CATALOG:END -->

I nomi delle modalità sono parole locali autentiche scelte per essere memorabili. Molte di queste varietà sono,
linguisticamente, lingue romanze o dialetti autonomi e non "dialetti dell'italiano": vedi la
[metodologia linguistica](docs/linguistic-methodology.md). "Dialetti italiani" è usato come etichetta divulgativa.

## Installazione

L'unità installabile è la cartella **`skills/italianaccent/`** (non l'intero repository).

### Con la Skills CLI (Claude Code, Codex, Cursor e altri agenti) — Linux, macOS, Windows

Richiede Node.js 22.20+.

```bash
npx skills add vapor16/ItalianAccent --skill italianaccent
```

Opzioni utili: `-a claude-code` / `-a codex` / `-a cursor` per scegliere l'agente, `-g` per installarla a livello
utente, `--list` per elencare soltanto le skill del repository.

### Come plugin di Claude Code

```text
/plugin marketplace add vapor16/ItalianAccent
/plugin install italianaccent@italianaccent
```

Le skill dei plugin hanno un namespace: si invocano con `/italianaccent:italianaccent <modalità>`.

### Manuale / git clone

macOS / Linux:

```bash
git clone https://github.com/vapor16/ItalianAccent.git
mkdir -p ~/.claude/skills && cp -R ItalianAccent/skills/italianaccent ~/.claude/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/vapor16/ItalianAccent.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse ItalianAccent\skills\italianaccent "$env:USERPROFILE\.claude\skills\"
```

Per altri agenti copia la stessa cartella nella loro directory delle skill.

### Claude.ai

Scarica `italianaccent-1.0.0.zip` dalla [release v1.0.0](https://github.com/vapor16/ItalianAccent/releases/tag/v1.0.0)
(oppure generalo con `python scripts/validate.py --zip`) e caricalo in **Personalizza → Skill → Carica una skill** (serve l'esecuzione di codice attiva). Poi attivala a
parole: *"Attiva ItalianAccent in modalità Wallera."*

## Avvio rapido

```text
/italianaccent                 # aiuto + catalogo
/italianaccent wallera         # napoletano, intensità 5, volgarità 5, proverbi attivi
Che cos'è Docker?
/italianaccent vulgarity 2     # abbassa i toni
/italianaccent daje            # passa al romanesco
/italianaccent off             # torna normale
```

Funziona anche in linguaggio naturale: *"Attiva ItalianAccent in modalità Trimone."* · *"Rispondimi utilizzando il
dialetto catanese con ItalianAccent."*

## Comandi

| Comando | Descrizione |
|---|---|
| `/italianaccent`, `help` | Aiuto e catalogo delle modalità disponibili |
| `list` | Modalità disponibili (e pianificate) |
| `<modalità>` | Attiva o cambia modalità (senza distinzione di maiuscole/accenti; alias come `uallera`, `boia dé`, `pòta`) |
| `<modalità> --intensity N --vulgarity N` | Attiva con opzioni (anche `--proverbs`, `--idioms`, `--humor`, `--sarcasm`, `--translation on/off`) |
| `random` | Modalità casuale |
| `status` | Modalità e configurazione attuali |
| `intensity 1-5` | Intensità dialettale |
| `vulgarity 0-5` | Livello di volgarità |
| `proverbs on/off`, `idioms on/off`, `humor on/off`, `sarcasm on/off` | Attiva/disattiva funzioni |
| `translation on/off` | Brevi glosse in italiano dopo proverbi e frasi difficili |
| `reset` | Ripristina i valori predefiniti, mantiene la modalità |
| `off` | Disattiva ItalianAccent |

## Configurazione: intensità dialettale e volgarità

Valori applicati all'attivazione ([`defaults.json`](skills/italianaccent/references/defaults.json)):

```json
{ "dialect_intensity": 5, "vulgarity": 5, "proverbs": true, "idioms": true, "humor": true,
  "sarcasm": true, "italian_translation": false, "stylistic_censorship": false }
```

L'intensità dialettale ha cinque livelli:

| Livello | Nome | Cosa cambia |
|---|---|---|
| 1 | Leggera | Frasi in italiano standard, con 1–3 parole o interiezioni locali per risposta; è possibile un proverbio locale. |
| 2 | Italiano regionale | Grammatica italiana con sintassi e lessico regionali: particelle discorsive locali, ordine delle parole e uso dei tempi regionali, parole regionali per le cose di tutti i giorni, troncamenti tipici della zona. |
| 3 | Mista | Alternanza naturale (code-switching): intere frasi in dialetto si alternano all'italiano. Il dialetto accompagna le parti emotive, ironiche e colloquiali; l'italiano le spiegazioni tecniche dense. |
| 4 | Dialetto prevalente | La maggior parte delle frasi è in dialetto, con morfologia e forme verbali dialettali. L'italiano è usato solo per i termini tecnici o dove il dialetto non ha una parola. |
| 5 | Piena (predefinita) | Tutto in dialetto, nei limiti delle risorse documentate della modalità: articoli, pronomi, paradigmi verbali, negazione, sintassi, grafia. I termini tecnici mantengono la forma inglese o italiana, ma sono flessi e inquadrati in dialetto. |

La volgarità ha sei livelli, da 0 a 5:

| Livello | Cosa aspettarsi |
|---|---|
| 0 | Nessuna volgarità. Solo interiezioni leggere e non volgari; i proverbi con contenuto volgare sono saltati. |
| 1 | Leggera: esclamazioni blande ed espressioni eufemistiche. |
| 2 | Colloquiale moderata: parolacce comuni e leggere, prese in giro amichevoli. |
| 3 | Volgarità naturale: parolacce di tutti i giorni, come nel parlare informale tra amici. |
| 4 | Fortemente volgare: linguaggio pesante, metafore volgari e insulti pungenti per scherzo. |
| 5 | Massima intensità stilistica (predefinita): tutta la gamma, bestemmie segnalate incluse, scritte per esteso e mai censurate. |

Le due impostazioni sono indipendenti: intensità dialettale e volgarità si regolano separatamente, in base alle proprie esigenze, alle preferenze e al contesto della conversazione. Un'immersione totale nel dialetto senza alcuna parolaccia è possibile con intensità 5 e volgarità 0.

I livelli di intensità più bassi si adattano all'esplorazione linguistica, alla conversazione quotidiana e ai contesti meno informali. I livelli di volgarità più alti sono pensati per utenti adulti e consenzienti che apprezzano l'umorismo irriverente.

I valori predefiniti all'attivazione sono intensità 5 e volgarità 5. Le regole di sicurezza della piattaforma ospitante si applicano sempre, a ogni livello: la volgarità cambia solo lo stile di un linguaggio comunque consentito e non supera mai rifiuti o avvertenze di sicurezza.

Combinazioni pratiche:

```text
/italianaccent wallera --intensity 5 --vulgarity 0   # napoletano pieno, nessuna parolaccia
/italianaccent daje --intensity 2 --vulgarity 1      # italiano regionale romanesco leggero, blando
/italianaccent mena --intensity 3 --vulgarity 3      # mix naturale leccese/italiano, parolacce quotidiane
/italianaccent belin                                 # predefiniti: 5/5
/italianaccent intensity 4                           # cambia solo l'intensità
/italianaccent vulgarity 0                           # cambia solo la volgarità, mantiene la modalità
/italianaccent reset                                 # torna a 5/5
```

## Test e valutazioni

- Test deterministici (`python scripts/validate.py && python -m pytest`): struttura, schemi, catalogo, fonti,
  duplicati, sicurezza, regressioni linguistiche confermate dall'audit.
- Valutazione assistita da AI sulla skill **installata** (`tests/behavioral/run_installed_eval.py`), con confronto
  con/senza ItalianAccent sullo stesso modello: risultati in [`tests/behavioral/results/v1.0.0/`](tests/behavioral/results/v1.0.0/).
- **Nessuna valutazione da parte di parlanti nativi** è stata ancora effettuata.

## Compatibilità

Claude Code (skill e plugin): documentata, verificata localmente. Claude.ai (ZIP), Codex e Cursor (via Skills CLI):
compatibili strutturalmente, non ancora testati. Dettagli in [docs/platform-compatibility.md](docs/platform-compatibility.md).

**Persistenza:** la modalità resta attiva per tutta la conversazione (la skill rilegge il profilo dopo la compattazione
del contesto). Non si trasferisce mai a nuove conversazioni (nessun accesso a memoria o cronologia): va attivata esplicitamente ogni volta. ItalianAccent non modifica mai `CLAUDE.md`, `AGENTS.md` o le tue impostazioni.

## Maturità e limiti

- Tutte le modalità sono **`experimental`**: ricercate da fonti documentate, **senza revisione di parlanti nativi**.
  Errori di grafia e forme rare sono possibili: segnalali!
- Ogni profilo segue una norma di riferimento (di solito la città principale); la variazione locale è enorme.
- Le fonti sulle parolacce sono in gran parte popolari e meno affidabili.
- La qualità dipende dal modello ospite.

## Privacy

ItalianAccent è fatta solo di file. Non raccoglie dati, non invia conversazioni, non richiede account, server, API key,
database o MCP aggiuntivi. (La Skills CLI di terze parti ha una propria telemetria anonima, disattivabile con
`DISABLE_TELEMETRY=1`.)

## Contribuire

Parlanti locali, linguisti e sviluppatori sono benvenuti: aggiungi parole, proverbi, parolacce, correggi la
grammatica, segnala forme inventate o contaminazioni, oppure revisiona un profilo. Parti da
[CONTRIBUTING.md](CONTRIBUTING.md) e [docs/adding-a-dialect.md](docs/adding-a-dialect.md).

## Roadmap

- **v1.0.0** (questa release): undici modalità sperimentali in Puglia, Campania, Lazio, Liguria, Lombardia, Sicilia e Toscana.
- **Prossimi passi**: revisioni dei parlanti nativi e primi profili `community-reviewed`, vocabolari e proverbi più ricchi.
- **Modalità future**: le ricerche già avviate su romagnolo (*pataca*), bolognese (*socmel*) e veneziano (*ostrega*)
  sono conservate in [`research/future-profiles/`](research/future-profiles/); altre varietà sono `planned` nel catalogo.

## Licenza

[MIT](LICENSE) per il codice e i contenuti originali di ItalianAccent. Il materiale di terzi mantiene la propria
licenza: vedi [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
