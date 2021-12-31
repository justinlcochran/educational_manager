from django.shortcuts import render, redirect
from .models import Standard, KnowShowChart, Assessment, Question, Answer
from django.apps import apps
from django.http import JsonResponse
import json


User = apps.get_model('users', 'User')
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


def assessmentDeveloper(request, pk, assessment_id):
    know_show_chart = KnowShowChart.objects.get(id=pk)
    assessment = Assessment.objects.get(id=assessment_id)
    content = json.loads(know_show_chart.content)
    know_requirement = content['know']
    show_requirement = content['show']

    know_satisfied = []
    show_satisfied = []
    questions_list = assessment.get_questions()
    for question in questions_list:
        k_sat = json.loads(question.satisfied)['know']
        s_sat = json.loads(question.satisfied)['show']
        for i in k_sat:
            know_satisfied.append(i)
        for i in s_sat:
            show_satisfied.append(i)
    know_remaining = [x for x in know_requirement if x not in know_satisfied]
    show_remaining = [x for x in show_requirement if x not in show_satisfied]
    if know_remaining or show_remaining:
        question_number = len(questions_list) + 1

        context = {
            'knowSatisfied': know_satisfied,
            'showSatisfied': show_satisfied,
            'knowRemaining': know_remaining,
            'showRemaining': show_remaining,
            'questionNumber': question_number,
            'ksid': pk,
            'aid': assessment_id,
        }
        return render(request, 'teacher/assessmentDeveloper.html', context)

    else:
        return redirect('teacher:teacherHome')


def saveQuestion(request, pk, assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    know_show_chart = KnowShowChart.objects.get(id=pk)
    content = json.loads(know_show_chart.content)
    know_requirement = content['know']
    show_requirement = content['show']
    know_satisfied = []
    show_satisfied = []
    queryDict = dict(request.POST)
    for key in queryDict:
        if queryDict[key] == ['on']:
            if key in know_requirement:
                know_satisfied.append(key)
            elif key in show_requirement:
                show_satisfied.append(key)
    satisfied_json = json.dumps({'know': know_satisfied, 'show': show_satisfied})
    new_question = Question(text=request.POST['question-text'], assessment=assessment, satisfied=satisfied_json)
    new_question.save()
    for key in queryDict:
        if 'answer' in key:
            if key == f'{queryDict["correct"][0]}-text':
                new_answer = Answer(text=request.POST[key], question=new_question, correct=True)
                new_answer.save()
            elif key != f'{queryDict["correct"][0]}-text':
                new_answer = Answer(text=request.POST[key], question=new_question, correct=False)
                new_answer.save()

    return redirect('teacher:assessmentDeveloper', pk, assessment_id)


def createAssessment(request, pk):
    know_show_chart = KnowShowChart.objects.get(id=pk)
    list_of_assessments = know_show_chart.get_assessments()
    new_assessment = Assessment(know_show_chart=know_show_chart,
                                title=f"ksid{know_show_chart.id}:{know_show_chart.standard.code} {len(list_of_assessments) + 1}")
    new_assessment.save()
    assessment_id = new_assessment.id
    return redirect('teacher:assessmentDeveloper', pk, assessment_id)

def create(request):
    return render(request, 'teacher/create.html')


def knowShowSelector(request):
    standard_codes = Standard.objects.all()
    context = {
        'standardCodes': standard_codes,
    }
    return render(request, 'teacher/knowShowSelector.html', context)


def getKnowShow(request, code):
    charts_query = list(KnowShowChart.objects.filter(standard=code).values())
    for know_show in charts_query:
        know_show['creator'] = f"{User.objects.get(id=know_show['creator_id']).first_name} {User.objects.get(id=know_show['creator_id']).last_name}"
    print(charts_query)
    return JsonResponse({'charts_query': charts_query})
