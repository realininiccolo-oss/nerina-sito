"""Pagina iniziale di nerina.eu — v4 (18/11/2026): percorso personalizzato.

1. benvenuto: marchio al centro, il messaggio, la scelta del tema (Recanati, Infinito, Ginestra);
2. due domande chiuse (che cosa cerchi · quale frase ti somiglia) che adattano gli esempi;
3. tre idee spiegate con un'animazione ciascuna: una persona, più ruoli (username) · il passero unisce · privacy
   europea (cursore della visibilità);
4. le funzioni (una pagina ciascuna), sicurezza, il pilota.
Senza JavaScript si vede la versione predefinita (data-predefinito) e il tema Recanati.
Fonti delle affermazioni: claude/sito-v4-esito-2026-11-18.md.
"""
import grafica as g
import temi
from funzioni import FUNZIONI, url_funzione, schermo

T = {
    "it": dict(
        h1="Il social network che unisce le persone.",
        attacco=("Sii chi vuoi, con un&#x27;identità vera alle spalle. Su Nerina conta l&#x27;essenza di un "
                 "incontro, non l&#x27;apparenza."),
        tema_domanda="Prima di cominciare: come vuoi vedere Nerina?",
        tema_nota="Sono i tre temi dell&#x27;app. Il sito resta nel tema che scegli; lo cambi quando vuoi.",
        temi={"recanati": "Caldo, terracotta", "infinito": "Calmo, blu di sera", "ginestra": "Vivo, prugna e cielo"},
        d1="Che cosa ti porta qui?",
        d1_opz=[("persone", "Conoscere persone affini"), ("lavoro", "Lavoro e opportunità"),
                ("eventi", "Eventi e posti"), ("azienda", "Ho un&#x27;azienda o un&#x27;associazione")],
        d2="Quale frase ti somiglia di più?",
        d2_opz=[("studio", "Studio"), ("lavoro", "Lavoro"), ("citta", "Sono in una città nuova"),
                ("tempo", "Ho più tempo per me")],
        ricomincia="Rispondi di nuovo",
        ruoli=dict(
            nome="Una persona, più ruoli",
            h2="Sei tante persone. Tutte vere.",
            p=["Con i colleghi, con chi corre con te, con chi condivide una passione: ogni contesto vuole "
               "informazioni diverse. Su Nerina hai fino a tre username, uno per ruolo sociale, ognuno con il suo "
               "omino e solo le informazioni che scegli. Chi ti incontra vede l&#x27;username giusto per quel "
               "contesto.",
               "Dietro ogni username c&#x27;è un&#x27;identità verificata con un documento. Sii chi vuoi, ma sempre "
               "tu."],
            verificata="identità verificata",
            varianti={
                "studio": [("giulia.studia", "Studio", "Analisi 1 · biblioteca il mercoledì", "infinito"),
                           ("giulia.volley", "Attività insieme", "pallavolo il martedì", "corallo"),
                           ("giulia.suona", "Amicizia", "chitarra · musica indie", "prugna")],
                "lavoro": [("prof.enrico", "Mentore e insegnamento", "nome, cognome e materia", "petrolio"),
                           ("enry.corre", "Attività insieme", "corsa in Franciacorta", "terra"),
                           ("enrico.lavora", "Lavoro e affari", "ingegnere · cerca soci", "ardesia")],
                "citta": [("marta.milano", "Amicizia", "nuova in città · cinema", "lampone"),
                          ("marta.cucina", "Attività insieme", "corsi di cucina", "ginestra"),
                          ("marta.design", "Lavoro e affari", "grafica · collaborazioni", "infinito")],
                "tempo": [("franco.cammina", "Attività insieme", "camminate in montagna", "foglia"),
                          ("franco.aiuta", "Volontariato", "protezione civile", "corallo"),
                          ("franco.legge", "Amicizia", "gialli e storia", "oliva")],
            }),
        passero=dict(
            nome="Il passero",
            h2="Il passero unisce. Voi decidete.",
            p=["Racconti nel Diario che cosa cerchi. Il passero, un&#x27;intelligenza artificiale, cerca tra le "
               "persone verificate di Nerina e ti porta una foglia: una proposta che deve avere senso per tutti e "
               "due. Niente punteggi, niente feed: accettate o rifiutate voi."],
            tu="Tu", altro="Un&#x27;altra persona", foglia="Foglia",
            varianti={
                "persone": ("Cerco qualcuno con cui correre la domenica mattina.",
                            "Vorrei un compagno di corsa, vicino a casa.",
                            "Corsa insieme · domenica mattina · in un parco pubblico"),
                "lavoro": ("Cerco chi mi aiuti a costruire il sito del mio progetto.",
                           "Vorrei lavorare a un progetto nuovo, la sera.",
                           "Lavoro e affari · un progetto in comune"),
                "eventi": ("Organizzo un torneo di briscola all&#x27;oratorio.",
                           "Mi piacerebbe giocare a carte con gente nuova.",
                           "Evento · torneo di briscola · sabato"),
                "azienda": ("La nostra libreria organizza un incontro con un autore.",
                            "Cerco presentazioni di libri vicino a casa.",
                            "Evento · incontro con l&#x27;autore · solo se l&#x27;hai permesso"),
            }),
        privacy=dict(
            nome="Privacy europea",
            h2="Nata in Europa. Chiusa di partenza.",
            p=["Nerina è costruita intorno alla cultura sociale europea: le regole europee sulla privacy sono il "
               "punto di partenza, non un ostacolo. Ogni dato parte da «Nessuno» e lo apri tu, un livello alla "
               "volta. Così contano le cose che vi accomunano, non quanto sei esposto."],
            cursore="Prova: chi vede un tuo dato?",
            livelli=[("Nessuno", "Solo tu. Nemmeno i passeri lo usano. È così di partenza."),
                     ("Passeri", "Lo usano i passeri per trovarti proposte. Nessuna persona lo legge."),
                     ("Interessati", "Chi ha una foglia o un abbinamento in corso con te."),
                     ("Connessioni", "Le tue connessioni."),
                     ("Pubblica", "Le persone verificate di Nerina. Mai il web: non si indicizza.")],
            fatti=["Il passero usa un modello europeo, di Mistral AI (Francia), e non riceve il tuo cognome, la "
                   "data di nascita né la foto.",
                   "I tuoi contenuti non si vendono, non servono alla pubblicità e non addestrano "
                   "l&#x27;intelligenza artificiale.",
                   "Se elimini l&#x27;account cancelliamo i tuoi dati e distruggiamo la chiave che li cifra."],
            link=("/informativa/", "Leggi l&#x27;informativa: che cosa è pronto e che cosa manca")),
        funzioni=dict(nome="Le funzioni", h2="Ogni cosa al suo posto.",
                      per_te="Per te, comincia da qui", tutte="Tutte le funzioni"),
        consigli={"persone": ["foglie", "username", "diario"], "lavoro": ["lavoro", "username", "foglie"],
                  "eventi": ["eventi", "wind", "foglie"], "azienda": ["eventi", "wind", "lavoro"]},
        sicurezza=dict(nome="Sicurezza", h2="Persone vere, regole chiare.",
                       p=["Si entra dai 16 anni, dopo la verifica di un documento d&#x27;identità, con un account a "
                          "testa. Chi ha 16 o 17 anni riceve proposte solo da persone vicine d&#x27;età. Puoi "
                          "segnalare e bloccare chiunque: ogni segnalazione la decide una persona."],
                       link=("/sicurezza-minori/", "Gli standard sulla sicurezza dei minori")),
        pilota=dict(h2="Nerina è su invito.",
                    p="Stiamo muovendo i primi passi con poche persone, nell&#x27;Unione europea. Durante il pilota è "
                      "gratuita e senza pubblicità.",
                    bottone=("/contatti/", "Scrivici")),
        editore=("Nerina è pubblicata con il nome <strong>Nerina Devs</strong>. Chi è il titolare del trattamento è "
                 "scritto nell&#x27;<a href=\"/informativa/#chi-tratta-i-dati\">informativa</a>."),
    ),
    "en": dict(
        h1="The social network that brings people together.",
        attacco=("Be whoever you want, with a real identity behind you. On Nerina what matters is the essence of a "
                 "connection, not appearances."),
        tema_domanda="Before we start: how would you like to see Nerina?",
        tema_nota="These are the app&#x27;s three themes. The site keeps the one you choose; change it any time.",
        temi={"recanati": "Warm, terracotta", "infinito": "Calm, evening blue", "ginestra": "Lively, plum and sky"},
        d1="What brings you here?",
        d1_opz=[("persone", "Meeting like-minded people"), ("lavoro", "Work and opportunities"),
                ("eventi", "Events and places"), ("azienda", "I run a business or an association")],
        d2="Which of these sounds most like you?",
        d2_opz=[("studio", "I study"), ("lavoro", "I work"), ("citta", "I just moved to a new city"),
                ("tempo", "I have more time for myself")],
        ricomincia="Answer again",
        ruoli=dict(
            nome="One person, several roles",
            h2="You are many people. All of them real.",
            p=["With colleagues, with your running partner, with people who share a passion: each context needs "
               "different details. On Nerina you have up to three usernames, one per social role, each with its own "
               "avatar and only the details you choose. People you meet see the username that fits that context.",
               "Behind every username there is an identity verified with a document. Be whoever you want, but "
               "always yourself."],
            verificata="verified identity",
            varianti={
                "studio": [("giulia.studies", "Study", "Calculus 1 · library on Wednesdays", "infinito"),
                           ("giulia.volley", "Activities together", "volleyball on Tuesdays", "corallo"),
                           ("giulia.plays", "Friendship", "guitar · indie music", "prugna")],
                "lavoro": [("prof.enrico", "Mentoring and teaching", "name, surname and subject", "petrolio"),
                           ("enry.runs", "Activities together", "running in Franciacorta", "terra"),
                           ("enrico.works", "Work and business", "engineer · looking for partners", "ardesia")],
                "citta": [("marta.milan", "Friendship", "new in town · cinema", "lampone"),
                          ("marta.cooks", "Activities together", "cooking classes", "ginestra"),
                          ("marta.design", "Work and business", "graphic design · collaborations", "infinito")],
                "tempo": [("franco.walks", "Activities together", "mountain walks", "foglia"),
                          ("franco.helps", "Volunteering", "civil protection", "corallo"),
                          ("franco.reads", "Friendship", "crime novels and history", "oliva")],
            }),
        passero=dict(
            nome="The sparrow",
            h2="The sparrow connects. You decide.",
            p=["You tell the Diary what you are looking for. The sparrow, an AI, searches among Nerina&#x27;s "
               "verified people and brings you a leaf: a proposal that has to make sense for both of you. No scores, "
               "no feed: you accept or decline."],
            tu="You", altro="Someone else", foglia="Leaf",
            varianti={
                "persone": ("I&#x27;m looking for someone to run with on Sunday mornings.",
                            "I&#x27;d like a running partner close to home.",
                            "Running together · Sunday morning · in a public park"),
                "lavoro": ("I need help building the website for my project.",
                           "I&#x27;d like to work on a new project in the evenings.",
                           "Work and business · a shared project"),
                "eventi": ("I&#x27;m organising a card tournament at the parish hall.",
                           "I&#x27;d love to play cards with new people.",
                           "Event · card tournament · Saturday"),
                "azienda": ("Our bookshop is hosting a meet-the-author evening.",
                            "I&#x27;m looking for book talks near home.",
                            "Event · meet the author · only if you allowed it"),
            }),
        privacy=dict(
            nome="European privacy",
            h2="Born in Europe. Closed by default.",
            p=["Nerina is built around European social culture: European privacy rules are the starting point, not an "
               "obstacle. Every detail starts at «Nobody» and you open it, one level at a time. So what counts is "
               "what you share, not how exposed you are."],
            cursore="Try it: who sees one of your details?",
            livelli=[("Nobody", "Only you. Not even the sparrows use it. This is the default."),
                     ("Sparrows", "The sparrows use it to find proposals for you. No person reads it."),
                     ("Interested", "People with a leaf or a match in progress with you."),
                     ("Connections", "Your connections."),
                     ("Public", "Verified people on Nerina. Never the web: it is not indexed.")],
            fatti=["The sparrow uses a European model by Mistral AI (France) and never receives your surname, date of "
                   "birth or photo.",
                   "Your content is not sold, not used for advertising and not used to train AI.",
                   "If you delete your account we erase your data and destroy the key that encrypts it."],
            link=("/en/informativa/", "Read the privacy policy: what is ready and what is missing")),
        funzioni=dict(nome="Features", h2="Everything in its place.",
                      per_te="For you, start here", tutte="All features"),
        consigli={"persone": ["foglie", "username", "diario"], "lavoro": ["lavoro", "username", "foglie"],
                  "eventi": ["eventi", "wind", "foglie"], "azienda": ["eventi", "wind", "lavoro"]},
        sicurezza=dict(nome="Safety", h2="Real people, clear rules.",
                       p=["You can join from 16, after an identity document is verified, with one account per person. "
                          "People aged 16 or 17 only get proposals from people close in age. You can report and "
                          "block anyone: a person decides every report."],
                       link=("/en/child-safety/", "Our child safety standards")),
        pilota=dict(h2="Nerina is invitation only.",
                    p="We are taking our first steps with a few people in the European Union. During the pilot it is "
                      "free and has no ads.",
                    bottone=("/en/contact/", "Write to us")),
        editore=("Nerina is published under the name <strong>Nerina Devs</strong>. The data controller is named in "
                 "the <a href=\"/en/informativa/#who-processes-the-data\">privacy policy</a>."),
    ),
}

PRED = {"cerca": "persone", "fase": "lavoro"}


def _variante(chiave, valore, html, tag="div", classe=""):
    pred = " data-predefinito" if PRED[chiave] == valore else " hidden"
    return f'<{tag} class="{classe}" data-se="{chiave}:{valore}"{pred}>{html}</{tag}>'


def _scelte(nome, opzioni, vai):
    return ('<div class="scelte" role="group">' + "".join(
        f'<button type="button" class="scelta" data-domanda="{nome}" data-valore="{v}" data-vai="{vai}" '
        f'aria-pressed="false">{t}</button>' for v, t in opzioni) + "</div>")


def _intestazione(nome, h2, ident):
    return f'<p class="sezione-nome">{nome}</p>\n<h2 id="{ident}-titolo">{h2}</h2>'


def _ruoli(t):
    r = t["ruoli"]
    blocchi = []
    for fase, usernames in r["varianti"].items():
        carte = "".join(
            f'<li class="ruolo r{n}"><svg class="ruolo-omino" viewBox="0 0 64 64" aria-hidden="true">'
            f'{g.omino(f"ru-{fase}-{n}", colore)}</svg>'
            f'<span class="ruolo-nome">{u}</span><span class="ruolo-contesto">{c}</span>'
            f'<span class="ruolo-info">{i}</span></li>'
            for n, (u, c, i, colore) in enumerate(usernames, 1))
        blocchi.append(_variante("fase", fase, f'<ul class="ruoli-carte">{carte}</ul>', classe="ruoli-variante"))
    persona = (f'<div class="ruoli-persona"><svg class="ruolo-omino grande" viewBox="0 0 64 64" aria-hidden="true">'
               f'{g.omino("ru-persona", "ardesia")}</svg><span class="verificata">{g.icona("consensi", "icona", 18)}'
               f'{r["verificata"]}</span></div>')
    linee = ('<svg class="ruoli-linee" viewBox="0 0 300 60" preserveAspectRatio="none" aria-hidden="true">'
             '<path class="l1" d="M150 0 C150 30 50 30 50 60"/><path class="l2" d="M150 0 V60"/>'
             '<path class="l3" d="M150 0 C150 30 250 30 250 60"/></svg>')
    testo = "".join(f"<p>{x}</p>" for x in r["p"])
    return (f'<section class="sezione" id="ruoli" aria-labelledby="ruoli-titolo">\n<div class="sezione-testo">'
            f'{_intestazione(r["nome"], r["h2"], "ruoli")}\n{testo}</div>\n'
            f'<div class="schema schema-ruoli anima" aria-hidden="true">{persona}{linee}{"".join(blocchi)}</div>\n</section>')


def _passero(t):
    p = t["passero"]
    blocchi = []
    for cerca, (a, b, f) in p["varianti"].items():
        blocchi.append(_variante("cerca", cerca, (
            f'<div class="dialogo"><p class="nuvola nuvola-a"><span>{p["tu"]}</span>{a}</p>'
            f'<div class="schema-passero">{g.logo_passero_solo()}</div>'
            f'<p class="nuvola nuvola-b"><span>{p["altro"]}</span>{b}</p></div>'
            f'<p class="foglia-proposta">{g.icona("foglia", "icona", 20)}<span><strong>{p["foglia"]}</strong> {f}</span></p>'),
            classe="passero-variante"))
    testo = "".join(f"<p>{x}</p>" for x in p["p"])
    return (f'<section class="sezione" id="passero" aria-labelledby="passero-titolo">\n<div class="sezione-testo">'
            f'{_intestazione(p["nome"], p["h2"], "passero")}\n{testo}</div>\n'
            f'<div class="schema schema-incontro anima">{"".join(blocchi)}</div>\n</section>')


def _privacy(t, lang):
    p = t["privacy"]
    anelli = "".join(f'<circle class="anello a{n}" cx="100" cy="100" r="{18 + n * 16}"/>' for n in range(5, 0, -1))
    testi = "".join(
        f'<p class="livello-testo" data-testo-livello="{n}"{"" if n == 1 else " hidden"}><strong>{nome}</strong> {d}</p>'
        for n, (nome, d) in enumerate(p["livelli"], 1))
    tacche = "".join(f"<li>{nome}</li>" for nome, _ in p["livelli"])
    fatti = "".join(f"<li>{x}</li>" for x in p["fatti"])
    testo = "".join(f"<p>{x}</p>" for x in p["p"])
    return f"""<section class="sezione" id="privacy" aria-labelledby="privacy-titolo">
<div class="sezione-testo">{_intestazione(p["nome"], p["h2"], "privacy")}
{testo}
<ul class="fatti">{fatti}</ul>
<p><a href="{p["link"][0]}">{p["link"][1]}</a></p></div>
<div class="schema schema-livelli anima" data-scatola-livelli data-livello="1">
<svg class="livelli-anelli" viewBox="0 0 200 200" aria-hidden="true">{anelli}<circle class="centro" cx="100" cy="100" r="14"/></svg>
<label class="cursore-etichetta" for="cursore-{lang}">{p["cursore"]}</label>
<input id="cursore-{lang}" class="cursore" type="range" min="1" max="5" step="1" value="1" data-livelli>
<ol class="tacche" aria-hidden="true">{tacche}</ol>
<div class="livelli-testi" aria-live="polite">{testi}</div>
</div>
</section>"""


def _funzioni(t, lang):
    f = t["funzioni"]
    consigli = []
    for cerca, chiavi in t["consigli"].items():
        voci = "".join(_carta_funzione(k, lang, piccola=True) for k in chiavi)
        consigli.append(_variante("cerca", cerca, f'<ul class="carte-funzioni carte-consigli">{voci}</ul>',
                                  classe="consigli-variante"))
    tutte = "".join(_carta_funzione(k, lang) for k in FUNZIONI)
    return (f'<section class="sezione sezione-larga" id="funzioni" aria-labelledby="funzioni-titolo">\n'
            f'<div class="sezione-testo">{_intestazione(f["nome"], f["h2"], "funzioni")}</div>\n'
            f'<h3 class="sottotitolo">{f["per_te"]}</h3>\n{"".join(consigli)}\n'
            f'<h3 class="sottotitolo">{f["tutte"]}</h3>\n<ul class="carte-funzioni">{tutte}</ul>\n</section>')


def _carta_funzione(chiave, lang, piccola=False):
    d = FUNZIONI[chiave][lang]
    img = schermo(FUNZIONI[chiave]["schermo"], lang, "", "carta-schermo")
    figura = f'<span class="carta-figura">{img}</span>' if img else f'<span class="carta-figura vuota">{g.icona(FUNZIONI[chiave]["icona"], "icona", 32)}</span>'
    return (f'<li><a class="carta-funzione{" piccola" if piccola else ""}" href="{url_funzione(chiave, lang)}">'
            f'{figura}<span class="carta-testo"><span class="carta-nome">{d["nome"]}</span>'
            f'<span class="carta-frase">{d["frase"]}</span></span></a></li>')


def _scelta_tema(t, lang):
    carte = []
    for nome, tema in temi.TEMI.items():
        c, s = tema["chiaro"], tema["scuro"]
        stile = (f"--a-carta:{c['carta']};--a-alta:{c['carta_alta']};--a-ink:{c['inchiostro']};--a-pri:{c['primario']};"
                 f"--a-amb:{c['ambra']};--a-bordo:{c['bordo']};--s-carta:{s['carta']};--s-alta:{s['carta_alta']};"
                 f"--s-ink:{s['inchiostro']};--s-pri:{s['primario']};--s-amb:{s['ambra']};--s-bordo:{s['bordo']}")
        carte.append(
            f'<button type="button" class="tema-carta" data-tema-scelta="{nome}" data-vai="#domanda-cerca" '
            f'aria-pressed="false" style="{stile}"><span class="tema-anteprima" aria-hidden="true">'
            f'<span class="ta-barra"></span><span class="ta-titolo"></span><span class="ta-riga"></span>'
            f'<span class="ta-riga corta"></span><span class="ta-foglia">{g.foglia_filo()}</span>'
            f'<span class="ta-bottone"></span></span>'
            f'<span class="tema-nome">{tema["nome"][lang]}</span><span class="tema-desc">{t["temi"][nome]}</span></button>')
    return (f'<div class="scelta-tema"><p class="domanda" id="domanda-tema">{t["tema_domanda"]}</p>'
            f'<div class="temi" role="group" aria-labelledby="domanda-tema">{"".join(carte)}</div>'
            f'<p class="nota">{t["tema_nota"]}</p></div>')


def casa(lang):
    t = T[lang]
    h1_id = "che-cos-e-nerina" if lang == "it" else "what-is-nerina"
    return f"""<section class="benvenuto" aria-labelledby="{h1_id}">
<div class="benvenuto-marchio">{g.logo("benvenuto", classe="logo logo-benvenuto")}</div>
<h1 id="{h1_id}" class="anima">{t["h1"]}</h1>
<p class="attacco anima">{t["attacco"]}</p>
{_scelta_tema(t, lang)}
</section>

<section class="domanda-blocco" id="domanda-cerca" aria-labelledby="d1">
<p class="domanda" id="d1">{t["d1"]}</p>
{_scelte("cerca", t["d1_opz"], "#domanda-fase")}
</section>
<section class="domanda-blocco" id="domanda-fase" aria-labelledby="d2" data-dopo="cerca">
<p class="domanda" id="d2">{t["d2"]}</p>
{_scelte("fase", t["d2_opz"], "#ruoli")}
<p class="ricomincia"><button type="button" class="link-bottone" data-ricomincia data-vai="#domanda-cerca">{t["ricomincia"]}</button></p>
</section>

{_ruoli(t)}

{_passero(t)}

{_privacy(t, lang)}

{_funzioni(t, lang)}

<section class="sezione" id="sicurezza" aria-labelledby="sicurezza-titolo">
<div class="sezione-testo">{_intestazione(t["sicurezza"]["nome"], t["sicurezza"]["h2"], "sicurezza")}
{"".join(f"<p>{x}</p>" for x in t["sicurezza"]["p"])}
<p><a href="{t["sicurezza"]["link"][0]}">{t["sicurezza"]["link"][1]}</a></p></div>
</section>

<section class="pilota anima" id="pilota" aria-labelledby="pilota-titolo">
<h2 id="pilota-titolo">{t["pilota"]["h2"]}</h2>
<p>{t["pilota"]["p"]}</p>
<p><a class="bottone" href="{t["pilota"]["bottone"][0]}">{t["pilota"]["bottone"][1]}</a></p>
</section>
<p class="editore">{t["editore"]}</p>"""
