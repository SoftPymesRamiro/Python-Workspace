from django.contrib import admin
from polls.models import Choice, Poll
#from polls.models import Choice

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date','question']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',                {'fields': ['question']}),
        ('Date information',        {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question','pub_date','was_published_recently') #Pone un titulos a las columnas
    list_filter = ['pub_date']      #Pone filtro de fechas
    search_fields = ['question']    #Pone un campo de busqueda

# Register your models here.
#admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)
 
