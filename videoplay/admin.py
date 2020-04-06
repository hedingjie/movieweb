from django.contrib import admin

# Register your models here.
from videoplay.models import Movie, User, UserComment, MoviePay

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(UserComment)
admin.site.register(MoviePay)