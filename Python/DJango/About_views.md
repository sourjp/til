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

## 3. django.views.genericの汎用ビューを利用する方法
    ここが詳しくてわかりやすいかも

    https://qiita.com/renjikari/items/af3e8958d2653e6f8d46


    また特徴としてクラスベースのメソッドになる
    https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/


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