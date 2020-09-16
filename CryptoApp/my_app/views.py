from django.http import HttpResponse, HttpResponseRedirect
from django.db import Error
from django.http import Http404
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import UserForm
from .models import User

# Create your views here.


def index(request):
    user_list = User.objects.all()
    context = {'user_list': user_list,}
    #output = ', '.join([str(u) for u in user_list])
    return render(request, 'my_app/index.html', context)


def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Http404("The user with id %s does not exist" % user_id)
    # user = get_object_or_404(User, pk=user_id)
    return render(request, 'my_app/detail.html',
                  {'user': user})


def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_app:index'))
        else:
            return HttpResponseBadRequest("Unable to create a new user.")
    else:
        form = UserForm()
        return render(request, 'my_app/create_user.html',
                      {
                          'form': form
                      })

def update_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
