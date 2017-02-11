from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
import logging

# Create your views here.
from .models import Problem, User, Submission, Contest


def index(request):
    contest_list = Contest.objects.all()
    context = {
        'contest_list': contest_list,
    }
    return render(request, 'virtual_contest/index.html', context)


def create_contest(request):
    if request.method == 'POST':
        contest_set = Contest.objects
        contest_id = len(contest_set.all()) + 1
        try:
            problems = request.POST.getlist('problem[]')
            users = request.POST.getlist('user[]')
            title = request.POST['title'] # need set name to html
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
        except (KeyError):
            return render(request, 'virtual_contest/create_contest.html', {
                'error_message': '必須項目の入力が不足しています'
            })
        else:
            new_contest = Contest(
                start_time=start_time,
                end_time=end_time,
                name=title
            )
            new_contest.save()
            prob_dict = get_prob_dict()
            user_dict = get_user_dict()
            for prob in problems:
                new_contest.problems.add(prob_dict[int(prob)])
            for user in users:
                new_contest.users.add(user_dict[int(user)])
            new_contest.save()
            return HttpResponseRedirect(reverse('virtual_contest:contest', args=(contest_id,)))
    else:
        return render(request, 'virtual_contest/create_contest.html')


def contest(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    return render(request, 'virtual_contest/contest.html', {'contest': contest})


def login(request):
    return HttpResponse("login")


def user_page(request, user_id):
    user_id = int(user_id)
    return HttpResponse("user %d" % user_id)


def get_prob_dict():
    dic = {}
    for prob in Problem.objects.all():
        dic[prob.problem_id] = prob
    return dic


def get_user_dict():
    dic = {}
    for user in User.objects.all():
        dic[user.user_id] = user
    return dic


def get_prob_from_id(prob_id):
    if not prob_id.isdigit():
        return None
    prob_id = int(prob_id)
    problems = Problem.objects.all()
    for prob in problems:
        if prob.problem_id == prob_id:
            return prob
    return None


def get_user_from_id(user_id):
    if not user_id.isdigit():
        return None
    user_id = int(user_id)
    users = User.objects.all()
    for user in users:
        if user.user_id == user_id:
            return user
    return None


def check_problem(request):
    import json
    if request.method == 'POST':
        prob_id = request.POST['id']
        prob = get_prob_from_id(prob_id)
        if prob is None:
            res = ''
        else:
            res = 'No.%4s: %s' % (prob_id, prob.name)
        response = json.dumps({'name': res})
        return HttpResponse(response, content_type='text/javascript')
    else:
        raise Http404


def check_user(request):
    import json
    if request.method == 'POST':
        user_id = request.POST['id']
        usr = get_user_from_id(user_id)
        if usr is None:
            res = ''
        else:
            res = usr.name
        response = json.dumps({'name': res})
        return HttpResponse(response, content_type='text/javascript')
    else:
        raise Http404
