from django.shortcuts import render

# Create your views here.


def products_list(request):
    return render(request, 'products_list.html',)

def publish(request):
    if request.method == "GET":
        return render(request, 'publish.html')
    elif request.method == "POST":
        app_name = request.POST["APP名称"]
        app_intro = request.POST["介绍"]
        app_url = request.POST["APP链接"]
        app_icon = request.FILES["APP图标"]
        app_image = request.FILES["大图"]
        return render(request, 'publish.html')