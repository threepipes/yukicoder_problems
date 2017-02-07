from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

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
        contest_id = len(contest_set.all())
        # TODO
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


def check_problem(request):
    import json
    if request.method == 'POST':
        problems = Problem.objects.all()
        prob_id = request.POST['id']
        res = ''
        for prob in problems:
            if str(prob.problem_id) == prob_id:
                res = 'No.%4s: %s' % (prob_id, prob.name)
                break
        response = json.dumps({'name': res})
        return HttpResponse(response, content_type='text/javascript')
    else:
        raise Http404


def check_user(request):
    import json
    if request.method == 'POST':
        users = User.objects.all()
        user_id = request.POST['id']
        res = ''
        for usr in users:
            if str(usr.user_id) == user_id:
                res = usr.name
                break
        response = json.dumps({'name': res})
        return HttpResponse(response, content_type='text/javascript')
    else:
        raise Http404
