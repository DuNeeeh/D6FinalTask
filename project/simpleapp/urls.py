from django.urls import path
from .import views
from .views import NewsList, NewsDetail, NewsSearchList, NewsCreate, NewsUpdate, NewsDelete, subscriptions

urlpatterns = [
    path('news/', views.NewsList.as_view(), name='news'),
    path('news/search/', NewsSearchList.as_view()),
    path('news/<int:pk>', views.NewsDetail.as_view(), name='news_each'),
    path('news/create/', views.NewsCreate.as_view(), name='news_edit'),
    path('news/<int:pk>/edit/', views.NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', views.NewsDelete.as_view(), name='news_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
