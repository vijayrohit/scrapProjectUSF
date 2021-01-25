from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import UserRegisterForm
from delivery.models import Post
UserModel = get_user_model()



@login_required
def profile(request):
    context = {
        'userPosts': Post.objects.filter(userId = request.user)
    }
    return render(request, 'users/profile.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            messages.success(request, 'Thank you for signing up! Please check your inbox/spam and verfiy your email id.')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Verify your Email'
            message = render_to_string('users/acc_activate_email.html', {
                'user': user,
                'domain': "scrap.rohitpantam.com",
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/register_complete.html')
    else:
        return HttpResponse('Activation link is invalid!')

# create a function to resolve email to username
def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

# create a view that authenticate user with email
def email_login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    username = get_user(email)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        pass