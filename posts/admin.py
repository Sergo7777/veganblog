from django.contrib import admin
from .models import Post, UserImage, CategoryPost, Message
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    class Meta:
        model = CategoryPost

class UserImageAdmin(admin.ModelAdmin):
    list_display = ["user", "foto",]
    class Meta:
        model = UserImage

class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "content"]
    class Meta:
        model = Message

admin.site.register(CategoryPost, CategoryPostAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(UserImage, UserImageAdmin)