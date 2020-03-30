# Templateの渡し方
## 1. loader()を利用してHttpResponceで返す方法

```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

## 2. render()を利用する方法

```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

リクエストオブジェクトには様々なデータが含まれる  
・method: GET, POSTなど (e.g. request.method)
・POST: request.POST['username']など。これはformのnameで与えたデータが合致する

renderは該当funcが実行されて、取得したデータを指定した.htmlファイルに乗せてレスポンスする。  
一方でrequestの場合はnamespaceを指定して、そのさきのファンクを読み出して実行する。  

つまりrenderでのurlはそのfuncが指定された時のviewsに依存するし、requestの場合は指定したviewsのurlに依存する

なのでlogoutの場合はredirectでloginに返すほうがスッキリする


## 3. django.views.genericの汎用ビューを利用する方法
ここが詳しくてわかりやすいかも

https://qiita.com/renjikari/items/af3e8958d2653e6f8d46


また特徴としてクラスベースのメソッドになる
https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/

`DB`と連動させてページを表示させるために使う。という考えかがた中心にある。  
つまりDBが絡まないならrenderもあり。  
classViewを使うならTemplateViewが該当する  

例えばGET methodを撮りたい場合は、
    request.method == 'GET'

しかし、djangoでは次のようにとる
    def get(self, request)

またclass内にtemplate_nameを指定しなかった場合は、path url + 汎用view名になる  
例えば、publishers/でlistのviewを使っていると、publishers_list.htmlになる。

またmodelから取得したデータはobject_xxxという名前でtemplateに渡される  
https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/

これを変えたければcontext_object_nameで名前を指定すると良い

またcontextが一つのモデルだけで足りない場合は、
def get_context_data によって追加すれば良い

・CRUDに当てはまるClassView
- Create
CreateView

- Read
ListView, DetailView

- Update
UpdateView

- Delete
DeleteView


＊ListView  
次のように渡すことで`objects_list`として Jinja2に渡すことができる

```ListViews.py
from django.views.generic import ListView
from .models import TestMoedel

class TestList(ListView):
    template_name = 'test.html'
    model = TestModel
```

*DetailView    
object pk(primary key) or slugを指定して詳細を表示させるclass  

viewsに<int:pk>で渡してあげる  
つまりviwsでpkを指定してdetailviewを開くと、次の例ならTestModelの指定したpkのdataを`object`としてDetailViewに渡せる  

```DetailViews.py
from django.views.generic import DetailView
from .models import TestMoedel

class TestDetail(DetailView):
    template_name = 'test.html'
    model = TestModel
```

funcviewsであれば引数にpkもとってあげれば良い  
これはlist viewからpkと合わせてdetailfuncをよんであげるイメージ
```FuncViews.py
def detail(request, pk):
    object = TestModel.objects.get(pk=pk)
    return render(request, 'test.html', {'object': object})
```

*CreateView

Fieldは指定したmodelのfiledを指定する  
formを入力した後のredirect先はreverse_lazyを使用する  
これはfunction viewの場合はreverseを使用する  
classの中ではreverse_lazyを使う  
ちなみに指定しているものはurlsのnamespaceである  

```CreateViews.py
from django.urls import reverse_lazy
from django.views.generic import CreteView
from .models import TestMoedel

class TestCreate(CreateView):
    template_name = 'test.html'
    model = TestModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')
```

*DeleteView  
DetailViewと同じで<int:pk>を利用してDBを指定する

```DeleteView.py
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import TestMoedel

class TestDelete(DeleteView):
    template_name = 'test.html'
    model = TestModel
    success_url = reverse_lazy('list')
```

*UpdateView  
こちらも同様に<int:pk>が必要  
ここで指定したfieldsはjinja2側では{{ form.as_p }}で出力される  
    -> 要はform fieldを`<p>`タグで囲ってずらずら出すってこと  
個別で出力する場合は{{ form.title }}, {{ form.model }}など。  

```UpdateView.py
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import TestMoedel

class TestUpdate(UpdateView):
    template_name = 'test.html'
    model = TestModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')
```