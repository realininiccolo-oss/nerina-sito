"""I tre temi dell'app (token-v12.css: Recanati v3, Infinito v4 «al chiaro di luna», Ginestra = palette «gelso»),
ognuno in chiaro e scuro. Da qui si genera temi.css e si controllano i contrasti (strumenti/controlla.py)."""

TEMI = {
    "recanati": {
        "nome": {"it": "Recanati", "en": "Recanati"},
        "chiaro": dict(carta="#f8f1e6", carta_alta="#fffaf2", carta_bassa="#efe5d6", inchiostro="#23170f",
                       inchiostro_2="#5c4b40", inchiostro_3="#6f5f53", bordo="#e2d5c4", bordo_forte="#8e7d6e",
                       primario="#a4432a", primario_forte="#86331e", primario_tenue="#f7ddd0", primario_testo="#92391f",
                       ambra="#d99a1e", ambra_testo="#8a5a00", ambra_tenue="#f9eac8", su_primario="#fffaf2"),
        "scuro": dict(carta="#1a120d", carta_alta="#251a14", carta_bassa="#120c08", inchiostro="#f1e8de",
                      inchiostro_2="#c2b3a6", inchiostro_3="#a19385", bordo="#3b2c23", bordo_forte="#75655a",
                      primario="#e48a68", primario_forte="#f0a383", primario_tenue="#43221a", primario_testo="#eb9877",
                      ambra="#e8b54a", ambra_testo="#efc568", ambra_tenue="#3e2c0c", su_primario="#120c08"),
    },
    "infinito": {
        "nome": {"it": "Infinito", "en": "Infinito"},
        "chiaro": dict(carta="#f1f2f0", carta_alta="#fafaf8", carta_bassa="#e4e7e6", inchiostro="#101a24",
                       inchiostro_2="#45505b", inchiostro_3="#59636e", bordo="#d3d8da", bordo_forte="#7b858f",
                       primario="#35546b", primario_forte="#273f52", primario_tenue="#dde6ec", primario_testo="#2f4c62",
                       ambra="#c99a3e", ambra_testo="#7b5a12", ambra_tenue="#f3e8cf", su_primario="#fafaf8"),
        "scuro": dict(carta="#0b111d", carta_alta="#131a28", carta_bassa="#060a13", inchiostro="#e8ebf0",
                      inchiostro_2="#b0b8c5", inchiostro_3="#8e97a6", bordo="#222b3b", bordo_forte="#5c677a",
                      primario="#a8bdd2", primario_forte="#c3d3e3", primario_tenue="#18243a", primario_testo="#b6c8da",
                      ambra="#e3cf93", ambra_testo="#ecdcaa", ambra_tenue="#2c2716", su_primario="#060a13"),
    },
    "ginestra": {
        "nome": {"it": "Ginestra", "en": "Ginestra"},
        "chiaro": dict(carta="#f9f2f2", carta_alta="#fffbfa", carta_bassa="#f0e6e6", inchiostro="#22141b",
                       inchiostro_2="#5c4652", inchiostro_3="#6f5a65", bordo="#e2d3d6", bordo_forte="#8e7c84",
                       primario="#8b2d5e", primario_forte="#6f2149", primario_tenue="#f5dce8", primario_testo="#7e2853",
                       ambra="#3f7cc4", ambra_testo="#2a5a99", ambra_tenue="#dde8f7", su_primario="#fffbfa"),
        "scuro": dict(carta="#1b1117", carta_alta="#261921", carta_bassa="#120a0f", inchiostro="#f3e8ed",
                      inchiostro_2="#c4b2bc", inchiostro_3="#a3919b", bordo="#3c2a34", bordo_forte="#77646e",
                      primario="#e78bb6", primario_forte="#f1a6c8", primario_tenue="#45202f", primario_testo="#ec9cc1",
                      ambra="#7fb0ec", ambra_testo="#9cc2f2", ambra_tenue="#1c2f4a", su_primario="#120a0f"),
    },
}


def _blocco(valori):
    return "".join(f"--{k.replace('_', '-')}:{v};" for k, v in valori.items())


def css():
    r = ["/* Generato da strumenti/temi.py: non modificare a mano. */"]
    r.append(f":root{{color-scheme:light dark;{_blocco(TEMI['recanati']['chiaro'])}}}")
    r.append(f"@media (prefers-color-scheme: dark){{:root{{{_blocco(TEMI['recanati']['scuro'])}}}}}")
    for nome, t in TEMI.items():
        r.append(f'html[data-palette="{nome}"]{{{_blocco(t["chiaro"])}}}')
        r.append(f'@media (prefers-color-scheme: dark){{html[data-palette="{nome}"]{{{_blocco(t["scuro"])}}}}}')
    return "\n".join(r) + "\n"
