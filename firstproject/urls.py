from django.contrib import admin
from django.urls import path, include

import app_blog.views
import app_portfolio.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', app_blog.views.home, name='home'),


   path('blog/', include('app_blog.urls') ),
   path('portfolio/', include('app_portfolio.urls') ),
   path('account/', include('app_signup.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
