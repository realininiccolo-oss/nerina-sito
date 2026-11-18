/* nerina.eu — script locale, v6 (18/11/2026).
   Fa solo queste cose, tutte nel browser di chi visita: tema scelto, percorso a due domande a scelta multipla
   (con il ritratto e le pagine costruite sulle risposte), schermate del tema, comparse allo scorrimento, cursore
   della visibilità. Niente cookie, niente richieste di rete, niente HTML scritto come testo: gli elementi nuovi si creano con
   createElement e textContent, oppure clonando i modelli già nella pagina.
   I dati del percorso stanno nel blocco <script type="application/json" id="percorso-dati"> (non si esegue).
   Il tema e le risposte restano in localStorage (preferenze chieste da chi visita); senza JavaScript il sito
   funziona lo stesso, con il tema Recanati e il profilo predefinito (università + amici). */
(function () {
  "use strict";
  var radice = document.documentElement;
  var CHIAVE_TEMA = "nerina-tema";
  var CHIAVE_PERCORSO = "nerina-percorso-v6";
  var TEMI = ["recanati", "infinito", "ginestra"];
  var MASSIMO = 3;

  function leggi(chiave) { try { return window.localStorage.getItem(chiave); } catch (e) { return null; } }
  function scrivi(chiave, valore) { try { window.localStorage.setItem(chiave, valore); } catch (e) { /* niente */ } }
  function togli(chiave) { try { window.localStorage.removeItem(chiave); } catch (e) { /* niente */ } }

  radice.classList.add("js");
  var temaSalvato = leggi(CHIAVE_TEMA);
  if (TEMI.indexOf(temaSalvato) >= 0) { radice.setAttribute("data-palette", temaSalvato); }
  togli("nerina-percorso");   /* risposte della v5, in un formato che non vale più */

  function temaAttuale() { return radice.getAttribute("data-palette") || "recanati"; }
  var scuro = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;
  function modoAttuale() { return scuro && scuro.matches ? "scuro" : "chiaro"; }

  /* schermate: sceglie il file del tema e del modo attuali fra quelli che esistono */
  function aggiornaSchermi() {
    var immagini = document.querySelectorAll("img[data-schermo]");
    for (var i = 0; i < immagini.length; i++) {
      var img = immagini[i];
      var varianti = (img.getAttribute("data-varianti") || "").split(" ");
      var prove = [temaAttuale() + "-" + modoAttuale(), temaAttuale() + "-chiaro", "recanati-" + modoAttuale(), "recanati-chiaro"];
      for (var k = 0; k < prove.length; k++) {
        if (varianti.indexOf(prove[k]) >= 0) {
          var src = "/immagini/app/" + img.getAttribute("data-schermo") + "-" + prove[k] + "-" + img.getAttribute("data-lingua") + ".webp";
          if (img.getAttribute("src") !== src) { img.setAttribute("src", src); }
          break;
        }
      }
    }
  }

  function scegliTema(nome, salva) {
    if (TEMI.indexOf(nome) < 0) { return; }
    radice.setAttribute("data-palette", nome);
    if (salva) { scrivi(CHIAVE_TEMA, nome); }
    var scelto = salva || leggi(CHIAVE_TEMA);
    var bottoni = document.querySelectorAll("[data-tema-scelta]");
    for (var i = 0; i < bottoni.length; i++) {
      bottoni[i].setAttribute("aria-pressed", scelto && bottoni[i].getAttribute("data-tema-scelta") === nome ? "true" : "false");
    }
    aggiornaSchermi();
  }

  /* ---------------------------------------------------------------- il percorso */

  var D = null;            /* dati del percorso, dal blocco JSON */
  var stato = { chi: [], cosa: [], passo: 0 };

  function caricaStato() {
    try {
      var s = JSON.parse(leggi(CHIAVE_PERCORSO) || "null");
      if (s && Array.isArray(s.chi) && Array.isArray(s.cosa) && typeof s.passo === "number") {
        stato = { chi: s.chi.slice(0, MASSIMO), cosa: s.cosa.slice(0, MASSIMO), passo: s.passo };
      }
    } catch (e) { /* stato vuoto */ }
  }
  function salvaStato() { scrivi(CHIAVE_PERCORSO, JSON.stringify(stato)); }

  function contiene(lista, x) { return lista.indexOf(x) >= 0; }
  function qualcuno(lista, altri) { for (var i = 0; i < lista.length; i++) { if (contiene(altri, lista[i])) { return true; } } return false; }

  function visibileCosa(tessera) {
    var solo = (tessera.getAttribute("data-solo") || "").split(" ").filter(Boolean);
    var nascondi = (tessera.getAttribute("data-nascondi") || "").split(" ").filter(Boolean);
    if (solo.length && !qualcuno(stato.chi, solo)) { return false; }
    return !qualcuno(stato.chi, nascondi);
  }

  /* lo stesso calcolo di strumenti/percorso.py (compone) */
  function componi() {
    var chi = stato.chi.length ? stato.chi : D.pred.chi;
    var cosa = stato.chi.length ? stato.cosa : D.pred.cosa;
    var usatiCol = [];
    function colore(c) {
      var lista = [c].concat(D.ordine_colori);
      for (var i = 0; i < lista.length; i++) { if (!contiene(usatiCol, lista[i])) { usatiCol.push(lista[i]); return lista[i]; } }
      return c;
    }
    var schede = [], porte = [], i, q;

    if (contiene(chi, "azienda")) {
      var a = D.azienda, altro = null;
      for (i = 0; i < chi.length; i++) { if (D.variante_org[chi[i]]) { altro = chi[i]; break; } }
      var v = a.varianti[altro ? D.variante_org[altro] : "libreria"];
      schede.push({ u: v.nome, ruolo: a.ruolo_org, mostra: a.mostra_org, icona: "org" });
      var tipi = [];
      for (i = 0; i < cosa.length; i++) { var t = D.org_tipo[cosa[i]]; if (t && !contiene(tipi, t)) { tipi.push(t); } }
      ["invito", "evento", "soci"].forEach(function (t) { if (tipi.length < 2 && !contiene(tipi, t)) { tipi.push(t); } });
      tipi.slice(0, 2).forEach(function (t) { schede.push({ u: v[t], ruolo: a.ruoli[t], mostra: "", icona: D.org_icona[t] }); });
      for (i = 0; i < cosa.length; i++) { var p = D.porte_org[cosa[i]]; if (p && !contiene(porte, p)) { porte.push(p); } }
      D.riempi_org.forEach(function (p) { if (!contiene(porte, p)) { porte.push(p); } });
      return { frase: a.frase, riga: cosa.length ? (D.righe[cosa[0]] || "") : "", schede: schede, sotto: a.sotto,
               privacy: D.privacy_pred, foglia: [v.foglia[0], v.nome, a.ruoli.evento, v.foglia[1]], porte: porte.slice(0, 3) };
    }

    var ordine = (contiene(chi, "superiori") ? ["superiori"] : []).concat(chi).filter(function (x, n, l) { return l.indexOf(x) === n; });
    var prof = D.profili[chi[0]], s = prof.serio;
    schede.push({ u: s.u, ruolo: s.ruolo, mostra: s.mostra, colore: colore(s.colore), testa: s.testa || "" });
    var usati = [s.u], tipiUsati = s.copre.slice(), nomi = [nomeDi(s.u)];
    function nomeDi(u) { var t = u.split("."); return contiene(D.prefissi, t[0]) && t.length > 1 ? t[1] : t[0]; }
    function senzaNome(u) {   /* ogni nome proprio una volta sola, se no gli username si collegano */
      var n = nomeDi(u), t = u.split(".");
      if (contiene(D.nomi, n) && contiene(nomi, n)) { return t.slice(contiene(D.prefissi, t[0]) ? 2 : 1).join("."); }
      return u;
    }
    function aggiungi(q) {
      if (schede.length >= MASSIMO || contiene(tipiUsati, q)) { return; }
      tipiUsati.push(q);
      var voce = null;
      for (var k = 0; k < ordine.length && !voce; k++) {
        var per = D.profili[ordine[k]].per;
        if (per[q] && !contiene(usati, per[q].u)) { voce = per[q]; }
      }
      if (!voce && D.riserva[q] && !contiene(usati, D.riserva[q].u)) { voce = D.riserva[q]; }
      var u = voce ? senzaNome(voce.u) : "";
      if (voce && u.indexOf(".") >= 0) { usati.push(voce.u); nomi.push(nomeDi(u)); schede.push({ u: u, ruolo: D.ruoli[q], mostra: voce.mostra, colore: colore(D.colori[q]), testa: "" }); }
    }
    for (i = 0; i < cosa.length; i++) { aggiungi(cosa[i]); }
    for (i = 1; i < chi.length && schede.length < MASSIMO; i++) {
      var s2 = D.profili[chi[i]] && D.profili[chi[i]].serio;
      var u2 = s2 ? senzaNome(s2.u) : "";
      if (s2 && !contiene(usati, s2.u) && u2.indexOf(".") >= 0) { usati.push(s2.u); nomi.push(nomeDi(u2)); schede.push({ u: u2, ruolo: s2.ruolo, mostra: s2.mostra, colore: colore(s2.colore), testa: s2.testa || "" }); }
    }
    var riserve = prof.riserva.concat(Object.keys(D.riserva));
    for (i = 0; i < riserve.length && schede.length < MASSIMO; i++) {
      if (visibileChiave(riserve[i], chi)) { aggiungi(riserve[i]); }
    }
    var q0 = cosa.length ? cosa[0] : prof.riserva[0];
    var foglia = D.foglie[chi[0] + "|" + q0] || null;
    for (i = 0; i < ordine.length && !foglia; i++) { foglia = D.foglie[ordine[i] + "|" + q0] || null; }
    foglia = foglia || D.foglie_riserva[q0];
    if (cosa.length) { porte.push(D.porte[cosa[0]]); }
    if (!contiene(porte, "username")) { porte.push("username"); }
    for (i = 1; i < cosa.length; i++) { if (!contiene(porte, D.porte[cosa[i]])) { porte.push(D.porte[cosa[i]]); } }
    D.riempi.forEach(function (p) { if (!contiene(porte, p)) { porte.push(p); } });
    return { frase: prof.frase, riga: cosa.length ? (D.righe[cosa[0]] || "") : "", schede: schede, sotto: D.sotto,
             privacy: prof.vede.replace("{1}", schede[0].u).replace("{3}", schede[schede.length - 1].u),
             foglia: foglia, porte: porte.slice(0, 3) };
  }

  /* regole della domanda 2 lette dalle tessere (data-solo, data-nascondi) */
  function visibileChiave(q, chi) {
    var t = document.querySelector('[data-domanda="cosa"][data-valore="' + q + '"]');
    if (!t) { return true; }
    var solo = (t.getAttribute("data-solo") || "").split(" ").filter(Boolean);
    var nascondi = (t.getAttribute("data-nascondi") || "").split(" ").filter(Boolean);
    if (solo.length && !qualcuno(chi, solo)) { return false; }
    return !qualcuno(chi, nascondi);
  }

  var numeroClone = 0;
  function clona(modello) {
    var c = modello.cloneNode(true);
    numeroClone += 1;
    var clip = c.querySelectorAll("clipPath");
    for (var i = 0; i < clip.length; i++) {
      var vecchio = clip[i].getAttribute("id"), nuovo = vecchio + "-c" + numeroClone;
      clip[i].setAttribute("id", nuovo);
      var uso = c.querySelectorAll('[clip-path="url(#' + vecchio + ')"]');
      for (var k = 0; k < uso.length; k++) { uso[k].setAttribute("clip-path", "url(#" + nuovo + ")"); }
    }
    c.removeAttribute("data-omino");
    c.removeAttribute("data-icona-scheda");
    c.setAttribute("aria-hidden", "true");
    return c;
  }
  function figura(s) {
    var m = s.icona ? document.querySelector('[data-icona-scheda="' + s.icona + '"]')
      : (document.querySelector('[data-omino="' + s.colore + "|" + (s.testa || "") + '"]') || document.querySelector('[data-omino="' + s.colore + '|"]'));
    return m ? clona(m) : document.createElement("span");
  }
  function span(classe, testo) { var x = document.createElement("span"); x.className = classe; x.textContent = testo; return x; }
  function metti(chiave, testo) {
    var el = document.querySelectorAll('[data-p="' + chiave + '"]');
    for (var i = 0; i < el.length; i++) { if (el[i].textContent !== testo) { el[i].textContent = testo; } }
  }

  function disegnaRitratto() {
    if (!D) { return; }
    var r = componi();
    metti("frase", r.frase);
    metti("riga", r.riga);
    metti("sotto", r.sotto);
    metti("privacy", r.privacy);
    var lista = document.querySelector('[data-p="schede"]');
    if (lista) {
      while (lista.firstChild) { lista.removeChild(lista.firstChild); }
      r.schede.forEach(function (s, n) {
        var li = document.createElement("li");
        li.className = "scheda s" + (n + 1);
        li.appendChild(figura(s));
        var testi = span("scheda-testi", "");
        testi.appendChild(span("scheda-u", s.u));
        testi.appendChild(span("scheda-ruolo", s.ruolo));
        if (s.mostra) { testi.appendChild(span("scheda-mostra", s.mostra)); }
        li.appendChild(testi);
        lista.appendChild(li);
      });
    }
    var f = r.foglia;
    metti("richiesta", f[0]);
    metti("foglia-u", f[1]);
    metti("foglia-tipo", f[2]);
    metti("motivo", f[3]);
    var box = document.querySelector('[data-p="foglia-figura"]');
    if (box) {
      while (box.firstChild) { box.removeChild(box.firstChild); }
      box.appendChild(figura(f[1].indexOf(" ") >= 0 ? { icona: "evento" } : { colore: "ginestra" }));
    }
    var porte = document.querySelectorAll("[data-porta]");
    for (var i = 0; i < porte.length; i++) {
      var pos = r.porte.indexOf(porte[i].getAttribute("data-porta"));
      if (pos >= 0) { porte[i].removeAttribute("hidden"); porte[i].style.order = String(pos); }
      else { porte[i].setAttribute("hidden", ""); }
    }
  }

  function applicaPercorso() {
    /* tessere della domanda 2: solo quelle che hanno senso per le risposte alla 1 */
    var cosa = document.querySelectorAll('[data-domanda="cosa"]');
    for (var i = 0; i < cosa.length; i++) {
      var vis = visibileCosa(cosa[i]);
      cosa[i].parentNode.hidden = !vis;
      if (!vis) { stato.cosa = stato.cosa.filter(function (x) { return x !== cosa[i].getAttribute("data-valore"); }); }
    }
    ["chi", "cosa"].forEach(function (d) {
      var scelte = stato[d];
      var tessere = document.querySelectorAll('[data-domanda="' + d + '"]');
      for (var k = 0; k < tessere.length; k++) {
        var pos = scelte.indexOf(tessere[k].getAttribute("data-valore"));
        tessere[k].setAttribute("aria-pressed", pos >= 0 ? "true" : "false");
        tessere[k].querySelector(".tessera-ordine").textContent = pos >= 0 ? String(pos + 1) : "";
        if (pos < 0 && scelte.length >= MASSIMO) { tessere[k].setAttribute("aria-disabled", "true"); }
        else { tessere[k].removeAttribute("aria-disabled"); }
      }
      var avanti = document.querySelector('[data-avanti="' + (d === "chi" ? 1 : 2) + '"]');
      if (avanti) { avanti.hidden = scelte.length === 0; }
    });
    if (!stato.chi.length) { stato.passo = 0; }
    else if (!stato.cosa.length && stato.passo > 1) { stato.passo = 1; }
    var seguiti = document.querySelectorAll("[data-dopo]");
    for (var s = 0; s < seguiti.length; s++) {
      seguiti[s].classList.toggle("in-attesa", stato.passo < Number(seguiti[s].getAttribute("data-dopo")));
    }
    disegnaRitratto();
  }

  function tocca(tessera) {
    if (tessera.getAttribute("aria-disabled") === "true") { return; }
    var d = tessera.getAttribute("data-domanda"), v = tessera.getAttribute("data-valore");
    var lista = stato[d], pos = lista.indexOf(v);
    if (pos >= 0) { lista.splice(pos, 1); } else if (lista.length < MASSIMO) { lista.push(v); }
    salvaStato();
    applicaPercorso();
  }

  function vai(selettore) {
    var meta = selettore && document.querySelector(selettore);
    if (!meta) { return; }
    var fermo = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    meta.scrollIntoView({ behavior: fermo ? "auto" : "smooth", block: "start" });
  }

  document.addEventListener("DOMContentLoaded", function () {
    scegliTema(temaAttuale(), false);
    var blocco = document.getElementById("percorso-dati");
    if (blocco) {
      try { D = JSON.parse(blocco.textContent); } catch (e) { D = null; }
      if (D) { caricaStato(); applicaPercorso(); } else { radice.classList.add("senza-percorso"); }
    }

    document.addEventListener("click", function (evento) {
      var tema = evento.target.closest("[data-tema-scelta]");
      if (tema) { evento.preventDefault(); scegliTema(tema.getAttribute("data-tema-scelta"), true); vai(tema.getAttribute("data-vai")); return; }
      var tessera = evento.target.closest("[data-domanda]");
      if (tessera && D) { evento.preventDefault(); tocca(tessera); return; }
      var avanti = evento.target.closest("[data-avanti]");
      if (avanti && D) {
        evento.preventDefault();
        stato.passo = Math.max(stato.passo, Number(avanti.getAttribute("data-avanti")));
        salvaStato(); applicaPercorso();
        vai(avanti.getAttribute("data-vai"));
        return;
      }
      var daCapo = evento.target.closest("[data-ricomincia]");
      if (daCapo && D) {
        evento.preventDefault();
        stato = { chi: [], cosa: [], passo: 0 };
        togli(CHIAVE_PERCORSO); applicaPercorso(); vai(daCapo.getAttribute("data-vai"));
      }
    });

    if (scuro && scuro.addEventListener) { scuro.addEventListener("change", aggiornaSchermi); }

    /* cursore della visibilità */
    var cursori = document.querySelectorAll("input[data-livelli]");
    for (var c = 0; c < cursori.length; c++) {
      (function (cursore) {
        var scatola = cursore.closest("[data-scatola-livelli]");
        var aggiorna = function () {
          scatola.setAttribute("data-livello", cursore.value);
          var testi = scatola.querySelectorAll("[data-testo-livello]");
          for (var t = 0; t < testi.length; t++) {
            if (testi[t].getAttribute("data-testo-livello") === cursore.value) { testi[t].removeAttribute("hidden"); }
            else { testi[t].setAttribute("hidden", ""); }
          }
          cursore.setAttribute("aria-valuetext", scatola.querySelector("[data-testo-livello='" + cursore.value + "'] strong").textContent);
        };
        cursore.addEventListener("input", aggiorna);
        aggiorna();
      })(cursori[c]);
    }

    /* la pagina si accende mentre la scorri */
    var animati = document.querySelectorAll(".anima");
    if ("IntersectionObserver" in window) {
      var osservatore = new IntersectionObserver(function (voci) {
        for (var v = 0; v < voci.length; v++) {
          if (voci[v].isIntersecting) { voci[v].target.classList.add("visibile"); osservatore.unobserve(voci[v].target); }
        }
      }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
      for (var a = 0; a < animati.length; a++) { osservatore.observe(animati[a]); }
    } else {
      for (var z = 0; z < animati.length; z++) { animati[z].classList.add("visibile"); }
    }
  });
})();
