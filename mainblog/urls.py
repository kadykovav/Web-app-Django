from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('blog/filter/', views.FilterPost.as_view(),name='filter'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post'),
    path('blog/<slug:slug>/update', views.PostUpdate.as_view(), name='update'),  # endpoint
    path('blog/create-post', views.PostCreate.as_view(), name='create'),
    path('blog/<slug:slug>/delete', views.PostDelete.as_view(), name='delete'),  # endpoint
    path('faq/', views.FaqPage.as_view(), name='faq'),
]
