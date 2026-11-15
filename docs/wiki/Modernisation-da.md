[English](Modernisation) · **Dansk** · [Bahasa Melayu](Modernisation-ms)

# Modernisering ift. den tidligere løsning

- `src/`-pakke med én funktion pr. trin i stedet for én klasse med `sleep`.
- Eksplicitte ventetider i stedet for faste; alle locators ét sted.
- Facebook-login (som lektionen beder om) i stedet for Google; indstillinger i
  en `Settings`-dataclass; enhedstests med en falsk driver.
- Ingen `from constants import *`, ingen HTML-dumps.
