from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from .tokengenerate import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
# Create your views here.
def registeration(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # email verification
                current_site = get_current_site(request)
                html_content = render_to_string('user/email-verification.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'user_id': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    subject="Verify your email to activate account",
                    body=text_content,
                    from_email='hitendra.chat360@gmail.com',
                    to=[user.email],
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                return redirect('email_verification_send')
        return render(request,'user/register.html',{'form':form})
    else:
        return redirect('product')

def user_login(request):
    if not request.user.is_authenticated:
        form = LoginForm(request,data=request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,f'Hi {user.username}, login successful!')
                    return redirect('product')
                else:
                    messages.error(request,'User not fount')
                    return redirect('login')
        return render(request,'user/login.html',{'form':form})
    else:
        return redirect('product')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'You have been logged out successfully')
    return redirect('login')

def email_verification(request,uidb64,token):
    user_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=user_id)
    if user and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,'Your email has been verified successfully. You can now log in.')
        return redirect('login')
    else:
        return redirect('email_verification_send_failed')

def email_verification_send(request):
    return render(request,'user/email-verification-send.html')


def email_verification_send_failed(request):
    return render(request,'user/email-verification-send-failed.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('product')
    else:
        form = ProfileForm(instance=request.user)
    return render(request,'user/profile.html',{'form':form, 'hide_sidebar':True})