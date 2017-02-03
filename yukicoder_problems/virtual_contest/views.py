from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Problem, User, Submission, Contest


def index(request):
    contest_list = Contest.objects.all()
    context = {
        'contest_list': contest_list,
    }
    return render(request, 'virtual_contest/index.html', context)


def create_contest(request):
    return render(request, 'virtual_contest/create_contest.html')


def contest(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    return render(request, 'virtual_contest/contest.html', {'contest': contest})


def login(request):
    return HttpResponse("login")


def user_page(request, user_id):
    user_id = int(user_id)
    return HttpResponse("user %d" % user_id)
