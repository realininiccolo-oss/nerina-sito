"""Pagina iniziale di nerina.eu — v3 (18/11/2026 mattina).

Un'idea sola: il passero ti porta una foglia. Apertura col passero del marchio; sotto, un filo verticale con
sei tappe che si legge dall'alto in basso, con una foglia che scende insieme a chi legge.
Ogni affermazione sul prodotto viene da un testo già pubblicato (fonti in claude/sito-grafica-v3-esito-2026-11-18.md).
Niente promesse nuove, niente «Scarica».
"""
import grafica as g

T = {
    "it": {
        "h1": "Trova chi parla la tua lingua.",
        "attacco": ("Nerina è un social senza feed e senza post. Racconti in privato al passero che cosa cerchi, "
                    "e lui ti porta solo proposte pensate per te."),
        "bottone": "Scopri come funziona",
        "nota": "Pilota su invito · dai 16 anni, con documento verificato · Unione europea",
        "tappe": [
            dict(id="perche", n="Perché Nerina", h2="I social sono diventati media.",
                 p=["Un flusso infinito da guardare, pensato per tenerti lì. Ma quello che cerchi davvero sono "
                    "persone simili a te, che parlano la tua lingua.",
                    "Nerina riparte da qui: niente da scorrere, niente da pubblicare."]),
            dict(id="come-funziona", n="Come funziona", h2="Tu racconti. Il passero cerca.",
                 passi=["Nel Diario racconti, scrivendo o a voce, che cosa ti serve: qualcuno con cui correre, un "
                        "lavoro vicino a casa, un posto dove ascoltare jazz.",
                        "Il passero cerca tra le persone e le aziende di Nerina, usando solo ciò che ognuno ha scelto "
                        "di mettere a disposizione.",
                        "Ti arriva una foglia: una proposta. Vi vedete con uno pseudonimo e vi rivelate solo se lo "
                        "volete tutti e due."],
                 schermo=("app-diario-it", "Il Diario di Nerina, dal prototipo grafico (persone e dati inventati)")),
            dict(id="passero", n="Il passero", h2="Lavora per te, non per il tuo tempo.",
                 punti=["<strong>Propone, non decide.</strong> Ogni foglia la accetti o la rifiuti tu.",
                        "<strong>Sa di essere un programma.</strong> Non si finge una persona e non fa conversazioni "
                        "romantiche o sessuali.",
                        "<strong>Sa fermarsi.</strong> Ha un limite di lavoro al giorno, poi riposa fino a domani.",
                        "<strong>È europeo.</strong> Usa un modello di Mistral AI, in Francia, e non riceve il tuo "
                        "cognome, la data di nascita né la foto."]),
            dict(id="privacy", n="Privacy", h2="Di partenza, non vede niente nessuno.",
                 p=["Scegli tu, dato per dato, chi vede che cosa."],
                 scala=("Nessuno", "Passeri", "Interessati", "Connessioni", "Pubblica"), partenza="di partenza",
                 scala_titolo="I cinque livelli di visibilità, dal più chiuso al più aperto",
                 punti=["Nelle foglie resti con uno pseudonimo finché non vi rivelate entrambi.",
                        "I dati più delicati si salvano solo con un tuo sì, uno per uno.",
                        "I tuoi contenuti non si vendono, non servono alla pubblicità e non addestrano "
                        "l&#x27;intelligenza artificiale.",
                        "Se elimini l&#x27;account, cancelliamo i tuoi dati e distruggiamo la chiave che li cifra."],
                 link=("/informativa/#che-cosa-manca-ancora", "Che cosa è già pronto e che cosa manca: l&#x27;informativa")),
            dict(id="sicurezza", n="Sicurezza", h2="Persone vere, regole chiare.",
                 p=["Si entra dai 16 anni, dopo la verifica di un documento d&#x27;identità, con un account a testa. "
                    "Chi ha 16 o 17 anni riceve proposte solo da persone vicine d&#x27;età.",
                    "Puoi segnalare e bloccare chiunque: ogni segnalazione la decide una persona."],
                 link=("/sicurezza-minori/", "Gli standard sulla sicurezza dei minori")),
            dict(id="pilota", n="Il pilota", h2="Nerina è su invito.",
                 p=["Stiamo muovendo i primi passi con poche persone, nell&#x27;Unione europea. Durante il pilota è "
                    "gratuita e senza pubblicità."],
                 bottone=("/contatti/", "Scrivici")),
        ],
        "editore": ("Nerina è pubblicata con il nome <strong>Nerina Devs</strong>. Chi è il titolare del trattamento "
                    "è scritto nell&#x27;<a href=\"/informativa/#chi-tratta-i-dati\">informativa</a>."),
    },
    "en": {
        "h1": "Find people who speak your language.",
        "attacco": ("Nerina is a social app with no feed and no posts. You tell the sparrow in private what you are "
                    "looking for, and it brings you only proposals made for you."),
        "bottone": "See how it works",
        "nota": "Invite-only pilot · from 16, with a verified ID · European Union",
        "tappe": [
            dict(id="perche", n="Why Nerina", h2="Social networks have turned into media.",
                 p=["An endless stream to watch, designed to keep you there. But what you are really looking for "
                    "is people like you, who speak your language.",
                    "Nerina starts again from there: nothing to scroll, nothing to post."]),
            dict(id="come-funziona", n="How it works", h2="You tell. The sparrow searches.",
                 passi=["In the Diary you say, in writing or out loud, what you need: someone to run with, a job "
                        "close to home, a place to listen to jazz.",
                        "The sparrow searches among the people and businesses on Nerina, using only what each "
                        "person has chosen to make available.",
                        "A leaf arrives: a proposal. You see each other under a pseudonym and reveal yourselves "
                        "only if you both want to."],
                 schermo=None),
            dict(id="passero", n="The sparrow", h2="It works for you, not for your screen time.",
                 punti=["<strong>It proposes, it does not decide.</strong> You accept or decline every leaf.",
                        "<strong>It knows it is a program.</strong> It never pretends to be a person and has no "
                        "romantic or sexual conversations.",
                        "<strong>It knows when to stop.</strong> It has a daily work limit, then it rests until "
                        "tomorrow.",
                        "<strong>It is European.</strong> It uses a model by Mistral AI, in France, and never "
                        "receives your surname, date of birth or photo."]),
            dict(id="privacy", n="Privacy", h2="By default, nobody sees anything.",
                 p=["You choose, detail by detail, who sees what."],
                 scala=("Nobody", "Sparrows", "Interested", "Connections", "Public"), partenza="default",
                 scala_titolo="The five visibility levels, from most closed to most open",
                 punti=["In a leaf you stay under a pseudonym until you both reveal yourselves.",
                        "The most sensitive details are saved only with your yes, one by one.",
                        "Your content is not sold, not used for advertising and not used to train AI.",
                        "If you delete your account, we erase your data and destroy the key that encrypts it."],
                 link=("/en/informativa/#what-is-not-ready-yet", "What is ready and what is missing: the privacy policy")),
            dict(id="sicurezza", n="Safety", h2="Real people, clear rules.",
                 p=["You can join from 16, after an identity document is verified, with one account per person. "
                    "People aged 16 or 17 only get proposals from people close in age.",
                    "You can report and block anyone: a person decides every report."],
                 link=("/en/child-safety/", "Our child safety standards")),
            dict(id="pilota", n="The pilot", h2="Nerina is invitation only.",
                 p=["We are taking our first steps with a few people in the European Union. During the pilot it is "
                    "free and has no ads."],
                 bottone=("/en/contact/", "Write to us")),
        ],
        "editore": ("Nerina is published under the name <strong>Nerina Devs</strong>. The data controller is named in "
                    "the <a href=\"/en/informativa/#who-processes-the-data\">privacy policy</a>."),
    },
}

FRECCIA = g.icona("freccia", "icona", 20)


def _tappa(t, i):
    corpo = "".join(f"<p>{x}</p>" for x in t.get("p", []))
    if "passi" in t:
        corpo += '<ol class="passi">' + "".join(f"<li>{x}</li>" for x in t["passi"]) + "</ol>"
    if "scala" in t:
        voci = "".join(
            f'<li{" class=\"scala-partenza\"" if k == 0 else ""}>{x}'
            f'{f" <span class=\"scala-etichetta\">{t["partenza"]}</span>" if k == 0 else ""}</li>'
            for k, x in enumerate(t["scala"]))
        corpo += f'<ol class="scala" aria-label="{t["scala_titolo"]}">{voci}</ol>'
    if "punti" in t:
        corpo += '<ul class="punti">' + "".join(f"<li>{x}</li>" for x in t["punti"]) + "</ul>"
    if "link" in t:
        corpo += f'<p class="tappa-link"><a href="{t["link"][0]}">{t["link"][1]}</a></p>'
    if "bottone" in t:
        corpo += f'<p><a class="bottone" href="{t["bottone"][0]}">{t["bottone"][1]}{FRECCIA}</a></p>'
    figura = ""
    if t.get("schermo"):
        f, alt = t["schermo"]
        figura = (f'<figure class="tappa-figura"><img src="/immagini/{f}.webp" width="540" height="1141" alt="{alt}" '
                  f'decoding="async"></figure>')
    classe = "tappa con-figura" if figura else "tappa"
    return (f'<section class="{classe}" id="{t["id"]}" aria-labelledby="{t["id"]}-titolo">\n'
            f'<span class="tappa-punto" aria-hidden="true">{i}</span>\n'
            f'<div class="tappa-testo"><p class="tappa-nome">{t["n"]}</p>\n'
            f'<h2 id="{t["id"]}-titolo">{t["h2"]}</h2>\n{corpo}</div>\n{figura}</section>')


def casa(lang):
    t = T[lang]
    h1_id = "che-cos-e-nerina" if lang == "it" else "what-is-nerina"
    tappe = "\n".join(_tappa(x, i) for i, x in enumerate(t["tappe"], 1))
    return f"""<section class="eroe" aria-labelledby="{h1_id}">
<div class="eroe-figura">{g.passero_eroe()}</div>
<div class="eroe-testo">
<h1 id="{h1_id}">{t["h1"]}</h1>
<p class="attacco">{t["attacco"]}</p>
<p class="eroe-azioni"><a class="bottone" href="#perche">{t["bottone"]}{g.icona("freccia", "icona freccia-giu", 20)}</a></p>
<p class="eroe-nota">{t["nota"]}</p>
</div>
</section>
<div class="percorso">
<div class="filo" aria-hidden="true"><span class="filo-pieno"></span><span class="filo-corsia"><span class="filo-foglia">{g.foglia_filo()}</span></span></div>
{tappe}
</div>
<p class="editore">{t["editore"]}</p>"""
