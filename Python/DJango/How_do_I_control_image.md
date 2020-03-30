# Imageについて

Djangoでimageを利用するには Pillow moduleが必要  
mediaを保存する場所をdjangoの設定ファイルに指定してあげる  
またdjangoの画像もurl patternで開く動作になる(adminから見る場合)  
ただ通常ではwebサイトで読み込むので不要。デバッグ用途ぐらい。  
MEDIA_URLはMEDIAを表示するためのURL

```settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

```urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```