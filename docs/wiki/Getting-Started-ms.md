[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

# Bermula

## Keperluan

Python 3.11 atau lebih baharu dan Google Chrome (Selenium Manager memuat turun pemacu yang sepadan sendiri). Satu-satunya kebergantungan semasa larian ialah `selenium`; semakan menggunakan `pytest` dan `ruff`. Docker hanya diperlukan untuk larian hujung-ke-hujung yang pilihan.

## Persediaan

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/050-tinder-auto-find-match.git
cd 050-tinder-auto-find-match
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; Linux/macOS: .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

## Jalankan

```bash
python -m tinder_bot
```

Ini membuka laman dalam Chrome, log masuk melalui tetingkap timbul Facebook, menutup tetingkap timbul lokasi, pemberitahuan dan kuki, dan menyukai profil, paling banyak `MAX_LIKES` (20 secara lalai). Ia memerlukan sambungan internet dan tetapan dalam persekitaran (`FACEBOOK_EMAIL`, `FACEBOOK_PASSWORD`; fail `.env.example` menyenaraikannya). Gunakan hanya dengan laman latihan kursus TinDog dan akaun ujian, jangan sekali-kali dengan akaun sebenar.

## Penggunaan yang bertanggungjawab

Mengautomasikan perkhidmatan pihak ketiga boleh melanggar syarat penggunaannya, dan profil yang disukai oleh bot adalah milik orang lain. Program ini ditulis untuk laman latihan kursus TinDog. Jujurlah dengan orang yang anda temui: beritahu mereka bahawa anda mengautomasikan swipe anda, dan patuhi had harian (TinDog 20, Tinder percuma 100). Jangan sekali-kali meletakkan kelayakan sebenar dalam repositori.

## Ujian

```bash
python -m pytest
```

Ujian unit dalam `tests/unit/` menggunakan pemacu palsu, jadi ia tidak membuka pelayar dan tidak menghubungi mana-mana laman.

## Lesen

Kod ini dilesenkan di bawah GNU Affero General Public License v3.0 only (AGPL-3.0-only). Lihat fail `LICENSE`.
