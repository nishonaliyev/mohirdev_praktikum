from django.urls import path
from .views import (news_list, news_detail, homePageView, ContactpageView, NewsCreateView, page404view, aboutUs, HomePageVIew, NewsUpdateView, NewsDeleteView, LocalNewsVIew, XorijNewsVIew, TechnologyNewsVIew, SportNewsVIew)

urlpatterns = [
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('about_us', aboutUs, name = 'about_us_page'),
    path('page404', page404view, name = '404_page'),
    path('', HomePageVIew.as_view(), name= 'home_page'),
    path('contact-us/', ContactpageView.as_view(), name = 'contact_page'),
    path('news/', news_list, name='all_news_list'),
    path("news/<slug:news>/", news_detail, name = 'news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('local_news/', LocalNewsVIew.as_view(), name='local_news_page'),
    path('xorij_news/', XorijNewsVIew.as_view(), name = 'xorij_news_page'),
    path('tex_news/', TechnologyNewsVIew.as_view(), name = 'tex_news_page'),
    path('sport/', SportNewsVIew.as_view(), name = 'sport_news_page'),

]