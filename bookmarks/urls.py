
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from bookmarks.views import * 
from bookmarks.feeds import *
from django.contrib.syndication.views import Feed

feeds = dict({
	'recent': RecentBookmarks
	#'user': UserBookmarks
})

urlpatterns =[
	#Browsing
	url(r'^$', views.main_page, name='main_page'),
	url(r'user/(\w+)/$', views.user_page, name='main_page'),
	url(r'^tag/([^\s]+)/$', views.tag_page, name='tag_page'),
	url(r'^tag/$', views.tag_cloud_page, name='tag_cloud_page'),
	url(r'^search/$', views.search_page, name='search'),
	url(r'^popular/$', views.popular_page),
	url(r'^bookmark/(\d+)/$', views.bookmark_page), 

	#Comments
	url(r'^comments/', include('django_comments.urls')),

	#Session Management
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', views.logout_page),
	url(r'^register/$', views.register_page),
	url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),
	url('^', include('django.contrib.auth.urls')),


	#Account Management
	url(r'^save/$', views.bookmark_save_page, name='bookmark_save_page'),
	url(r'^vote/$', views.bookmark_vote_page), 

	#Feeds
	 url(r'^feeds/(?P<url>.*)/$', RecentBookmarks()),

	#Friends
	url(r'^friends/(\w+)/$', views.friends_page),
	url(r'^friend/add/$', views.friend_add),
	url(r'^friend/invite/$', views.friend_invite), 
	url(r'^friend/accept/(\w+)/$', views.friend_accept), 
]