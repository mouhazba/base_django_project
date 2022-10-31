from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserForm

class Signup(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

