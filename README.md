# webhook

ntfy.sh uzerinden telefona bildirim gonderen basit webhook ornekleri.

## Kurulum

```
pip install requests
```

## Dosyalar

- `notify.py` - ntfy.sh'a POST atan gonderici fonksiyon
- `receiver.py` - standart kutuphane (`http.server`) ile webhook alici
- `scraper_example.py` - notify()'in gercek bir scriptte nasil kullanilacagini gosteren ornek

## Kullanim

```
python notify.py
```

Telefonda ntfy uygulamasi acik ve ilgili topic'e abone olunca bildirim gelir.
