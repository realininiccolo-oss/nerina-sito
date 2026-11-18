"""Le funzioni di Nerina, una pagina ciascuna (18/11/2026).

Testi dalle decisioni di prodotto (memoria del progetto, 26/10-17/11) e dai testi legali pubblicati; niente prezzi,
niente funzioni dei soli maggiorenni, niente BB. Schermate: immagini/app/{schermo}-{tema}-{modo}-{lingua}.webp.
"""
import pathlib

import grafica as g

RADICE = pathlib.Path(__file__).resolve().parent.parent
CARTELLA_APP = RADICE / "immagini" / "app"

FUNZIONI = {
    "diario": dict(
        slug={"it": "diario", "en": "diary"}, schermo=["diario"], icona="diario",
        it=dict(nome="Diario", frase="Racconta, scrivendo o a voce.",
                attacco="Il Diario è dove parli con il passero. Non è una bacheca: quello che scrivi non lo legge nessun altro.",
                passi=["Scrivi o detta quello che ti serve, o com&#x27;è andata la giornata. Il passero ti fa domande "
                       "finché ha capito.",
                       "Quando è pronto, ti propone di partire: premi «Invia passero» e lui va a cercare.",
                       "In «Ricordi» gli dici come vuoi che ti ascolti; in «Argomenti» vedi e correggi ciò che ha "
                       "capito di te."],
                privacy=["Il testo della giornata resta solo in memoria fino a «Chiudi giornata»: non va su disco.",
                         "L&#x27;audio diventa testo e non si salva.",
                         "I dati delicati (per esempio religione o orientamento) si salvano solo con un tuo sì, uno per uno."]),
        en=dict(nome="Diary", frase="Tell it, in writing or out loud.",
                attacco="The Diary is where you talk to the sparrow. It is not a wall: nobody else reads what you write.",
                passi=["Write or speak what you need, or how your day went. The sparrow asks questions until it "
                       "understands.",
                       "When it is ready, it offers to fly: tap «Send the sparrow» and it goes searching.",
                       "In «Memories» you tell it how you want to be listened to; in «Topics» you see and correct what "
                       "it has understood about you."],
                privacy=["The day&#x27;s text stays only in memory until «Close the day»: it is not written to disk.",
                         "Audio becomes text and is not stored.",
                         "Sensitive details (for example religion or orientation) are saved only with your yes, one by one."])),
    "passero": dict(
        slug={"it": "passero", "en": "sparrow"}, schermo=["passero"], icona="cerca",
        it=dict(nome="Passero", frase="Il tuo messaggero, non il tuo padrone.",
                attacco="Il passero è un&#x27;intelligenza artificiale che lavora per te: ascolta, cerca, propone. Poi si fa da parte.",
                passi=["Quando gli hai raccontato abbastanza, lo mandi in volo con «Invia passero».",
                       "Ragiona come una persona che conosce tutti: guarda gli interessi in comune e quello che ognuno "
                       "sceglie di mostrare, non punteggi.",
                       "Torna con le foglie, le sue proposte. Ha un limite di lavoro al giorno: quando lo raggiunge, "
                       "riposa fino a domani."],
                privacy=["È un programma e lo dice: non si finge una persona, può sbagliare, non fa conversazioni "
                         "romantiche o sessuali.",
                         "Usa un modello di Mistral AI (Francia, Unione europea) e non riceve il tuo cognome, la data di "
                         "nascita né la foto.",
                         "Usa solo i dati che hai messo almeno a «Passeri»."]),
        en=dict(nome="Sparrow", frase="Your messenger, not your master.",
                attacco="The sparrow is an AI that works for you: it listens, searches, proposes. Then it steps aside.",
                passi=["Once you have told it enough, you send it off with «Send the sparrow».",
                       "It reasons like a person who knows everyone: it looks at shared interests and at what each "
                       "person chooses to show, not at scores.",
                       "It comes back with leaves, its proposals. It has a daily work limit: when it reaches it, it "
                       "rests until tomorrow."],
                privacy=["It is a program and says so: it never pretends to be a person, it can be wrong, and it has "
                         "no romantic or sexual conversations.",
                         "It uses a model by Mistral AI (France, European Union) and never receives your surname, date "
                         "of birth or photo.",
                         "It only uses details you have set to at least «Sparrows»."])),
    "foglie": dict(
        slug={"it": "foglie", "en": "leaves"}, schermo=["foglie", "foglia"], icona="foglia",
        it=dict(nome="Foglie", frase="Proposte, non un feed.",
                attacco="Una foglia è una proposta del passero: una persona, un gruppo per un&#x27;attività, un posto, "
                        "un evento o un lavoro.",
                passi=["Nella foglia vedi l&#x27;username dell&#x27;altra persona e le cose in comune che lei sceglie di "
                       "mostrare.",
                       "Accetti o rifiuti. Il passero propone solo se l&#x27;incontro ha senso per tutti e due.",
                       "Se accettate, potete scrivervi nella chat breve e incontrarvi: tra sconosciuti, in un luogo "
                       "pubblico."],
                privacy=["Per amicizia e opportunità il tipo di legame si rivela solo quando lo accettate tutti.",
                         "La chat breve ha pochi messaggi, si cancella dopo 24 ore e non permette di mandare immagini.",
                         "Chi blocchi sparisce dalle tue foglie, con tutti i suoi username."]),
        en=dict(nome="Leaves", frase="Proposals, not a feed.",
                attacco="A leaf is a proposal from the sparrow: a person, a group for an activity, a place, an event or a job.",
                passi=["In a leaf you see the other person&#x27;s username and the things you share that they choose to show.",
                       "You accept or decline. The sparrow only proposes when the meeting makes sense for both of you.",
                       "If you both accept, you can write in the short chat and meet: between strangers, in a public place."],
                privacy=["For friendship and opportunities, the kind of connection is revealed only when everyone accepts.",
                         "The short chat has few messages, is deleted after 24 hours and does not allow images.",
                         "Anyone you block disappears from your leaves, with all their usernames."])),
    "rete": dict(
        slug={"it": "rete", "en": "network"}, schermo=["rete", "connessioni"], icona="persone",
        it=dict(nome="Rete", frase="Le tue persone, in ordine.",
                attacco="La Rete raccoglie le tue connessioni: in elenco, in aree o come una mappa delle persone a cui sei legato.",
                passi=["Ti colleghi con l&#x27;username e il codice Finestra dell&#x27;altro, senza dare nome e cognome.",
                       "Raggruppi le connessioni in aree con un nome e un colore, e dai a ognuno un nome tutto tuo.",
                       "Il passero propone più volentieri incontri verso le connessioni che ti piacciono."],
                privacy=["Con «Escludi» nascondi ciò che condividi alle tue connessioni, o anche alle loro.",
                         "Ogni username ha la sua Finestra: 16 cifre che dai solo a chi vuoi.",
                         "Un blocco vale per la persona, su tutti i suoi username."]),
        en=dict(nome="Network", frase="Your people, in order.",
                attacco="The Network gathers your connections: as a list, in areas, or as a map of the people you are linked to.",
                passi=["You connect with the other person&#x27;s username and Window code, without giving your name.",
                       "You group connections into areas with a name and a colour, and give everyone a name of your own.",
                       "The sparrow is keener to propose meetings with the connections you like."],
                privacy=["With «Exclude» you hide what you share from your connections, or from theirs too.",
                         "Each username has its own Window: 16 digits you give only to whom you want.",
                         "A block applies to the person, across all their usernames."])),
    "wind": dict(
        slug={"it": "wind", "en": "wind"}, schermo=["wind"], icona="europa-ue",
        it=dict(nome="Wind", frase="Che aria tira, senza spiare nessuno.",
                attacco="Il Wind racconta che cosa piace alle persone intorno a te: musica, sport, posti, idee.",
                passi=["Fai una domanda breve: «che musica ascoltano le mie connessioni?», «che cosa fanno i ragazzi in "
                       "Lombardia nel fine settimana?».",
                       "Scegli dove guardare: le tue connessioni a due o tre passi, intorno a te, l&#x27;Italia, l&#x27;Europa.",
                       "Il passero risponde con un riassunto in parole («molti», «alcuni»), senza percentuali; "
                       "«Approfondisci» apre il rapporto completo."],
                privacy=["I tuoi gusti contano nel Wind solo se lo accendi, reparto per reparto. Di partenza è spento.",
                         "Il Wind risponde solo su gruppi di almeno 50 persone.",
                         "Le aziende vedono solo dati aggregati, mai le persone."]),
        en=dict(nome="Wind", frase="Which way the wind blows, without spying on anyone.",
                attacco="The Wind tells you what people around you like: music, sport, places, ideas.",
                passi=["Ask a short question: «what music do my connections listen to?», «what do young people in "
                       "Lombardy do at the weekend?».",
                       "Choose where to look: your connections two or three steps away, around you, Italy, Europe.",
                       "The sparrow answers with a summary in words («many», «some»), without percentages; «Learn more» "
                       "opens the full report."],
                privacy=["Your tastes count in the Wind only if you switch it on, section by section. It is off by default.",
                         "The Wind only answers about groups of at least 50 people.",
                         "Businesses only see aggregated data, never people."])),
    "eventi": dict(
        slug={"it": "eventi", "en": "events"}, schermo=["eventi", "evento"], icona="luogo",
        it=dict(nome="Eventi", frase="Dalla cena al torneo.",
                attacco="Gli Eventi riuniscono più persone: una cena, una mostra, un torneo all&#x27;oratorio.",
                passi=["Tre viste: Inviti, Partecipo, Organizzo. Cerchi gli eventi pubblici con una frase, senza filtri.",
                       "Chi organizza sceglie l&#x27;invito: pubblico, oppure mirato, con il passero che porta la foglia a "
                       "chi corrisponde alla descrizione, entro un numero massimo di persone.",
                       "Il passero ti propone eventi da quello che racconti nel Diario."],
                privacy=["Chi vede che partecipi lo scegli tu: di partenza, nessuno.",
                         "Chi organizza un evento è registrato e ne è responsabile."]),
        en=dict(nome="Events", frase="From dinner to the tournament.",
                attacco="Events bring several people together: a dinner, an exhibition, a card tournament at the parish hall.",
                passi=["Three views: Invitations, Going, Organising. You search public events with a sentence, no filters.",
                       "Organisers choose the invitation: public, or targeted, with the sparrow taking the leaf to "
                       "people who match the description, up to a maximum number.",
                       "The sparrow suggests events from what you tell the Diary."],
                privacy=["You choose who sees that you are going: by default, nobody.",
                         "Whoever organises an event is registered and responsible for it."])),
    "lavoro": dict(
        slug={"it": "lavoro", "en": "work"}, schermo=["lavoro"], icona="lavoro",
        it=dict(nome="Lavoro", frase="Il curriculum lo mostri tu.",
                attacco="Annunci e candidature passano dalle foglie, con regole chiare per tutti e due.",
                passi=["Compili il curriculum e scegli, parte per parte, chi può vederlo.",
                       "Le aziende pubblicano la retribuzione e tu vedi esattamente l&#x27;esperienza richiesta.",
                       "Il passero ti porta gli annunci adatti come foglie; puoi indicare lo stipendio che vorresti."],
                privacy=["L&#x27;azienda non vede mai il tuo stipendio ideale come numero.",
                         "Nessuna decisione solo automatica: decide sempre una persona dell&#x27;azienda.",
                         "Chi ha 16 o 17 anni vede solo gli annunci aperti alla sua età."]),
        en=dict(nome="Work", frase="You decide who sees your CV.",
                attacco="Job ads and applications go through leaves, with clear rules for both sides.",
                passi=["You fill in your CV and choose, part by part, who can see it.",
                       "Businesses publish the pay, and you see exactly the experience they ask for.",
                       "The sparrow brings you suitable ads as leaves; you can state the salary you would like."],
                privacy=["The business never sees your ideal salary as a number.",
                         "No solely automated decisions: a person at the business always decides.",
                         "People aged 16 or 17 only see ads open to their age."])),
    "username": dict(
        slug={"it": "username", "en": "usernames"}, schermo=["username", "profilo"], icona="identita",
        it=dict(nome="Username e identità", frase="Una persona, fino a tre ruoli.",
                attacco="Ti verifichi una volta con un documento. Poi scegli come presentarti in ogni contesto.",
                passi=["Nome, cognome e data di nascita sono i tuoi e restano verificati: non si cambiano.",
                       "Hai fino a tre username, ognuno con i suoi contesti (amicizia, attività insieme, studio, lavoro "
                       "e affari, volontariato, mentore e insegnamento, acquisti e scambi) e le sue informazioni.",
                       "Ogni username ha il suo omino e la sua Finestra. Il passero sceglie quale mostrare a seconda "
                       "della proposta."],
                privacy=["Chi ti incontra vede l&#x27;username che usi con lui; nome e cognome solo se scegli di mostrarli.",
                         "Ogni informazione ha cinque livelli di visibilità, da «Nessuno» a «Pubblica».",
                         "Un account a persona: dietro ogni username c&#x27;è sempre qualcuno di vero."]),
        en=dict(nome="Usernames and identity", frase="One person, up to three roles.",
                attacco="You verify yourself once with a document. Then you choose how to present yourself in each context.",
                passi=["Your name, surname and date of birth are your own and stay verified: they cannot be changed.",
                       "You have up to three usernames, each with its contexts (friendship, activities together, study, "
                       "work and business, volunteering, mentoring and teaching, buying and swapping) and its details.",
                       "Each username has its own avatar and Window. The sparrow picks which one to show depending on "
                       "the proposal."],
                privacy=["People you meet see the username you use with them; your name only if you choose to show it.",
                         "Every detail has five visibility levels, from «Nobody» to «Public».",
                         "One account per person: behind every username there is always someone real."])),
}

ETICHETTE = {
    "it": dict(indice="/funzioni/", funzioni="Funzioni", titolo_indice="Le funzioni di Nerina",
               attacco_indice="Otto funzioni, una pagina ciascuna. Sono tutte nella stessa app.",
               come="Come funziona", privacy="La tua privacy", di="Funzione {n} di {tot}",
               prima="Precedente", dopo="Successiva", casa="/", nota_schermo="Schermata dell&#x27;app, con persone e dati inventati.",
               in_arrivo="La schermata di questa funzione arriva a breve."),
    "en": dict(indice="/en/features/", funzioni="Features", titolo_indice="Nerina&#x27;s features",
               attacco_indice="Eight features, one page each. All in the same app.",
               come="How it works", privacy="Your privacy", di="Feature {n} of {tot}",
               prima="Previous", dopo="Next", casa="/en/", nota_schermo="App screen, with made-up people and data.",
               in_arrivo="The screen for this feature is coming soon."),
}


def url_funzione(chiave, lang):
    return f'{ETICHETTE[lang]["indice"]}{FUNZIONI[chiave]["slug"][lang]}/'


def varianti(nome, lang):
    """Temi e modi disponibili per una schermata in una lingua, es. ['recanati-chiaro', ...]."""
    return sorted(p.name[len(nome) + 1:-len(f"-{lang}.webp")]
                  for p in CARTELLA_APP.glob(f"{nome}-*-*-{lang}.webp"))


def schermo(candidati, lang, alt, classe="schermo"):
    for nome in candidati:
        v = varianti(nome, lang)
        if v:
            pred = "recanati-chiaro" if "recanati-chiaro" in v else v[0]
            return (f'<img class="{classe}" src="/immagini/app/{nome}-{pred}-{lang}.webp" width="480" height="1014" '
                    f'alt="{alt}" loading="lazy" decoding="async" data-schermo="{nome}" data-lingua="{lang}" '
                    f'data-varianti="{" ".join(v)}">')
    return ""


def pagina(chiave, lang):
    e = ETICHETTE[lang]
    chiavi = list(FUNZIONI)
    n = chiavi.index(chiave)
    d = FUNZIONI[chiave][lang]
    img = schermo(FUNZIONI[chiave]["schermo"], lang, d["nome"])
    figura = f'<figure class="funzione-figura">{img}<figcaption>{e["nota_schermo"]}</figcaption></figure>' if img else ""
    passi = "".join(f"<li>{x}</li>" for x in d["passi"])
    privacy = "".join(f"<li>{x}</li>" for x in d["privacy"])
    prima = chiavi[n - 1] if n > 0 else None
    dopo = chiavi[n + 1] if n < len(chiavi) - 1 else None
    nav = '<nav class="funzione-nav" aria-label="' + e["funzioni"] + '">'
    if prima:
        nav += (f'<a class="fn-prima" href="{url_funzione(prima, lang)}"><span>{e["prima"]}</span>'
                f'{FUNZIONI[prima][lang]["nome"]}</a>')
    if dopo:
        nav += (f'<a class="fn-dopo" href="{url_funzione(dopo, lang)}"><span>{e["dopo"]}</span>'
                f'{FUNZIONI[dopo][lang]["nome"]}</a>')
    nav += "</nav>"
    return f"""<p class="briciole"><a href="{e["indice"]}">{e["funzioni"]}</a> <span aria-hidden="true">›</span> {d["nome"]}</p>
<section class="funzione-testa{"" if img else " senza-figura"}">
<div>
<p class="sezione-nome">{e["di"].format(n=n + 1, tot=len(chiavi))}</p>
<h1>{d["nome"]}</h1>
<p class="frase">{d["frase"]}</p>
<p class="attacco">{d["attacco"]}</p>
</div>
{figura}
</section>
<section class="funzione-parte anima" aria-labelledby="come-{chiave}">
<h2 id="come-{chiave}">{e["come"]}</h2>
<ol class="passi-funzione">{passi}</ol>
</section>
<section class="funzione-parte anima" aria-labelledby="privacy-{chiave}">
<h2 id="privacy-{chiave}">{e["privacy"]}</h2>
<ul class="punti-privacy">{privacy}</ul>
</section>
{nav}"""


def indice(lang):
    from casa_carte import carta  # noqa: E402  (evita l'import circolare in testa)
    e = ETICHETTE[lang]
    carte = "".join(carta(k, lang) for k in FUNZIONI)
    return (f'<section class="funzioni-indice"><h1>{e["titolo_indice"]}</h1><p class="attacco">{e["attacco_indice"]}</p>'
            f'<ul class="porte-stanze porte-tutte">{carte}</ul></section>')
