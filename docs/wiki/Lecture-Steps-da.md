[English](Lecture-Steps) · **Dansk** · [Bahasa Melayu](Lecture-Steps-ms)

# Lektionens trin

Skærmbillederne af hvert trin laves af end-to-end-kørslen (`tests/e2e/README.md`) i `docs/screenshots/`; de ligger ikke i repositoriet.

## Trin 1 - Se siden igennem manuelt

**Det lærte vi:** klik først selv igennem og notér, hvilke elementer koden skal
ramme. Gode locators kommer af at kende siden.

## Trin 2 - Gå til login-siden

**Det lærte vi:** `driver.get`, XPath-locators (`locators.py`) og at vente med
`WebDriverWait` + `element_to_be_clickable` i stedet for faste `sleep`. Det
undgår `NoSuchElementException` på langsomme sider.

## Trin 3 - Facebook-popup

**Det lærte vi:** login åbner et ekstra browservindue. Vi skifter med
`driver.window_handles` og `switch_to.window`, udfylder formularen og skifter
tilbage. Loginoplysninger ligger i miljøvariabler, aldrig i koden.

## Trin 4 - Luk alle forespørgsler
Lokation, notifikationer, cookies.

**Det lærte vi:** modale popups blokerer alt bagved. Vi klikker ALLOW, NOT
INTERESTED og I ACCEPT og springer en popup over, hvis den ikke dukker op
(`TimeoutException` håndteres og logges).

## Trin 5 - Tryk Like

**Det lærte vi:** undtagelser som styring af en ustabil brugerflade:
`NoSuchElementException` betyder "indlæser stadig, vent 2 sek. og prøv igen";
`ElementClickInterceptedException` betyder "en match-popup er i vejen, klik
BACK TO TINDER". En pause mellem likes gør, at botten ikke ligner en bot.
Løkken stopper ved den indstillede grænse.
