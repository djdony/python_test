from django.contrib import admin
from .models import Poll, Question, Answer
import nested_admin


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1


class PollAdmin(nested_admin.NestedModelAdmin):
    list_display = ['id', 'title', 'date_start', 'date_end']
    list_display_links = ['id', 'title']
    search_fields = ('title',)
    inlines = [QuestionInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date_start']
        else:
            return []


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Poll, PollAdmin)
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Answer, AnswerAdmin)