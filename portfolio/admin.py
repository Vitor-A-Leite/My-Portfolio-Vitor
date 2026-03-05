from django.contrib import admin
from .models import Profile, Education, Experience, Skills, Languages, Projects, SoftSkills

# Register your models here.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(SoftSkills)
admin.site.register(Languages)
admin.site.register(Projects)
