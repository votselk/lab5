from articles.models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def create_post(request):
    form = {
        'text': request.POST.get("text",""), 'title': request.POST.get("title","")
    }
            # в словаре form будет храниться информация, введенная пользователем
    if form["text"] and form["title"]:
        # если поля заполнены без ошибок
        n = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
        n.save()
        return redirect('get_article', article_id=n.id)
        # перейти на страницу поста
    else:
    # если введенные данные некорректны
        form['errors'] = u"Не все поля заполнены"
        return render(request, 'create_post.html', {'form': form})

