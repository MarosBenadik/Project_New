from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Question, Topic, Message
from .forms import QuestionForm


class Questions(View):
	def get(self, request, *args, **kwargs):
	    q = request.GET.get('q') if request.GET.get('q') != None else ''
	    questions = Question.objects.filter(
	        Q(topic__name__icontains=q) |
	        Q(name__icontains=q) |
	        Q(description__icontains=q)
	    )

	    topics = Topic.objects.all()
	    questions_count = questions.count()
	    feeds = Message.objects.filter(Q(question__topic__name__icontains=q)).order_by('-created')

	    context = {'questions': questions, 'topics': topics, 'questions_count': questions_count, 'feeds': feeds}
	    return render(request, 'questions.html', context)


class QuestionView(View):
	def get(self, request, pk, *args, **kwargs):
	    question = Question.objects.get(id=pk)
	    question_messages = question.message_set.all().order_by('-created')
	    participants = question.participants.all()

	    context = {'question': question, 'question_messages': question_messages, 'participants': participants}
	    return render(request, 'question.html', context)

	def post(self, request, pk, *args, **kwargs):
		question = Question.objects.get (id=pk)

		message = Message.objects.create (
			user=request.user,
			question=question,
			body=request.POST.get ('body')
		)
		question.participants.add (request.user)
		return redirect ('question', pk=question.id)


class CreateQuestion(View):
	def get(self, request, *args, **kwargs):
		form = QuestionForm()
		topics = Topic.objects.all()

		context = {'form': form, 'topics': topics}
		return render (request, 'question_form.html', context)

	def post(self, request, *args, **kwargs):

		topic_name = request.POST.get ('topic')
		topic, created = Topic.objects.get_or_create (name=topic_name)
		Question.objects.create (
			host=request.user,
			topic=topic,
			name=request.POST.get ('name'),
			description=request.POST.get ('description')
		)
		return redirect ('home')


class UpdateQuestion(View):
	def get(self, request, pk, *args, **kwargs):
		question = Question.objects.get (id=pk)
		form = QuestionForm (instance=question)
		topics = Topic.objects.all ()

		if request.user != question.host:
			return HttpResponse ('You dont have the authorisation to update question!')

		context = {'form': form, 'topics': topics, 'question': question}
		return render (request, 'question_form.html', context)

	def post(self, request, pk, *args, **kwargs):
		question = Question.objects.get (id=pk)
		topic_name = request.POST.get ('topic')
		topic, created = Topic.objects.get_or_create (name=topic_name)
		question.name = request.POST.get ('name')
		question.topic = topic
		question.description = request.POST.get ('description')
		question.save ()
		return redirect ('home')


class DeleteQuestion(View):
	def get(self, request, pk, *args, **kwargs):
		question = Question.objects.get(id=pk)

		if request.user != question.host:
			return HttpResponse ('You dont have the authorisation to update question!')

		return render (request, 'delete.html', {'obj': question})

	def post(self, request, pk, *args, **kwargs):
		question = Question.objects.get (id=pk)
		question.delete ()
		return redirect ('home')

class DeleteMesage(View):
	def post(self, request, pk, *args, **kwargs):
		message = Message.objects.get (id=pk)

		if request.user != message.user:
			return HttpResponse ('You dont have the authorisation to update question!')

		if request.method == 'POST':
			message.delete ()
			return redirect ('home')
		return render (request, 'delete.html', {'obj': message})