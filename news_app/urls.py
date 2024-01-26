from django.urls import path
from .views import (news_list, news_detail, homePageView, ContactpageView,
                    page404view, aboutUs, HomePageVIew,
                    LocalNewsVIew, XorijNewsVIew, TechnologyNewsVIew, SportNewsVIew)

urlpatterns = [
    path('about_us', aboutUs, name = 'about_us_page'),
    path('page404', page404view, name = '404_page'),
    path('', HomePageVIew.as_view(), name= 'home_page'),
    path('contact-us/', ContactpageView.as_view(), name = 'contact_page'),
    path('news/', news_list, name='all_news_list'),
    path("news/<slug:news>/", news_detail, name = 'news_detail_page'),
    path('local_news/', LocalNewsVIew.as_view(), name='local_news_page'),
    path('xorij_news/', XorijNewsVIew.as_view(), name = 'xorij_news_page'),
    path('tex_news/', TechnologyNewsVIew.as_view(), name = 'tex_news_page'),
    path('sport/', SportNewsVIew.as_view(), name = 'sport_news_page'),

]