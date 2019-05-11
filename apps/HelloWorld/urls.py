from django.conf.urls import url
from django.views.generic.base import RedirectView #重定向到给定的URL
#from django.contrib import admin

#0、复制文件夹改名
#1、这里加上
#2、py文件复制替换
#3、html文件复制替换

from . import chinese_jiangfei, chinese_jinzu, chinese_yesir, chinese_xiaoen

#pattern模范，典范，模型，模式
urlpatterns = [
    url(r'^favicon.ico',RedirectView.as_view(url=r'/static/favicon.ico')),

    url(r'^jiangfei$', chinese_jiangfei.jiangfei),
    url(r'^accept_cmd_jiangfei', chinese_jiangfei.accept_cmd_jiangfei),

    url(r'^jinzu$', chinese_jinzu.jinzu),
    url(r'^accept_cmd_jinzu', chinese_jinzu.accept_cmd_jinzu),

    url(r'^yesir$', chinese_yesir.yesir),
    url(r'^accept_cmd_yesir', chinese_yesir.accept_cmd_yesir),

    url(r'^xiaoen$', chinese_xiaoen.xiaoen),
    url(r'^accept_cmd_xiaoen', chinese_xiaoen.accept_cmd_xiaoen),

]
