from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import change_language
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns 
import notifications.urls

urlpatterns = [
    path('change_language/', 
         change_language, 
         name='change_language'),
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('accounts/'), include('accounts.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('', include('core.urls')),
    path(_('deposit'), include('deposit.urls')),
    path('withdraw', include('withdraw.urls')),
    path('timeline/', include('userprofile.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('msg/', include('message.urls')),
    path('admins/', include('admin.common.urls')),
    prefix_default_language=False
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
