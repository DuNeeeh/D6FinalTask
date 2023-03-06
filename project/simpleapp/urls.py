from django.urls import path
from .import views
from .views import NewsList, NewsDetail, NewsSearchList, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('news/', views.NewsList.as_view(), name='news'),
    path('news/search/', NewsSearchList.as_view()),
    path('news/<int:pk>', views.NewsDetail.as_view(), name='news_each'),
    path('news/create/', views.NewsCreate.as_view(), name='news_edit'),
    path('news/<int:pk>/edit/', views.NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', views.NewsDelete.as_view(), name='news_delete'),
]
# urlpatterns = [
#     path('articles/', views.ArticlesList.as_view(), name='articles_list'),
#     path('articles/<int:pk>', views.ArticlesDetail.as_view(), name='articles_detail'),
#     path('articles/create/', views.ArticlesCreate.as_view(), name='articles_create'),
#     path('articles/<int:pk>/edit/', views.ArticlesUpdate.as_view(), name='articles_update'),
#     path('articles/<int:pk>/delete/', views.ArticlesDelete.as_view(), name='articles_delete'),
# ]
