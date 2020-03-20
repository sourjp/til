# あ




# ログインセッションについて

user-social-oauthの時はbackendsにてuserのログイン管理を行なっている
UserFormのcurrent_userと同じ考え方。


```ログインしていない状態
{'associated': [], 'not_associated': ['twitter'], 'backends': ['twitter']} 
```

```ログインした状態
{'associated': <QuerySet [<UserSocialAuth: sourjp>]>, 'not_associated': [], 'backends': ['twitter']}
```

次のように書くことで認証時の違いが作れる。
ログアウト処理で消えるので、多分クッキーのsession idを見ているはず。

```参考例
{% if not backends.associated %}
    <a href="{% url 'user_auth:top'  %}">Login</a>
{% else %}
    <a href="{% url 'user_auth:logout' %}">Logout</a>
{% endif %}
```

