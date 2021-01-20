from django.contrib import admin
from home.models import Contact , ContactModel ,ArticleModel

# Register your models here.

admin.site.register(ContactModel)
admin.site.register(Contact)
admin.site.register(ArticleModel)
