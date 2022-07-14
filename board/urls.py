
from django.urls import URLPattern, path
# include 삭제                         
from board import views
# 해당 앱(board) 의 views.py import 해오기

urlpatterns = [
    path('', views.board),
    # board의 url을 모두 모아 관리하는 페이지이므로
    # 아무것도 추가하지 않은 ' ' 은
    # http://127.0.0.1:8000/boards 인 상태
    # http://127.0.0.1:8000/boards 실행 시
    # views의 board 함수 실행

    path('first/', views.boardfirst)
    # http://127.0.0.1:8000/boards/first 실행 시
    # views의 boardfirst 함수 실행
]

