[English](Lecture-Steps) · [Dansk](Lecture-Steps-da) · **Bahasa Melayu**

# Langkah pelajaran

Tangkapan skrin setiap langkah dihasilkan oleh larian hujung-ke-hujung (`tests/e2e/README.md`) ke dalam `docs/screenshots/`; ia tidak disimpan dalam repositori.

## Langkah 1 - Lihat laman web secara manual

**Apa yang kita pelajari:** sebelum menulis kod, klik sendiri dan catat elemen
yang perlu disasarkan. Locator yang baik datang daripada mengenali halaman.

## Langkah 2 - Pergi ke halaman log masuk

**Apa yang kita pelajari:** `driver.get`, locator XPath (`locators.py`) dan
menunggu dengan `WebDriverWait` + `element_to_be_clickable` dan bukannya
`sleep` tetap. Ini mengelakkan `NoSuchElementException` pada halaman yang
perlahan.

## Langkah 3 - Tetingkap timbul Facebook

**Apa yang kita pelajari:** log masuk membuka tetingkap pelayar kedua. Kita
bertukar dengan `driver.window_handles` dan `switch_to.window`, mengisi borang,
kemudian kembali. Kelayakan disimpan dalam pemboleh ubah persekitaran, bukan
dalam kod.

## Langkah 4 - Tutup semua permintaan
Lokasi, pemberitahuan, kuki.

**Apa yang kita pelajari:** tetingkap modal menghalang semua yang di
belakangnya. Kita klik ALLOW, NOT INTERESTED dan I ACCEPT, dan langkau yang
tidak muncul (`TimeoutException` dikendalikan dan dilog).

## Langkah 5 - Tekan Like

**Apa yang kita pelajari:** pengecualian sebagai kawalan aliran untuk UI yang
tidak stabil: `NoSuchElementException` bermaksud "masih memuat, tunggu 2 saat
dan cuba lagi"; `ElementClickInterceptedException` bermaksud "tetingkap padanan
menghalang, klik BACK TO TINDER". Jeda antara "like" menjadikan bot kurang
ketara. Gelung berhenti pada had yang ditetapkan.
