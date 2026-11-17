"""Pezzi grafici del sito nerina.eu (grafica v1, 18/11/2026).

Fonti, tutte nel progetto Nerina e copiate qui a mano:
- passero dell'intestazione: design/prototipo-v12/riferimento/icona-invia-passero.svg (Claude Design, v12);
- scritta «nerina» con la foglia: design/prototipo-v12/riferimento/logo-nerina.svg (v12);
- icone dei blocchi: design/icone-profilo/icone-profilo.svg (codice-invito, identita, luoghi-frequentati, consensi);
- omino: claude/grafica/omino-schede-v1.md §2.6 (stile A, approvato il 17/11).
Tutto è SVG in linea: nessuna richiesta fuori da nerina.eu.
"""

CREMA = "#FFFDF7"

# Passero in volo (icona del pulsante «invia al passero» della v12), viewBox 0 0 24 24, solo tratto.
PASSERO_D = (
    "M21.71 10.43L19.68 9.87A2.6 2.6 0 0 0 15.01 11.61C14.47 12.01 13.93 12.41 13.4 12.81"
    "C12.32 9.04 8.39 6.28 2.59 5.67C3.54 8.76 5.91 11.79 9.42 14.42C8.7 14.95 8.08 15.47 7.54 15.87"
    "L2.3 16.08L3.62 19L8.08 17.2C10.11 18.36 12.97 18.47 15.41 17.33C17.65 16.22 19.26 14.41 19.66 12.62"
    "A2.6 2.6 0 0 0 20.35 11.38ZM14.68 12.02C14.79 9.21 13.52 6.59 11 5C10.92 6.24 10.77 7.69 10.8 8.84"
    "M18.41 10.7L18.42 10.7"
)

# Scritta «nerina» (lettere) e foglia sulla i, dal logo della v12.
SCRITTA_D = open(__file__.replace("grafica.py", "scritta.txt"), encoding="utf-8").read().strip()
FOGLIA_D = "M0 0C-6 -6.5 -2.5 -17.5 14 -20.5C15.5 -8.5 9 -1 0 0Z"


def passero(classe="passero", px=24):
    return (
        f'<svg class="{classe}" width="{px}" height="{px}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true" focusable="false"><path d="{PASSERO_D}"/></svg>'
    )


def scritta(classe="scritta"):
    return (
        f'<svg class="{classe}" viewBox="6 -86 288.1 89" aria-hidden="true" focusable="false">'
        f'<path class="scritta-lettere" d="{SCRITTA_D}"/>'
        f'<path class="scritta-foglia" transform="translate(165.00 -59.79) rotate(-5) scale(0.98)" d="{FOGLIA_D}"/>'
        f"</svg>"
    )


def marchio(href, etichetta):
    return (
        f'<a class="marchio" href="{href}" aria-label="{etichetta}">'
        f'<span class="marchio-passero">{passero(px=24)}</span>{scritta()}</a>'
    )


_ICONE = {
    "invito": '<path d="M18.5 5.5 5 12l13.5 6.5"/><path d="M18.5 5.5Q21.5 12 18.5 18.5"/>'
              '<circle class="accento-pieno" cx="5" cy="12" r="2"/>',
    "identita": '<circle cx="12" cy="12" r="9"/><circle class="accento" cx="12" cy="12" r="4.5"/>'
                '<circle class="pieno" cx="12" cy="12" r="1.25"/>',
    "luogo": '<path d="M12 18.5c-3-3-6.5-6-6.5-9.5a6.5 6.5 0 0 1 13 0c0 3.5-3.5 6.5-6.5 9.5z"/>'
             '<circle class="accento" cx="12" cy="9" r="2.5"/><path d="M6.5 18.5c0 1.5 2.5 3 5.5 3s5.5-1.5 5.5-3"/>',
    "consensi": '<rect x="3.5" y="3.5" width="17" height="17" rx="5.5"/>'
                '<path class="accento" d="M8 12.5l2.5 2.5L16 9"/>',
    # Dodici punti in cerchio: l'Unione europea, disegnata come le altre icone (tratto 1,75).
    "europa": "".join(
        f'<circle class="accento-pieno" cx="{12 + 8 * __import__("math").sin(i * 0.5236):.2f}" '
        f'cy="{12 - 8 * __import__("math").cos(i * 0.5236):.2f}" r="1.4"/>'
        for i in range(12)
    ),
    "busta": '<rect x="3" y="5.5" width="18" height="13" rx="3"/><path class="accento" d="M4 7.5l8 6 8-6"/>',
    "scudo": '<path d="M12 3l7 2.8v5.7c0 4.3-3 7.9-7 9.5-4-1.6-7-5.2-7-9.5V5.8z"/>'
             '<path class="accento" d="M8.8 12.2l2.2 2.2 4.2-4.4"/>',
    "pagina": '<path d="M7 3.5h7l4 4V19a1.5 1.5 0 0 1-1.5 1.5h-9.5A1.5 1.5 0 0 1 5.5 19V5A1.5 1.5 0 0 1 7 3.5z"/>'
              '<path d="M14 3.5V7.5h4"/><path class="accento" d="M8.5 12h7M8.5 15.5h5"/>',
    "cestino": '<path d="M4.5 7h15"/><path d="M9.5 7V5h5v2"/><path d="M6.5 7l1 12.5h9l1-12.5"/>'
               '<path class="accento" d="M10.5 10.5v6M13.5 10.5v6"/>',
    "freccia": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
    "bozza": '<path d="M4 20l4.5-1 10-10a2.1 2.1 0 0 0-3-3l-10 10z"/><path class="accento" d="M14 7.5l3 3"/>',
}


def icona(nome, classe="icona", px=24):
    return (
        f'<svg class="{classe}" width="{px}" height="{px}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        f"{_ICONE[nome]}</svg>"
    )


# ---------------------------------------------------------------- omino (omino-schede-v1 §2.6)

COLORI = {
    "foglia": ("#3C7A4A", "#214328"), "ginestra": ("#8A6A00", "#4B3A00"), "infinito": ("#2F5D9E", "#193356"),
    "corallo": ("#B2473E", "#612722"), "prugna": ("#7A4A8C", "#43284D"), "petrolio": ("#1F7173", "#113E3F"),
    "terra": ("#9C5A2E", "#553119"), "oliva": ("#5E7024", "#333D13"), "lampone": ("#A63D6B", "#5B213A"),
    "ardesia": ("#4A5A78", "#283142"),
}

_VESTITI = {
    "felpa": '<path d="M23 41 C23 50 41 50 41 41" fill="none" stroke="#FFFDF7" stroke-width="1.6"/>'
             '<path d="M29 48 V54 M35 48 V54" stroke="#FFFDF7" stroke-width="1.4" stroke-linecap="round"/>',
    "scollo": '<path d="M26 40 L32 50 L38 40 Z" fill="#FFFDF7"/>'
              '<path d="M27.5 41 Q32 49 36.5 41" fill="none" stroke="C" stroke-width="1.3"/>'
              '<circle cx="32" cy="46.8" r="1.6" fill="C"/>',
    "colletto": '<path d="M32 41 C26 40 23 45 27 47.5 C29.5 48.5 32 45 32 41 Z M32 41 C38 40 41 45 37 47.5 '
                'C34.5 48.5 32 45 32 41 Z" fill="#FFFDF7"/><circle cx="32" cy="51" r="1.2" fill="#FFFDF7"/>'
                '<circle cx="32" cy="55" r="1.2" fill="#FFFDF7"/>',
}

_VISO = {
    "guance": '<ellipse cx="25" cy="29.5" rx="2.8" ry="1.9" fill="#E8828C"/>'
              '<ellipse cx="39" cy="29.5" rx="2.8" ry="1.9" fill="#E8828C"/>',
    "occhiali_tondi": '<circle cx="27.3" cy="24.5" r="3.6" fill="none" stroke="#24262A" stroke-width="1.4"/>'
                      '<circle cx="36.7" cy="24.5" r="3.6" fill="none" stroke="#24262A" stroke-width="1.4"/>'
                      '<path d="M30.9 24 H33.1" stroke="#24262A" stroke-width="1.4"/>',
    "barba": '<path d="M21.3 26 C21.5 35 26.5 38.5 32 38.5 C37.5 38.5 42.5 35 42.7 26 C40.5 31.5 36.5 33 32 33 '
             'C27.5 33 23.5 31.5 21.3 26 Z" fill="S"/>',
}

_TESTA = {
    "visiera": '<path d="M20.5 23 C20.5 11.5 43.5 11.5 43.5 23 Z" fill="S"/>'
               '<path d="M32 13 V22.5" stroke="#FFFDF7" stroke-width=".9" opacity=".45"/>'
               '<circle cx="32" cy="12.6" r="1.4" fill="S"/>'
               '<path d="M40.5 21.2 C46 20.2 51 21 52.5 23.6 C48 25 42.5 24.8 40.5 24 Z" fill="S"/>'
               '<rect x="20.5" y="21.3" width="23" height="2" fill="#FFFDF7" opacity=".3"/>',
    "chioma": '<path d="M19.5 27 C18 11 46 11 44.5 27 L45.5 46 C43 47.5 40.5 46.5 40 44 L40.5 24 C37 19.5 27 19.5 '
              '23.5 24 L24 44 C23.5 46.5 21 47.5 18.5 46 Z" fill="S"/>',
    "basco": '<ellipse cx="30" cy="16" rx="13" ry="5" transform="rotate(-12 30 16)" fill="S"/>'
             '<rect x="30" y="8" width="2.5" height="4" rx="1" fill="S"/>',
}

_CIAO = (
    '<rect x="7.2" y="11" width="3.6" height="10" rx="1.8" transform="rotate(-16 9 20)"/>'
    '<rect x="10.6" y="9.5" width="3.6" height="11" rx="1.8" transform="rotate(-5 12.4 20)"/>'
    '<rect x="14" y="10" width="3.6" height="10.5" rx="1.8" transform="rotate(6 15.8 20)"/>'
    '<rect x="17.2" y="12.5" width="3.4" height="8.5" rx="1.7" transform="rotate(18 19 20)"/>'
    '<path d="M8.5 26 C5.5 25 3 22 3.5 19.8 C4 18.2 6 18.4 7.6 20.2 L10 23 Z"/>'
    '<path d="M7 22 C6.5 18.5 9 17 13.5 17 C18 17 20.5 18.5 20.3 22.5 C20 28 18.5 33 13.5 33 C8.5 33 7.5 28 7 22 Z"/>'
    '<path d="M24 11.5 Q26.5 16.5 24.5 21.5" fill="none" stroke="#FFFDF7" stroke-width="2.4" stroke-linecap="round"/>'
)
_CUORE = (
    '<g transform="translate(11.2 18.4) scale(.65)"><path d="M32 59 C22 52.5 20 46 23.8 42 C27 38.8 31 40.3 32 43.6 '
    'C33 40.3 37 38.8 40.2 42 C44 46 42 52.5 32 59 Z" fill="#E35D6A" stroke="#FFFDF7" stroke-width="3" '
    'stroke-linejoin="round"/></g>'
)


def omino(uid, colore, testa=None, vestito=None, viso=(), gesto=None):
    """Omino in viewBox 0 0 64 64, da mettere dentro un altro SVG con <g transform>."""
    c, s = COLORI[colore]
    clip = f"om-{uid}"
    corpo = (f'<g clip-path="url(#{clip})"><circle cx="32" cy="25" r="11" fill="{CREMA}"/>'
             f'<path d="M12 64 C12 47 21 40 32 40 C43 40 52 47 52 64 Z" fill="{CREMA}"/></g>')
    parti = [f'<clipPath id="{clip}"><circle cx="32" cy="32" r="32"/></clipPath>',
             f'<circle cx="32" cy="32" r="32" fill="{c}"/>', corpo]
    if vestito:
        parti.append(f'<g clip-path="url(#{clip})"><path d="M12 64 C12 47 21 40 32 40 C43 40 52 47 52 64 Z" fill="S"/></g>')
        parti.append(_VESTITI[vestito])
    for v in ("guance", "barba", "occhiali_tondi"):
        if v in viso:
            parti.append(_VISO[v])
    if testa:
        parti.append(_TESTA[testa])
    if gesto == "ciao":
        b = "S" if vestito else CREMA
        parti.append(f'<g clip-path="url(#{clip})"><path d="M19.5 61 C17.5 55 15.5 50.5 14.8 46" fill="none" '
                     f'stroke="{b}" stroke-width="5.5" stroke-linecap="round"/></g>')
        parti.append(f'<g transform="translate(4.5 25) scale(.62) rotate(-10 14 24)" fill="{CREMA}" stroke="S" '
                     f'stroke-width="2" stroke-linejoin="round">{_CIAO}</g>')
    elif gesto == "cuore":
        parti.append(_CUORE)
    parti.append('<circle class="omino-anello" cx="32" cy="32" r="31.5" fill="none" stroke-width="1"/>')
    svg = "".join(parti)
    return svg.replace('"S"', f'"{s}"').replace('"C"', f'"{c}"')


def illustrazione_casa():
    """Colline all'alba (o di notte, nel tema scuro), due omini e il passero che li unisce. Decorativa."""
    foglia = lambda x, y, r, cl: (f'<path class="{cl}" transform="translate({x} {y}) rotate({r}) scale(1.1)" '
                                   f'd="{FOGLIA_D}"/>')
    om1 = omino("casa-1", "infinito", testa="visiera", vestito="felpa", gesto="ciao")
    om2 = omino("casa-2", "petrolio", testa="chioma", vestito="scollo", viso=("guance",), gesto="cuore")
    return f"""<svg class="illustrazione" viewBox="0 0 480 380" aria-hidden="true" focusable="false">
<defs>
<linearGradient id="ill-cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="ill-cielo-1"/><stop offset="1" class="ill-cielo-2"/></linearGradient>
<radialGradient id="ill-alone" cx=".5" cy=".5" r=".5"><stop offset="0" class="ill-alone-1"/><stop offset="1" class="ill-alone-2"/></radialGradient>
<clipPath id="ill-cornice"><rect width="480" height="380" rx="32"/></clipPath>
</defs>
<g clip-path="url(#ill-cornice)">
<rect width="480" height="380" fill="url(#ill-cielo)"/>
<circle cx="350" cy="150" r="120" fill="url(#ill-alone)"/>
<circle class="ill-sole" cx="350" cy="150" r="34"/>
<g class="ill-stelle"><circle cx="70" cy="60" r="1.6"/><circle cx="130" cy="34" r="1.2"/><circle cx="220" cy="70" r="1.4"/><circle cx="420" cy="48" r="1.2"/><circle cx="455" cy="96" r="1.5"/><circle cx="36" cy="128" r="1.1"/></g>
<path class="ill-colle-3" d="M0 214 C60 188 120 182 190 196 C260 210 320 176 390 170 C430 166 460 176 480 184 V380 H0 Z"/>
<path class="ill-torre" d="M140 192 v-34 h4 v-7 h10 v7 h4 v34 z M168 194 h24 v-15 l-12 -9 l-12 9 z"/>
<path class="ill-colle-2" d="M0 250 C70 222 140 226 210 240 C290 256 360 222 480 230 V380 H0 Z"/>
<path class="ill-colle-1" d="M0 300 C90 276 170 286 240 296 C330 309 400 284 480 290 V380 H0 Z"/>
<path class="ill-filari" d="M30 336 C120 318 200 326 260 334 M60 356 C150 340 240 346 330 356 M250 322 C330 308 400 306 470 312" fill="none" stroke-width="2" stroke-linecap="round" stroke-dasharray="2 9"/>
{foglia(52, 312, -20, "ill-foglia-1")}{foglia(430, 330, 15, "ill-foglia-2")}{foglia(392, 258, -60, "ill-foglia-1")}
</g>
<path class="ill-rotta" d="M112 250 C130 150 190 112 232 108 M268 112 C310 118 356 160 370 250" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="1 9"/>
<g transform="translate(212 64)"><rect class="ill-bollo" width="76" height="76" rx="22"/>
<g transform="translate(13 13) scale(2.08)" class="ill-passero" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="{PASSERO_D}"/></g></g>
<g transform="translate(52 236) scale(1.6)">{om1}</g>
<g transform="translate(428 236) scale(-1.6 1.6)">{om2}</g>
</svg>"""


def illustrazione_404():
    return f"""<svg class="illustrazione illustrazione-piccola" viewBox="0 0 240 160" aria-hidden="true" focusable="false">
<defs><linearGradient id="ill4-cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="ill-cielo-1"/><stop offset="1" class="ill-cielo-2"/></linearGradient>
<clipPath id="ill4-cornice"><rect width="240" height="160" rx="24"/></clipPath></defs>
<g clip-path="url(#ill4-cornice)"><rect width="240" height="160" fill="url(#ill4-cielo)"/>
<circle class="ill-sole" cx="180" cy="62" r="18"/>
<path class="ill-colle-2" d="M0 118 C50 100 110 104 150 112 C190 120 215 106 240 108 V160 H0 Z"/>
<path class="ill-colle-1" d="M0 138 C60 126 120 132 170 138 C200 142 222 134 240 136 V160 H0 Z"/>
<path class="ill-rotta" d="M30 104 C50 60 80 44 104 52" fill="none" stroke-width="2" stroke-linecap="round" stroke-dasharray="1 7"/>
<g transform="translate(96 26)"><rect class="ill-bollo" width="48" height="48" rx="14"/>
<g transform="translate(8 8) scale(1.33)" class="ill-passero" fill="none" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="{PASSERO_D}"/></g></g>
</g></svg>"""
