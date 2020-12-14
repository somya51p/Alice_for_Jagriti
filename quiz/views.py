from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from .forms import QuizQuestionForm, OptionFormSet
from .models import Question, User_Answer, Attempt, Chapter,Option
# Create your views here.

@login_required
def home(request):
    attempts = Attempt.objects.all()
    return render(request, 'quiz/index.html', {'attempts': attempts})

@login_required
def quiz_for_chapteri(request, num):
    try:
        questions = Question.objects.filter(chapter=Chapter.objects.get(pk=int(num)))
    except:
        return HttpResponse("well done! But you are little early")

    if request.method == 'POST':
        total_score = 0
        attempt = Attempt(chapter=Chapter.objects.get(pk=int(num)), user=User.objects.get(username=request.user.username),total_score=total_score)
        attempt.save()
        for i, question in enumerate(questions):
            try:
                selected_choice = int(request.POST[f'answer{i+1}'])
                user_answer = User_Answer(attempt=attempt, question=question, user_ans=question.option_set.get(pk=selected_choice))
                user_answer.save()
                print(f"{user_answer} is user answer")
                if (selected_choice) == question.option_set.get(is_correct = True).id:
                    total_score += question.score
            except:
                total_score += 0

        attempt.total_score = total_score
        attempt.save()
        request.session['attempt_id'] = attempt.pk
        request.session['total_score'] = total_score
        print("here is "+ str(request.session['attempt_id']))
        return redirect('quiz:result')   
        # return HttpResponse(f" so {request.user.username} your total score is {total_score}")
    return render(request,'chap/quiz.html',{'questions': questions})

@staff_member_required(login_url='/login_admin/')
def add_question(request):
    context = {}
    if request.method == 'POST':
        ques_form = QuizQuestionForm(request.POST)
        # option_form = QuizOptionForm(request.POST)
        if ques_form.is_valid():
            ques = ques_form.save()

            return redirect('quiz:add_Option',ques_id=ques.pk)
        else:
            context['ques_form'] = ques_form
            # context['option_form'] = option_form

    else:
        context['ques_form'] = QuizQuestionForm()
        # context['option_form'] = QuizOptionForm()
    
    return render(request, 'quiz/addQues.html', context)



def add_Option(request, ques_id):
    ques = Question.objects.get(pk=ques_id)

    context = {'question':ques}

    if request.method == 'POST':
        option_formset = OptionFormSet(request.POST,instance = ques)
        if option_formset.is_valid():
            option_formset.save()
            context['added'] = True


    context['option_formset'] = OptionFormSet(instance = ques)


    return render(request, 'quiz/addedQues.html', context)

@login_required
def result(request):
    attempt_id = request.session['attempt_id']
    attempt = Attempt.objects.get(pk=attempt_id)
    user_answer = User_Answer.objects.filter(attempt=attempt)
    context = {}
    context['user'] = attempt.user
    context['attempt_no'] = Attempt.objects.filter(user=attempt.user).count()
    context['no_of_questions'] = (user_answer.count())
    context['total_score'] = request.session['total_score']
    context['max_possible_score'] = 4 * int(user_answer.count())
    # list to store tuple of user answer and correct answer and max marks respectively
    ans_list = []
    for ans in user_answer:
        ans_list += [[ans.user_ans, Option.objects.get(question=ans.question, is_correct=True), ans.question.score]]
    context['answers'] = ans_list

    return render(request, 'results.html', context)