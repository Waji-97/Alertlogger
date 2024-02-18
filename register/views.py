from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.urls import reverse_lazy

class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('webhook:index')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully updated.')
        return super().form_valid(form)
