"""Prova dei percorsi della home v6 con Playwright e il Chrome del contenitore.

Uso: python3 strumenti/prova_percorso.py CARTELLA_USCITA [PORTA]
Per ogni percorso, a 390 e a 1280 px: sceglie il tema, tocca le tessere, preme «Avanti», confronta il ritratto con
strumenti/percorso.compone(), controlla errori JS, richieste esterne e scorrimento orizzontale, e fotografa il ritratto.
Prova anche le regole della domanda 2, il limite di tre scelte e la pagina senza JavaScript.
"""
import functools
import http.server
import json
import pathlib
import shutil
import sys
import threading

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import percorso as P  # noqa: E402

RADICE = pathlib.Path(__file__).resolve().parent.parent
PERCORSI = [
    ("superiori", "it", "recanati", "light", ["superiori"], ["amici", "serate"]),
    ("insegno", "it", "infinito", "dark", ["insegno"], ["amici", "causa"]),
    ("azienda", "it", "ginestra", "light", ["azienda"], ["clienti", "assumere"]),
    ("tre-e-tre", "it", "recanati", "dark", ["universita", "sport", "creativo"], ["serate", "relazione", "soci"]),
    ("universita", "it", "infinito", "light", ["universita"], ["amici"]),
    ("pensione-en", "en", "ginestra", "dark", ["pensione", "volontario"], ["attivita", "mentore"]),
]
MISURE = {"390": (390, 844), "1280": (1280, 800)}


class Gestore(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main():
    uscita = pathlib.Path(sys.argv[1])
    porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8766
    uscita.mkdir(parents=True, exist_ok=True)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", porta), functools.partial(Gestore, directory=str(RADICE)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{porta}"
    problemi, righe = [], []
    eseguibile = shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=eseguibile, args=["--no-proxy-server"])
        for nome, lang, tema, modo, chi, cosa in PERCORSI:
            for misura, (w, h) in MISURE.items():
                ctx = browser.new_context(viewport={"width": w, "height": h}, color_scheme=modo, reduced_motion="reduce")
                pg = ctx.new_page()
                errori, esterne = [], []
                pg.on("pageerror", lambda x: errori.append(str(x)))
                pg.on("console", lambda m: errori.append(m.text) if m.type == "error" else None)
                pg.on("request", lambda r: esterne.append(r.url) if not r.url.startswith(base) and not r.url.startswith("data:") else None)
                pg.goto(base + ("/" if lang == "it" else "/en/"), wait_until="networkidle")
                pg.click(f'[data-tema-scelta="{tema}"]')
                for c in chi:
                    pg.click(f'[data-domanda="chi"][data-valore="{c}"]')
                pg.click('[data-avanti="1"]')
                visibili = pg.eval_on_selector_all('[data-domanda="cosa"]', "l => l.filter(b => !b.parentNode.hidden).map(b => b.dataset.valore)")
                attese = [k for k, _ in P.DATI[lang]["cosa"] if P.visibile_cosa(k, chi)]
                if visibili != attese:
                    problemi.append(f"{nome} {misura}: tessere della domanda 2 {visibili} invece di {attese}")
                for c in cosa:
                    pg.click(f'[data-domanda="cosa"][data-valore="{c}"]')
                pg.click('[data-avanti="2"]')
                pg.wait_for_timeout(400)
                r = P.compone(lang, chi, cosa)
                visto = pg.evaluate("""() => ({
                    frase: document.querySelector('[data-p=frase]').textContent,
                    riga: document.querySelector('[data-p=riga]').textContent,
                    schede: [...document.querySelectorAll('[data-p=schede] .scheda-u')].map(x => x.textContent),
                    privacy: document.querySelector('[data-p=privacy]').textContent,
                    foglia: document.querySelector('[data-p="foglia-u"]').textContent,
                    porte: [...document.querySelectorAll('[data-porta]:not([hidden])')].sort((a, b) => a.style.order - b.style.order).map(x => x.dataset.porta),
                    largo: document.documentElement.scrollWidth,
                    ordine: [...document.querySelectorAll('[data-domanda=chi][aria-pressed=true]')].map(x => x.dataset.valore + x.querySelector('.tessera-ordine').textContent)
                })""")
                atteso = dict(frase=r["frase"], riga=r["riga"], schede=[s["u"] for s in r["schede"]], privacy=r["privacy"],
                              foglia=r["foglia"][1], porte=r["porte"])
                for k, v in atteso.items():
                    if visto[k] != v:
                        problemi.append(f"{nome} {misura}: {k} = {visto[k]!r}, atteso {v!r}")
                if visto["largo"] > w:
                    problemi.append(f"{nome} {misura}: scorrimento orizzontale ({visto['largo']}px)")
                el = pg.query_selector("#ritratto")
                el.scroll_into_view_if_needed()
                pg.wait_for_timeout(300)
                el.screenshot(path=str(uscita / f"ritratto-{nome}-{misura}.png"))
                if misura == "390" and nome in ("superiori", "azienda"):
                    pg.query_selector("#chi").screenshot(path=str(uscita / f"domanda-chi-{nome}-{misura}.png"))
                    pg.query_selector("#cosa").screenshot(path=str(uscita / f"domanda-cosa-{nome}-{misura}.png"))
                if misura == "1280" and nome in ("tre-e-tre", "insegno"):
                    pg.screenshot(path=str(uscita / f"pagina-{nome}-{misura}.png"), full_page=True)
                for x in errori:
                    problemi.append(f"{nome} {misura}: errore JS {x}")
                for x in sorted(set(esterne)):
                    problemi.append(f"{nome} {misura}: richiesta esterna {x}")
                righe.append(f"{nome:12} {misura:4} {tema:8} {modo:5} chi={'+'.join(chi)} cosa={'+'.join(cosa)} → "
                             f"{' · '.join(visto['schede'])} | porte {','.join(visto['porte'])} | {visto['ordine']}")
                ctx.close()

        # limite di tre, regole, ricomincia
        ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
        pg = ctx.new_page()
        pg.goto(base + "/", wait_until="networkidle")
        for c in ("superiori", "sport", "creativo", "volontario"):
            pg.click(f'[data-domanda="chi"][data-valore="{c}"]', force=True)
        scelte = pg.eval_on_selector_all('[data-domanda=chi][aria-pressed=true]', "l => l.map(b => b.dataset.valore)")
        if scelte != ["superiori", "sport", "creativo"]:
            problemi.append(f"limite di tre: scelte {scelte}")
        if pg.get_attribute('[data-domanda=chi][data-valore=volontario]', "aria-disabled") != "true":
            problemi.append("limite di tre: la quarta tessera non è disattivata")
        pg.click('[data-avanti="1"]')
        if not pg.is_hidden('[data-domanda=cosa][data-valore=relazione]'):
            problemi.append("relazione visibile a chi va alle superiori")
        pg.click('[data-domanda="cosa"][data-valore="amici"]')
        pg.click('[data-avanti="2"]')
        pg.reload(wait_until="networkidle")
        if pg.is_hidden("#ritratto"):
            problemi.append("le risposte non restano dopo il ricaricamento")
        pg.click("[data-ricomincia]")
        if not pg.is_hidden("#ritratto") or not pg.is_hidden("#cosa"):
            problemi.append("Ricomincia non nasconde il resto del percorso")
        ctx.close()

        # senza JavaScript: profilo predefinito, domande nascoste
        for misura, (w, h) in MISURE.items():
            ctx = browser.new_context(viewport={"width": w, "height": h}, java_script_enabled=False)
            pg = ctx.new_page()
            pg.goto(base + "/", wait_until="networkidle")
            if not pg.is_hidden("#chi") or pg.is_hidden("#ritratto"):
                problemi.append(f"senza JS {misura}: domande visibili o ritratto nascosto")
            u = pg.eval_on_selector_all("[data-p=schede] .scheda-u", "l => l.map(x => x.textContent)")
            atteso = [s["u"] for s in P.compone("it", P.PRED["chi"], P.PRED["cosa"])["schede"]]
            if u != atteso:
                problemi.append(f"senza JS {misura}: schede {u}, attese {atteso}")
            if pg.evaluate("document.documentElement.scrollWidth") > w:
                problemi.append(f"senza JS {misura}: scorrimento orizzontale")
            pg.screenshot(path=str(uscita / f"senza-js-{misura}.png"), full_page=True)
            ctx.close()

        # con il movimento acceso: nessun errore
        ctx = browser.new_context(viewport={"width": 1280, "height": 800})
        pg = ctx.new_page()
        errori = []
        pg.on("pageerror", lambda x: errori.append(str(x)))
        pg.goto(base + "/en/", wait_until="networkidle")
        pg.click('[data-domanda="chi"][data-valore="genitore"]')
        pg.click('[data-avanti="1"]')
        pg.click('[data-domanda="cosa"][data-valore="serate"]')
        pg.click('[data-avanti="2"]')
        pg.wait_for_timeout(2500)
        problemi += [f"movimento: errore JS {x}" for x in errori]
        ctx.close()
        browser.close()
    server.shutdown()
    (uscita / "percorsi.txt").write_text("\n".join(righe) + "\n", encoding="utf-8")
    print("\n".join(righe))
    for p in problemi:
        print("PROBLEMA", p)
    print("percorsi:", len(righe), "· problemi:", len(problemi))
    return 1 if problemi else 0


if __name__ == "__main__":
    sys.exit(main())
