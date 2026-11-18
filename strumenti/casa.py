"""Pagina iniziale di nerina.eu — v5 (18/11/2026): un percorso a stanze, ognuna a tutta pagina.

soglia (marchio) → luce (tema) → che cosa cerchi → il luogo (piazza, laboratorio, cortile, bottega) → chi sei oggi →
più ruoli → il passero → privacy → le stanze (funzioni) → su invito.
Con JavaScript ogni stanza si apre dopo la risposta e il resto del percorso prende l'aria del luogo scelto;
senza, si vede tutto con le risposte predefinite. Pochissime parole: una riga per stanza.
Le righe di marketing sono di Niccolò (18/11, 10:06), riscritte.
"""
import grafica as g
import scene
import temi
from funzioni import FUNZIONI, url_funzione, schermo

T = {
    "it": dict(
        h1="Il social network che unisce le persone.",
        entra="Entra",
        luce="Scegli la tua luce.",
        cerca="Che cosa cerchi?",
        cerca_opz=[("persone", "Persone affini"), ("lavoro", "Lavoro"), ("eventi", "Eventi"),
                   ("azienda", "Per la mia attività")],
        luoghi={"persone": ("La piazza", "Qui le persone non si scorrono. Si incontrano."),
                "lavoro": ("Il laboratorio", "Qui conta quello che sai fare, non quanti ti seguono."),
                "eventi": ("Il cortile", "Qui ogni sera qualcuno organizza qualcosa."),
                "azienda": ("La bottega", "Qui ti trova chi ti cerca davvero.")},
        fase="E tu, chi sei oggi?",
        fase_opz=[("studio", "Studio"), ("lavoro", "Lavoro"), ("citta", "Città nuova"), ("tempo", "Tempo per me")],
        ruoli=("Sei più di un profilo.",
               "Sii chi vuoi, con un&#x27;identità verificata: fino a tre username, uno per ogni ruolo."),
        verificata="identità verificata",
        username={
            "studio": [("giulia.studia", "Studio", "infinito"), ("giulia.volley", "Attività insieme", "corallo"),
                       ("giulia.suona", "Amicizia", "prugna")],
            "lavoro": [("prof.enrico", "Mentore", "petrolio"), ("enry.corre", "Attività insieme", "terra"),
                       ("enrico.lavora", "Lavoro e affari", "ardesia")],
            "citta": [("marta.milano", "Amicizia", "lampone"), ("marta.cucina", "Attività insieme", "ginestra"),
                      ("marta.design", "Lavoro e affari", "infinito")],
            "tempo": [("franco.cammina", "Attività insieme", "foglia"), ("franco.aiuta", "Volontariato", "corallo"),
                      ("franco.legge", "Amicizia", "oliva")]},
        passero=("Il passero porta una foglia.",
                 "Conta l&#x27;essenza di un incontro, non l&#x27;apparenza. Il passero propone; voi decidete."),
        incontri={"persone": ("Cerco qualcuno con cui correre la domenica.", "Vorrei un compagno di corsa.",
                              "Corsa insieme · domenica · in un parco"),
                  "lavoro": ("Mi serve chi sappia costruire un sito.", "Vorrei un progetto nuovo, la sera.",
                             "Lavoro e affari · un progetto in comune"),
                  "eventi": ("Organizzo un torneo di briscola.", "Giocherei a carte con gente nuova.",
                             "Evento · torneo di briscola · sabato"),
                  "azienda": ("La libreria ospita un autore.", "Cerco presentazioni di libri.",
                              "Evento · incontro con l&#x27;autore")},
        privacy=("Nessuno vede niente. Finché non vuoi tu.",
                 "Costruita intorno alla cultura sociale europea: per proteggere la privacy e superare le barriere "
                 "sociali."),
        livelli=["Nessuno", "Passeri", "Interessati", "Connessioni", "Pubblica"],
        livelli_testi=["Solo tu.", "Solo i passeri, per trovarti proposte.", "Chi ha una foglia con te.",
                       "Le tue connessioni.", "Le persone verificate di Nerina. Mai il web."],
        cursore="Chi vede un tuo dato?",
        informativa=("/informativa/", "Informativa"),
        stanze="Le stanze di Nerina.", tutte="Tutte le stanze",
        consigli={"persone": ["foglie", "username", "diario"], "lavoro": ["lavoro", "username", "foglie"],
                  "eventi": ["eventi", "wind", "foglie"], "azienda": ["eventi", "wind", "lavoro"]},
        invito=("Su invito.", "Poche persone, nell&#x27;Unione europea. Gratis e senza pubblicità, nel pilota.",
                ("/contatti/", "Scrivici")),
        ricomincia="Ricomincia",
        editore=("Nerina è pubblicata con il nome <strong>Nerina Devs</strong>. Chi è il titolare del trattamento è "
                 "scritto nell&#x27;<a href=\"/informativa/#chi-tratta-i-dati\">informativa</a>."),
    ),
    "en": dict(
        h1="The social network that brings people together.",
        entra="Come in",
        luce="Choose your light.",
        cerca="What are you looking for?",
        cerca_opz=[("persone", "Like-minded people"), ("lavoro", "Work"), ("eventi", "Events"),
                   ("azienda", "For my business")],
        luoghi={"persone": ("The square", "Here people are not scrolled. They are met."),
                "lavoro": ("The workshop", "Here what counts is what you can do, not how many follow you."),
                "eventi": ("The courtyard", "Here someone is organising something every evening."),
                "azienda": ("The shop", "Here you are found by the people who are really looking for you.")},
        fase="And you, who are you today?",
        fase_opz=[("studio", "Studying"), ("lavoro", "Working"), ("citta", "New in town"), ("tempo", "Time for me")],
        ruoli=("You are more than a profile.",
               "Be whoever you want, with a verified identity: up to three usernames, one for each role."),
        verificata="verified identity",
        username={
            "studio": [("giulia.studies", "Study", "infinito"), ("giulia.volley", "Activities", "corallo"),
                       ("giulia.plays", "Friendship", "prugna")],
            "lavoro": [("prof.enrico", "Mentoring", "petrolio"), ("enry.runs", "Activities", "terra"),
                       ("enrico.works", "Work and business", "ardesia")],
            "citta": [("marta.milan", "Friendship", "lampone"), ("marta.cooks", "Activities", "ginestra"),
                      ("marta.design", "Work and business", "infinito")],
            "tempo": [("franco.walks", "Activities", "foglia"), ("franco.helps", "Volunteering", "corallo"),
                      ("franco.reads", "Friendship", "oliva")]},
        passero=("The sparrow brings a leaf.",
                 "What counts is the essence of a meeting, not appearances. The sparrow proposes; you decide."),
        incontri={"persone": ("I&#x27;m looking for someone to run with on Sundays.", "I&#x27;d like a running partner.",
                              "Running together · Sunday · in a park"),
                  "lavoro": ("I need someone who can build a website.", "I&#x27;d like a new project, in the evenings.",
                             "Work and business · a shared project"),
                  "eventi": ("I&#x27;m organising a card tournament.", "I&#x27;d play cards with new people.",
                             "Event · card tournament · Saturday"),
                  "azienda": ("The bookshop is hosting an author.", "I&#x27;m looking for book talks.",
                              "Event · meet the author")},
        privacy=("Nobody sees anything. Until you want them to.",
                 "Built around European social culture: to protect privacy and break down social barriers."),
        livelli=["Nobody", "Sparrows", "Interested", "Connections", "Public"],
        livelli_testi=["Only you.", "Only the sparrows, to find proposals for you.", "People with a leaf with you.",
                       "Your connections.", "Verified people on Nerina. Never the web."],
        cursore="Who sees one of your details?",
        informativa=("/en/informativa/", "Privacy policy"),
        stanze="Nerina&#x27;s rooms.", tutte="All rooms",
        consigli={"persone": ["foglie", "username", "diario"], "lavoro": ["lavoro", "username", "foglie"],
                  "eventi": ["eventi", "wind", "foglie"], "azienda": ["eventi", "wind", "lavoro"]},
        invito=("By invitation.", "A few people, in the European Union. Free and without ads, during the pilot.",
                ("/en/contact/", "Write to us")),
        ricomincia="Start again",
        editore=("Nerina is published under the name <strong>Nerina Devs</strong>. The data controller is named in "
                 "the <a href=\"/en/informativa/#who-processes-the-data\">privacy policy</a>."),
    ),
}

PRED = {"cerca": "persone", "fase": "lavoro"}
FRECCIA_GIU = g.icona("freccia", "icona freccia-giu", 22)


def _var(chiave, valore, html, classe=""):
    pred = " data-predefinito" if PRED[chiave] == valore else " hidden"
    return f'<div class="{classe}" data-se="{chiave}:{valore}"{pred}>{html}</div>'


def _scelte(nome, opzioni, vai, vignette):
    return ('<div class="scelte-illustrate" role="group">' + "".join(
        f'<button type="button" class="scelta-illustrata" data-domanda="{nome}" data-valore="{v}" data-vai="{vai}" '
        f'aria-pressed="false">{scene.vignetta(vignette.get(v, v))}<span>{t}</span></button>'
        for v, t in opzioni) + "</div>")


def _luce(t, lang):
    carte = "".join(
        f'<button type="button" class="finestra-tema" data-tema-scelta="{n}" data-vai="#cerca" aria-pressed="false">'
        f'{scene.finestra_tema(n)}<span>{temi.TEMI[n]["nome"][lang]}</span></button>' for n in temi.TEMI)
    return (f'<section class="stanza stanza-luce" id="luce" aria-labelledby="luce-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="luce-t">{t["luce"]}</h2>'
            f'<div class="finestre anima" role="group" aria-labelledby="luce-t">{carte}</div></div>\n</section>')


def _luoghi(t):
    blocchi = []
    for chiave, (nome, riga) in t["luoghi"].items():
        blocchi.append(_var("cerca", chiave, (
            f'<section class="stanza stanza-luogo-scena luogo-{chiave}" aria-label="{nome}">'
            f'<div class="stanza-in"><h2 class="luogo-nome anima">{nome}</h2><p class="sussurro-piccolo anima">{riga}</p>'
            f'<a class="avanti anima" href="#fase" aria-label="{t["fase"]}">{FRECCIA_GIU}</a></div>'
            f'{scene.luogo(chiave)}</section>')))
    return f'<div id="luogo" data-dopo="cerca">{"".join(blocchi)}</div>'


def _ruoli(t):
    persona = (f'<div class="ruoli-persona"><svg class="ruolo-omino grande" viewBox="0 0 64 64" aria-hidden="true">'
               f'{g.omino("ru-persona", "ardesia")}</svg><span class="verificata">{g.icona("consensi", "icona", 16)}'
               f'{t["verificata"]}</span></div>')
    linee = ('<svg class="ruoli-linee" viewBox="0 0 300 60" preserveAspectRatio="none" aria-hidden="true">'
             '<path class="l1" d="M150 0 C150 30 50 30 50 60"/><path class="l2" d="M150 0 V60"/>'
             '<path class="l3" d="M150 0 C150 30 250 30 250 60"/></svg>')
    var = "".join(_var("fase", fase, '<ul class="ruoli-carte">' + "".join(
        f'<li class="ruolo r{n}"><svg class="ruolo-omino" viewBox="0 0 64 64" aria-hidden="true">'
        f'{g.omino(f"ru-{fase}-{n}", col)}</svg><span class="ruolo-nome">{u}</span>'
        f'<span class="ruolo-contesto">{c}</span></li>' for n, (u, c, col) in enumerate(lista, 1)) + "</ul>",
        classe="ruoli-variante") for fase, lista in t["username"].items())
    h2, riga = t["ruoli"]
    return (f'<section class="stanza stanza-luogo" id="ruoli" aria-labelledby="ruoli-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="ruoli-t">{h2}</h2>'
            f'<div class="schema-ruoli anima">{persona}{linee}{var}</div>'
            f'<p class="sussurro-piccolo anima">{riga}</p></div>\n</section>')


def _passero(t):
    var = "".join(_var("cerca", c, (
        f'<div class="dialogo"><p class="nuvola nuvola-a">{a}</p>'
        f'<span class="schema-passero">{g.logo_passero_solo()}</span><p class="nuvola nuvola-b">{b}</p></div>'
        f'<p class="foglia-proposta">{g.icona("foglia", "icona", 20)}<span>{f}</span></p>'), classe="passero-variante")
        for c, (a, b, f) in t["incontri"].items())
    h2, riga = t["passero"]
    return (f'<section class="stanza stanza-luogo" id="passero" aria-labelledby="passero-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="passero-t">{h2}</h2>'
            f'<div class="schema-incontro anima">{var}</div>'
            f'<p class="sussurro-piccolo anima">{riga}</p></div>\n</section>')


def _privacy(t, lang):
    anelli = "".join(f'<circle class="anello a{n}" cx="100" cy="100" r="{18 + n * 16}"/>' for n in range(5, 0, -1))
    testi = "".join(f'<p class="livello-testo" data-testo-livello="{n}"{"" if n == 1 else " hidden"}>'
                    f'<strong>{nome}</strong> {d}</p>'
                    for n, (nome, d) in enumerate(zip(t["livelli"], t["livelli_testi"]), 1))
    tacche = "".join(f"<li>{x}</li>" for x in t["livelli"])
    h2, riga = t["privacy"]
    return f"""<section class="stanza stanza-luogo" id="privacy" aria-labelledby="privacy-t">
<div class="stanza-in">
<h2 class="sussurro anima" id="privacy-t">{h2}</h2>
<div class="schema-livelli anima" data-scatola-livelli data-livello="1">
<svg class="livelli-anelli" viewBox="0 0 200 200" aria-hidden="true">{anelli}<circle class="centro" cx="100" cy="100" r="14"/></svg>
<label class="cursore-etichetta" for="cursore-{lang}">{t["cursore"]}</label>
<input id="cursore-{lang}" class="cursore" type="range" min="1" max="5" step="1" value="1" data-livelli>
<ol class="tacche" aria-hidden="true">{tacche}</ol>
<div class="livelli-testi" aria-live="polite">{testi}</div>
</div>
<p class="sussurro-piccolo anima">{riga} <a href="{t["informativa"][0]}">{t["informativa"][1]}</a></p>
</div>
</section>"""


def _stanze(t, lang):
    from casa_carte import carta
    var = "".join(_var("cerca", c, '<ul class="porte-stanze">' + "".join(carta(k, lang) for k in chiavi) + "</ul>")
                  for c, chiavi in t["consigli"].items())
    indice = "/funzioni/" if lang == "it" else "/en/features/"
    return (f'<section class="stanza stanza-luogo" id="stanze" aria-labelledby="stanze-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="stanze-t">{t["stanze"]}</h2><div class="anima">{var}</div>'
            f'<p class="anima"><a class="link-tutte" href="{indice}">{t["tutte"]}</a></p></div>\n</section>')


def casa(lang):
    t = T[lang]
    h1_id = "che-cos-e-nerina" if lang == "it" else "what-is-nerina"
    v_cerca = {}
    v_fase = {"lavoro": "lavoro-fase"}
    h2, riga, (url, bott) = t["invito"]
    return f"""<section class="stanza soglia" id="soglia" aria-labelledby="{h1_id}">
<div class="stanza-in">
{g.logo("soglia", classe="logo logo-soglia", alt="Nerina")}
<h1 class="sussurro anima" id="{h1_id}">{t["h1"]}</h1>
<a class="entra anima" href="#luce">{t["entra"]}{FRECCIA_GIU}</a>
</div>
</section>
{_luce(t, lang)}
<section class="stanza" id="cerca" aria-labelledby="cerca-t">
<div class="stanza-in"><h2 class="sussurro anima" id="cerca-t">{t["cerca"]}</h2>
{_scelte("cerca", t["cerca_opz"], "#luogo", v_cerca)}</div>
</section>
{_luoghi(t)}
<section class="stanza stanza-luogo" id="fase" aria-labelledby="fase-t" data-dopo="cerca">
<div class="stanza-in"><h2 class="sussurro anima" id="fase-t">{t["fase"]}</h2>
{_scelte("fase", t["fase_opz"], "#ruoli", v_fase)}</div>
</section>
<div class="dopo-fase" data-dopo="fase">
{_ruoli(t)}
{_passero(t)}
{_privacy(t, lang)}
{_stanze(t, lang)}
<section class="stanza stanza-luogo stanza-invito" id="invito" aria-labelledby="invito-t">
<div class="stanza-in">
<h2 class="sussurro anima" id="invito-t">{h2}</h2>
<p class="sussurro-piccolo anima">{riga}</p>
<p class="anima"><a class="bottone" href="{url}">{bott}</a></p>
<p class="ricomincia"><button type="button" class="link-bottone" data-ricomincia data-vai="#cerca">{t["ricomincia"]}</button></p>
<p class="editore">{t["editore"]}</p>
</div>
</section>
</div>"""
