from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    pass


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()
        token = default_token_generator.make_token(new_user)
        new_user.email_verification_token = token
        new_user.save()
        uid = urlsafe_base64_encode(force_str(new_user.pk).encode())
        verification_url = reverse('users:activate', kwargs={'uidb64': uid, 'token': token})
        verification_url = self.request.build_absolute_uri(verification_url)
        send_mail(
            subject='Registration',
            message=render_to_string('users/verify_email.txt', {'verification_url': verification_url}),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False,


        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_pass = User.objects.make_random_password()
    send_mail(
        subject='new_password',
        message=f'Your new password {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]

    )
    request.user.set_password(new_pass)
    request.user.save()
    return redirect(reverse('catalog:index'))


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user and user.email_verification_token == token:
        user.is_active = True
        user.save()
        return redirect('users:login')
    else:
        return redirect('users:verification_failed')


class VerificationFailedView(TemplateView):
    template_name = 'users/verification_failed.html'
