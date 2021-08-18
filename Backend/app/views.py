from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, UserDataInsert
from .models import Data
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView


class DataView(ListView):
    model = Data


class HomeView(TemplateView):
    template_name = 'app/home.html'


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = UserDataInsert
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = UserDataInsert(request.POST)
        if form.is_valid():
            usr = request.user
            sample_rec = form.cleaned_data['sample_rec']
            seq_last = form.cleaned_data['seq_last']
            sample_pen = form.cleaned_data['sample_pen']
            sample_rejected = form.cleaned_data['sample_rejected']
            reason = form.cleaned_data['reason']
            remark = form.cleaned_data['remark']
            reg = Data(user=usr, sample_rec=sample_rec, seq_last=seq_last, sample_pen=sample_pen,
                       sample_rejected=sample_rejected, reason=reason, remark=remark)
            reg.save()
            messages.success(request, 'Congratulation !! Your Profile Update Successfully')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


class CustomerRegView(View):
    def get(self, request):
        form = UserRegistrationForm
        return render(request, 'app/registration.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfully')
            return render(request, 'app/login.html')
        return render(request, 'app/registration.html', {'form': form})


def add_show(request):
    pass
