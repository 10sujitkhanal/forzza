from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.contrib import messages
from accounts.models import User
from userprofile.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class ProfileEditView(UpdateView):
    model = Profile
    template_name = "profile/edit-my-profile.html"
    context_object_name = "profile"
    object = None
    fields = "__all__"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def post(self, request, *args, **kwargs):
        print(request.POST.get('first_name'))
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.about = request.POST.get('about')
        if request.POST.get('gender') == "male":
            user.gender = "male"
        else:
            user.gender = "female"
        user.save()
        profile = user.profile
        profile.country = request.POST.get('country')
        profile.city = request.POST.get('city')
        profile.phone = request.POST.get('phone')
        profile.save()
        return redirect(reverse_lazy('profile:edit-profile'))




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile:change-password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile/change_password.html', {
        'form': form
    })


