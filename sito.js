/* nerina.eu — script locale (18/11/2026).
   Fa solo cinque cose, tutte nel browser di chi visita: tema scelto, percorso a domande, schermate del tema,
   comparse allo scorrimento, cursore della visibilità. Niente cookie, niente richieste di rete.
   Il tema e le risposte restano in localStorage (preferenze chieste da chi visita); senza JavaScript il sito
   funziona lo stesso, con il tema Recanati e il percorso completo. */
(function () {
  "use strict";
  var radice = document.documentElement;
  var CHIAVE_TEMA = "nerina-tema";
  var CHIAVE_PERCORSO = "nerina-percorso";
  var TEMI = ["recanati", "infinito", "ginestra"];

  function leggi(chiave) { try { return window.localStorage.getItem(chiave); } catch (e) { return null; } }
  function scrivi(chiave, valore) { try { window.localStorage.setItem(chiave, valore); } catch (e) { /* niente */ } }

  radice.classList.add("js");
  var temaSalvato = leggi(CHIAVE_TEMA);
  if (TEMI.indexOf(temaSalvato) >= 0) { radice.setAttribute("data-palette", temaSalvato); }

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

  /* percorso: ogni domanda chiusa mostra le parti adatte alla risposta */
  var percorso = {};
  try { percorso = JSON.parse(leggi(CHIAVE_PERCORSO) || "{}") || {}; } catch (e) { percorso = {}; }

  function applicaPercorso() {
    var parti = document.querySelectorAll("[data-se]");
    for (var i = 0; i < parti.length; i++) {
      var regola = parti[i].getAttribute("data-se").split(":");
      var risposta = percorso[regola[0]];
      var valori = regola[1].split(" ");
      var mostra = risposta ? valori.indexOf(risposta) >= 0 : parti[i].hasAttribute("data-predefinito");
      if (mostra) { parti[i].removeAttribute("hidden"); } else { parti[i].setAttribute("hidden", ""); }
    }
    var bottoni = document.querySelectorAll("[data-domanda]");
    for (var j = 0; j < bottoni.length; j++) {
      var d = bottoni[j].getAttribute("data-domanda");
      bottoni[j].setAttribute("aria-pressed", percorso[d] === bottoni[j].getAttribute("data-valore") ? "true" : "false");
    }
    var seguiti = document.querySelectorAll("[data-dopo]");
    for (var k = 0; k < seguiti.length; k++) {
      seguiti[k].classList.toggle("in-attesa", !percorso[seguiti[k].getAttribute("data-dopo")]);
    }
  }

  function vai(selettore) {
    var meta = selettore && document.querySelector(selettore);
    if (!meta) { return; }
    var fermo = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    meta.scrollIntoView({ behavior: fermo ? "auto" : "smooth", block: "start" });
  }

  document.addEventListener("DOMContentLoaded", function () {
    scegliTema(temaAttuale(), false);
    applicaPercorso();

    document.addEventListener("click", function (evento) {
      var tema = evento.target.closest("[data-tema-scelta]");
      if (tema) { evento.preventDefault(); scegliTema(tema.getAttribute("data-tema-scelta"), true); vai(tema.getAttribute("data-vai")); return; }
      var risposta = evento.target.closest("[data-domanda]");
      if (risposta) {
        evento.preventDefault();
        percorso[risposta.getAttribute("data-domanda")] = risposta.getAttribute("data-valore");
        scrivi(CHIAVE_PERCORSO, JSON.stringify(percorso));
        applicaPercorso();
        vai(risposta.getAttribute("data-vai"));
        return;
      }
      var daCapo = evento.target.closest("[data-ricomincia]");
      if (daCapo) { evento.preventDefault(); percorso = {}; scrivi(CHIAVE_PERCORSO, "{}"); applicaPercorso(); vai(daCapo.getAttribute("data-vai")); }
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

    /* comparse allo scorrimento */
    var animati = document.querySelectorAll(".anima");
    if ("IntersectionObserver" in window) {
      var osservatore = new IntersectionObserver(function (voci) {
        for (var v = 0; v < voci.length; v++) {
          if (voci[v].isIntersecting) { voci[v].target.classList.add("visibile"); osservatore.unobserve(voci[v].target); }
        }
      }, { rootMargin: "0px 0px -12% 0px", threshold: 0.15 });
      for (var a = 0; a < animati.length; a++) { osservatore.observe(animati[a]); }
    } else {
      for (var z = 0; z < animati.length; z++) { animati[z].classList.add("visibile"); }
    }
  });
})();
