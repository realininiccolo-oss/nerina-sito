"""Illustrazioni del percorso (18/11/2026): tutte dentro una finestra ad arco, come quella di Recanati.

- finestra_tema(nome): Recanati (colline e torre al tramonto), Infinito (la siepe e l'orizzonte di notte),
  Ginestra (il vulcano e la ginestra), con i colori fissi di ogni tema;
- domanda(nome): l'illustrazione delle due domande del percorso («chi», «cosa»), nei colori del tema scelto.
v6 (18/11): tolti i quattro luoghi (piazza, laboratorio, cortile, bottega) e le vignette delle risposte.
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


def domanda(nome):
    """Finestra ad arco grande (viewBox 0 0 120 160) per le due domande, con i colori del tema (classi d-*)."""
    gid = f"dm-{nome}"
    stelle = "".join(f'<circle class="d-stella luce" cx="{x}" cy="{y}" r="{r}"/>'
                     for x, y, r in ((22, 58, .9), (96, 50, .8), (70, 30, .6), (40, 34, .7), (104, 84, .6), (14, 90, .7)))
    if nome == "chi":
        # una persona, e dietro tre ombre di colori diversi: i suoi ruoli
        ombre = "".join(f'<g class="d-ombra o{n}" transform="translate({dx} {dy})"><circle cx="60" cy="92" r="11"/>'
                        f'<path d="M40 160 C40 128 48 110 60 110 C72 110 80 128 80 160Z"/></g>'
                        for n, (dx, dy) in enumerate(((-26, 8), (0, -6), (26, 8)), 1))
        corpo = (f'{stelle}<circle class="d-luna" cx="60" cy="48" r="13"/>{ombre}'
                 '<g class="d-persona"><circle cx="60" cy="100" r="11"/>'
                 '<path d="M40 160 C40 132 48 118 60 118 C72 118 80 132 80 160Z"/></g>')
    else:
        # un sentiero verso l'orizzonte, luci lontane e una foglia in volo
        luci = "".join(f'<circle class="d-luce luce" cx="{x}" cy="{y}" r="{r}"/>'
                       for x, y, r in ((30, 104, 1.6), (44, 101, 1.2), (78, 102, 1.4), (92, 105, 1.8), (60, 99, 1.1)))
        corpo = (f'{stelle}<path class="d-colle" d="M0 108 C24 98 46 100 62 104 C82 109 100 98 120 100 V160 H0Z"/>'
                 f'{luci}<path class="d-sentiero" d="M52 160 C56 140 60 124 61 106 C62 124 68 140 76 160Z"/>'
                 f'<path class="d-foglia foglia-vola" transform="translate(70 70) rotate(-24) scale(1.3)" d="{FOGLIA}"/>')
    return (f'<svg class="domanda-figura" viewBox="0 0 120 160" aria-hidden="true" focusable="false">'
            f'<defs><clipPath id="{gid}-c"><path d="{ARCO}"/></clipPath>'
            f'<linearGradient id="{gid}-g" x1="0" y1="0" x2="0" y2="1"><stop class="d-s1" offset="0"/>'
            f'<stop class="d-s2" offset="1"/></linearGradient></defs>'
            f'<g clip-path="url(#{gid}-c)"><rect width="120" height="160" fill="url(#{gid}-g)"/>{corpo}</g>'
            f'<path d="{ARCO}" fill="none" stroke="currentColor" stroke-opacity=".18"/></svg>')
