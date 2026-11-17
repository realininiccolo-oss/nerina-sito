"""Costruisce le pagine di nerina.eu con la grafica v1 (18/11/2026).

Parte dalle pagine del commit b2f5422 («Sito minimo nerina.eu 17/11»), lette con git:
- tiene <head> (lang, hreflang, noindex, titolo) e il contenuto di <main>;
- cambia solo le frasi col nome (decisione 17/11, passo 4) e l'impaginazione;
- rifà testata, piè di pagina, pagina iniziale e 404.
Uso: python3 strumenti/costruisci.py   (dalla radice del repository)
"""
import html
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import grafica as g  # noqa: E402
import casa as casa_v2  # noqa: E402

RADICE = pathlib.Path(__file__).resolve().parent.parent
SORGENTE = "b2f5422"

PAGINE = [
    "index.html", "contatti/index.html", "elimina-account/index.html", "sicurezza-minori/index.html",
    "informativa/index.html", "termini/index.html",
    "en/index.html", "en/contact/index.html", "en/delete-account/index.html", "en/child-safety/index.html",
    "en/informativa/index.html", "en/terms/index.html",
]

EDITORE_IT = ("Nerina è pubblicata con il nome <strong>Nerina Devs</strong>. Chi è il titolare del trattamento è "
              "scritto nell&#x27;<a href=\"/informativa/#chi-tratta-i-dati\">informativa</a>.")
# [I] in inglese l'ancora è #who-processes-the-data: #chi-tratta-i-dati non esiste nella pagina inglese.
EDITORE_EN = ("Nerina is published under the name <strong>Nerina Devs</strong>. The data controller is named in the "
              "<a href=\"/en/informativa/#who-processes-the-data\">privacy policy</a>.")

# Passo 4: frasi col nome → frasi nuove (testo HTML esatto di b2f5422). Ogni frase deve comparire una volta sola.
NOME = {
    "contatti/index.html": [
        ("Nerina Devs è il nome con cui Niccolò Realini pubblica l&#x27;app. Nel pilota la gestisce questa persona, "
         "non una società, con domicilio a Erbusco (BS).",
         EDITORE_IT + " Nel pilota Nerina è gestita da una persona fisica, non da una società, a Erbusco (BS)."),
        ("il punto di contatto è Niccolò, a support@nerina.eu",
         "il punto di contatto è il responsabile della sicurezza dei minori, a support@nerina.eu"),
    ],
    "elimina-account/index.html": [
        ("Nerina Devs è il nome con cui Niccolò Realini pubblica l&#x27;app.", EDITORE_IT),
    ],
    "sicurezza-minori/index.html": [
        ("Nerina Devs è il nome con cui Niccolò Realini pubblica l&#x27;app.", EDITORE_IT),
        ("Il punto di contatto per la sicurezza dei minori è <strong>Niccolò</strong>, che gestisce Nerina.",
         "Il punto di contatto per la sicurezza dei minori è il <strong>responsabile della sicurezza dei minori di "
         "Nerina</strong>."),
    ],
    "en/contact/index.html": [
        ("Nerina Devs is the name under which Niccolò Realini publishes the app. During the pilot it is run by this "
         "person, not a company, based in Erbusco (BS), Italy.",
         EDITORE_EN + " During the pilot Nerina is run by a private individual, not a company, in Erbusco (BS), Italy."),
        ("the point of contact is Niccolò, at support@nerina.eu",
         "the point of contact is the child safety officer, at support@nerina.eu"),
    ],
    "en/delete-account/index.html": [
        ("Nerina Devs is the name under which Niccolò Realini publishes the app.", EDITORE_EN),
    ],
    "en/child-safety/index.html": [
        ("Nerina Devs is the name under which Niccolò Realini publishes the app.", EDITORE_EN),
        ("The child safety point of contact is <strong>Niccolò</strong>, who runs Nerina.",
         "The child safety point of contact is Nerina&#x27;s <strong>child safety officer</strong>."),
    ],
    # [I] solo l'indirizzo del link, non il testo: l'ancora #il-diario-e-il-passero non esiste nell'informativa.
    "termini/index.html": [
        ('href="/informativa/#il-diario-e-il-passero"', 'href="/informativa/#il-passero-e-il-modello-linguistico"'),
    ],
}

CHROME = {
    "it": dict(salta="Vai al contenuto", casa="/", marchio="Nerina, pagina iniziale", pagine="Pagine del sito",
               tabella="Tabella: scorre di lato", indice="In questa pagina", sezioni="Sezioni",
               voci=[("come-funziona", "Come funziona"), ("passero", "Il passero"), ("privacy", "Privacy"),
                     ("domande", "Domande")],
               titolo="Nerina · Trova chi parla la tua lingua",
               descrizione="Nerina è il social senza feed e senza post: racconti in privato al passero, "
                           "un&#x27;intelligenza artificiale, che cosa cerchi, e lui ti porta proposte pensate per te. "
                           "Privacy dal primo giorno. Pilota su invito."),
    "en": dict(salta="Skip to content", casa="/en/", marchio="Nerina, home page", pagine="Site pages",
               tabella="Table: scrolls sideways", indice="On this page", sezioni="Sections",
               voci=[("come-funziona", "How it works"), ("passero", "The sparrow"), ("privacy", "Privacy"),
                     ("domande", "FAQ")],
               titolo="Nerina · Find people who speak your language",
               descrizione="Nerina is the social app with no feed and no posts: tell the sparrow, an AI, in private "
                           "what you are looking for, and it brings you proposals made for you. Privacy from day one. "
                           "Invite-only pilot."),
}


def originale(percorso):
    return subprocess.run(["git", "show", f"{SORGENTE}:{percorso}"], cwd=RADICE, check=True,
                          capture_output=True, text=True).stdout


def parti(testo):
    lang = re.search(r'<html lang="([^"]+)"', testo).group(1)
    testa = re.search(r"<head>\n(.*?)</head>", testo, re.S).group(1)
    nav = re.search(r'<nav aria-label="Language · Lingua">(.*?)</nav>', testo, re.S).group(1)
    corpo = re.search(r"<main>\n?(.*?)</main>", testo, re.S).group(1)
    piede = re.findall(r'<a href="([^"]+)">([^<]+)</a>', re.search(r"<footer>(.*?)</footer>", testo, re.S).group(1))
    return lang, testa, nav, corpo, piede


def testata(lang, nav, casa=False):
    c = CHROME[lang]
    base = "" if casa else c["casa"]
    sezioni = "".join(f'<li><a href="{base}#{i}">{t}</a></li>' for i, t in c["voci"])
    return (f'<a class="salta" href="#contenuto">{c["salta"]}</a>\n'
            f'<header class="testata"><div class="testata-in">\n{g.marchio(c["casa"], c["marchio"])}\n'
            f'<nav class="sezioni" aria-label="{c["sezioni"]}"><ul>{sezioni}</ul></nav>\n'
            f'<nav class="lingua" aria-label="Language · Lingua">{nav}</nav>\n</div></header>')


def piede(lang, voci, nav, attuale):
    c = CHROME[lang]
    li = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == attuale else ""}>{t}</a></li>' for h, t in voci)
    return (f'<footer class="piede"><div class="piede-in">\n<div class="piede-marchio">{g.logo(classe="logo logo-piede", piccolo=True)}</div>\n'
            f'<nav aria-label="{c["pagine"]}"><ul>{li}</ul></nav>\n<p class="piede-lingua">{nav}</p>\n</div></footer>')


def documento(lang, testa, classe, corpo_html, nav, voci, attuale):
    colori = ('<meta name="theme-color" content="#f8f1e6" media="(prefers-color-scheme: light)">\n'
              '<meta name="theme-color" content="#1a120d" media="(prefers-color-scheme: dark)">\n')
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n{testa}{colori}</head>\n<body class="{classe}">\n'
            f"{testata(lang, nav, classe == 'pagina-casa')}\n<main id=\"contenuto\">\n{corpo_html.strip()}\n</main>\n"
            f"{piede(lang, voci, nav, attuale)}\n</body>\n</html>\n")


def impagina(corpo, lang):
    c = CHROME[lang]
    # indice «In questa pagina:» / «On this page:» + elenco di link
    corpo, n = re.subn(
        r"<p>(In questa pagina:|On this page:)</p>\n?(<(ul|ol)>.*?</\3>)",
        lambda m: f'<nav class="indice" aria-label="{c["indice"]}"><p class="indice-titolo">{m.group(1)}</p>'
                  f"{m.group(2)}</nav>", corpo, count=1, flags=re.S)
    if not n:
        # elenco fatto solo di ancore nella stessa pagina (sicurezza dei minori)
        corpo = re.sub(r"<ul>((?:<li><a href=\"#[^\"]+\">[^<]+</a></li>)+)</ul>",
                       lambda m: f'<nav class="indice" aria-label="{c["indice"]}"><ul>{m.group(1)}</ul></nav>',
                       corpo, count=1)
    corpo = corpo.replace('<div class="tabella-pubblica">',
                          f'<div class="tabella-pubblica" role="region" tabindex="0" aria-label="{c["tabella"]}">')
    corpo = corpo.replace('<p class="bozza-pagina" role="note">',
                          f'<p class="bozza-pagina" role="note">{g.icona("bozza")}<span>') \
        if 'class="bozza-pagina"' in corpo else corpo
    corpo = re.sub(r'(<p class="bozza-pagina" role="note">.*?)</p>', r"\1</span></p>", corpo, count=1, flags=re.S)
    return corpo


def pagina_404():
    testa = ('<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
             '<meta name="color-scheme" content="light dark">\n<title>Pagina non trovata · Page not found · Nerina</title>\n'
             '<meta name="robots" content="noindex">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
             '<link rel="stylesheet" href="/fonti/fonti-v12.css">\n<link rel="stylesheet" href="/sito.css">\n')
    corpo = (f'<p class="logo-404">{g.logo(classe="logo logo-grande")}</p>\n'
             '<section>\n<h1>Pagina non trovata</h1>\n<p>Questo indirizzo non esiste su nerina.eu. '
             'Forse è cambiato o c&#x27;è un errore di battitura.</p>\n'
             '<p><a href="/">Torna a «Che cos&#x27;è Nerina»</a> · <a href="/contatti/">Contatti</a></p>\n</section>\n'
             '<section lang="en">\n<h2>Page not found</h2>\n<p>This address does not exist on nerina.eu. '
             'It may have changed, or there may be a typo.</p>\n'
             '<p><a href="/en/">Go to «What is Nerina»</a> · <a href="/en/contact/">Contact</a></p>\n</section>')
    voci = [("/", "Che cos&#x27;è Nerina"), ("/contatti/", "Contatti"), ("/informativa/", "Informativa"),
            ("/termini/", "Termini"), ("/sicurezza-minori/", "Sicurezza dei minori"),
            ("/elimina-account/", "Elimina l&#x27;account")]
    nav = '<a href="/en/" hreflang="en" lang="en">English</a>'
    return documento("it", testa, "pagina-404", corpo, nav, voci, None)


def main():
    for p in PAGINE:
        lang, testa, nav, corpo, voci = parti(originale(p))
        for vecchio, nuovo in NOME.get(p, []):
            n = corpo.count(vecchio)
            if n != 1:
                sys.exit(f"{p}: «{vecchio[:50]}…» trovato {n} volte, atteso 1")
            corpo = corpo.replace(vecchio, nuovo)
        if p in ("index.html", "en/index.html"):
            corpo, classe = casa_v2.casa(lang), "pagina-casa"
            c = CHROME[lang]
            testa = re.sub(r"<title>.*?</title>", f"<title>{c['titolo']}</title>", testa)
            testa = testa.replace("</title>\n", f"</title>\n<meta name=\"description\" content=\"{c['descrizione']}\">\n", 1)
        else:
            corpo, classe = impagina(corpo, lang), "pagina-testo"
        attuale = "/" + p.removesuffix("index.html")
        (RADICE / p).write_text(documento(lang, testa, classe, corpo, nav, voci, attuale), encoding="utf-8")
        print("scritta", p)
    (RADICE / "404.html").write_text(pagina_404(), encoding="utf-8")
    (RADICE / ".nojekyll").write_text("", encoding="utf-8")
    print("scritte 404.html e .nojekyll")


if __name__ == "__main__":
    main()
