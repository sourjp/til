# settings.py

STATIC_URL はstaticファイルを表示する時のURL
STATIC_ROOTはstatic fileを探すきのroot directory

```settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

個別で指定したい場合は次の方法もある
```settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

cssファイルをURLで表示したい場合は次のようにurlを定義してあげる

```urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
```

またJINJA2では {% load static %} でstaticファイルを読み込む必要がある