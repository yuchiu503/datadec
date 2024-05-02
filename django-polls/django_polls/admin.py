from django.contrib import admin

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # admin后台添加字段
    # fields = ["pub_date", "question_text"]

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline] #让choice选项在Question页面中，方便编辑

    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question,QuestionAdmin)