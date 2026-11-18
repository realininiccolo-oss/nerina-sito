"""Pagina iniziale di nerina.eu — v6 (18/11/2026): «il percorso che ti riconosce».

soglia (marchio) → luce (tema) → «Chi sei?» → «Che cosa cerchi?» → il ritratto (una frase, tre username, una riga)
→ il passero porta una foglia → privacy → le stanze → su invito.
Le due domande sono a scelta multipla (fino a tre, l'ordine dei tocchi decide il peso). I dati del percorso sono nel
blocco JSON «percorso-dati» (strumenti/percorso.py); sito.js costruisce le schede con createElement/textContent.
Senza JavaScript le domande restano nascoste e si vede il profilo predefinito (università + amici).
v6: tolti i luoghi (piazza, laboratorio, cortile, bottega) e «E tu, chi sei oggi?».
"""
import html

import grafica as g
import percorso as P
import scene
import temi
from casa_carte import carta
from funzioni import FUNZIONI

T = {
    "it": dict(
        h1="Il social network che unisce le persone.",
        entra="Entra",
        luce="Scegli la tua luce.",
        passero=("Il passero porta una foglia.", "L&#x27;attività in comune non basta: servono anche gli interessi."),
        nel_diario="Nel tuo Diario", perche="Perché",
        privacy_riga=("Costruita intorno alla cultura sociale europea: per proteggere la privacy e superare le "
                      "barriere sociali."),
        livelli=["Nessuno", "Passeri", "Interessati", "Connessioni", "Pubblica"],
        livelli_testi=["Solo tu.", "Solo i passeri, per trovarti proposte.", "Chi ha una foglia con te.",
                       "Le tue connessioni.", "Le persone verificate di Nerina. Mai il web."],
        cursore="Chi vede un tuo dato?",
        informativa=("/informativa/", "Informativa"),
        stanze="Le stanze per te.", tutte="Tutte le stanze",
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
        passero=("The sparrow brings a leaf.", "A shared activity is not enough: you need shared interests too."),
        nel_diario="In your Diary", perche="Why",
        privacy_riga="Built around European social culture: to protect privacy and break down social barriers.",
        livelli=["Nobody", "Sparrows", "Interested", "Connections", "Public"],
        livelli_testi=["Only you.", "Only the sparrows, to find proposals for you.", "People with a leaf with you.",
                       "Your connections.", "Verified people on Nerina. Never the web."],
        cursore="Who sees one of your details?",
        informativa=("/en/informativa/", "Privacy policy"),
        stanze="The rooms for you.", tutte="All rooms",
        invito=("By invitation.", "A few people, in the European Union. Free and without ads, during the pilot.",
                ("/en/contact/", "Write to us")),
        ricomincia="Start again",
        editore=("Nerina is published under the name <strong>Nerina Devs</strong>. The data controller is named in "
                 "the <a href=\"/en/informativa/#who-processes-the-data\">privacy policy</a>."),
    ),
}

FRECCIA_GIU = g.icona("freccia", "icona freccia-giu", 22)
e = html.escape


def _luce(t, lang):
    carte = "".join(
        f'<button type="button" class="finestra-tema" data-tema-scelta="{n}" data-vai="#chi" aria-pressed="false">'
        f'{scene.finestra_tema(n)}<span>{temi.TEMI[n]["nome"][lang]}</span></button>' for n in temi.TEMI)
    return (f'<section class="stanza stanza-luce" id="luce" aria-labelledby="luce-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="luce-t">{t["luce"]}</h2>'
            f'<div class="finestre anima" role="group" aria-labelledby="luce-t">{carte}</div></div>\n</section>')


def _domanda(nome, lang, passo, vai, dopo=None):
    d = P.DATI[lang]
    titolo = d[f"{nome}_t"]
    tessere = []
    for k, testo in d[nome]:
        regole = ""
        if nome == "cosa":
            if k in P.NASCONDI:
                regole += f' data-nascondi="{" ".join(P.NASCONDI[k])}"'
            if k in P.SOLO:
                regole += f' data-solo="{" ".join(P.SOLO[k])}"'
        tessere.append(
            f'<li><button type="button" class="tessera" data-domanda="{nome}" data-valore="{k}"{regole} '
            f'aria-pressed="false" aria-describedby="{nome}-fino">{P.icona(k)}<span class="tessera-testo">{e(testo)}</span>'
            f'<span class="tessera-ordine" aria-hidden="true"></span></button></li>')
    attesa = f' data-dopo="{dopo}"' if dopo else ""
    return (f'<section class="stanza stanza-domanda" id="{nome}" aria-labelledby="{nome}-t"{attesa}>\n'
            f'<div class="stanza-in domanda-in"><div class="domanda-figura-box anima">{scene.domanda(nome)}</div>'
            f'<div class="domanda-corpo"><h2 class="sussurro anima" id="{nome}-t">{titolo}</h2>'
            f'<ul class="tessere anima" role="group" aria-labelledby="{nome}-t">{"".join(tessere)}</ul>'
            f'<p class="fino" id="{nome}-fino">{d["fino"]}</p>'
            f'<p class="avanti-box"><button type="button" class="bottone avanti-bottone" data-avanti="{passo}" '
            f'data-vai="{vai}" hidden>{d["avanti"]}{g.icona("freccia", "icona", 20)}</button></p></div></div>\n</section>')


def _figura_scheda(s, uid):
    if s.get("icona"):
        return f'<span class="scheda-figura scheda-icona">{P.icona(s["icona"], 30, "icona")}</span>'
    return (f'<svg class="scheda-figura" viewBox="0 0 64 64" aria-hidden="true">'
            f'{g.omino(uid, s["colore"], testa=s.get("testa"))}</svg>')


def _scheda(s, n):
    mostra = f'<span class="scheda-mostra" data-p="mostra">{e(s["mostra"])}</span>' if s["mostra"] else ""
    return (f'<li class="scheda s{n}">{_figura_scheda(s, f"pred-{n}")}<span class="scheda-testi">'
            f'<span class="scheda-u">{e(s["u"])}</span><span class="scheda-ruolo">{e(s["ruolo"])}</span>{mostra}'
            f'</span></li>')


def _modelli():
    """Omini e icone che sito.js clona per le schede (fuori dalla vista, mai display:none per i clipPath)."""
    omini = [(c, None) for c in g.COLORI] + [("corallo", "visiera"), ("prugna", "basco")]
    parti = [f'<svg class="scheda-figura" viewBox="0 0 64 64" data-omino="{c}|{tt or ""}">'
             f'{g.omino(f"m-{c}-{tt or 0}", c, testa=tt)}</svg>' for c, tt in omini]
    parti += [f'<span class="scheda-figura scheda-icona" data-icona-scheda="{k}">{P.icona(k, 30, "icona")}</span>'
              for k in ("org", "invito", "evento", "assumere", "soci")]
    return f'<div class="modelli" aria-hidden="true">{"".join(parti)}</div>'


def _ritratto(r):
    schede = "".join(_scheda(s, n) for n, s in enumerate(r["schede"], 1))
    return (f'<section class="stanza stanza-ritratto" id="ritratto" aria-labelledby="ritratto-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="ritratto-t" data-p="frase">{e(r["frase"])}</h2>'
            f'<p class="sussurro-piccolo anima" data-p="riga">{e(r["riga"])}</p>'
            f'<ul class="schede anima" data-p="schede">{schede}</ul>'
            f'<p class="sotto-schede anima" data-p="sotto">{e(r["sotto"])}</p></div>\n</section>')


def _figura_foglia(nome, uid):
    if " " in nome:          # un evento o un'organizzazione: icona
        return f'<span class="scheda-figura scheda-icona">{P.icona("evento", 30, "icona")}</span>'
    return f'<svg class="scheda-figura" viewBox="0 0 64 64" aria-hidden="true">{g.omino(uid, "ginestra")}</svg>'


def _passero(t, r):
    richiesta, altro, tipo, motivo = r["foglia"]
    h2, riga = t["passero"]
    return (f'<section class="stanza" id="passero" aria-labelledby="passero-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="passero-t">{h2}</h2>'
            f'<div class="schema-incontro anima">'
            f'<p class="nuvola"><span class="nuvola-etichetta">{t["nel_diario"]}</span>'
            f'<span data-p="richiesta">{e(richiesta)}</span></p>'
            f'<span class="schema-passero">{g.logo_passero_solo()}</span>'
            f'<div class="foglia-carta"><span class="foglia-figura" data-p="foglia-figura">{_figura_foglia(altro, "fg-pred")}</span>'
            f'<span class="scheda-testi"><span class="scheda-u" data-p="foglia-u">{e(altro)}</span>'
            f'<span class="scheda-ruolo">{g.icona("foglia", "icona", 16)}<span data-p="foglia-tipo">{e(tipo)}</span></span></span>'
            f'<p class="motivo"><span class="motivo-etichetta">{t["perche"]}</span> <span data-p="motivo">{e(motivo)}</span></p>'
            f'</div></div>'
            f'<p class="sussurro-piccolo anima">{riga}</p></div>\n</section>')


def _privacy(t, lang, r):
    anelli = "".join(f'<circle class="anello a{n}" cx="100" cy="100" r="{18 + n * 16}"/>' for n in range(5, 0, -1))
    testi = "".join(f'<p class="livello-testo" data-testo-livello="{n}"{"" if n == 1 else " hidden"}>'
                    f'<strong>{nome}</strong> {d}</p>'
                    for n, (nome, d) in enumerate(zip(t["livelli"], t["livelli_testi"]), 1))
    tacche = "".join(f"<li>{x}</li>" for x in t["livelli"])
    return f"""<section class="stanza" id="privacy" aria-labelledby="privacy-t">
<div class="stanza-in">
<h2 class="sussurro sussurro-medio anima" id="privacy-t" data-p="privacy">{e(r["privacy"])}</h2>
<div class="schema-livelli anima" data-scatola-livelli data-livello="1">
<svg class="livelli-anelli" viewBox="0 0 200 200" aria-hidden="true">{anelli}<circle class="centro" cx="100" cy="100" r="14"/></svg>
<label class="cursore-etichetta" for="cursore-{lang}">{t["cursore"]}</label>
<input id="cursore-{lang}" class="cursore" type="range" min="1" max="5" step="1" value="1" data-livelli>
<ol class="tacche" aria-hidden="true">{tacche}</ol>
<div class="livelli-testi" aria-live="polite">{testi}</div>
</div>
<p class="sussurro-piccolo anima">{t["privacy_riga"]} <a href="{t["informativa"][0]}">{t["informativa"][1]}</a></p>
</div>
</section>"""


def _stanze(t, lang, r):
    carte = []
    for k in FUNZIONI:
        c = carta(k, lang).replace("<li>", f'<li data-porta="{k}"'
                                   + (f' style="order:{r["porte"].index(k)}"' if k in r["porte"] else " hidden") + ">", 1)
        carte.append(c)
    indice = "/funzioni/" if lang == "it" else "/en/features/"
    return (f'<section class="stanza" id="stanze" aria-labelledby="stanze-t">\n<div class="stanza-in">'
            f'<h2 class="sussurro anima" id="stanze-t">{t["stanze"]}</h2>'
            f'<ul class="porte-stanze anima" data-p="porte">{"".join(carte)}</ul>'
            f'<p class="anima"><a class="link-tutte" href="{indice}">{t["tutte"]}</a></p></div>\n</section>')


def casa(lang):
    t = T[lang]
    r = P.compone(lang, P.PRED["chi"], P.PRED["cosa"])
    h1_id = "che-cos-e-nerina" if lang == "it" else "what-is-nerina"
    h2, riga, (url, bott) = t["invito"]
    return f"""<section class="stanza soglia" id="soglia" aria-labelledby="{h1_id}">
<div class="stanza-in">
{g.logo("soglia", classe="logo logo-soglia", alt="Nerina")}
<h1 class="sussurro anima" id="{h1_id}">{t["h1"]}</h1>
<a class="entra anima" href="#luce">{t["entra"]}{FRECCIA_GIU}</a>
</div>
</section>
{_luce(t, lang)}
{_domanda("chi", lang, 1, "#cosa")}
{_domanda("cosa", lang, 2, "#ritratto", dopo="1")}
<div class="dopo-cosa" data-dopo="2">
{_ritratto(r)}
{_passero(t, r)}
{_privacy(t, lang, r)}
{_stanze(t, lang, r)}
<section class="stanza stanza-invito" id="invito" aria-labelledby="invito-t">
<div class="stanza-in">
<h2 class="sussurro anima" id="invito-t">{h2}</h2>
<p class="sussurro-piccolo anima">{riga}</p>
<p class="anima"><a class="bottone" href="{url}">{bott}</a></p>
<p class="ricomincia"><button type="button" class="link-bottone" data-ricomincia data-vai="#chi">{t["ricomincia"]}</button></p>
<p class="editore">{t["editore"]}</p>
</div>
</section>
</div>
{_modelli()}
<script type="application/json" id="percorso-dati">{P.json_lingua(lang)}</script>"""
