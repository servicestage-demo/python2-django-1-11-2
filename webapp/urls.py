"""webapp URL Configuration

The `urlpatterns` list routes URLs to templates. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function templates
    1. Add an import:  from my_app import templates
    2. Add a URL to urlpatterns:  path('', templates.home, name='home')
Class-based templates
    1. Add an import:  from other_app.templates import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import helloworld
from django.views.static import serve

url(r'^static/(?P<path>.*)$', serve, {'document_root': '/static/images'}),

urlpatterns = [
    url(r'^$', helloworld.hello),
]



handler404 = helloworld.page_not_found
handler500 = helloworld.server_error




# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
