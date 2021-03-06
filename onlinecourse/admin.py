from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminFormSet
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question.course.through
    extra = 5
class ChoiceInline(admin.TabularInline):
    model = Choice.question.through
    extra = 5  
class QuestionAdmin(admin.ModelAdmin)    :
    Inline =[ChoiceInline]
    list_display = ('question_text','grade')
    extra=5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline,QuestionInline]
    #inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
  
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']  


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin) 
