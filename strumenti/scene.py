"""Illustrazioni del percorso (18/11/2026): tutte dentro una finestra ad arco, come quella di Recanati.

- finestra_tema(nome): Recanati (colline e torre al tramonto), Infinito (la siepe e l'orizzonte di notte),
  Ginestra (il vulcano e la ginestra), con i colori fissi di ogni tema;
- vignetta(nome): le risposte alle due domande, nei colori del tema scelto (classi v-*);
- luogo(nome): i quattro posti in cui porta la prima risposta (piazza, laboratorio, cortile, bottega).
Disegni geometrici, senza testo. Le versioni definitive possono arrivare da Claude Design
(claude/prompt-design-illustrazioni-sito-2026-11-18.md).
"""
import temi

ARCO = "M0 160 V60 A60 60 0 0 1 120 60 V160 Z"          # viewBox 0 0 120 160
ARCO_Q = "M0 100 V50 A50 50 0 0 1 100 50 V100 Z"         # viewBox 0 0 100 100
FOGLIA = "M0 0C-6 -6.5 -2.5 -17.5 14 -20.5C15.5 -8.5 9 -1 0 0Z"


def finestra_tema(nome):
    t, s = temi.TEMI[nome]["chiaro"], temi.TEMI[nome]["scuro"]
    gid = f"ft-{nome}"
    if nome == "recanati":
        cielo = (t["ambra_tenue"], t["carta_alta"])
        corpo = (f'<circle cx="82" cy="74" r="11" fill="{t["ambra"]}" opacity=".9"/>'
                 f'<path d="M0 104 C22 94 40 92 62 98 C84 104 100 94 120 92 V160 H0Z" fill="{t["primario_tenue"]}"/>'
                 f'<path d="M30 100 v-16 h3 v-4 h5 v4 h3 v16z" fill="{t["primario"]}" opacity=".55"/>'
                 f'<path d="M0 118 C30 108 58 112 80 118 C98 123 110 116 120 114 V160 H0Z" fill="{t["primario"]}" opacity=".65"/>'
                 f'<path d="M0 134 C36 126 72 132 120 128 V160 H0Z" fill="{t["primario_forte"]}"/>')
    elif nome == "infinito":
        cielo = (s["carta_bassa"], s["primario_tenue"])
        stelle = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{s["inchiostro"]}" opacity=".7"/>'
                         for x, y, r in ((18, 70, .8), (40, 46, .6), (100, 64, .7), (66, 34, .5), (88, 96, .5), (26, 98, .6)))
        corpo = (f'{stelle}<circle cx="78" cy="58" r="9" fill="{s["ambra"]}"/>'
                 f'<path d="M0 122 H120" stroke="{s["primario"]}" stroke-width=".6" opacity=".6"/>'
                 f'<path d="M0 132 C6 124 12 126 16 130 C20 122 28 122 32 129 C36 121 46 121 50 128 C55 120 64 122 68 128 '
                 f'C72 121 82 121 86 128 C91 121 100 122 104 129 C108 123 116 124 120 128 V160 H0Z" fill="{s["carta_bassa"]}"/>')
    else:  # ginestra
        cielo = (t["primario"], t["primario_tenue"])
        fiori = "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#e9c24a"/>'
                        for x, y in ((24, 118), (30, 112), (36, 120), (90, 114), (96, 108), (100, 118), (62, 124)))
        corpo = (f'<circle cx="36" cy="72" r="8" fill="{t["carta_alta"]}" opacity=".85"/>'
                 f'<path d="M14 132 L52 92 H70 L108 132Z" fill="{s["carta_alta"]}" opacity=".9"/>'
                 f'<path d="M52 92 Q61 86 70 92" fill="none" stroke="{t["primario_tenue"]}" stroke-width="1.5" opacity=".6"/>'
                 f'<path d="M0 136 C30 128 80 132 120 130 V160 H0Z" fill="{s["carta"]}"/>'
                 f'<path d="M30 140 C28 126 26 118 24 112 M30 140 C32 128 36 122 36 116 M96 140 C94 126 96 116 96 106 '
                 f'M96 140 C98 130 100 124 100 116" stroke="#6f8f4a" stroke-width="1.4" fill="none"/>{fiori}')
    return (f'<svg class="finestra" viewBox="0 0 120 160" aria-hidden="true" focusable="false">'
            f'<defs><clipPath id="{gid}-c"><path d="{ARCO}"/></clipPath>'
            f'<linearGradient id="{gid}-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{cielo[0]}"/>'
            f'<stop offset="1" stop-color="{cielo[1]}"/></linearGradient></defs>'
            f'<g clip-path="url(#{gid}-c)"><rect width="120" height="160" fill="url(#{gid}-g)"/>{corpo}</g>'
            f'<path d="{ARCO}" fill="none" stroke="currentColor" stroke-opacity=".18"/></svg>')


_VIGNETTE = {
    # che cosa cerchi
    "persone": ('<circle class="v-pieno" cx="36" cy="60" r="8"/><path class="v-pieno" d="M22 100 C22 82 29 74 36 74 C43 74 50 82 50 100Z"/>'
                '<circle class="v-medio" cx="64" cy="60" r="8"/><path class="v-medio" d="M50 100 C50 82 57 74 64 74 C71 74 78 82 78 100Z"/>'
                f'<path class="v-acc" transform="translate(45 42) rotate(-20) scale(.7)" d="{FOGLIA}"/>'),
    "lavoro": ('<rect class="v-chiaro" x="24" y="34" width="52" height="40" rx="2"/><path class="v-linea" d="M50 34 V74 M24 54 H76"/>'
               '<path class="v-pieno" d="M14 82 H86 V86 H14Z"/><path class="v-pieno" d="M66 82 V70 L60 64"/>'
               '<path class="v-acc" d="M56 64 H66 L62 58 H58Z"/>'),
    "eventi": ('<path class="v-linea" d="M4 34 Q50 58 96 34"/>'
               + "".join(f'<circle class="v-amb luce" cx="{x}" cy="{y}" r="2.6"/>' for x, y in ((16, 40), (32, 46), (50, 47), (68, 46), (84, 40)))
               + '<path class="v-pieno" d="M18 84 H44 M31 84 V98 M56 84 H82 M69 84 V98" stroke-width="3"/>'
               '<circle class="v-medio" cx="24" cy="74" r="5"/><circle class="v-medio" cx="76" cy="74" r="5"/>'),
    "azienda": ('<path class="v-acc" d="M18 44 H82 L86 56 H14Z"/>'
                + "".join(f'<path class="v-chiaro" d="M{18 + i * 16} 44 H{26 + i * 16} L{27 + i * 16} 56 H{19 + i * 16}Z"/>' for i in range(4))
                + '<rect class="v-medio" x="20" y="56" width="60" height="42"/><rect class="v-chiaro" x="26" y="62" width="22" height="18"/>'
                '<rect class="v-pieno" x="56" y="66" width="18" height="32"/>'),
    # chi sei oggi
    "studio": ('<rect class="v-acc" x="26" y="82" width="48" height="8" rx="1"/><rect class="v-pieno" x="30" y="74" width="40" height="8" rx="1"/>'
               '<rect class="v-medio" x="24" y="66" width="44" height="8" rx="1"/><path class="v-linea" d="M74 66 V44 Q74 38 66 38"/>'
               '<path class="v-amb" d="M58 34 H70 L66 42 H62Z"/>'),
    "lavoro-fase": ('<rect class="v-pieno" x="14" y="58" width="18" height="42"/><rect class="v-medio" x="34" y="44" width="22" height="56"/>'
                    '<rect class="v-pieno" x="58" y="64" width="14" height="36"/><rect class="v-medio" x="74" y="52" width="14" height="48"/>'
                    + "".join(f'<rect class="v-amb luce" x="{x}" y="{y}" width="3" height="3"/>' for x, y in ((39, 52), (47, 52), (39, 62), (47, 72), (78, 60), (78, 70), (19, 66))) ),
    "citta": ('<path class="v-medio" d="M40 100 L48 52 H52 L60 100Z"/><path class="v-linea" d="M50 98 V88 M50 82 V74 M50 68 V60"/>'
              '<path class="v-pieno" d="M74 100 V46"/><path class="v-acc" d="M74 48 H90 L94 53 L90 58 H74Z"/>'
              '<circle class="v-amb" cx="28" cy="40" r="6"/>'),
    "tempo": ('<circle class="v-amb" cx="68" cy="40" r="10"/><circle class="v-medio" cx="30" cy="58" r="14"/><path class="v-pieno" d="M30 70 V96"/>'
              '<path class="v-pieno" d="M46 84 H84 M50 84 V96 M80 84 V96 M46 78 H84" stroke-width="3"/>'),
}


def vignetta(nome):
    gid = f"vg-{nome}"
    return (f'<svg class="vignetta" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
            f'<defs><clipPath id="{gid}"><path d="{ARCO_Q}"/></clipPath></defs>'
            f'<g clip-path="url(#{gid})"><rect class="v-fondo" width="100" height="100"/>{_VIGNETTE[nome]}</g></svg>')


def luogo(nome):
    """Scena larga in fondo alla stanza del luogo (viewBox 0 0 1440 480)."""
    if nome == "persone":      # la piazza al tramonto
        portici = "".join(f'<path d="M{x} 480 V330 A40 40 0 0 1 {x + 80} 330 V480Z" class="l-vuoto"/>' for x in range(40, 1440, 120))
        lampioni = "".join(f'<path class="l-pieno" d="M{x} 480 V300" stroke-width="4"/><circle class="l-luce luce" cx="{x}" cy="294" r="9"/>'
                           f'<circle class="l-alone" cx="{x}" cy="294" r="34"/>' for x in (230, 720, 1210))
        corpo = (f'<rect class="l-pieno" x="0" y="250" width="1440" height="230"/>{portici}{lampioni}'
                 '<circle class="l-figura" cx="680" cy="402" r="14"/><path class="l-figura" d="M660 480 C660 446 668 424 680 424 C692 424 700 446 700 480Z"/>'
                 '<circle class="l-figura" cx="760" cy="402" r="14"/><path class="l-figura" d="M740 480 C740 446 748 424 760 424 C772 424 780 446 780 480Z"/>'
                 f'<path class="l-foglia foglia-vola" transform="translate(712 360) rotate(-18) scale(1.6)" d="{FOGLIA}"/>')
    elif nome == "lavoro":     # il laboratorio di mattina
        vetri = "".join(f'<rect class="l-vetro" x="{x}" y="{y}" width="150" height="120" rx="4"/>'
                        for x in (440, 600, 760) for y in (90, 220))
        corpo = (f'<rect class="l-cornice" x="428" y="78" width="494" height="276" rx="8"/>{vetri}'
                 '<path class="l-luce-fascio" d="M440 354 L300 480 H1100 L922 354Z"/>'
                 '<rect class="l-pieno" x="180" y="400" width="1080" height="14" rx="4"/><path class="l-pieno" d="M240 414 V480 M1200 414 V480" stroke-width="10"/>'
                 '<path class="l-pieno" d="M1020 400 V330 L980 300" stroke-width="6" fill="none"/><path class="l-acc" d="M950 296 H1000 L986 270 H964Z"/>'
                 '<path class="l-pianta" d="M300 400 C296 360 280 336 262 324 M300 400 C304 356 322 332 344 322 M300 400 V344"/>')
    elif nome == "eventi":     # il cortile di sera
        fili = ""
        for k, (y, s) in enumerate(((60, 70), (110, 90), (160, 60))):
            fili += f'<path class="l-filo" d="M0 {y} Q720 {y + s * 2} 1440 {y}"/>'
            for i in range(1, 18):
                x = i * 80
                t = x / 1440
                yy = (1 - t) ** 2 * y + 2 * (1 - t) * t * (y + s * 2) + t ** 2 * y
                fili += f'<circle class="l-luce luce l{(i + k) % 3}" cx="{x}" cy="{yy:.0f}" r="5"/>'
        tavoli = "".join(f'<path class="l-pieno" d="M{x - 70} 420 H{x + 70} M{x - 50} 420 V480 M{x + 50} 420 V480" stroke-width="8"/>'
                         f'<circle class="l-figura" cx="{x - 40}" cy="388" r="13"/><circle class="l-figura" cx="{x + 40}" cy="388" r="13"/>'
                         for x in (300, 720, 1140))
        corpo = f'{fili}{tavoli}'
    else:                      # la bottega
        strisce = "".join(f'<path class="{"l-acc" if i % 2 else "l-chiaro"}" d="M{300 + i * 70} 150 H{370 + i * 70} L{376 + i * 70} 210 H{294 + i * 70}Z"/>' for i in range(12))
        barattoli = "".join(f'<rect class="l-vetro" x="{x}" y="{y}" width="34" height="44" rx="6"/>' for x in range(380, 1080, 70) for y in (250,))
        corpo = (f'<rect class="l-pieno" x="290" y="140" width="860" height="12"/>{strisce}'
                 f'<rect class="l-muro" x="300" y="210" width="840" height="270"/>'
                 f'<path class="l-pieno" d="M360 300 H1080" stroke-width="6"/>{barattoli}'
                 '<rect class="l-pieno" x="600" y="330" width="240" height="150"/><rect class="l-luce-fascio" x="620" y="350" width="200" height="130"/>'
                 '<circle class="l-figura" cx="720" cy="300" r="0"/>')
    return (f'<svg class="luogo-scena scena-{nome}" viewBox="0 0 1440 480" preserveAspectRatio="xMidYMax slice" '
            f'aria-hidden="true" focusable="false">{corpo}</svg>')
