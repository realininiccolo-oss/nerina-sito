"""Dati del percorso della home — v6 (18/11/2026): «il percorso che ti riconosce».

Due domande a scelta multipla (fino a tre risposte ciascuna, l'ordine dei tocchi decide il peso), poi il ritratto
(una frase, tre username, una riga) e le pagine dopo, tutte costruite sulle risposte.

Scelte [I] di questa versione (Niccolò, 18/11 11:05):
- gli username hanno un nome proprio, ma solo diminutivi che valgono per lui e per lei (ale, fede, vale, simo…)
  o cognomi: il sito non conosce il genere di chi guarda;
- l'username «serio» (scuola, lavoro, studenti) porta il cognome; quello dell'amicizia un diminutivo; il più
  privato (serate, relazione) spesso nessun nome: così si vede che i tre non si collegano;
- «Una relazione (18+)» c'è, ma non la vede chi ha scelto «Vado alle superiori» né chi parla per un'azienda;
- per i 16-17enni esempi sobri: niente alcol, niente discoteca, niente relazione.

Il JSON di ogni lingua va in <script type="application/json" id="percorso-dati">; sito.js lo legge e costruisce le
schede con createElement/textContent. compone() qui sotto fa lo stesso calcolo di sito.js, per la pagina senza
JavaScript (profilo predefinito universita + amici) e per le prove.
"""
import json

PRED = {"chi": ["universita"], "cosa": ["amici"]}

# Icone a linea delle tessere (viewBox 24, tratto 1,75, come grafica.icona).
ICONE = {
    "superiori": '<rect x="6" y="7.5" width="12" height="13" rx="3"/><path d="M9 7.5V6a3 3 0 0 1 6 0v1.5"/>'
                 '<path class="accento" d="M9 13h6"/>',
    "universita": '<path d="M3 9.5l9-4.5 9 4.5-9 4.5z"/><path d="M7 11.5v4c0 1.5 2.5 3 5 3s5-1.5 5-3v-4"/>'
                  '<path class="accento" d="M21 9.5v5"/>',
    "lavoro": '<rect x="3.5" y="7.5" width="17" height="12" rx="2.5"/><path d="M9 7.5V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.5"/>'
              '<path class="accento" d="M3.5 12.5h17"/>',
    "professione": '<path d="M4 9l1.5-4.5h13L20 9"/><path d="M4 9c0 3.4 5.3 3.4 5.3 0 0 3.4 5.4 3.4 5.4 0 0 3.4 5.3 3.4 5.3 0"/>'
                   '<path d="M5.5 12v7.5h13V12"/><path class="accento" d="M10 19.5V15h4v4.5"/>',
    "insegno": '<rect x="3.5" y="4.5" width="17" height="11" rx="1.5"/><path d="M8 20l2-4.5M16 20l-2-4.5"/>'
               '<path class="accento" d="M7 9h6M7 12h4"/>',
    "genitore": '<circle cx="9" cy="6.5" r="2.5"/><path d="M4.5 20v-5a4.5 4.5 0 0 1 9 0v5"/>'
                '<circle class="accento" cx="17.5" cy="11.5" r="1.8"/><path class="accento" d="M15 20v-2.5a2.5 2.5 0 0 1 5 0V20"/>',
    "nuovo": '<path d="M12 3.5v17"/><path d="M12 5.5h6l2 2-2 2h-6"/><path class="accento" d="M12 11.5H6l-2 2 2 2h6"/>',
    "sport": '<circle cx="12" cy="12" r="8.5"/><path class="accento" d="M12 3.5c-2.5 2.5-3.5 5.5-3.5 8.5s1 6 3.5 8.5'
             'M12 3.5c2.5 2.5 3.5 5.5 3.5 8.5s-1 6-3.5 8.5M3.5 12h17"/>',
    "creativo": '<path d="M9 18V6.5l10-2V16"/><circle cx="7" cy="18" r="2"/><circle class="accento" cx="17" cy="16" r="2"/>',
    "volontario": '<path d="M3.5 14l4-1 3 2h3a1.5 1.5 0 0 1 0 3H10"/><path d="M13.5 18l5-2.5a1.5 1.5 0 0 1 1.5 2.5l-6 3.5H8L3.5 19.5"/>'
                  '<path class="accento" d="M12 10c-3-1.8-3.8-3.6-2.5-4.8a1.8 1.8 0 0 1 2.5.2 1.8 1.8 0 0 1 2.5-.2c1.3 1.2.5 3-2.5 4.8z"/>',
    "pensione": '<path d="M5 10h11v4a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5z"/><path d="M16 11h1.5a2.5 2.5 0 0 1 0 5H16"/>'
                '<path class="accento" d="M9 4.5c-1 1.2 1 2.3 0 3.5M12.5 4.5c-1 1.2 1 2.3 0 3.5"/>',
    "azienda": '<path d="M5 20.5v-15l8-2v17"/><path d="M13 9.5l6 2v9"/><path d="M3.5 20.5h17"/>'
               '<path class="accento" d="M8 8h2M8 11.5h2M8 15h2M15.5 14h1.5"/>',
    # che cosa cerchi
    "amici": '<path d="M3.5 5.5h11v7h-6l-3 2.5v-2.5h-2z"/><path class="accento" d="M17.5 9h3v7h-1.5v2.5L16 16h-4.5v-1.5"/>',
    "attivita": '<circle cx="6" cy="16" r="3.5"/><circle cx="18" cy="16" r="3.5"/><path d="M6 16l4-7h5l3 7M10 9l2.5 7h-6"/>'
                '<path class="accento" d="M8.5 6h3"/>',
    "studio": '<path d="M12 6.5C10 5 7 4.5 3.5 5v13c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5z"/>'
              '<path class="accento" d="M12 6.5v13"/>',
    "serate": '<path d="M3 5.5c6 4 12 4 18 0"/><circle class="accento-pieno" cx="7" cy="8.2" r="1.3"/>'
              '<circle class="accento-pieno" cx="12" cy="9.3" r="1.3"/><circle class="accento-pieno" cx="17" cy="8.2" r="1.3"/>'
              '<path d="M4.5 15h15M7 15v5.5M17 15v5.5"/>',
    "soci": '<circle cx="9" cy="12" r="5"/><circle class="accento" cx="15" cy="12" r="5"/>',
    "mentore": '<path d="M9.5 17h5M10.5 20h3"/><path d="M12 3.5a5.5 5.5 0 0 0-3 10.1V17h6v-3.4a5.5 5.5 0 0 0-3-10.1z"/>'
               '<path class="accento" d="M12 8v4"/>',
    "causa": '<path d="M6 21V4"/><path class="accento" d="M6 4.5h11l-2.5 3.5 2.5 3.5H6"/>',
    "clienti": '<path d="M3.5 12.5v-8h8l9 9-8 8z"/><circle class="accento" cx="8" cy="9" r="1.5"/>',
    "assumere": '<circle cx="10" cy="8" r="3.5"/><path d="M3.5 20a6.5 6.5 0 0 1 13 0"/><path class="accento" d="M19 8v6M16 11h6"/>',
    "relazione": '<path d="M12 19.5s-7-4.3-7-9.5A3.8 3.8 0 0 1 12 7.5a3.8 3.8 0 0 1 7 2.5c0 5.2-7 9.5-7 9.5z"/>',
    # schede dell'organizzazione
    "org": '<path d="M5 20.5v-15l8-2v17"/><path d="M13 9.5l6 2v9"/><path d="M3.5 20.5h17"/>'
           '<path class="accento" d="M8 8h2M8 11.5h2M8 15h2M15.5 14h1.5"/>',
    "invito": '<path d="M18.5 5.5 5 12l13.5 6.5"/><path d="M18.5 5.5Q21.5 12 18.5 18.5"/>'
              '<circle class="accento-pieno" cx="5" cy="12" r="2"/>',
    "evento": '<rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'
              '<circle class="accento-pieno" cx="15.5" cy="15" r="1.6"/>',
}


def icona(nome, px=28, classe="icona tessera-icona"):
    return (f'<svg class="{classe}" width="{px}" height="{px}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
            f'{ICONE[nome]}</svg>')


# Colori dell'omino (grafica.COLORI) per ogni tipo di scheda; se due schede coincidono, sito.js prende il successivo.
COLORI_COSA = {"amici": "prugna", "attivita": "corallo", "studio": "infinito", "serate": "lampone", "lavoro": "ardesia",
               "soci": "petrolio", "mentore": "foglia", "causa": "oliva", "clienti": "terra", "assumere": "ginestra",
               "relazione": "lampone"}
ORDINE_COLORI = ["infinito", "corallo", "prugna", "foglia", "ginestra", "petrolio", "terra", "oliva", "lampone", "ardesia"]

# Regole della domanda 2: chi non vede l'opzione, e le opzioni solo per alcuni profili.
NASCONDI = {"amici": ["azienda"], "attivita": ["azienda"], "studio": ["pensione", "azienda"],
            "lavoro": ["pensione", "azienda"], "soci": ["superiori"], "relazione": ["superiori", "azienda"]}
SOLO = {"clienti": ["professione", "azienda"], "assumere": ["professione", "azienda"]}
PORTE = {"amici": "foglie", "attivita": "eventi", "studio": "foglie", "serate": "eventi", "lavoro": "lavoro",
         "soci": "lavoro", "mentore": "foglie", "causa": "eventi", "clienti": "lavoro", "assumere": "lavoro",
         "relazione": "foglie"}
PORTE_ORG = {"clienti": "eventi", "serate": "eventi", "causa": "eventi", "mentore": "eventi", "assumere": "lavoro",
             "soci": "rete"}
RIEMPI = ["foglie", "diario", "eventi", "passero"]
RIEMPI_ORG = ["eventi", "lavoro", "rete"]


# Nomi propri (diminutivi unisex e cognomi): in un ritratto ogni nome compare una volta sola, se no i tre username
# si collegherebbero. Al secondo uso il nome cade: «robi.orto.e.bocce» diventa «orto.e.bocce».
NOMI = ["ale", "fede", "vale", "simo", "dani", "fra", "manu", "michi", "giuli", "cri", "robi", "gabri", "sam",
        "ferri", "bianchi", "rossi", "conti", "moretti", "galli", "greco", "ricci", "esposito", "marini",
        "alex", "jamie", "robin", "jo", "kit", "frankie", "ash", "charlie", "drew", "taylor", "morgan",
        "price", "hughes", "reid", "walsh", "ellis", "shaw", "kerr", "hart"]
PREFISSI = ["prof", "mx"]


def nome_di(u):
    t = u.split(".")
    return t[1] if t[0] in PREFISSI and len(t) > 1 else t[0]


def senza_nome(u, usati):
    """Toglie il nome proprio se è già in un'altra scheda del ritratto."""
    n = nome_di(u)
    if n in NOMI and n in usati:
        t = u.split(".")
        return ".".join(t[2:] if t[0] in PREFISSI else t[1:])
    return u


def _u(u, mostra):
    return {"u": u, "mostra": mostra}


DATI = {
    "it": {
        "chi_t": "Chi sei?", "cosa_t": "Che cosa cerchi?", "fino": "Scegline fino a tre.", "avanti": "Avanti",
        "chi": [("superiori", "Vado alle superiori"), ("universita", "Studio all'università"), ("lavoro", "Lavoro"),
                ("professione", "Ho un'attività o una professione mia"), ("insegno", "Insegno"),
                ("genitore", "Sono genitore"), ("nuovo", "Vivo in una città nuova"), ("sport", "Faccio sport"),
                ("creativo", "Suono, disegno o scrivo"), ("volontario", "Faccio volontariato"),
                ("pensione", "Sono in pensione"), ("azienda", "Parlo per un'azienda o un'associazione")],
        "cosa": [("amici", "Amici che parlano la mia lingua"), ("attivita", "Qualcuno con cui fare una cosa"),
                 ("studio", "Compagni di studio"), ("serate", "Uscire, serate, eventi"), ("lavoro", "Lavoro"),
                 ("soci", "Collaboratori o soci"), ("mentore", "Imparare da qualcuno, o insegnare"),
                 ("causa", "Una causa per cui darmi da fare"), ("clienti", "Clienti"),
                 ("assumere", "Persone da assumere"), ("relazione", "Una relazione (18+)")],
        "ruoli": {"amici": "Amicizia", "attivita": "Attività insieme", "studio": "Studio", "serate": "Serate",
                  "lavoro": "Lavoro e affari", "soci": "Network", "mentore": "Mentore e insegnamento",
                  "causa": "Volontariato", "clienti": "Lavoro e affari", "assumere": "Lavoro e affari",
                  "relazione": "Partner"},
        "righe": {"amici": "Il passero conosce chi parla la tua lingua.",
                  "attivita": "Una cosa da fare, e qualcuno con cui farla.",
                  "studio": "Qualcuno con cui aprire lo stesso libro.",
                  "serate": "Stasera, con chi ha voglia della stessa cosa.",
                  "lavoro": "Il curriculum lo mostri tu, a chi vuoi tu.",
                  "soci": "La tua stessa idea, l'altra metà delle competenze.",
                  "mentore": "Chi sa già, e chi vuole imparare.",
                  "causa": "Chi vuole darsi da fare per la stessa cosa.",
                  "clienti": "I clienti arrivano da una richiesta, non da una pubblicità.",
                  "assumere": "Chi cerca proprio il lavoro che offri.",
                  "relazione": "Con calma, con qualcuno che parla la tua lingua."},
        "sotto": "Tre username. Una persona verificata. Nessuno li collega, se non vuoi tu.",
        "verificata": "identità verificata",
        "profili": {
            "superiori": {
                "frase": "Amici della tua età. Ognuno con un'identità verificata.",
                "serio": {"u": "ferri.4b", "ruolo": "Scuola", "mostra": "nome e cognome, solo ai compagni",
                          "colore": "infinito", "copre": ["studio"]},
                "vede": "I compagni vedono {1}. Mai {3}.",
                "per": {"amici": _u("ale.cuffie.sempre", "solo l'username"),
                        "attivita": _u("ale.in.battuta", "solo l'username"),
                        "serate": _u("karaoke.stonato", "solo l'username"),
                        "studio": _u("ferri.ripasso.di.mate", "nome e cognome"),
                        "lavoro": _u("ale.lavoretto.estivo", "nome e cognome, a chi offre lavoro"),
                        "mentore": _u("vorrei.capire.fisica", "solo l'username"),
                        "causa": _u("ale.e.il.canile", "solo l'username")},
                "riserva": ["amici", "serate", "mentore"]},
            "universita": {
                "frase": "La facoltà, gli amici, le serate. Tre nomi che nessuno collega.",
                "serio": {"u": "bianchi.ing", "ruolo": "Studio e lavoro", "mostra": "nome e cognome visibili",
                          "colore": "infinito", "copre": ["studio", "lavoro"]},
                "vede": "I compagni di corso vedono {1}. Mai {3}.",
                "per": {"amici": _u("fede.tra.una.lezione", "solo l'username"),
                        "serate": _u("modalita.loca", "solo l'username"),
                        "attivita": _u("fede.corre.al.parco", "solo l'username"),
                        "soci": _u("idee.alle.3", "solo l'username"),
                        "mentore": _u("fede.vuole.imparare", "solo l'username"),
                        "causa": _u("fede.mani.libere", "solo l'username"),
                        "relazione": _u("caffe.lungo", "età a fascia, niente nome")},
                "riserva": ["amici", "serate", "attivita"]},
            "insegno": {
                "frase": "In classe hai un ruolo. Fuori, sei tu.",
                "serio": {"u": "prof.rossi.storia", "ruolo": "Mentore e insegnamento",
                          "mostra": "nome e cognome, agli studenti", "colore": "petrolio", "copre": ["mentore"]},
                "vede": "Gli studenti vedono {1}. Mai {3}.",
                "per": {"amici": _u("vale.sui.sentieri", "solo l'username"),
                        "attivita": _u("vale.sui.sentieri", "solo l'username"),
                        "serate": _u("solo.il.sabato", "solo l'username"),
                        "causa": _u("vale.doposcuola.gratis", "solo l'username"),
                        "studio": _u("vale.studia.tedesco", "solo l'username"),
                        "lavoro": _u("rossi.cerca.cattedra", "nome e cognome, a chi offre lavoro"),
                        "soci": _u("rossi.progetti.scuola", "nome e cognome"),
                        "relazione": _u("cena.e.libri", "età a fascia, niente nome")},
                "riserva": ["amici", "serate", "causa"]},
            "lavoro": {
                "frase": "Colleghi di passione, non solo d'ufficio.",
                "serio": {"u": "conti.logistica", "ruolo": "Lavoro e affari", "mostra": "nome e cognome visibili",
                          "colore": "ardesia", "copre": ["lavoro"]},
                "vede": "I colleghi vedono {1}. Mai {3}.",
                "per": {"attivita": _u("simo.dopo.le.18", "solo l'username"),
                        "amici": _u("simo.fuori.ufficio", "solo l'username"),
                        "serate": _u("fuori.orario", "solo l'username"),
                        "soci": _u("progetto.serale", "solo l'username"),
                        "mentore": _u("simo.impara.il.codice", "solo l'username"),
                        "causa": _u("simo.dona.il.sabato", "solo l'username"),
                        "studio": _u("simo.inglese.serale", "solo l'username"),
                        "relazione": _u("caffe.la.domenica", "età a fascia, niente nome")},
                "riserva": ["attivita", "serate", "amici"]},
            "professione": {
                "frase": "Il tuo mestiere, a chi lo stava cercando.",
                "serio": {"u": "studio.grafico.moretti", "ruolo": "Lavoro e affari",
                          "mostra": "nome dell'attività e il tuo", "colore": "terra", "copre": ["lavoro"]},
                "vede": "I clienti vedono {1}. Mai {3}.",
                "per": {"clienti": _u("moretti.loghi.a.mano", "nome e cognome"),
                        "assumere": _u("moretti.cerca.stagista", "nome dell'attività"),
                        "amici": _u("dani.pausa.pranzo", "solo l'username"),
                        "attivita": _u("dani.in.bici", "solo l'username"),
                        "serate": _u("dani.dopo.cena", "solo l'username"),
                        "soci": _u("moretti.cerca.socio", "nome e cognome"),
                        "mentore": _u("moretti.insegna.grafica", "nome e cognome"),
                        "causa": _u("dani.grafica.gratis", "solo l'username"),
                        "studio": _u("dani.corso.serale", "solo l'username"),
                        "relazione": _u("matite.e.vinili", "età a fascia, niente nome")},
                "riserva": ["amici", "attivita", "serate"]},
            "genitore": {
                "frase": "Altri genitori qui vicino. Per davvero.",
                "serio": {"u": "galli.genitore.3a", "ruolo": "Scuola dei figli",
                          "mostra": "nome e cognome, agli altri genitori", "colore": "foglia", "copre": []},
                "vede": "Gli altri genitori vedono {1}. Mai {3}.",
                "per": {"attivita": _u("manu.parco.alle.17", "solo l'username"),
                        "amici": _u("manu.caffe.dopo.scuola", "solo l'username"),
                        "serate": _u("finalmente.una.sera", "solo l'username"),
                        "causa": _u("galli.festa.di.classe", "nome e cognome"),
                        "mentore": _u("manu.impara.a.cucinare", "solo l'username"),
                        "lavoro": _u("galli.part.time", "nome e cognome, a chi offre lavoro"),
                        "studio": _u("manu.torna.a.studiare", "solo l'username"),
                        "soci": _u("galli.idea.nel.cassetto", "nome e cognome"),
                        "relazione": _u("ricomincio.da.un.caffe", "età a fascia, niente nome")},
                "riserva": ["attivita", "serate", "amici"]},
            "nuovo": {
                "frase": "Una città nuova. Qualcuno che parla la tua lingua.",
                "serio": {"u": "greco.da.lunedi.qui", "ruolo": "Amicizia", "mostra": "nome e cognome, se vuoi",
                          "colore": "ginestra", "copre": ["amici"]},
                "vede": "I vicini vedono {1}. Mai {3}.",
                "per": {"attivita": _u("fra.scatoloni.chiusi", "solo l'username"),
                        "serate": _u("prima.uscita", "solo l'username"),
                        "lavoro": _u("greco.cerca.qui", "nome e cognome, a chi offre lavoro"),
                        "mentore": _u("fra.impara.il.dialetto", "solo l'username"),
                        "causa": _u("fra.da.una.mano", "solo l'username"),
                        "studio": _u("fra.corso.di.lingua", "solo l'username"),
                        "soci": _u("greco.riparte.da.qui", "nome e cognome"),
                        "relazione": _u("un.caffe.in.centro", "età a fascia, niente nome")},
                "riserva": ["attivita", "serate", "causa"]},
            "sport": {
                "frase": "Qualcuno per la prossima partita. Al tuo livello.",
                "serio": {"u": "ricci.terzino", "ruolo": "Attività insieme", "mostra": "nome e cognome, alla squadra",
                          "colore": "corallo", "testa": "visiera", "copre": ["attivita"]},
                "vede": "La squadra vede {1}. Mai {3}.",
                "per": {"amici": _u("michi.spogliatoio.allegro", "solo l'username"),
                        "serate": _u("terzo.tempo", "solo l'username"),
                        "mentore": _u("michi.tecnica.da.rifare", "solo l'username"),
                        "causa": _u("michi.allena.i.piccoli", "solo l'username"),
                        "lavoro": _u("ricci.istruttore.di.nuoto", "nome e cognome, a chi offre lavoro"),
                        "soci": _u("ricci.apre.una.palestra", "nome e cognome"),
                        "studio": _u("michi.scienze.motorie", "solo l'username"),
                        "relazione": _u("corsa.e.colazione", "età a fascia, niente nome")},
                "riserva": ["amici", "serate", "mentore"]},
            "creativo": {
                "frase": "Qualcuno con cui creare, non qualcuno che ti segua.",
                "serio": {"u": "giuli.chitarra.in.cantina", "ruolo": "Attività insieme", "mostra": "solo l'username",
                          "colore": "prugna", "testa": "basco", "copre": ["attivita"]},
                "vede": "Chi suona con te vede {1}. Mai {3}.",
                "per": {"amici": _u("giuli.quaderno.nero", "solo l'username"),
                        "serate": _u("jam.del.giovedi", "solo l'username"),
                        "soci": _u("giuli.band.cercasi", "solo l'username"),
                        "mentore": _u("giuli.lezioni.di.chitarra", "solo l'username"),
                        "lavoro": _u("esposito.illustrazioni", "nome e cognome, a chi offre lavoro"),
                        "causa": _u("giuli.murales.di.quartiere", "solo l'username"),
                        "studio": _u("giuli.armonia.da.rifare", "solo l'username"),
                        "relazione": _u("mostre.la.domenica", "età a fascia, niente nome")},
                "riserva": ["amici", "serate", "soci"]},
            "volontario": {
                "frase": "Chi vuole darsi da fare, vicino a te.",
                "serio": {"u": "cri.turno.del.sabato", "ruolo": "Volontariato", "mostra": "nome e cognome, al gruppo",
                          "colore": "oliva", "copre": ["causa"]},
                "vede": "Il gruppo vede {1}. Mai {3}.",
                "per": {"amici": _u("cri.mani.libere", "solo l'username"),
                        "attivita": _u("cri.camminate.lunghe", "solo l'username"),
                        "serate": _u("cena.di.gruppo", "solo l'username"),
                        "mentore": _u("cri.primo.soccorso", "solo l'username"),
                        "lavoro": _u("marini.terzo.settore", "nome e cognome, a chi offre lavoro"),
                        "soci": _u("marini.nuova.associazione", "nome e cognome"),
                        "studio": _u("cri.lingua.dei.segni", "solo l'username"),
                        "relazione": _u("cuore.da.volontario", "età a fascia, niente nome")},
                "riserva": ["amici", "attivita", "serate"]},
            "pensione": {
                "frase": "Il tempo libero, finalmente in compagnia.",
                "serio": {"u": "robi.ora.ho.tempo", "ruolo": "Amicizia", "mostra": "nome e cognome, se vuoi",
                          "colore": "terra", "copre": ["amici"]},
                "vede": "Gli amici di sempre vedono {1}. Mai {3}.",
                "per": {"attivita": _u("robi.orto.e.bocce", "solo l'username"),
                        "serate": _u("ballo.liscio", "solo l'username"),
                        "mentore": _u("robi.insegno.il.mestiere", "solo l'username"),
                        "causa": _u("robi.aiuta.coi.compiti", "solo l'username"),
                        "soci": _u("robi.consigli.alle.imprese", "nome e cognome"),
                        "relazione": _u("compagnia.a.teatro", "età a fascia, niente nome")},
                "riserva": ["attivita", "serate", "mentore"]},
        },
        "riserva": {"amici": _u("giuli.libri.e.passeggiate", "solo l'username"),
                    "attivita": _u("simo.cammina.piano", "solo l'username"),
                    "studio": _u("dani.studia.inglese", "solo l'username"),
                    "serate": _u("stasera.esco", "solo l'username"),
                    "lavoro": _u("conti.disponibile", "nome e cognome, a chi offre lavoro"),
                    "soci": _u("idee.cercasi", "solo l'username"),
                    "mentore": _u("cri.foto.analogica", "solo l'username"),
                    "causa": _u("mani.per.il.quartiere", "solo l'username"),
                    "clienti": _u("moretti.su.misura", "nome e cognome"),
                    "assumere": _u("moretti.cerca.persone", "nome dell'attività"),
                    "relazione": _u("senza.fretta", "età a fascia, niente nome")},
        # richiesta scritta nel Diario → foglia (username dell'altra persona o evento, tipo) → perché
        "foglie": {
            "universita|amici": ["Vorrei amici con cui parlare di qualcosa che non sia l'esame.", "giuli.vinili",
                                 "Amicizia", "Ingegneria · la stessa biblioteca · la stessa band"],
            "universita|serate": ["Stasera ho voglia di ballare, ma i miei amici dormono.", "fra.notte.fonda",
                                  "Serate", "Elettronica · la stessa zona · le serate del giovedì"],
            "universita|studio": ["Mi serve qualcuno per preparare Analisi 1.", "dani.analisi.uno", "Studio",
                                  "Analisi 1 · la stessa aula studio"],
            "universita|relazione": ["Mi piacerebbe conoscere qualcuno, con calma.", "libri.e.vinili", "Partner",
                                     "Gli stessi libri · la stessa musica · la stessa idea di domenica"],
            "universita|soci": ["Ho un'idea per un'app, mi manca chi sa disegnarla.", "dani.disegna.interfacce",
                                "Network", "App · la sera · tu il codice, l'altra metà il disegno"],
            "superiori|amici": ["Vorrei amici che ascoltano la mia stessa musica.", "ale.indie.sempre", "Amicizia",
                                "La stessa musica · lo stesso paese · un anno di differenza"],
            "superiori|attivita": ["Cerco qualcuno per giocare a pallavolo il sabato.", "cri.schiacciata",
                                   "Attività insieme", "Pallavolo · il palazzetto del paese · la stessa età"],
            "superiori|serate": ["Sabato c'è il karaoke all'oratorio: chi viene?", "Karaoke all'oratorio",
                                 "Evento", "Karaoke · sabato pomeriggio · a 2 km"],
            "superiori|mentore": ["Non capisco la fisica. Qualcuno me la spiega?", "bianchi.fisica",
                                  "Mentore e insegnamento", "Fisica · in biblioteca, un luogo pubblico · persona verificata"],
            "superiori|studio": ["Cerco qualcuno per ripassare inglese.", "michi.english", "Studio",
                                 "Inglese · la stessa scuola, un'altra classe"],
            "insegno|amici": ["Fuori da scuola mi manca qualcuno con cui camminare in montagna.", "manu.sentieri",
                              "Amicizia", "Trekking · la storia dei posti · i rifugi del Bresciano"],
            "insegno|causa": ["Vorrei organizzare un doposcuola gratuito.", "Associazione Mani Aperte",
                              "Volontariato", "Doposcuola · il tuo quartiere · il sabato"],
            "insegno|serate": ["Una sera a teatro, in compagnia.", "Prosa al Teatro Sociale", "Evento",
                               "Teatro · sabato sera · a 20 minuti"],
            "lavoro|attivita": ["Dopo le 18 vorrei correre con qualcuno.", "simo.10km", "Attività insieme",
                                "Corsa · il parco vicino all'ufficio · i 10 km"],
            "lavoro|soci": ["Ho un'idea per un'app, mi manca chi sa programmare.", "robi.codice.di.sera", "Network",
                            "App · la sera · tu l'idea, l'altra metà il codice"],
            "lavoro|serate": ["Venerdì sera, qualcosa di diverso dal solito aperitivo.", "Cena con delitto",
                              "Evento", "Gialli · venerdì sera · a 15 minuti"],
            "professione|clienti": ["Faccio loghi su misura: chi ne cerca uno?", "pasticceria.galli",
                                    "Lavoro e affari", "Cerca un logo · a 5 km · ama lo stesso stile"],
            "professione|assumere": ["Cerco uno stagista che sappia disegnare.", "dani.portfolio",
                                     "Lavoro e affari", "Illustrazione · cerca uno stage · a 10 km"],
            "genitore|amici": ["Vorrei conoscere altri genitori della scuola dei miei figli.", "sam.due.bimbi",
                               "Amicizia", "La stessa scuola · il parco alle 17 · la montagna d'estate"],
            "genitore|serate": ["Una sera libera: voglio uscire con altri adulti.", "Cena del giovedì", "Evento",
                                "Cucina · il giovedì · una sera per sé"],
            "nuovo|amici": ["Sono qui da una settimana e non conosco nessuno.", "vale.qui.da.un.anno", "Amicizia",
                            "La tua stessa città d'origine · la stessa musica · lo stesso quartiere"],
            "nuovo|attivita": ["Cerco qualcuno per scoprire la città a piedi.", "fra.passeggiate.lente",
                               "Attività insieme", "Passeggiate · il centro storico · la fotografia"],
            "sport|attivita": ["Cerco il quarto per il padel di mercoledì.", "ricci.padel", "Attività insieme",
                               "Padel · mercoledì sera · lo stesso livello"],
            "creativo|soci": ["Cerco una band: suono il basso.", "giuli.batteria", "Network",
                              "Rock anni '90 · una sala prove a Brescia · il basso che manca"],
            "creativo|amici": ["Vorrei qualcuno con cui disegnare all'aperto.", "dani.acquerelli", "Amicizia",
                               "Acquerello · i colli · la domenica mattina"],
            "volontario|causa": ["Vorrei aiutare in una raccolta alimentare.", "Associazione Mani Aperte",
                                 "Volontariato", "Raccolta alimentare · sabato · a 3 km"],
            "pensione|mentore": ["Ho fatto il falegname per quarant'anni: vorrei insegnarlo.", "manu.vuole.imparare",
                                 "Mentore e insegnamento", "Falegnameria · un laboratorio di quartiere · il martedì"],
            "pensione|attivita": ["Cerco compagni per le bocce.", "gabri.bocce.e.carte", "Attività insieme",
                                  "Bocce · il circolo del paese · le carte, dopo"],
            "pensione|serate": ["Mi manca ballare.", "Serata di liscio", "Evento", "Liscio · sabato sera · a 6 km"],
        },
        "foglie_riserva": {
            "amici": ["Vorrei amici che parlano la mia lingua.", "giuli.libri.e.passeggiate", "Amicizia",
                      "Gli stessi libri · le stesse passeggiate · lo stesso quartiere"],
            "attivita": ["Cerco qualcuno con cui camminare la domenica.", "simo.cammina.piano", "Attività insieme",
                         "Camminate · la domenica · lo stesso passo"],
            "studio": ["Cerco qualcuno con cui studiare inglese.", "dani.studia.inglese", "Studio",
                       "Inglese · la stessa biblioteca"],
            "serate": ["Stasera vorrei uscire, ma non so con chi.", "Concerto acustico", "Evento",
                       "Musica dal vivo · stasera · a 10 minuti"],
            "lavoro": ["Cerco lavoro vicino a casa.", "Panificio Galli", "Lavoro e affari",
                       "Cerca personale · a 2 km · retribuzione scritta nell'annuncio"],
            "soci": ["Ho un'idea e mi manca un socio.", "robi.cerca.idee", "Network",
                     "Lo stesso obiettivo · competenze diverse · la stessa città"],
            "mentore": ["Vorrei imparare a fotografare.", "cri.foto.analogica", "Mentore e insegnamento",
                        "Fotografia · in un luogo pubblico · il sabato"],
            "causa": ["Vorrei darmi da fare per il mio quartiere.", "Associazione Mani Aperte", "Volontariato",
                      "Il tuo quartiere · il sabato mattina"],
            "clienti": ["Cerco clienti qui vicino.", "pasticceria.galli", "Lavoro e affari",
                        "Cerca proprio quello che fai · a 5 km"],
            "assumere": ["Cerco una persona per il negozio.", "manu.cerca.lavoro", "Lavoro e affari",
                         "Esperienza nella vendita · a 4 km · disponibile da subito"],
            "relazione": ["Mi piacerebbe conoscere qualcuno, senza fretta.", "caffe.e.mostre", "Partner",
                          "Le stesse mostre · gli stessi film · la stessa idea di domenica"],
        },
        "azienda": {
            "frase": "Il passero ti porta a chi ti sta già cercando.",
            "sotto": "Un'organizzazione verificata. Niente feed: i tuoi inviti arrivano come foglie.",
            "ruolo_org": "Scheda dell'organizzazione", "mostra_org": "verificata, con il suo nome",
            "ruoli": {"invito": "Invito mirato", "evento": "Evento", "assumere": "Cerchiamo", "soci": "Rete"},
            "varianti": {
                "libreria": {"nome": "Libreria Il Portico",
                             "invito": "A chi ama i gialli, a meno di 10 km. Al più 100 persone.",
                             "evento": "Il giallista in libreria · giovedì alle 18:30",
                             "assumere": "Libraio part-time · retribuzione scritta nell'annuncio",
                             "soci": "Le librerie della zona, per un festival",
                             "foglia": ["Vorrei una presentazione di un giallo, la sera.", "Gialli · la sera · a 4 km"]},
                "sport": {"nome": "Polisportiva del Borgo",
                          "invito": "A chi cerca una squadra di pallavolo, dai 16 anni. Al più 100 persone.",
                          "evento": "Torneo di pallavolo · domenica mattina",
                          "assumere": "Allenatore per i ragazzi · retribuzione scritta nell'annuncio",
                          "soci": "Le società vicine, per un torneo insieme",
                          "foglia": ["Cerco una squadra di pallavolo.", "Pallavolo · la domenica · a 3 km"]},
                "volontario": {"nome": "Associazione Mani Aperte",
                               "invito": "A chi vuole aiutare il sabato mattina. Al più 100 persone.",
                               "evento": "Raccolta alimentare · sabato mattina",
                               "assumere": "Coordinamento dei volontari · part-time",
                               "soci": "Le associazioni vicine, per una raccolta comune",
                               "foglia": ["Vorrei aiutare qualcuno, il sabato.", "Volontariato · il sabato · a 3 km"]},
                "creativo": {"nome": "Scuola di musica La Chiave",
                             "invito": "A chi suona e cerca una band. Al più 100 persone.",
                             "evento": "Jam aperta · venerdì sera",
                             "assumere": "Insegnante di chitarra · retribuzione scritta nell'annuncio",
                             "soci": "Le sale prove della zona, per un concerto",
                             "foglia": ["Cerco gente con cui suonare.", "Musica dal vivo · il venerdì · a 5 km"]},
            },
            "vede": None,
        },
        "privacy_pred": "Nessuno vede niente. Finché non vuoi tu.",
    },
    "en": {
        "chi_t": "Who are you?", "cosa_t": "What are you looking for?", "fino": "Pick up to three.", "avanti": "Next",
        "chi": [("superiori", "I'm in high school"), ("universita", "I'm at university"), ("lavoro", "I work"),
                ("professione", "I run my own business or practice"), ("insegno", "I teach"),
                ("genitore", "I'm a parent"), ("nuovo", "I live in a new city"), ("sport", "I play sport"),
                ("creativo", "I play, draw or write"), ("volontario", "I volunteer"), ("pensione", "I'm retired"),
                ("azienda", "I speak for a company or association")],
        "cosa": [("amici", "Friends who speak my language"), ("attivita", "Someone to do something with"),
                 ("studio", "Study partners"), ("serate", "Going out, evenings, events"), ("lavoro", "Work"),
                 ("soci", "Collaborators or partners"), ("mentore", "Learning from someone, or teaching"),
                 ("causa", "A cause to work for"), ("clienti", "Clients"), ("assumere", "People to hire"),
                 ("relazione", "A relationship (18+)")],
        "ruoli": {"amici": "Friendship", "attivita": "Activities", "studio": "Study", "serate": "Evenings",
                  "lavoro": "Work and business", "soci": "Network", "mentore": "Mentoring and teaching",
                  "causa": "Volunteering", "clienti": "Work and business", "assumere": "Work and business",
                  "relazione": "Partner"},
        "righe": {"amici": "The sparrow knows who speaks your language.",
                  "attivita": "Something to do, and someone to do it with.",
                  "studio": "Someone to open the same book with.",
                  "serate": "Tonight, with people in the mood for the same thing.",
                  "lavoro": "You show your CV, to whoever you choose.",
                  "soci": "Your same idea, the other half of the skills.",
                  "mentore": "People who already know, and people who want to learn.",
                  "causa": "People who want to work for the same thing.",
                  "clienti": "Clients come from a request, not from an ad.",
                  "assumere": "People looking for exactly the job you offer.",
                  "relazione": "Slowly, with someone who speaks your language."},
        "sotto": "Three usernames. One verified person. Nobody links them, unless you want to.",
        "verificata": "verified identity",
        "profili": {
            "superiori": {
                "frase": "Friends your age. Each one with a verified identity.",
                "serio": {"u": "price.year11", "ruolo": "School", "mostra": "full name, classmates only",
                          "colore": "infinito", "copre": ["studio"]},
                "vede": "Your classmates see {1}. Never {3}.",
                "per": {"amici": _u("alex.headphones.on", "username only"),
                        "attivita": _u("alex.at.the.net", "username only"),
                        "serate": _u("offkey.karaoke", "username only"),
                        "studio": _u("price.maths.revision", "full name"),
                        "lavoro": _u("alex.summer.job", "full name, to employers"),
                        "mentore": _u("help.me.with.physics", "username only"),
                        "causa": _u("alex.dog.shelter", "username only")},
                "riserva": ["amici", "serate", "mentore"]},
            "universita": {
                "frase": "Your course, your friends, your nights out. Three names nobody links.",
                "serio": {"u": "hughes.engineering", "ruolo": "Study and work", "mostra": "full name visible",
                          "colore": "infinito", "copre": ["studio", "lavoro"]},
                "vede": "Your coursemates see {1}. Never {3}.",
                "per": {"amici": _u("sam.between.lectures", "username only"),
                        "serate": _u("wild.mode.on", "username only"),
                        "attivita": _u("sam.runs.the.park", "username only"),
                        "soci": _u("ideas.at.3am", "username only"),
                        "mentore": _u("sam.wants.to.learn", "username only"),
                        "causa": _u("sam.spare.hands", "username only"),
                        "relazione": _u("long.coffee", "age range, no name")},
                "riserva": ["amici", "serate", "attivita"]},
            "insegno": {
                "frase": "In class you have a role. Outside, you're you.",
                "serio": {"u": "mx.reid.history", "ruolo": "Mentoring and teaching", "mostra": "full name, to students",
                          "colore": "petrolio", "copre": ["mentore"]},
                "vede": "Your students see {1}. Never {3}.",
                "per": {"amici": _u("jamie.on.the.trails", "username only"),
                        "attivita": _u("jamie.on.the.trails", "username only"),
                        "serate": _u("saturdays.only", "username only"),
                        "causa": _u("jamie.homework.club", "username only"),
                        "studio": _u("jamie.learns.german", "username only"),
                        "lavoro": _u("reid.next.school", "full name, to employers"),
                        "soci": _u("reid.school.projects", "full name"),
                        "relazione": _u("dinner.and.books", "age range, no name")},
                "riserva": ["amici", "serate", "causa"]},
            "lavoro": {
                "frase": "Colleagues in passion, not just in the office.",
                "serio": {"u": "walsh.logistics", "ruolo": "Work and business", "mostra": "full name visible",
                          "colore": "ardesia", "copre": ["lavoro"]},
                "vede": "Your colleagues see {1}. Never {3}.",
                "per": {"attivita": _u("robin.after.six", "username only"),
                        "amici": _u("robin.out.of.office", "username only"),
                        "serate": _u("after.hours", "username only"),
                        "soci": _u("evening.project", "username only"),
                        "mentore": _u("robin.learns.to.code", "username only"),
                        "causa": _u("robin.gives.saturdays", "username only"),
                        "studio": _u("robin.evening.spanish", "username only"),
                        "relazione": _u("sunday.coffee", "age range, no name")},
                "riserva": ["attivita", "serate", "amici"]},
            "professione": {
                "frase": "Your craft, for the people who were looking for it.",
                "serio": {"u": "ellis.design.studio", "ruolo": "Work and business",
                          "mostra": "business name and yours", "colore": "terra", "copre": ["lavoro"]},
                "vede": "Your clients see {1}. Never {3}.",
                "per": {"clienti": _u("ellis.hand.drawn.logos", "full name"),
                        "assumere": _u("ellis.hiring.intern", "business name"),
                        "amici": _u("jo.long.lunch", "username only"),
                        "attivita": _u("jo.on.two.wheels", "username only"),
                        "serate": _u("jo.after.dinner", "username only"),
                        "soci": _u("ellis.seeks.partner", "full name"),
                        "mentore": _u("ellis.teaches.design", "full name"),
                        "causa": _u("jo.free.design", "username only"),
                        "studio": _u("jo.night.class", "username only"),
                        "relazione": _u("pencils.and.vinyl", "age range, no name")},
                "riserva": ["amici", "attivita", "serate"]},
            "genitore": {
                "frase": "Other parents nearby. For real.",
                "serio": {"u": "shaw.parent.year3", "ruolo": "The kids' school", "mostra": "full name, to other parents",
                          "colore": "foglia", "copre": []},
                "vede": "Other parents see {1}. Never {3}.",
                "per": {"attivita": _u("kit.park.at.five", "username only"),
                        "amici": _u("kit.coffee.after.drop.off", "username only"),
                        "serate": _u("finally.a.night.out", "username only"),
                        "causa": _u("shaw.class.party", "full name"),
                        "mentore": _u("kit.learns.to.cook", "username only"),
                        "lavoro": _u("shaw.part.time", "full name, to employers"),
                        "studio": _u("kit.back.to.study", "username only"),
                        "soci": _u("shaw.idea.in.a.drawer", "full name"),
                        "relazione": _u("starting.with.a.coffee", "age range, no name")},
                "riserva": ["attivita", "serate", "amici"]},
            "nuovo": {
                "frase": "A new city. Someone who speaks your language.",
                "serio": {"u": "kerr.here.since.monday", "ruolo": "Friendship", "mostra": "full name, if you like",
                          "colore": "ginestra", "copre": ["amici"]},
                "vede": "Your neighbours see {1}. Never {3}.",
                "per": {"attivita": _u("frankie.boxes.still.packed", "username only"),
                        "serate": _u("first.night.out", "username only"),
                        "lavoro": _u("kerr.looking.here", "full name, to employers"),
                        "mentore": _u("frankie.learns.italian", "username only"),
                        "causa": _u("frankie.lends.a.hand", "username only"),
                        "studio": _u("frankie.language.class", "username only"),
                        "soci": _u("kerr.fresh.start", "full name"),
                        "relazione": _u("coffee.in.town", "age range, no name")},
                "riserva": ["attivita", "serate", "causa"]},
            "sport": {
                "frase": "Someone for the next match. At your level.",
                "serio": {"u": "hart.left.back", "ruolo": "Activities", "mostra": "full name, to the team",
                          "colore": "corallo", "testa": "visiera", "copre": ["attivita"]},
                "vede": "The team sees {1}. Never {3}.",
                "per": {"amici": _u("ash.locker.room", "username only"),
                        "serate": _u("third.half", "username only"),
                        "mentore": _u("ash.fixing.my.serve", "username only"),
                        "causa": _u("ash.coaches.kids", "username only"),
                        "lavoro": _u("hart.swim.instructor", "full name, to employers"),
                        "soci": _u("hart.opens.a.gym", "full name"),
                        "studio": _u("ash.sports.science", "username only"),
                        "relazione": _u("run.then.breakfast", "age range, no name")},
                "riserva": ["amici", "serate", "mentore"]},
            "creativo": {
                "frase": "Someone to create with, not someone to follow you.",
                "serio": {"u": "charlie.basement.guitar", "ruolo": "Activities", "mostra": "username only",
                          "colore": "prugna", "testa": "basco", "copre": ["attivita"]},
                "vede": "The people you play with see {1}. Never {3}.",
                "per": {"amici": _u("charlie.black.notebook", "username only"),
                        "serate": _u("thursday.jam", "username only"),
                        "soci": _u("charlie.band.wanted", "username only"),
                        "mentore": _u("charlie.guitar.lessons", "username only"),
                        "lavoro": _u("morgan.illustration", "full name, to employers"),
                        "causa": _u("charlie.street.murals", "username only"),
                        "studio": _u("charlie.music.theory", "username only"),
                        "relazione": _u("sunday.galleries", "age range, no name")},
                "riserva": ["amici", "serate", "soci"]},
            "volontario": {
                "frase": "People who want to help, near you.",
                "serio": {"u": "drew.saturday.shift", "ruolo": "Volunteering", "mostra": "full name, to the group",
                          "colore": "oliva", "copre": ["causa"]},
                "vede": "The group sees {1}. Never {3}.",
                "per": {"amici": _u("drew.spare.hands", "username only"),
                        "attivita": _u("drew.long.walks", "username only"),
                        "serate": _u("group.dinner", "username only"),
                        "mentore": _u("drew.first.aid", "username only"),
                        "lavoro": _u("taylor.charity.sector", "full name, to employers"),
                        "soci": _u("taylor.new.association", "full name"),
                        "studio": _u("drew.sign.language", "username only"),
                        "relazione": _u("big.heart.small.town", "age range, no name")},
                "riserva": ["amici", "attivita", "serate"]},
            "pensione": {
                "frase": "Free time, finally in good company.",
                "serio": {"u": "robin.time.at.last", "ruolo": "Friendship", "mostra": "full name, if you like",
                          "colore": "terra", "copre": ["amici"]},
                "vede": "Your old friends see {1}. Never {3}.",
                "per": {"attivita": _u("robin.garden.and.bowls", "username only"),
                        "serate": _u("ballroom.saturdays", "username only"),
                        "mentore": _u("robin.teaches.the.trade", "username only"),
                        "causa": _u("robin.homework.club", "username only"),
                        "soci": _u("robin.advises.startups", "full name"),
                        "relazione": _u("company.at.the.theatre", "age range, no name")},
                "riserva": ["attivita", "serate", "mentore"]},
        },
        "riserva": {"amici": _u("charlie.books.and.walks", "username only"),
                    "attivita": _u("sam.walks.slowly", "username only"),
                    "studio": _u("jo.studies.english", "username only"),
                    "serate": _u("out.tonight", "username only"),
                    "lavoro": _u("walsh.available", "full name, to employers"),
                    "soci": _u("ideas.wanted", "username only"),
                    "mentore": _u("drew.film.photos", "username only"),
                    "causa": _u("hands.for.the.neighbourhood", "username only"),
                    "clienti": _u("ellis.made.to.measure", "full name"),
                    "assumere": _u("ellis.hiring", "business name"),
                    "relazione": _u("no.rush", "age range, no name")},
        "foglie": {
            "universita|amici": ["I'd like friends to talk to about something other than exams.", "charlie.vinyl",
                                 "Friendship", "Engineering · the same library · the same band"],
            "universita|serate": ["I feel like dancing tonight, but my friends are asleep.", "frankie.small.hours",
                                  "Evenings", "Electronic music · the same area · Thursday nights"],
            "universita|studio": ["I need someone to prepare Calculus 1 with.", "jo.calculus.one", "Study",
                                  "Calculus 1 · the same study room"],
            "universita|relazione": ["I'd like to meet someone, slowly.", "books.and.vinyl", "Partner",
                                     "The same books · the same music · the same idea of Sunday"],
            "universita|soci": ["I've got an idea for an app, I need someone who can design it.", "jo.draws.interfaces",
                                "Network", "App · evenings · you the code, the other half the design"],
            "superiori|amici": ["I'd like friends who listen to my kind of music.", "alex.indie.always", "Friendship",
                                "The same music · the same town · one year apart"],
            "superiori|attivita": ["I'm looking for someone to play volleyball with on Saturdays.", "drew.spike",
                                   "Activities", "Volleyball · the town sports hall · the same age"],
            "superiori|serate": ["There's karaoke at the youth club on Saturday: who's coming?", "Youth club karaoke",
                                 "Event", "Karaoke · Saturday afternoon · 2 km away"],
            "superiori|mentore": ["I don't get physics. Can someone explain it?", "hughes.physics",
                                  "Mentoring and teaching", "Physics · at the library, a public place · verified person"],
            "superiori|studio": ["I'm looking for someone to revise English with.", "ash.english", "Study",
                                 "English · the same school, another class"],
            "insegno|amici": ["Outside school I miss someone to go hiking with.", "kit.trails", "Friendship",
                              "Hiking · the history of places · mountain huts"],
            "insegno|causa": ["I'd like to set up a free homework club.", "Open Hands Association", "Volunteering",
                              "Homework club · your neighbourhood · Saturdays"],
            "insegno|serate": ["A night at the theatre, but not on my own.", "A play at the town theatre", "Event",
                               "Theatre · Saturday night · 20 minutes away"],
            "lavoro|attivita": ["After six I'd like to run with someone.", "robin.10k", "Activities",
                                "Running · the park near the office · 10k"],
            "lavoro|soci": ["I've got an idea for an app, I need someone who can code.", "sam.codes.at.night",
                            "Network", "App · evenings · you the idea, the other half the code"],
            "lavoro|serate": ["Friday night, something other than the usual drinks.", "Murder mystery dinner",
                              "Event", "Crime novels · Friday night · 15 minutes away"],
            "professione|clienti": ["I make custom logos: who needs one?", "shaw.bakery", "Work and business",
                                    "Looking for a logo · 5 km away · likes the same style"],
            "professione|assumere": ["I'm looking for an intern who can draw.", "jo.portfolio", "Work and business",
                                     "Illustration · looking for an internship · 10 km away"],
            "genitore|amici": ["I'd like to meet other parents from my kids' school.", "sam.two.kids", "Friendship",
                               "The same school · the park at five · the mountains in summer"],
            "genitore|serate": ["A free evening: I want to go out with other grown-ups.", "Thursday supper club",
                                "Event", "Cooking · Thursdays · an evening for yourself"],
            "nuovo|amici": ["I've been here a week and I don't know anyone.", "taylor.here.a.year", "Friendship",
                            "The same home town · the same music · the same neighbourhood"],
            "nuovo|attivita": ["I'm looking for someone to explore the city on foot.", "frankie.slow.walks",
                               "Activities", "Walking · the old town · photography"],
            "sport|attivita": ["Looking for a fourth for padel on Wednesday.", "hart.padel", "Activities",
                               "Padel · Wednesday night · the same level"],
            "creativo|soci": ["Looking for a band: I play bass.", "morgan.drums", "Network",
                              "90s rock · a rehearsal room in Brescia · the missing bass"],
            "creativo|amici": ["I'd like someone to draw outdoors with.", "jo.watercolours", "Friendship",
                               "Watercolour · the hills · Sunday mornings"],
            "volontario|causa": ["I'd like to help with a food drive.", "Open Hands Association", "Volunteering",
                                 "Food drive · Saturday · 3 km away"],
            "pensione|mentore": ["I was a carpenter for forty years: I'd like to teach it.", "kit.wants.to.learn",
                                 "Mentoring and teaching", "Woodwork · a community workshop · Tuesdays"],
            "pensione|attivita": ["Looking for people to play bowls with.", "frankie.bowls.and.cards", "Activities",
                                  "Bowls · the village club · cards afterwards"],
            "pensione|serate": ["I miss dancing.", "Ballroom evening", "Event", "Ballroom · Saturday night · 6 km away"],
        },
        "foglie_riserva": {
            "amici": ["I'd like friends who speak my language.", "charlie.books.and.walks", "Friendship",
                      "The same books · the same walks · the same neighbourhood"],
            "attivita": ["I'm looking for someone to walk with on Sundays.", "sam.walks.slowly", "Activities",
                         "Walking · Sundays · the same pace"],
            "studio": ["I'm looking for someone to study English with.", "jo.studies.english", "Study",
                       "English · the same library"],
            "serate": ["I'd like to go out tonight, but I don't know who with.", "Acoustic gig", "Event",
                       "Live music · tonight · 10 minutes away"],
            "lavoro": ["I'm looking for work close to home.", "Shaw's Bakery", "Work and business",
                       "Hiring · 2 km away · pay stated in the listing"],
            "soci": ["I have an idea and I need a partner.", "robin.seeks.ideas", "Network",
                     "The same goal · different skills · the same city"],
            "mentore": ["I'd like to learn photography.", "drew.film.photos", "Mentoring and teaching",
                        "Photography · in a public place · Saturdays"],
            "causa": ["I'd like to do something for my neighbourhood.", "Open Hands Association", "Volunteering",
                      "Your neighbourhood · Saturday mornings"],
            "clienti": ["I'm looking for clients nearby.", "shaw.bakery", "Work and business",
                        "Looking for exactly what you do · 5 km away"],
            "assumere": ["I'm looking for someone for the shop.", "kit.looking.for.work", "Work and business",
                         "Retail experience · 4 km away · available now"],
            "relazione": ["I'd like to meet someone, no rush.", "coffee.and.galleries", "Partner",
                          "The same galleries · the same films · the same idea of Sunday"],
        },
        "azienda": {
            "frase": "The sparrow takes you to the people already looking for you.",
            "sotto": "A verified organisation. No feed: your invitations arrive as leaves.",
            "ruolo_org": "Organisation profile", "mostra_org": "verified, under its own name",
            "ruoli": {"invito": "Targeted invitation", "evento": "Event", "assumere": "We're hiring", "soci": "Network"},
            "varianti": {
                "libreria": {"nome": "The Arcade Bookshop",
                             "invito": "To people who love crime novels, within 10 km. Up to 100 people.",
                             "evento": "Crime author at the bookshop · Thursday 6:30 pm",
                             "assumere": "Part-time bookseller · pay stated in the listing",
                             "soci": "Local bookshops, for a festival",
                             "foglia": ["I'd like a crime novel book talk, in the evening.",
                                        "Crime novels · evenings · 4 km away"]},
                "sport": {"nome": "Borgo Sports Club",
                          "invito": "To people looking for a volleyball team, aged 16 and up. Up to 100 people.",
                          "evento": "Volleyball tournament · Sunday morning",
                          "assumere": "Youth coach · pay stated in the listing",
                          "soci": "Nearby clubs, for a joint tournament",
                          "foglia": ["I'm looking for a volleyball team.", "Volleyball · Sundays · 3 km away"]},
                "volontario": {"nome": "Open Hands Association",
                               "invito": "To people who want to help on Saturday mornings. Up to 100 people.",
                               "evento": "Food drive · Saturday morning",
                               "assumere": "Volunteer coordinator · part-time",
                               "soci": "Nearby associations, for a joint food drive",
                               "foglia": ["I'd like to help someone, on Saturdays.", "Volunteering · Saturdays · 3 km away"]},
                "creativo": {"nome": "The Key Music School",
                             "invito": "To people who play and are looking for a band. Up to 100 people.",
                             "evento": "Open jam · Friday night",
                             "assumere": "Guitar teacher · pay stated in the listing",
                             "soci": "Local rehearsal rooms, for a gig",
                             "foglia": ["I'm looking for people to play music with.", "Live music · Fridays · 5 km away"]},
            },
            "vede": None,
        },
        "privacy_pred": "Nobody sees anything. Until you want them to.",
    },
}

VARIANTE_ORG = {"sport": "sport", "volontario": "volontario", "creativo": "creativo"}
ORG_TIPO = {"clienti": "invito", "serate": "evento", "causa": "evento", "mentore": "evento", "assumere": "assumere",
            "soci": "soci"}
ORG_ICONA = {"invito": "invito", "evento": "evento", "assumere": "assumere", "soci": "soci"}


def json_lingua(lang):
    """Il blocco JSON che legge sito.js (senza le etichette delle tessere, che sono nell'HTML)."""
    d = DATI[lang]
    dati = {k: d[k] for k in ("ruoli", "righe", "sotto", "profili", "riserva", "foglie", "foglie_riserva", "azienda",
                              "privacy_pred")}
    dati.update(colori=COLORI_COSA, ordine_colori=ORDINE_COLORI, porte=PORTE, porte_org=PORTE_ORG, riempi=RIEMPI,
                riempi_org=RIEMPI_ORG, nomi=NOMI, prefissi=PREFISSI, variante_org=VARIANTE_ORG, org_tipo=ORG_TIPO, org_icona=ORG_ICONA, pred=PRED)
    testo = json.dumps(dati, ensure_ascii=False, separators=(",", ":"))
    return testo.replace("</", "<\\/")   # mai «</script» dentro il blocco


def visibile_cosa(chiave, chi):
    if chiave in SOLO and not any(c in SOLO[chiave] for c in chi):
        return False
    return not any(c in NASCONDI.get(chiave, []) for c in chi)


def compone(lang, chi, cosa):
    """Stesso calcolo di sito.js: restituisce frase, riga, schede, privacy, foglia, porte."""
    d = DATI[lang]
    cosa = [c for c in cosa if visibile_cosa(c, chi)]
    usati_col = []

    def colore(c):
        lista = [c] + ORDINE_COLORI
        for x in lista:
            if x not in usati_col:
                usati_col.append(x)
                return x
        return c

    if "azienda" in chi:
        a = d["azienda"]
        altro = next((c for c in chi if c in VARIANTE_ORG), None)
        v = a["varianti"][VARIANTE_ORG.get(altro, "libreria")]
        schede = [{"u": v["nome"], "ruolo": a["ruolo_org"], "mostra": a["mostra_org"], "icona": "org"}]
        tipi = []
        for c in cosa:
            t = ORG_TIPO.get(c)
            if t and t not in tipi:
                tipi.append(t)
        for t in ("invito", "evento", "soci"):
            if len(tipi) >= 2:
                break
            if t not in tipi:
                tipi.append(t)
        for t in tipi[:2]:
            schede.append({"u": v[t], "ruolo": a["ruoli"][t], "mostra": "", "icona": ORG_ICONA[t]})
        porte = []
        for c in cosa:
            p = PORTE_ORG.get(c)
            if p and p not in porte:
                porte.append(p)
        for p in RIEMPI_ORG:
            if p not in porte:
                porte.append(p)
        riga = d["righe"].get(cosa[0], "") if cosa else ""
        foglia = [v["foglia"][0], v["nome"], a["ruoli"]["evento"], v["foglia"][1]]
        return dict(frase=a["frase"], riga=riga, schede=schede, sotto=a["sotto"], privacy=d["privacy_pred"],
                    foglia=foglia, porte=porte[:3])

    ordine = list(dict.fromkeys((["superiori"] if "superiori" in chi else []) + list(chi)))
    p = d["profili"][chi[0]]
    s = p["serio"]
    schede = [{"u": s["u"], "ruolo": s["ruolo"], "mostra": s["mostra"], "colore": colore(s["colore"]),
               "testa": s.get("testa")}]
    usati = {s["u"]}
    nomi = {nome_di(s["u"])}
    tipi = set(s["copre"])

    def aggiungi(q):
        if len(schede) >= 3 or q in tipi:
            return
        tipi.add(q)
        voce = next((d["profili"][x]["per"][q] for x in ordine
                     if q in d["profili"][x]["per"] and d["profili"][x]["per"][q]["u"] not in usati), None)
        voce = voce or (d["riserva"].get(q) if d["riserva"].get(q, {}).get("u") not in usati else None)
        u = senza_nome(voce["u"], nomi) if voce else ""
        if voce and "." in u:
            usati.add(voce["u"])
            nomi.add(nome_di(u))
            schede.append({"u": u, "ruolo": d["ruoli"][q], "mostra": voce["mostra"],
                           "colore": colore(COLORI_COSA[q]), "testa": None})

    for q in cosa:
        aggiungi(q)
    for x in chi[1:]:
        if len(schede) >= 3:
            break
        s2 = d["profili"].get(x, {}).get("serio")
        u2 = senza_nome(s2["u"], nomi) if s2 else ""
        if s2 and s2["u"] not in usati and "." in u2:
            usati.add(s2["u"])
            nomi.add(nome_di(u2))
            schede.append({"u": u2, "ruolo": s2["ruolo"], "mostra": s2["mostra"], "colore": colore(s2["colore"]),
                           "testa": s2.get("testa")})
    for q in p["riserva"] + list(d["riserva"]):
        if len(schede) >= 3:
            break
        if visibile_cosa(q, chi):
            aggiungi(q)
    riga = d["righe"].get(cosa[0], "") if cosa else ""
    privacy = p["vede"].replace("{1}", schede[0]["u"]).replace("{3}", schede[-1]["u"])
    q0 = cosa[0] if cosa else p["riserva"][0]
    foglia = d["foglie"].get(f"{chi[0]}|{q0}") or next(
        (d["foglie"][f"{x}|{q0}"] for x in ordine if f"{x}|{q0}" in d["foglie"]), None) or d["foglie_riserva"][q0]
    porte = []
    for q in cosa[:1]:
        porte.append(PORTE[q])
    if "username" not in porte:
        porte.append("username")
    for q in cosa[1:]:
        if PORTE[q] not in porte:
            porte.append(PORTE[q])
    for x in RIEMPI:
        if x not in porte:
            porte.append(x)
    return dict(frase=p["frase"], riga=riga, schede=schede, sotto=d["sotto"], privacy=privacy, foglia=foglia,
                porte=porte[:3])
