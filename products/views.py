from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Products
from django.utils import timezone
# Create your views here.


def products_list(request):
    return render(request, 'products_list.html',)


@login_required
def publish(request):
    if request.method == "GET":
        return render(request, 'publish.html')
    elif request.method == "POST":
        app_title = request.POST["标题"]
        app_intro = request.POST["介绍"]
        app_url = request.POST["APP链接"]
        try:
            app_icon = request.FILES["APP图标"]
            app_image = request.FILES["大图"]

            product = Products()
            product.app_title = app_title
            product.app_intro = app_intro
            product.app_url = app_url
            product.app_icon = app_icon
            product.app_image = app_image

            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()

            return redirect('product list page')

        except Exception as err:
            return render(request, 'publish.html', {'错误': '请上传图片!'})

