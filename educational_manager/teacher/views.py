from django.shortcuts import render, redirect
from .models import Standard, KnowShowChart
from django.http import JsonResponse
import json


# Create your views here.
def home(request):
    standard_list = Standard.objects.all()
    context = {
        "standard_list": standard_list,
    }
    return render(request, 'teacher/home.html', context)


def knowShowChart(request):
    standardCodes = Standard.objects.all()

    context = {'standardCodes': standardCodes}
    return render(request, 'teacher/knowShowChart.html', context)


def getStandards(request):
    standard_list = list(Standard.objects.values())
    return JsonResponse({"standard_list": standard_list})


def saveKnowShowChart(request):
    know_list = [request.POST[key] for key in request.POST if 'know' in key and request.POST[key] != '']
    show_list = [request.POST[key] for key in request.POST if 'show' in key and request.POST[key] != '']
    scaffold_list = [request.POST[key] for key in request.POST if 'scaffold' in key and request.POST[key] != '']
    standard = Standard.objects.get(code=request.POST['standardsDropDown'])
    if request.method == 'POST':
        content = json.dumps({
            'know': know_list,
            'show': show_list,
            'scaffold': scaffold_list,
        })
        chart = KnowShowChart(content=content, standard=standard, creator=request.user)
        chart.save()
    return redirect('teacher:knowShowChart')


def assessmentDeveloper(request, pk):
    know_show_chart = KnowShowChart.objects.get(id=pk)
    know_show_dict = json.loads(know_show_chart.content)
    knows = know_show_dict['know']
    shows = know_show_dict['show']
    context = {
        'knows': knows,
        'shows': shows,
    }
    return render(request, 'teacher/assessmentDeveloper.html', context)


def saveQuestion(request, pk):
    print(request.POST)
    return redirect('teacher:assessmentDeveloper', pk)
