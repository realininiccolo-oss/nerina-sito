"""Pagina iniziale di nerina.eu (grafica v2, 18/11/2026): testi e struttura.

Testi nuovi chiesti da Niccolò il 17/11 alle 23:57 («vendila bene»). Regola: ogni affermazione sul prodotto
viene da un testo già pubblicato (informativa, termini, elimina-account, sicurezza-minori); la fonte di ogni
frase è nell'esito claude/sito-grafica-v2-esito-2026-11-18.md. Niente promesse nuove, niente «Scarica».
"""
import grafica as g

T = {
    "it": {
        "occhiello": "Pilota su invito · Unione europea",
        "h1": 'Trova chi parla <em>la tua lingua</em>.',
        "attacco": ("Nerina è un social senza feed e senza post. Racconti in privato al passero, un&#x27;intelligenza "
                    "artificiale, che cosa cerchi: persone, lavoro, posti. Lui cerca per te e ti porta solo proposte "
                    "pensate per te."),
        "azioni": [("#come-funziona", "Scopri come funziona"), ("#privacy", "La privacy prima di tutto")],
        "nota": "Si entra solo su invito, dai 16 anni, dopo la verifica di un documento d&#x27;identità.",
        "nastro": ["Niente feed", "Niente post", "Niente pubblicità", "Persone verificate",
                   "Ogni dato parte da «Nessuno»", "Un&#x27;IA che sa fermarsi", "Pseudonimo fino al sì di tutti e due"],
        "perche": dict(
            occhiello="Perché Nerina",
            h2="I social di oggi sono media. Nerina è fatta per incontrarsi.",
            p=["Per anni ci hanno promesso di metterci in contatto. Poi i social sono diventati media: un flusso "
               "infinito di contenuti, costruito per tenerci a guardare il più a lungo possibile. Seguiamo, mettiamo "
               "like, scorriamo.",
               "E il desiderio da cui tutto era partito, trovare persone simili a noi che parlano la nostra stessa "
               "lingua, è rimasto in fondo al feed. <strong>Nerina riparte da lì.</strong>"],
            didascalia="I social media e Nerina a confronto",
            colonne=("", "Social media", "Nerina"),
            righe=[("Che cosa vedi", "Un feed infinito di contenuti", "Poche proposte, pensate per te"),
                   ("Che cosa fai", "Pubblichi per farti vedere", "Racconti in privato che cosa cerchi"),
                   ("Il tuo tempo", "Più resti, meglio è per loro", "Il passero ha un limite al giorno, poi riposa"),
                   ("Le relazioni", "Follower e like", "Connessioni che scegliete in due"),
                   ("La pubblicità", "Decide molto di ciò che vedi", "Nel pilota non c&#x27;è"),
                   ("I tuoi contenuti", "Profilo in vetrina", "Ogni dato parte da «Nessuno»")]),
        "come": dict(
            occhiello="Come funziona", h2="Tre passi. Nessuno scroll.",
            passi=[("diario", "Racconti",
                    "Nel Diario scrivi, o detti, quello che ti serve: qualcuno con cui correre la domenica, un lavoro "
                    "vicino a casa, un posto dove si suona jazz. Non è un post e non finisce su nessuna bacheca."),
                   ("cerca", "Il passero cerca",
                    "Cerca per te tra le persone e le aziende di Nerina. Usa solo quello che ognuno ha messo a "
                    "disposizione dei passeri: ciò che hai lasciato a «Nessuno» non lo usa nemmeno lui."),
                   ("foglia", "Arriva una foglia",
                    "È una proposta: una persona, un lavoro, un posto o un evento. Vi vedete con uno pseudonimo; "
                    "accetti o rifiuti, e vi rivelate solo se lo scegliete tutti e due.")],
            schermi=[("app-diario", "Il Diario: qui racconti al passero la tua giornata"),
                     ("app-passero", "Il passero, pronto a partire"),
                     ("app-foglie", "Le foglie: le proposte del passero")],
            didascalia="Schermate dal prototipo grafico dell&#x27;app (persone e dati inventati)."),
        "passero": dict(
            occhiello="Il passero",
            h2="Un&#x27;intelligenza artificiale che lavora per te, non per il tuo tempo.",
            attacco=("Il passero è il cuore di Nerina: ascolta, cerca, propone. Poi si fa da parte, perché a "
                     "decidere sei sempre tu."),
            punti=[("diario", "Ascolta come parli",
                    "Gli scrivi come scriveresti a un amico, o gli parli: l&#x27;audio diventa testo e non si salva."),
                   ("consensi", "Propone, non decide",
                    "Ogni proposta la accetti o la rifiuti tu. Nessuna decisione solo automatica che abbia "
                    "effetti giuridici su di te."),
                   ("maschera", "Sa di essere un programma",
                    "Non si finge una persona e può sbagliare. Non fa conversazioni romantiche o sessuali, "
                    "con nessuno."),
                   ("orologio", "Sa quando fermarsi",
                    "Ha un limite di lavoro al giorno per ogni persona: quando lo raggiunge, riposa fino "
                    "all&#x27;indomani. Nessun motivo per tenerti incollato allo schermo."),
                   ("europa-ue", "Europeo, e discreto",
                    "Usa un modello linguistico di Mistral AI, un&#x27;azienda francese, che non conserva i tuoi "
                    "messaggi dopo la risposta. Il passero non riceve il tuo cognome, la data di nascita né la foto.")]),
        "privacy": dict(
            occhiello="Privacy",
            h2="La privacy non è un&#x27;impostazione. È il progetto.",
            attacco=("Sui social media il profilo è una vetrina. Su Nerina scegli tu, dato per dato, chi vede che "
                     "cosa, e di partenza non lo vede nessuno."),
            livelli_titolo="I cinque livelli di visibilità",
            livelli=[("Nessuno", "Solo tu. Nemmeno i passeri lo usano.", "di partenza"),
                     ("Passeri", "Lo usano i passeri per gli abbinamenti. Nessuna persona lo legge.", ""),
                     ("Interessati", "Chi ha una foglia o un abbinamento in corso con te.", ""),
                     ("Connessioni", "Le tue connessioni e chi ha una foglia con te.", ""),
                     ("Pubblica", "Le persone verificate di Nerina. Mai il web.", "")],
            schede=[("maschera", "Pseudonimo fino al sì di tutti e due",
                     "Nelle foglie l&#x27;altra persona ti vede con uno pseudonimo, finché non scegliete entrambi "
                     "di rivelarvi."),
                    ("diario", "Il Diario non va su disco",
                     "Il testo della giornata resta solo in memoria fino a «Chiudi giornata». Poi resta un "
                     "riassunto, senza dati particolari."),
                    ("consensi", "I dati delicati, solo con un sì",
                     "Opinioni politiche, religione, orientamento sessuale: si salvano solo con un sì per ogni "
                     "dato, e partono da «Nessuno»."),
                    ("occhio-chiuso", "Una foto per riconoscervi, niente di più",
                     "Niente riconoscimento facciale. Togliamo dal file la posizione e il modello del telefono, "
                     "e la foto non va mai al modello linguistico."),
                    ("gruppo", "Le aziende vedono solo gruppi",
                     "Dati aggregati di almeno 5 persone. Nel lavoro, solo ciò che il tuo curriculum mostra "
                     "alle aziende."),
                    ("lucchetto", "Fuori dal web",
                     "Anche il livello «Pubblica» resta dentro Nerina: non si indicizza e non si esporta."),
                    ("persone", "Escludi chi conosci",
                     "Puoi nascondere ciò che condividi alle tue connessioni, o anche alle loro."),
                    ("cuore-no", "I tuoi contenuti non sono in vendita",
                     "Non li usiamo per la pubblicità, non li vendiamo e non li usiamo per addestrare modelli di "
                     "intelligenza artificiale."),
                    ("chiave", "Elimini, e la chiave sparisce",
                     "Quando elimini l&#x27;account cancelliamo i tuoi dati e distruggiamo la chiave che li cifra. "
                     "Anche dal web, senza l&#x27;app.")],
            nota=("Nerina oggi è in pilota: che cosa è già pronto e che cosa manca ancora lo trovi scritto "
                  "nell&#x27;<a href=\"/informativa/#che-cosa-manca-ancora\">informativa sulla privacy</a>.")),
        "usi": dict(
            occhiello="Per che cosa",
            h2="Un solo posto per le persone, il lavoro e i luoghi.",
            schede=[("persone", "Persone",
                     "Amicizie, compagni di attività, persone con le tue stesse passioni, vicino a te."),
                    ("lavoro", "Lavoro",
                     "Un curriculum che mostri solo a chi vuoi tu. Le aziende non vedono mai il tuo stipendio "
                     "ideale come numero."),
                    ("luogo", "Posti ed eventi",
                     "Locali, luoghi ed eventi. Chi vede che partecipi lo decidi tu: di partenza, nessuno."),
                    ("acquisti", "Acquisti",
                     "Le aziende possono proporti un loro prodotto solo se lo permetti tu, reparto per reparto.")]),
        "sicurezza": dict(
            occhiello="Sicurezza",
            h2="Persone vere, regole chiare.",
            punti=[("identita", "Identità verificata",
                    "Si entra dai 16 anni, dopo la verifica di un documento d&#x27;identità. Un account a testa."),
                   ("scudo", "Più tutele per chi ha 16 o 17 anni",
                    "Proposte solo con persone vicine d&#x27;età e niente ricerca di partner."),
                   ("consensi", "Segnali, blocchi, decide una persona",
                    "Puoi segnalare e bloccare chiunque. Ogni segnalazione la decide una persona, che ti spiega "
                    "la decisione."),
                   ("luogo", "Incontri in luoghi pubblici", "Le proposte di incontro indicano un luogo pubblico.")],
            link=("/sicurezza-minori/", "Leggi gli standard sulla sicurezza dei minori")),
        "domande": dict(
            occhiello="Domande", h2="Domande frequenti",
            voci=[("Quanto costa?", "Durante il pilota Nerina è gratuita: non paghi nulla e non c&#x27;è pubblicità."),
                  ("Come si entra?",
                   "Nel pilota si entra solo con un invito personale. Servono almeno 16 anni e la verifica di un "
                   "documento d&#x27;identità."),
                  ("Il passero legge quello che scrivo?",
                   "Sì, perché per aiutarti deve capire che cosa cerchi. Il testo va al modello linguistico di "
                   "Mistral AI (Francia), che non lo conserva dopo la risposta. Il passero non riceve il tuo cognome, "
                   "la data di nascita né la foto profilo."),
                  ("Chi vede il mio profilo?",
                   "Chi scegli tu, dato per dato, con cinque livelli: da «Nessuno» a «Pubblica». Di partenza ogni "
                   "dato è a «Nessuno». Anche «Pubblica» resta dentro Nerina."),
                  ("Dove stanno i miei dati?",
                   "Il modello linguistico è di un fornitore europeo, Mistral AI. Per il pilota l&#x27;hosting "
                   "previsto è in un centro dati nell&#x27;Unione europea. I dettagli sono nell&#x27;"
                   "<a href=\"/informativa/#a-chi-vanno-i-dati\">informativa</a>."),
                  ("Posso cancellare tutto?",
                   "Sì, quando vuoi: dall&#x27;app, oppure dal web senza l&#x27;app. Cancelliamo i tuoi dati e "
                   "distruggiamo la chiave che li cifra. <a href=\"/elimina-account/\">Elimina il tuo account</a>.")]),
        "invito": dict(
            h2="Il pilota è su invito.",
            p=("Nerina sta muovendo i primi passi con poche persone, nell&#x27;Unione europea. Hai domande, o vuoi "
               "saperne di più? Scrivici."),
            bottone=("/contatti/", "Scrivici")),
        "editore": ("Nerina è pubblicata con il nome <strong>Nerina Devs</strong>. Chi è il titolare del trattamento "
                    "è scritto nell&#x27;<a href=\"/informativa/#chi-tratta-i-dati\">informativa</a>."),
        "porte": [("/contatti/", "Contatti", "busta"), ("/informativa/", "Informativa sulla privacy", "pagina"),
                  ("/termini/", "Termini d&#x27;uso", "consensi"),
                  ("/sicurezza-minori/", "Sicurezza dei minori", "scudo"),
                  ("/elimina-account/", "Elimina il tuo account", "cestino")],
        "porte_titolo": "Le pagine di Nerina",
    },
    "en": {
        "occhiello": "Invite-only pilot · European Union",
        "h1": 'Find people who speak <em>your language</em>.',
        "attacco": ("Nerina is a social app with no feed and no posts. You tell the sparrow, an AI, in private "
                    "what you are looking for: people, work, places. It searches for you and brings you only "
                    "proposals made for you."),
        "azioni": [("#come-funziona", "See how it works"), ("#privacy", "Privacy comes first")],
        "nota": "Invitation only, from the age of 16, after an identity document is verified.",
        "nastro": ["No feed", "No posts", "No ads", "Verified people", "Every detail starts at «Nobody»",
                   "An AI that knows when to stop", "Pseudonymous until you both say yes"],
        "perche": dict(
            occhiello="Why Nerina",
            h2="Today&#x27;s social networks are media. Nerina is made for meeting people.",
            p=["For years we were promised they would bring us together. Then social networks turned into media: "
               "an endless stream of content, built to keep us watching for as long as possible. We follow, we "
               "like, we scroll.",
               "And the wish that started it all, finding people like us who speak our own language, got lost at "
               "the bottom of the feed. <strong>Nerina starts again from there.</strong>"],
            didascalia="Social media and Nerina compared",
            colonne=("", "Social media", "Nerina"),
            righe=[("What you see", "An endless feed of content", "A few proposals, made for you"),
                   ("What you do", "You post to be seen", "You say in private what you are looking for"),
                   ("Your time", "The longer you stay, the better for them", "The sparrow has a daily limit, then it rests"),
                   ("Relationships", "Followers and likes", "Connections you both choose"),
                   ("Ads", "They shape much of what you see", "None in the pilot"),
                   ("Your content", "A profile on display", "Every detail starts at «Nobody»")]),
        "come": dict(
            occhiello="How it works", h2="Three steps. No scrolling.",
            passi=[("diario", "You tell",
                    "In the Diary you write, or speak, what you need: someone to run with on Sundays, a job close to "
                    "home, a place with live jazz. It is not a post and it never lands on a wall."),
                   ("cerca", "The sparrow searches",
                    "It searches for you among the people and businesses on Nerina. It only uses what each person "
                    "has made available to the sparrows: what you left at «Nobody» is off limits, even for it."),
                   ("foglia", "A leaf arrives",
                    "A leaf is a proposal: a person, a job, a place or an event. You see each other under a "
                    "pseudonym; you accept or decline, and you reveal yourselves only if you both choose to.")],
            schermi=[("app-diario", "The Diary: where you tell the sparrow about your day"),
                     ("app-passero", "The sparrow, ready to fly"),
                     ("app-foglie", "Leaves: the sparrow&#x27;s proposals")],
            didascalia="Screens from the app&#x27;s design prototype (made-up people and data, in Italian)."),
        "passero": dict(
            occhiello="The sparrow",
            h2="An AI that works for you, not for your screen time.",
            attacco=("The sparrow is the heart of Nerina: it listens, searches and proposes. Then it steps aside, "
                     "because you always decide."),
            punti=[("diario", "It listens the way you talk",
                    "Write to it as you would to a friend, or talk to it: the audio becomes text and is not stored."),
                   ("consensi", "It proposes, it does not decide",
                    "You accept or decline every proposal. No solely automated decision with legal effects on you."),
                   ("maschera", "It knows it is a program",
                    "It never pretends to be a person and it can make mistakes. It has no romantic or sexual "
                    "conversations, with anyone."),
                   ("orologio", "It knows when to stop",
                    "It has a daily work limit for each person: when it reaches it, it rests until the next day. "
                    "No reason to keep you glued to the screen."),
                   ("europa-ue", "European, and discreet",
                    "It uses a language model by Mistral AI, a French company, which does not keep your messages "
                    "after the reply. The sparrow never receives your surname, date of birth or photo.")]),
        "privacy": dict(
            occhiello="Privacy",
            h2="Privacy is not a setting. It is the design.",
            attacco=("On social media your profile is a shop window. On Nerina you choose, detail by detail, who "
                     "sees what, and by default nobody does."),
            livelli_titolo="The five visibility levels",
            livelli=[("Nobody", "Only you. Not even the sparrows use it.", "default"),
                     ("Sparrows", "Used by the sparrows for matching. No person reads it.", ""),
                     ("Interested", "People with a leaf or a match in progress with you.", ""),
                     ("Connections", "Your connections and people with a leaf with you.", ""),
                     ("Public", "Verified people on Nerina. Never the web.", "")],
            schede=[("maschera", "Pseudonymous until you both say yes",
                     "In a leaf the other person sees you under a pseudonym, until you both choose to reveal "
                     "yourselves."),
                    ("diario", "The Diary is not written to disk",
                     "The day&#x27;s text stays only in memory until «Close the day». Then a summary remains, "
                     "without special categories of data."),
                    ("consensi", "Sensitive details, only with a yes",
                     "Political opinions, religion, sexual orientation: saved only with a yes for each one, and "
                     "they start at «Nobody»."),
                    ("occhio-chiuso", "A photo to recognise each other, nothing more",
                     "No facial recognition. We strip location and phone model from the file, and the photo never "
                     "goes to the language model."),
                    ("gruppo", "Businesses only see groups",
                     "Aggregated data of at least 5 people. For jobs, only what your CV shows to businesses."),
                    ("lucchetto", "Off the web",
                     "Even «Public» stays inside Nerina: it is not indexed and not exported."),
                    ("persone", "Hide from people you know",
                     "You can hide what you share from your connections, or from theirs too."),
                    ("cuore-no", "Your content is not for sale",
                     "We do not use it for advertising, we do not sell it and we do not use it to train AI models."),
                    ("chiave", "Delete, and the key is gone",
                     "When you delete your account we erase your data and destroy the key that encrypts it. "
                     "From the web too, without the app.")],
            nota=("Nerina is in its pilot: what is ready and what is still missing is written in the "
                  "<a href=\"/en/informativa/#what-is-not-ready-yet\">privacy policy</a>.")),
        "usi": dict(
            occhiello="What for",
            h2="One place for people, work and places.",
            schede=[("persone", "People", "Friends, activity partners, people who share your passions, near you."),
                    ("lavoro", "Work",
                     "A CV you show only to whom you want. Businesses never see your ideal salary as a number."),
                    ("luogo", "Places and events",
                     "Venues, places and events. You decide who sees that you take part: by default, nobody."),
                    ("acquisti", "Shopping",
                     "Businesses can propose a product only if you allow it, department by department.")]),
        "sicurezza": dict(
            occhiello="Safety",
            h2="Real people, clear rules.",
            punti=[("identita", "Verified identity",
                    "You can join from the age of 16, after an identity document is verified. One account per person."),
                   ("scudo", "Extra protection at 16 and 17",
                    "Proposals only with people close in age, and no partner search."),
                   ("consensi", "Report, block, a person decides",
                    "You can report and block anyone. A person decides every report and explains the decision."),
                   ("luogo", "Meetings in public places", "Proposals to meet point to a public place.")],
            link=("/en/child-safety/", "Read our child safety standards")),
        "domande": dict(
            occhiello="Questions", h2="Frequently asked questions",
            voci=[("How much does it cost?", "During the pilot Nerina is free: you pay nothing and there are no ads."),
                  ("How do I join?",
                   "During the pilot you can join only with a personal invitation. You must be at least 16 and "
                   "verify an identity document."),
                  ("Does the sparrow read what I write?",
                   "Yes, because it needs to understand what you are looking for. The text goes to Mistral AI&#x27;s "
                   "language model (France), which does not keep it after the reply. The sparrow never receives "
                   "your surname, date of birth or profile photo."),
                  ("Who sees my profile?",
                   "Whoever you choose, detail by detail, with five levels: from «Nobody» to «Public». By default "
                   "every detail is at «Nobody». Even «Public» stays inside Nerina."),
                  ("Where is my data?",
                   "The language model comes from a European provider, Mistral AI. For the pilot, hosting is "
                   "planned in a data centre in the European Union. Details are in the "
                   "<a href=\"/en/informativa/#who-receives-the-data\">privacy policy</a>."),
                  ("Can I delete everything?",
                   "Yes, whenever you want: in the app, or on the web without the app. We erase your data and "
                   "destroy the key that encrypts it. <a href=\"/en/delete-account/\">Delete your account</a>.")]),
        "invito": dict(
            h2="The pilot is invitation only.",
            p=("Nerina is taking its first steps with a few people in the European Union. Questions, or want to "
               "know more? Write to us."),
            bottone=("/en/contact/", "Write to us")),
        "editore": ("Nerina is published under the name <strong>Nerina Devs</strong>. The data controller is named in "
                    "the <a href=\"/en/informativa/#who-processes-the-data\">privacy policy</a>."),
        "porte": [("/en/contact/", "Contact", "busta"), ("/en/informativa/", "Privacy policy", "pagina"),
                  ("/en/terms/", "Terms of use", "consensi"), ("/en/child-safety/", "Child safety", "scudo"),
                  ("/en/delete-account/", "Delete your account", "cestino")],
        "porte_titolo": "Nerina&#x27;s pages",
    },
}


def _intestazione(occhiello, h2, id_):
    return f'<p class="occhiello">{occhiello}</p>\n<h2 id="{id_}-titolo">{h2}</h2>'


def casa(lang):
    t = T[lang]
    h1_id = "che-cos-e-nerina" if lang == "it" else "what-is-nerina"
    azioni = "".join(
        f'<a class="bottone{" bottone-secondario" if i else ""}" href="{h}">{s}</a>' for i, (h, s) in enumerate(t["azioni"]))
    nastro_voci = "".join(f"<li>{g.icona('foglia', 'icona nastro-foglia', 18)}{v}</li>" for v in t["nastro"])
    nastro_copia = nastro_voci.replace("<li>", '<li class="copia">')
    p = t["perche"]
    righe = "\n".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td></tr>' for a, b, c in p["righe"])
    c = t["come"]
    passi = "\n".join(
        f'<li class="passo rivela">{g.icona(i, "icona icona-grande", 28)}<span class="passo-n" aria-hidden="true">{n}</span>'
        f"<h3>{h}</h3><p>{d}</p></li>" for n, (i, h, d) in enumerate(c["passi"], 1))
    schermi = "\n".join(
        f'<img class="schermo schermo-{n}" src="/immagini/{f}.webp" width="540" height="1141" alt="{a}" '
        f'loading="lazy" decoding="async">' for n, (f, a) in enumerate(c["schermi"], 1))
    pa = t["passero"]
    punti_passero = "\n".join(f'<li class="rivela">{g.icona(i, "icona", 24)}<div><h3>{h}</h3><p>{d}</p></div></li>'
                              for i, h, d in pa["punti"])
    pr = t["privacy"]
    livelli = "\n".join(
        f'<li class="livello{" livello-partenza" if x else ""}"><span class="livello-nome">{n}</span>'
        f'{f"<span class=\"livello-etichetta\">{x}</span>" if x else ""}<span class="livello-testo">{d}</span></li>'
        for n, d, x in pr["livelli"])
    schede_privacy = "\n".join(f'<li class="scheda rivela">{g.icona(i, "icona", 24)}<h3>{h}</h3><p>{d}</p></li>'
                               for i, h, d in pr["schede"])
    u = t["usi"]
    usi = "\n".join(f'<li class="scheda scheda-uso rivela">{g.icona(i, "icona icona-grande", 28)}<h3>{h}</h3><p>{d}</p></li>'
                    for i, h, d in u["schede"])
    s = t["sicurezza"]
    sicurezza = "\n".join(f'<li class="rivela">{g.icona(i, "icona", 24)}<div><h3>{h}</h3><p>{d}</p></div></li>'
                          for i, h, d in s["punti"])
    d = t["domande"]
    domande = "\n".join(f"<details class=\"domanda\"><summary><h3>{q}</h3>{g.icona('freccia', 'icona freccia-giu', 20)}"
                        f"</summary><div class=\"risposta\"><p>{r}</p></div></details>" for q, r in d["voci"])
    inv = t["invito"]
    porte = "\n".join(f'<li><a href="{h}">{g.icona(i)}<span>{x}</span>{g.icona("freccia", "icona freccia", 20)}</a></li>'
                      for h, x, i in t["porte"])
    return f"""<section class="eroe" aria-labelledby="{h1_id}">
<div class="eroe-testo">
<p class="occhiello entra">{t["occhiello"]}</p>
<h1 id="{h1_id}" class="entra r1">{t["h1"]}</h1>
<p class="attacco entra r2">{t["attacco"]}</p>
<div class="azioni entra r3">{azioni}</div>
<p class="nota-eroe entra r4">{g.icona("identita", "icona", 20)}<span>{t["nota"]}</span></p>
</div>
<div class="eroe-figura entra r2">
{g.illustrazione_eroe()}
</div>
</section>
<div class="nastro" aria-hidden="true"><ul class="nastro-scorre">{nastro_voci}{nastro_copia}</ul></div>

<section class="banda banda-notte" id="perche" aria-labelledby="perche-titolo">
<div class="contenitore">
<div class="banda-testa rivela">{_intestazione(p["occhiello"], p["h2"], "perche")}</div>
<div class="manifesto rivela">{"".join(f"<p>{x}</p>" for x in p["p"])}</div>
<div class="confronto-riquadro rivela" role="region" tabindex="0" aria-label="{p["didascalia"]}">
<table class="confronto"><caption class="solo-lettori">{p["didascalia"]}</caption>
<thead><tr><td></td><th scope="col">{p["colonne"][1]}</th><th scope="col">{p["colonne"][2]}</th></tr></thead>
<tbody>
{righe}
</tbody></table></div>
</div>
</section>

<section class="banda" id="come-funziona" aria-labelledby="come-funziona-titolo">
<div class="contenitore griglia-come">
<div>
<div class="rivela">{_intestazione(c["occhiello"], c["h2"], "come-funziona")}</div>
<ol class="passi">
{passi}
</ol>
</div>
<figure class="telefoni rivela">
<div class="telefoni-scena">
{schermi}
</div>
<figcaption>{c["didascalia"]}</figcaption>
</figure>
</div>
</section>

<section class="banda banda-calda" id="passero" aria-labelledby="passero-titolo">
<div class="contenitore griglia-passero">
<div class="passero-palco rivela">{g.passero_grande("ritratto")}</div>
<div>
<div class="rivela">{_intestazione(pa["occhiello"], pa["h2"], "passero")}</div>
<p class="attacco-sezione rivela">{pa["attacco"]}</p>
<ul class="elenco-icone">
{punti_passero}
</ul>
</div>
</div>
</section>

<section class="banda" id="privacy" aria-labelledby="privacy-titolo">
<div class="contenitore">
<div class="banda-testa rivela">{_intestazione(pr["occhiello"], pr["h2"], "privacy")}
<p class="attacco-sezione">{pr["attacco"]}</p></div>
<div class="livelli-riquadro rivela">
<h3 class="livelli-titolo">{pr["livelli_titolo"]}</h3>
<ol class="livelli">
{livelli}
</ol>
</div>
<ul class="schede-griglia">
{schede_privacy}
</ul>
<p class="nota-onesta rivela">{pr["nota"]}</p>
</div>
</section>

<section class="banda banda-calda" id="per-che-cosa" aria-labelledby="per-che-cosa-titolo">
<div class="contenitore">
<div class="banda-testa rivela">{_intestazione(u["occhiello"], u["h2"], "per-che-cosa")}</div>
<ul class="schede-griglia schede-quattro">
{usi}
</ul>
</div>
</section>

<section class="banda" id="sicurezza" aria-labelledby="sicurezza-titolo">
<div class="contenitore griglia-sicurezza">
<div class="rivela">{_intestazione(s["occhiello"], s["h2"], "sicurezza")}
<p><a class="link-freccia" href="{s["link"][0]}">{s["link"][1]}{g.icona("freccia", "icona", 18)}</a></p></div>
<ul class="elenco-icone elenco-due">
{sicurezza}
</ul>
</div>
</section>

<section class="banda banda-calda" id="domande" aria-labelledby="domande-titolo">
<div class="contenitore contenitore-stretto">
<div class="banda-testa rivela">{_intestazione(d["occhiello"], d["h2"], "domande")}</div>
<div class="domande">
{domande}
</div>
</div>
</section>

<section class="banda" aria-labelledby="invito-titolo">
<div class="contenitore">
<div class="invito rivela">
<div><h2 id="invito-titolo">{inv["h2"]}</h2><p>{inv["p"]}</p></div>
<a class="bottone bottone-chiaro" href="{inv["bottone"][0]}">{inv["bottone"][1]}{g.icona("freccia", "icona", 20)}</a>
</div>
<p class="editore">{t["editore"]}</p>
<nav aria-label="{t["porte_titolo"]}"><ul class="porte">
{porte}
</ul></nav>
</div>
</section>"""
