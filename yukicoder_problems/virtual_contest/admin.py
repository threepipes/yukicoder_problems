from django.contrib import admin

# Register your models here.
from .models import User, Contest, Submission, Problem

admin.site.register(User)
admin.site.register(Contest)
admin.site.register(Submission)
admin.site.register(Problem)
