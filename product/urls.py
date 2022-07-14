from django.urls import URLPattern, path
# include 삭제                         
from product import views
# 해당 앱 의 views.py import 해오기

urlpatterns = [
    path('', views.productlist),
    # product의 url을 모두 모아 관리하는 페이지이므로
    # 아무것도 추가하지 않은 ' ' 은
    # http://127.0.0.1:8000/products 인 상태
    # http://127.0.0.1:8000/products 실행 시
    # views의 productlist 함수 실행

    path('first/', views.productfirst)
    # http://127.0.0.1:8000/products/first 실행 시
    # views의 productfirst 함수 실행
    
]

