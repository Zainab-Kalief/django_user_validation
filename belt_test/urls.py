from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_app.urls', namespace='users')),
    url(r'^books/', include('apps.book_app.urls', namespace='books')),
]
