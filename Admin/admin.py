from django.contrib import admin

# Register your models here.
from Admin.models import Human , Pet


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    # exclude = ('age',)
    search_fields = ('name' ,)
    list_filter = ('name' ,)
    list_per_page = 5

    def parse_sex(self):
        if self.sex:
            return '男'
        else:
            return '女'

    parse_sex.short_description = '性别'
    list_display = ('name' , 'age' , parse_sex)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
