# Maxway

Maxway - fast food online dastavka platformasi uchun backend-markazli Python loyiha.
Loyiha tashqi paketlarsiz ishlaydi: HTTP server, REST API va SQLite bazasi Python standart kutubxonasi bilan yozilgan.

## PyCharm orqali ishga tushirish

1. PyCharm oching.
2. `File -> Open` orqali shu papkani tanlang:
   `C:\Users\User\Documents\Codex\2026-05-13\menga-web-sayt-loyiha-yaratib-ber`
3. Python interpreter sifatida Python 3.13 ni tanlang.
4. Yuqoridagi run konfiguratsiyadan `Run Maxway Backend` ni tanlab ishga tushiring.
5. Brauzerda `http://127.0.0.1:8000` manzilini oching.

Terminal orqali ham ishlatish mumkin:

```powershell
python -m app.main
```

## Tuzilma

```text
app/
  database.py      SQLite sxema va boshlang'ich menyu
  repository.py    mahsulot, buyurtma va admin logikasi
  server.py        REST API va statik frontend serveri
  main.py          loyiha entry point
static/
  index.html       Maxway buyurtma interfeysi
  styles.css       responsive dizayn
  app.js           frontend va API integratsiyasi
  assets/          lokal PNG mahsulot rasmlari
docs/
  API.md           endpointlar xaritasi
tests/
  test_repository.py
```

## Test

```powershell
python -m unittest discover -s tests
```

## Muhim API endpointlar

- `GET /api/health`
- `GET /api/categories`
- `GET /api/products`
- `POST /api/orders`
- `GET /api/admin/orders`
- `PATCH /api/admin/orders/{id}/status`

SQLite fayl birinchi ishga tushishda `data/maxway.sqlite3` ichida yaratiladi.
