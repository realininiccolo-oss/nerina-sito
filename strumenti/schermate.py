"""Schermate del sito (con prefers-reduced-motion: la pagina intera senza le comparse allo scorrimento) servito in locale (Playwright + Chrome del contenitore).

Uso: python3 strumenti/schermate.py CARTELLA_USCITA [PORTA]
Serve la radice del repository su 127.0.0.1 e fotografa Home, Elimina account e Informativa
a 390×844 e 1280×800, in chiaro e in scuro. Controlla anche che a 390 px non ci sia scorrimento orizzontale.
"""
import functools
import http.server
import pathlib
import shutil
import sys
import threading

from playwright.sync_api import sync_playwright

RADICE = pathlib.Path(__file__).resolve().parent.parent
PAGINE = {"home": "/", "elimina-account": "/elimina-account/", "informativa": "/informativa/",
          "home-en": "/en/", "contatti": "/contatti/", "404": "/non-esiste/",
          "funzioni": "/funzioni/", "foglie": "/funzioni/foglie/", "username": "/funzioni/username/",
          "wind-en": "/en/features/wind/", "features-en": "/en/features/"}
FOTO = ["home", "elimina-account", "informativa"]
MISURE = {"390": (390, 844), "1280": (1280, 800)}


class Gestore(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_head(self):  # come GitHub Pages: 404.html per gli indirizzi che non esistono
        percorso = self.translate_path(self.path)
        p = pathlib.Path(percorso)
        if not p.exists() and not (p.is_dir() and (p / "index.html").exists()):
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            return open(RADICE / "404.html", "rb")
        return super().send_head()


def main():
    uscita = pathlib.Path(sys.argv[1])
    porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8765
    uscita.mkdir(parents=True, exist_ok=True)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", porta), functools.partial(Gestore, directory=str(RADICE)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    problemi = []
    esterne = []
    eseguibile = shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=eseguibile, args=["--no-proxy-server"])
        for tema in ("light", "dark"):
            for misura, (w, h) in MISURE.items():
                ctx = browser.new_context(viewport={"width": w, "height": h}, color_scheme=tema,
                                          device_scale_factor=1, reduced_motion="reduce")
                pagina = ctx.new_page()
                pagina.on("request", lambda r: esterne.append(r.url)
                          if not r.url.startswith(f"http://127.0.0.1:{porta}") and not r.url.startswith("data:") else None)
                for nome, url in PAGINE.items():
                    pagina.goto(f"http://127.0.0.1:{porta}{url}", wait_until="networkidle")
                    pagina.evaluate("document.fonts.ready"); pagina.wait_for_timeout(1300)
                    largo = pagina.evaluate("document.documentElement.scrollWidth")
                    if misura == "390" and largo > 390:
                        problemi.append(f"{nome} {tema}: scorrimento orizzontale ({largo}px)")
                    if nome in FOTO:
                        pagina.screenshot(path=str(uscita / f"{nome}-{misura}-{'chiaro' if tema == 'light' else 'scuro'}.png"),
                                          full_page=(nome == "home"))
                ctx.close()
        browser.close()
    server.shutdown()
    for p in problemi:
        print("PROBLEMA", p)
    for u in sorted(set(esterne)):
        print("RICHIESTA ESTERNA", u)
    print("schermate in", uscita, "· problemi:", len(problemi), "· richieste esterne:", len(set(esterne)))
    return 1 if problemi or esterne else 0


if __name__ == "__main__":
    sys.exit(main())
