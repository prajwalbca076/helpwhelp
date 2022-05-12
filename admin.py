from django.contrib import admin
from .models import User
from .models import Whelp
from .models import Post

admin.site.register(User)
admin.site.register(Whelp)
admin.site.register(Post)
