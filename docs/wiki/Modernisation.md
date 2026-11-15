**English** · [Dansk](Modernisation-da) · [Bahasa Melayu](Modernisation-ms)

# Modernisation compared with the earlier solution

- `src/` package with one function per step instead of one class with `sleep`.
- Explicit waits instead of fixed sleeps; locators in one module.
- Facebook login (as the lecture asks) instead of Google; settings via a
  `Settings` dataclass; unit tests with a fake driver.
- No `from constants import *`, no HTML dumps, no profile path with `os.getcwd`.
