from django.contrib import admin
from .models import Post, UserImage
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

class UserImageAdmin(admin.ModelAdmin):
    list_display = ["user", "foto",]
    class Meta:
        model = UserImage
admin.site.register(Post, PostAdmin)
admin.site.register(UserImage, UserImageAdmin)