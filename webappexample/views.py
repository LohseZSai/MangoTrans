import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.http import HttpResponse
oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("profile")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def generic(request):
    # 直接渲染页面，不检查用户登录状态
    return render(request, 'generic.html')

def image_translator(request):
    if request.method == 'POST':
        # 这里可以添加处理上传的图片和翻译的逻辑
        # 返回翻译后的图片或链接
        return HttpResponse("Image translated successfully!")
    return render(request, 'image_translation.html')

def pdf_translator(request):
    if request.method == 'POST':
        # 这里可以添加处理上传的PDF和翻译的逻辑
        # 返回翻译后的PDF或链接
        return HttpResponse("PDF translated successfully!")
    return render(request, 'pdf_translation.html')

def contact(request):
    # 这里可以处理从联系表单收到的POST请求
    if request.method == 'POST':
        render(request, 'contact.html')
    return render(request, 'contact.html')


    
    
def profile(request):
    # 检查用户是否已认证
    if not request.session.get('user'):
        # 用户未登录，重定向到登录页面，并传递当前页面路径作为 next 参数
        return redirect(f"{reverse('login')}?next={request.path}")
    
    # 如果用户已认证，渲染个人中心页面
    return render(request, 'profile.html', {
        "session": request.session.get("user"),
        "pretty": json.dumps(request.session.get("user"), indent=4),
    })   
    
    
    