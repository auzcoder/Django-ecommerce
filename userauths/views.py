from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_views(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            username = username.title()
            messages.success(request, f"Assalomu aleykum {username}, sizni akkauntingiz muvaffaqiyatli yaratildi!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
                                    )
            login(request, new_user)

            return redirect('core:index')
    else:
        form = UserRegisterForm()
        messages.success(request, "Sizda xatolik mavjud")

    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context=context)


def login_views(request):
    if request.user.is_authenticated:
        return redirect('core:index')

    if request.method == 'POST':
        email = request.POST.get('email')
