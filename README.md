# SGE-TRASU

Sistema de gestión del flujo interno y seguimiento de expedientes de segunda instancia del TRASU (alternativa ALT-06-R).

Proyecto del curso **SI707U — Ingeniería de Software**, Facultad de Ingeniería Industrial y de Sistemas, Universidad Nacional de Ingeniería. Grupo 7, 2026-2.

> Proyecto académico. No es un sistema oficial de OSIPTEL ni cuenta con patrocinio institucional. Los nombres, expedientes y códigos que aparecen en los mockups son ficticios.

## Alcance

El sistema apoya la coordinación del trabajo interno sobre cada expediente: responsables, asignaciones y reasignaciones, versiones documentales, revisiones, observaciones, subsanaciones, plazos, alertas y auditoría.

No automatiza la decisión jurídica ni reemplaza a SISTRAM, SISDOC o SGD. Firma, numeración, notificación y archivo quedan fuera de su frontera.

## Estructura

```
docs/
└── mockups/        Prototipos de interfaz en HTML/CSS y sus capturas PNG
```

## Mockups

| Pantalla | Fuente | Captura |
|---|---|---|
| 6.1 Situación temporal del expediente | [HTML](docs/mockups/6.1-situacion-temporal.html) | [PNG](docs/mockups/6.1-situacion-temporal.png) |
| 6.1b Situación temporal — cómputo no validado | [HTML](docs/mockups/6.1-situacion-temporal.html) (`#no-validado`) | [PNG](docs/mockups/6.1b-situacion-temporal-no-validado.png) |
| 6.2 Constancia de salida e intercambio externo | [HTML](docs/mockups/6.2-constancia-salida.html) | [PNG](docs/mockups/6.2-constancia-salida.png) |

Para verlos basta abrir el HTML en un navegador. Para regenerar las capturas después de modificar un mockup:

```bash
pip install playwright
python docs/mockups/capturar.py
```

El script usa Google Chrome instalado; con `--chromium` usa el navegador de Playwright (`playwright install chromium`).

## Tecnologías previstas

Java 17 con Spring Boot 3, Spring Data JPA y Spring Security en el backend; HTML, CSS y JavaScript en el frontend; PostgreSQL como base de datos.
