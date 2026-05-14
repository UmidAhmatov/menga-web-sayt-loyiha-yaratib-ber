# Maxway

Maxway - fast food online dastavka platformasi uchun backend-markazli Python loyiha.
Loyihaga Django backend va Docker qo'shildi. Frontend bir xil qoladi, API esa Django modellari va SQLite bazasi orqali ishlaydi.

## Docker bilan ishga tushirish

Docker eng oson yo'l:

```powershell
docker compose up --build
```

Keyin brauzerda oching:

```text
http://127.0.0.1:8000
```

Django admin:

```text
http://127.0.0.1:8000/admin/
```

Local demo admin Docker orqali avtomatik yaratiladi:

```text
login: admin
parol: admin12345
```

## PyCharm orqali Django ishga tushirish

1. PyCharm oching.
2. `File -> Open` orqali shu papkani tanlang:
   `C:\Users\User\Documents\Codex\2026-05-13\menga-web-sayt-loyiha-yaratib-ber`
3. Python interpreter sifatida Python 3.13 ni tanlang.
4. Terminalda dependency o'rnating:

```powershell
pip install -r requirements.txt
```

5. Django bazasini tayyorlang:

```powershell
python django_app/manage.py migrate
python django_app/manage.py seed_maxway
```

6. Run konfiguratsiyadan `Run Maxway Django` ni tanlang yoki terminaldan ishga tushiring:

```powershell
python django_app/manage.py runserver 127.0.0.1:8000
```

## Tuzilma

```text
django_app/
  manage.py
  maxway/          Django settings va URLs
  orders/          Django models, views, services, admin, seed command
app/
  ...              eski dependency-free backend varianti
static/
  index.html       Maxway buyurtma interfeysi
  styles.css       responsive dizayn
  app.js           frontend va API integratsiyasi
  assets/          lokal PNG mahsulot rasmlari
Dockerfile
docker-compose.yml
docs/
  API.md           endpointlar xaritasi
```

## Test

```powershell
python django_app/manage.py test orders
python -m unittest discover -s tests
```

## Muhim API endpointlar

- `GET /api/health`
- `GET /api/categories`
- `GET /api/products`
- `POST /api/orders`
- `GET /api/admin/orders`
- `PATCH /api/admin/orders/{id}/status`

Django SQLite fayl Docker ichida `/app/data/maxway_django.sqlite3`, lokalda esa `data/maxway_django.sqlite3` ichida yaratiladi.
