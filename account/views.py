from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import SignUpForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.utils import timezone
from account.models import User
from Booking.models import Item


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.conf import settings

def home(request):
    # Fetch items from the database
    items = Item.objects.all()
    
    # Pass items to the template context
    context = {
        'items': items
    }
    
    # Render the homepage template with the context
    return render(request, 'homepage.html', context)



def custom_admin_login_view(request, **kwargs):
    response = login(request, **kwargs)
    user = request.user
    if user.is_authenticated and user.is_admin:
        if not user.is_approved:
            return render(request, 'pending_approval.html')
        else:
            return redirect('admin')
    else:
        return response


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Deactivate the user until they confirm their email
            user.is_staff = True
            user.save()
            if user.is_admin:
               user.is_approved=True
               user.email_confirmed = True
               user.is_staff = True
               user.is_superuser = True 
               user.save()
       
            
        
            

            # Send email with confirmation link
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            return redirect('registration_success')  # Redirect to a success page after sending email
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def confirm_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        return render(request, 'confirm_email.html', {'user': user})
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('activation_error')
    
 
 
 


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # Clear any existing session data to ensure a fresh login
        if request.user.is_authenticated:
            logout(request)
            request.session.flush()  # Ensure the session is completely cleared

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    if user.email_confirmed:
                        if user.is_admin:
                            if user.is_approved:
                                login(request, user)
                                return redirect('admin_dashboard')
                            else:
                                messages.error(request, 'Your account is pending approval.')
                        elif user.is_employee:
                            if user.is_approved:
                                login(request, user)
                                return redirect('employee')
                            else:
                                messages.error(request, 'Your account is pending approval.')
                        elif user.is_customer:
                            login(request, user)
                            return redirect('home')
                    else:
                        messages.error(request, 'Your email is not confirmed. Please check your email for the confirmation link.')
                else:
                    messages.error(request, 'Your account is inactive.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        # Ensure activation link is not expired
        if user.date_joined + timezone.timedelta(minutes=3) >= timezone.now():
            user.email_confirmed = True
            user.save()
            messages.success(request, 'Your account has been activated successfully.')
            return redirect(reverse('login'))  # Redirect to the login page
        else:
            messages.error(request, 'Activation link has expired. Please request a new one.')
    else:
        messages.error(request, 'Invalid activation link.')
    return render(request, 'activation_error.html')  # Render an error page


@login_required
@staff_member_required
def admin_dashboard(request):
    return render(request, 'adminDasboard.html', {'user': request.user})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return render(request, 'homepage.html')

@login_required(login_url='login')
def admin_page(request):
    return render(request, 'admin.html')

@login_required(login_url='login')
def customer(request):
    return redirect('customer.html')

@login_required(login_url='login')
def employee(request):
    return render(request, 'employee.html')


def approved(request):
    return render(request, 'approved.html')


def pending_approval_view(request):
    return render(request, 'pending_approval.html')


def registration_success(request):
    return render(request, 'registration_success.html')

def profile_page(request):
    return render(request, 'profilePage.html')

def itemDiv(request):
    return render(request, 'itemDiv.html')




def my_view(request):
    if request.user.is_authenticated:  # Check if the user is authenticated
        customer = request.user  # Assuming the user is logged in and represents a customer
        token = default_token_generator.make_token(request.user)  # Generate a token for the authenticated user
        
        # Fetch all items from the database
        items = Item.objects.all()
        
        # Pass customer information, token, and items to the template context
        return render(request, 'customer.html', {'customer': customer, 'token': token, 'items': items})
    else:
        # Handle the case when the user is not authenticated
        return render(request, 'login_required.html')  # Render a template indicating that login is required