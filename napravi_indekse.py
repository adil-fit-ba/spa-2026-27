"""Pravi početnu stranicu repozitorija i vjezbe-NN/index.html (isti izgled kao repozitorij Modeliranja i simulacija).
Pokretanje: python -I napravi_indekse.py   (iz korijena repozitorija)."""
import io, os, sys
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
CSS = """<style>
:root { --papir: #eef1f4; --list: #fff; --tinta: #17212b; --siva: #56636f; --linija: #d3dae1; --narandza: #b9531a;
  --f-naslov: Cambria, Georgia, serif; --f-tekst: "Segoe UI", "Helvetica Neue", Arial, sans-serif; }
@media (prefers-color-scheme: dark) { :root { --papir: #10161c; --list: #18212a; --tinta: #e3e9ee; --siva: #9ba8b4; --linija: #2a3540; --narandza: #f0894a; color-scheme: dark; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--papir); color: var(--tinta); font: 17px/1.5 var(--f-tekst); }
main { max-width: 960px; margin: 0 auto; padding: 2rem max(16px, env(safe-area-inset-left)) 3rem; }
h1, h2, h3 { font-family: var(--f-naslov); line-height: 1.2; margin: 0 0 0.4rem; }
h1 { font-size: 2.1rem; } h2 { font-size: 1.6rem; margin-top: 2.6rem; padding-top: 1.2rem; border-top: 1px solid var(--linija); }
h3 { font-size: 1.2rem; margin-top: 1.6rem; }
.oznaka { font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--narandza); }
.siva { color: var(--siva); }
.veze { display: grid; gap: 0.7rem; grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr)); margin-top: 0.8rem; }
.veze a { display: block; text-decoration: none; background: var(--list); border: 1px solid var(--linija); border-radius: 6px; padding: 0.8rem 1rem; color: var(--tinta); }
.veze a:hover, .veze a:focus-visible { border-color: var(--narandza); }
.veze b { color: var(--narandza); }
.veze span { display: block; color: var(--siva); font-size: 0.9rem; }
footer { margin-top: 2.5rem; font-size: 0.85rem; color: var(--siva); border-top: 1px solid var(--linija); padding-top: 0.8rem; }
</style>"""
k = lambda href, naslov, opis: f'    <a href="{href}"><b>{naslov}</b><span>{opis}</span></a>\n'
grupa = lambda naslov, kartice: f'  <h3>{naslov}</h3>\n  <div class="veze">\n{"".join(kartice)}  </div>\n'


def v04(p):
    return (grupa("Prezentacija", [
        k(p + "V04-analiza.html", "Analiza algoritama",
          "Brojanje koraka, obrasci petlji, rast niza i mjerenje na kodu s vježbi V01–V03 (32 slajda).")])
      + grupa("Mini-prezentacije sa živim primjerima", [
        k(p + "mini/v04-brojanje-petlji.html", "Brojanje petlji", "Suma niza korak po korak i osam obrazaca petlji s tabelom vrijednosti."),
        k(p + "mini/v04-rast-niza.html", "Rast niza", "Dodavanje uz +1, ×1,5 ili ×2: kapacitet, kopiranja i izmjereno vrijeme."),
        k(p + "mini/v04-mjerenje.html", "Mjerenje", "Red, get(i) u petlji i prostor; Debug i Release, medijan i raspon 10 ponavljanja.")])
      + grupa("Kod", [
        k(p + "SPA-V04-analiza-postavka.zip", "Postavka (ZIP, Visual Studio)", "Projekat ASP: lista, stek i red urađeni; Analiza.h sa stubovima (0 / 30 testova), mjerenje dato.")]))


def stranica(naslov, opis, tijelo, oznaka="Strukture podataka i algoritmi · FIT UNMO 2026/27"):
    return f"""<!doctype html>
<html lang="bs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{naslov}</title>
<meta name="description" content="{opis}">
{CSS}
</head>
<body>
<main>
  <span class="oznaka">{oznaka}</span>
{tijelo}
  <footer>Strukture podataka i algoritmi, Fakultet informacijskih tehnologija, Univerzitet „Džemal Bijedić“ u Mostaru, 2026/27.</footer>
</main>
</body>
</html>
"""


uvod = ('  <p class="siva">Stranice rade u web pregledniku, bez instalacije. Prezentacije se listaju strelicama ← → ili prevlačenjem; '
        'opcija „Čitanje“ prikazuje sve slajdove na jednoj stranici. Kod se otvara u Visual Studiju.</p>\n')
root = ('  <h1>Strukture podataka i algoritmi: materijali s vježbi</h1>\n' + uvod
        + '  <h2>Vježbe 4 (27.10.2026.): analiza algoritama</h2>\n' + v04("vjezbe-04/"))
io.open(os.path.join(REPO, "index.html"), "w", encoding="utf-8", newline="\n").write(
    stranica("Strukture podataka i algoritmi 2026/27 — materijali s vježbi", "Materijali s vježbi: prezentacije, mini-prezentacije i kod.", root, "FIT UNMO · 2026/27"))
io.open(os.path.join(REPO, "vjezbe-04", "index.html"), "w", encoding="utf-8", newline="\n").write(
    stranica("Vježbe 4 — analiza algoritama", "Strukture podataka i algoritmi, FIT UNMO 2026/27: materijali vježbi 4.",
             '  <h1>Vježbe 4: analiza algoritama</h1>\n  <p class="siva">Utorak, 27.10.2026. ' + uvod.split('siva">')[1] + v04("")))
print("ok")
