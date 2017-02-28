from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render


from decorators import ajax_required
from questions.forms import AnswerForm, QuestionForm
from questions.models import Answer, Question



@login_required
def questions(request):

    return unanswered(request)


@login_required
def unanswered(request):

    questions = Question.get_unanswered()
    return _questions(request, questions, 'unanswered')


@login_required
def _questions(request, questions, active):
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')

    #import pdb; pdb.set_trace()
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'questions.html', {
        'questions': questions,
        'active': active,
        'username': request.user.username
    })


@login_required
def answered(request):
    questions = Question.get_answered()
    return _questions(request, questions, 'answered')


@login_required
def all(request):
    questions = Question.objects.all()
    return _questions(request, questions, 'all')


@login_required
def ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            question.user = request.user
            question.title = form.cleaned_data.get('title')
            question.description = form.cleaned_data.get('description')
            question.save()
            tags = form.cleaned_data.get('tags')
            question.create_tags(tags)
            return redirect('/questions/')

        else:
            return render(request, 'questions/ask.html', {'form': form})

    else:
        form = QuestionForm()

    return render(request, 'questions/ask.html', {'form': form})




