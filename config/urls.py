from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from proyecto_final.blog.view import ListBlogPage, DetailBlogPage

urlpatterns = [
    #path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    #path(
    #     "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    # ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    #path("users/", include("proyecto_final.users.urls", namespace="users")),
    #path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("", TemplateView.as_view(template_name="blog/home.html"), name="home"),
    path("aboutus", TemplateView.as_view(template_name="blog/aboutus.html"), name="aboutus"),
    path("pages", ListBlogPage.as_view(), name="pages"),
    path("pages/<int:pk>", DetailBlogPage.as_view(), name="page-detail"),
    path("pages/", include("proyecto_final.blog.urls", namespace="pages")),
    path("accounts/", include("proyecto_final.accounts.urls", namespace="accounts")),
    path("messages/", include("proyecto_final.messages_blog.urls", namespace="messages")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
