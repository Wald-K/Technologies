from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.list import ListView


from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')

def get_all_users(request):
    users = User.objects.all()
    return render(request, 'core/index.html', {'users': users})

class UserListView(ListView):
    model = User
    template_name = 'core/index.html'
    context_object_name = 'users'







