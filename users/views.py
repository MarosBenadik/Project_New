from django.db import models
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login
from mainfeed.models import Post
from django.views import View
from question.models import Question
from booking.models.event import Event
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile, FreelanceProfile, BusinessProfile

from django.http import HttpResponse


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        groups_get = Group.objects.get(user=user)
        groups = groups_get.name
        events = Event.objects.filter(user=user)
        total_event = len(events)
        if groups == 'business':
            profile = BusinessProfile.objects.get(businessuser=user.pk)
            context = {
                'user': user,
                'profile': profile,
                'groups': groups,
                'events': events,
                'total_event': total_event,
            }
        elif groups == 'freelancer':
            questions = Post.objects.filter
            profile = FreelanceProfile.objects.get(freelanceuser=user.pk)
            context = {
                'user': user,
                'profile': profile,
                'groups': groups,
                'events': events,
                'total_event': total_event,
            }
        else:
            profile = UserProfile.objects.get (user=user.pk)
            context = {
                'user': user,
                'profile': profile,
                'groups': groups,
                'events': events,
            }

        return render(request, "dashboard.html", context)

class Register(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, "users/register.html",
                {"form": CustomUserCreationForm}
                )

    def post(self, request, *args, **kwargs):

        form = CustomUserCreationForm(request.POST)

        group = request.POST.get ('groups')

        if form.is_valid():
            user = form.save(commit=False)


            # More authentication Such as Github,
            # user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            # email = request.POST['email']
            # Registration Email
            # send_mail('Dakujeme za registraciu z KrasaVoVrecku!', 'Registraciou suhlasite z podmienkamy tejto applikacie', 'settings.EMAIL_HOST_USER', [email],
                      #fail_silently=False)

            if group == '1':
                businessprofile = BusinessProfile(businessuser=user)
                user_group = Group.objects.get(name='business')
                user.groups.add (user_group)
                businessprofile.save()
            elif group == '2':
                freelanceprofile = FreelanceProfile(freelanceuser=user)
                user_group = Group.objects.get(name='business')
                user.groups.add(user_group)
                freelanceprofile.save()
            else:
                user_group = Group.objects.get(name='user')
                user.groups.add(user_group)
                profile = UserProfile(user=user)
                profile.save()

            login (request, user)

            context = {
                'user': user
            }
            return render(request, 'dashboard.html', context)
        return redirect('register')


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user

        posts = Post.objects.filter(author=user).order_by('-created_on')

        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False


        number_of_followers = len(followers)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
        }

        return render(request, 'users/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'profilepicture']
    template_name = 'users/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user