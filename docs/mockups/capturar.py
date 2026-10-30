"""Regenera los PNG de los mockups a partir de sus HTML.

Uso:
    pip install playwright
    python capturar.py              # usa Google Chrome instalado
    python capturar.py --chromium   # usa el Chromium de Playwright (playwright install chromium)
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

CARPETA = pathlib.Path(__file__).resolve().parent

# (archivo HTML, sufijo de URL, PNG de salida)
CAPTURAS = [
    ("6.1-situacion-temporal.html", "", "6.1-situacion-temporal.png"),
    ("6.1-situacion-temporal.html", "#no-validado", "6.1b-situacion-temporal-no-validado.png"),
    ("6.2-constancia-salida.html", "", "6.2-constancia-salida.png"),
]


def main():
    canal = None if "--chromium" in sys.argv else "chrome"
    with sync_playwright() as p:
        navegador = p.chromium.launch(channel=canal)
        pagina = navegador.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        for html, sufijo, png in CAPTURAS:
            pagina.goto((CARPETA / html).as_uri() + sufijo)
            pagina.wait_for_timeout(300)
            pagina.screenshot(path=CARPETA / png, full_page=True)
            print("generado", png)
        navegador.close()


if __name__ == "__main__":
    main()
