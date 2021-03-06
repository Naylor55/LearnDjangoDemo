"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Article
from app.models import Category
from django.views.generic import ListView


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

def List(request):
    assert isinstance(request,HttpRequest)
    data = Article.objects.filter(status='p'),
    return render(request,
        'app/List.html',
        {
            'title':'List',
            'message':'This is the  list  page.',
            'data':data,
            'year':datetime.now().year,
        })




class IndexView(ListView):
    """
    首页视图,继承自ListVIew，用于展示从数据库中获取的文章列表
    """

    template_name = "app/blog.html"
    # template_name属性用于指定使用哪个模板进行渲染

    context_object_name = "article_list"
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）

    def get_queryset(self):
        """
        过滤数据，获取所有已发布文章，并且将内容转成markdown形式
        """
        article_list = Article.objects.filter(status='p')
        # 获取数据库中的所有已发布的文章，即filter(过滤)状态为'p'(已发布)的文章。
        for article in article_list:
            article.body = str(article.body,)
            # 将markdown标记的文本转为html文本
        
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)