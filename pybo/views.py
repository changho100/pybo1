# pybo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer

# Create your views here.
def index(request): 
    # Question 테이블에 데이터가 없으면 초기 데이터 추가
    if Question.objects.count() == 0:
        Question.objects.create(subject="Django란?", content="Django는 파이썬 기반 웹 프레임워크입니다.")
        Question.objects.create(subject="Python의 장점은?", content="간결하고 생산성이 높습니다.")
        Question.objects.create(subject="HTML이란?", content="웹 페이지를 만드는 마크업 언어입니다.")
    question_list = Question.objects.all()
    return render(request, 'pybo/index.html', {'question_list': question_list})

def question_create(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        if subject and content:
            Question.objects.create(subject=subject, content=content)
            return redirect('index')
    return render(request, 'pybo/question_form.html')

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pybo/question_detail.html', {'question': question})

def question_edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        if subject and content:
            question.subject = subject
            question.content = content
            question.save()
            return redirect('question_detail', question_id=question.id)
    return render(request, 'pybo/question_form.html', {'question': question})

def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        question.delete()
        return redirect('index')
    return render(request, 'pybo/question_delete_confirm.html', {'question': question})
