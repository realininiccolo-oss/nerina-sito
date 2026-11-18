"""Carte delle funzioni («stanze»): nella home (porte) e nell'indice /funzioni/."""
import grafica as g
from funzioni import FUNZIONI, url_funzione, schermo


def carta(chiave, lang):
    d = FUNZIONI[chiave][lang]
    img = schermo(FUNZIONI[chiave]["schermo"], lang, "", "carta-schermo")
    figura = img or g.icona(FUNZIONI[chiave]["icona"], "icona", 32)
    return (f'<li><a class="porta" href="{url_funzione(chiave, lang)}"><span class="porta-figura'
            f'{"" if img else " vuota"}">{figura}</span><span class="porta-nome">{d["nome"]}</span>'
            f'<span class="porta-frase">{d["frase"]}</span></a></li>')
