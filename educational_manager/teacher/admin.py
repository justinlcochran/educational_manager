from django.contrib import admin
from .models import Standard, KnowShowChart, Question, Answer, ScopeAndSequence, Assessment

# Register your models here.
admin.site.register(Standard)
admin.site.register(KnowShowChart)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ScopeAndSequence)
admin.site.register(Assessment)
