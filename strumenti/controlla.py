"""Controlli prima della pubblicazione di nerina.eu (grafica v1, 18/11/2026).

Uso: python3 strumenti/controlla.py   (dalla radice del repository). Esce con 1 se un controllo fallisce.
1. Il nome del titolare compare solo in informativa e termini (it, en).
2. Niente <script>, niente risorse (src, href di link) fuori da nerina.eu, niente @import o url() esterni nel CSS.
3. Ogni link interno porta a un file esistente; ogni ancora esiste nella pagina d'arrivo.
4. noindex esattamente dove c'era in b2f5422 (più 404.html, pagina nuova).
5. Testo visibile di <main> uguale a b2f5422, salvo le frasi del passo 4 (testo estratto, non HTML).
   Pagine delle funzioni e indice: nuove dal 18/11, nessun confronto. La pagina iniziale (it, en) è esclusa dal 18/11: testi nuovi chiesti da Niccolò (17/11 23:57); per lei si
   controlla solo che abbia la riga di Nerina Devs con il link all'informativa.
6. Contrasto ≥ 4,5:1 per testo e link nei due temi (valori letti da sito.css).
"""
import html.parser
import pathlib
import re
import subprocess
import sys
from urllib.parse import urlparse

RADICE = pathlib.Path(__file__).resolve().parent.parent
SORGENTE = "b2f5422"
NOME = re.compile(r"Niccol|Realini")
CON_NOME = {"informativa/index.html", "termini/index.html", "en/informativa/index.html", "en/terms/index.html"}
PAGINE_VECCHIE = [
    "index.html", "contatti/index.html", "elimina-account/index.html", "sicurezza-minori/index.html",
    "informativa/index.html", "termini/index.html", "en/index.html", "en/contact/index.html",
    "en/delete-account/index.html", "en/child-safety/index.html", "en/informativa/index.html", "en/terms/index.html",
]
BLOCCHI = {"p", "li", "h1", "h2", "h3", "h4", "td", "th", "tr", "div", "section", "nav", "ul", "ol", "table",
           "main", "header", "footer", "thead", "tbody", "br"}

ED_IT = ("Nerina è pubblicata con il nome Nerina Devs. Chi è il titolare del trattamento è scritto nell'informativa.")
ED_EN = "Nerina is published under the name Nerina Devs. The data controller is named in the privacy policy."
# Passo 4, in testo semplice: vecchio → nuovo. Tutto il resto del testo deve restare identico.
ATTESI = {
    "index.html": [("Nerina è l'app di Nerina Devs, il nome con cui Niccolò Realini pubblica l'app.", ED_IT)],
    "en/index.html": [("Nerina is the app by Nerina Devs, the name under which Niccolò Realini publishes the app.",
                       ED_EN)],
    "contatti/index.html": [
        ("Nerina Devs è il nome con cui Niccolò Realini pubblica l'app. Nel pilota la gestisce questa persona, "
         "non una società, con domicilio a Erbusco (BS).",
         ED_IT + " Nel pilota Nerina è gestita da una persona fisica, non da una società, a Erbusco (BS)."),
        ("il punto di contatto è Niccolò,", "il punto di contatto è il responsabile della sicurezza dei minori,")],
    "elimina-account/index.html": [("Nerina Devs è il nome con cui Niccolò Realini pubblica l'app.", ED_IT)],
    "sicurezza-minori/index.html": [
        ("Nerina Devs è il nome con cui Niccolò Realini pubblica l'app.", ED_IT),
        ("è Niccolò, che gestisce Nerina.", "è il responsabile della sicurezza dei minori di Nerina.")],
    "en/contact/index.html": [
        ("Nerina Devs is the name under which Niccolò Realini publishes the app. During the pilot it is run by this "
         "person, not a company, based in Erbusco (BS), Italy.",
         ED_EN + " During the pilot Nerina is run by a private individual, not a company, in Erbusco (BS), Italy."),
        ("the point of contact is Niccolò,", "the point of contact is the child safety officer,")],
    "en/delete-account/index.html": [("Nerina Devs is the name under which Niccolò Realini publishes the app.", ED_EN)],
    "en/child-safety/index.html": [
        ("Nerina Devs is the name under which Niccolò Realini publishes the app.", ED_EN),
        ("is Niccolò, who runs Nerina.", "is Nerina's child safety officer.")],
}

# Coppie testo/sfondo usate in sito.css (variabili). Tutte devono stare ≥ 4,5:1 nei due temi.
COPPIE = [
    ("inchiostro", "carta", "testo e titoli"), ("inchiostro", "carta-alta", "schede, indice"),
    ("inchiostro", "carta-bassa", "intestazioni delle tabelle, lingua"), ("inchiostro-2", "carta", "testo"),
    ("inchiostro-2", "carta-alta", "schede"), ("inchiostro-2", "carta-bassa", "lingua non scelta"),
    ("inchiostro-3", "carta", "note"), ("inchiostro-3", "carta-alta", "note nelle schede"),
    ("primario-testo", "carta", "link e nomi delle sezioni"), ("primario-testo", "carta-alta", "contesti degli username"),
    ("carta", "inchiostro", "bottoni e scelte"), ("inchiostro", "ambra-tenue", "riquadro Bozza"),
    ("inchiostro", "primario-tenue", "la piazza"), ("inchiostro-2", "primario-tenue", "la piazza, righe"),
    ("inchiostro-3", "primario-tenue", "la piazza, note"), ("inchiostro-2", "ambra-tenue", "la bottega, righe"),
    ("inchiostro-3", "carta-bassa", "tacche e note"),
]


class Estrattore(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.dentro_main = 0
        self.svg = 0
        self.testo = []
        self.ids = set()
        self.link = []      # (tag, attributo, valore)
        self.script = False
        self.script_inline = False
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "script":
            self.script = self.script or a.get("src") != "/sito.js"
            self.script_inline = True
        if tag == "meta" and a.get("name") == "robots" and "noindex" in (a.get("content") or ""):
            self.noindex = True
        for k in ("src", "href", "srcset", "poster", "data"):
            if k in a:
                self.link.append((tag, k, a[k]))
        if tag == "svg":
            self.svg += 1
        if tag == "main":
            self.dentro_main += 1
        if self.dentro_main and tag in BLOCCHI:
            self.testo.append(" ")

    def handle_endtag(self, tag):
        if tag == "svg":
            self.svg -= 1
        if self.dentro_main and tag in BLOCCHI:
            self.testo.append(" ")
        if tag == "main":
            self.dentro_main -= 1

    def handle_data(self, d):
        if self.dentro_main and not self.svg:
            self.testo.append(d)


def leggi(testo):
    e = Estrattore()
    e.feed(testo)
    return e


def normalizza(t):
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r" · ", " ", t)       # i separatori «·» tra i link della vecchia home diventano schede
    return t


def vecchio(p):
    return subprocess.run(["git", "show", f"{SORGENTE}:{p}"], cwd=RADICE, capture_output=True, text=True,
                          check=True).stdout


def luminanza(esa):
    esa = esa.lstrip("#")
    r, g, b = (int(esa[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrasto(a, b):
    la, lb = sorted((luminanza(a), luminanza(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def file_di(percorso):
    if percorso.endswith("/") or percorso == "":
        return RADICE / percorso.lstrip("/") / "index.html"
    f = RADICE / percorso.lstrip("/")
    return f / "index.html" if f.is_dir() else f


def main():
    errori = []
    pagine = sorted(p.relative_to(RADICE).as_posix() for p in RADICE.rglob("*.html") if ".git" not in p.parts)
    analisi = {p: leggi((RADICE / p).read_text(encoding="utf-8")) for p in pagine}

    # 1. nome
    for p in pagine:
        if NOME.search((RADICE / p).read_text(encoding="utf-8")) and p not in CON_NOME:
            errori.append(f"[1] nome presente in {p}")
    for p in CON_NOME:
        if not NOME.search((RADICE / p).read_text(encoding="utf-8")):
            errori.append(f"[1] nome assente in {p} (deve restare: art. 13 GDPR)")

    # 2. script e risorse esterne
    for p, e in analisi.items():
        if e.script:
            errori.append(f"[2] script diverso da /sito.js in {p}")
        for tag, k, v in e.link:
            u = urlparse(v)
            esterno = u.scheme in ("http", "https", "") and u.netloc not in ("", "nerina.eu", "www.nerina.eu")
            if tag == "a":
                continue   # i link testuali verso altri siti sono ammessi
            if esterno or u.scheme not in ("", "http", "https", "data"):
                errori.append(f"[2] risorsa esterna in {p}: <{tag} {k}={v}>")
            elif u.netloc in ("nerina.eu", "www.nerina.eu") and tag != "link":
                errori.append(f"[2] risorsa assoluta in {p}: {v}")
    js = (RADICE / "sito.js").read_text(encoding="utf-8")
    for vietato in ("fetch(", "XMLHttpRequest", "document.cookie", "sendBeacon", "WebSocket", "http://", "https://",
                    "import(", "eval(", "innerHTML"):
        if vietato in js:
            errori.append(f"[2] sito.js contiene {vietato}")
    for css in RADICE.rglob("*.css"):
        t = css.read_text(encoding="utf-8")
        for m in re.finditer(r"@import|url\(\s*['\"]?(https?:)?//", t):
            errori.append(f"[2] {css.relative_to(RADICE)}: {m.group(0)} esterno")

    for p, e in analisi.items():
        if p.startswith("en/") and any(v.endswith("-it.webp") for _, _, v in e.link + [("", "", x) for x in re.findall(r'src="([^"]+)"', (RADICE / p).read_text(encoding="utf-8"))]):
            errori.append(f"[2] {p}: schermata in italiano nella pagina inglese")

    # 3. link interni e ancore; ogni immagine o script locale esiste
    for p, e in analisi.items():
        for tag, k, v in e.link:
            if k == "src" and v.startswith("/") and not (RADICE / v.lstrip("/").split("?")[0]).exists():
                errori.append(f"[3] {p}: file mancante {v}")
            if k != "href":
                continue
            u = urlparse(v)
            if u.scheme in ("mailto", "tel"):
                continue
            if u.netloc and u.netloc not in ("nerina.eu", "www.nerina.eu"):
                continue
            if u.path:
                dest = file_di(u.path) if u.path.startswith("/") else file_di(str((pathlib.Path("/" + p).parent / u.path)))
            else:
                dest = RADICE / p
            if not dest.exists():
                errori.append(f"[3] {p}: link rotto {v}")
                continue
            if u.fragment and dest.suffix == ".html":
                ids = analisi.get(dest.relative_to(RADICE).as_posix()) or leggi(dest.read_text(encoding="utf-8"))
                if u.fragment not in ids.ids:
                    errori.append(f"[3] {p}: ancora mancante {v}")

    # 4. noindex
    for p in PAGINE_VECCHIE:
        prima = leggi(vecchio(p)).noindex
        if prima != analisi[p].noindex:
            errori.append(f"[4] {p}: noindex prima={prima} ora={analisi[p].noindex}")
    if not analisi["404.html"].noindex:
        errori.append("[4] 404.html senza noindex")

    # 5. testo visibile
    for p, riga in (("index.html", ED_IT), ("en/index.html", ED_EN)):
        if riga not in normalizza("".join(analisi[p].testo)):
            errori.append(f"[5] {p}: manca la riga «{riga[:40]}…»")
    for p in PAGINE_VECCHIE:
        if p in ("index.html", "en/index.html"):
            continue
        prima = normalizza("".join(leggi(vecchio(p)).testo))
        for a, b in ATTESI.get(p, []):
            if prima.count(a) != 1:
                errori.append(f"[5] {p}: frase attesa non trovata nel testo vecchio: {a[:60]}…")
            prima = prima.replace(a, b)
        ora = normalizza("".join(analisi[p].testo))
        if prima != ora:
            i = next((k for k in range(min(len(prima), len(ora))) if prima[k] != ora[k]), min(len(prima), len(ora)))
            errori.append(f"[5] {p}: testo diverso dal carattere {i}: prima «…{prima[max(0,i-40):i+60]}» "
                          f"ora «…{ora[max(0,i-40):i+60]}»")

    # 6. contrasto, su tutti i temi (strumenti/temi.py)
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    import temi
    righe_contrasto = []
    for nome, t in temi.TEMI.items():
        for modo in ("chiaro", "scuro"):
            tema = {k.replace("_", "-"): v for k, v in t[modo].items()}
            for fg, bg, uso in COPPIE:
                r = contrasto(tema[fg], tema[bg])
                righe_contrasto.append(f"{nome:8} {modo:6} {fg} su {bg} ({uso}): {r:.2f}")
                if r < 4.5:
                    errori.append(f"[6] {nome} {modo}: {fg} {tema[fg]} su {bg} {tema[bg]} = {r:.2f} < 4,5 ({uso})")
            r = contrasto(tema["ambra-testo"], tema["carta"])
            if r < 3:
                errori.append(f"[6] {nome} {modo}: anello di focus {r:.2f} < 3")

    print("Pagine controllate:", len(pagine))
    print("Contrasti:")
    for r in righe_contrasto:
        print("  ", r)
    if errori:
        print(f"\n{len(errori)} CONTROLLI FALLITI:")
        for e in errori:
            print(" -", e)
        return 1
    print("\nTutti i controlli 1-6 superati.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
