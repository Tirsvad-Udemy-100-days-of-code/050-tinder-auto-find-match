[English](Modernisation) · [Dansk](Modernisation-da) · **Bahasa Melayu**

# Pemodenan berbanding penyelesaian terdahulu

- Pakej `src/` dengan satu fungsi bagi setiap langkah dan bukannya satu kelas
  dengan `sleep`.
- Penantian eksplisit; semua locator di satu tempat.
- Log masuk Facebook (seperti pelajaran) dan bukannya Google; tetapan dalam
  dataclass `Settings`; ujian unit dengan pemacu palsu.
- Tiada `from constants import *`, tiada longgokan HTML.
