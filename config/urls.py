from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

]

urlpatterns += i18n_patterns(
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls', namespace='products')),
    path('shop/', include('shop.urls', namespace='shops')),
    path('blog/', include('blog.urls', namespace='blogs')),
    path('', include('pages.urls', namespace='pages'))
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
