from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CaptchaForm

def login_user(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None and form.is_valid():
            login(request, user)
            print('VALID')
            messages.success(request, ("Pomyślnie zalogowany"))
            return redirect('patient-ls')

        else:
            print('INVALID')
            messages.success(request, ("Błąd logowania, proszę spróbować jeszcze raz"))
            return redirect('login')   
    else:
        form = CaptchaForm()
        return render(request, 'login.html', {'form':form})

def logout_user(request):
        logout(request)
        messages.success(request, ("Pomyślnie wylogowany"))
        return redirect('login')



# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # Authenticate
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             print('VALID')
#             messages.success(request, ("Pomyślnie zalogowany"))
#             return redirect('patient-ls')

#         else:
#             print('INVALID')
#             messages.success(request, ("Błąd logowania, proszę spróbować jeszcze raz"))
#             return redirect('login')   
#     else:
#         captcha = CaptchaForm() 
#         context = {'captcha':captcha}
#         return render(request, 'login.html', context)

# def logout_user(request):
#         logout(request)
#         messages.success(request, ("Pomyślnie wylogowany"))
#         return redirect('login')



