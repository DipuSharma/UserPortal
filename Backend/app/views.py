from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect

from .forms import UserRegistrationForm, LoginForm, UserDataInsert
from .models import Data
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView
from django.db.models import Count, Max, Min, Avg


class DataView(ListView):
    model = Data


class HomeView(TemplateView):
    def get(self, request):
        data = Data.objects.order_by('-id')
        dd = Data.objects.all().select_related('user')
        newdata = Data.objects.values('user').annotate(latest_date=Max('id')).all()
        for d in newdata:
            print(d)
        if data:
            return render(request, 'app/home.html', {'data': data, 'newdata': newdata})
        else:
            messages.success(request, 'Data Not Present')
            return render(request, 'app/home.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = UserDataInsert()
        if request.user.is_authenticated:
            data = Data.objects.filter(user=request.user).order_by('-id')
            return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'data': data})
        else:
            return render(request, 'app/profile.html', {'form': form})

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


# Registr
class CustomerRegView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'app/registration.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfully')
            form = UserRegistrationForm()
        else:
            form = UserRegistrationForm()
            messages.success(request, 'Data Not Uploaded Successfully')
        return render(request, 'app/registration.html', {'form': form})


#  Update Function
def update():
    pass


def delete_data(request, id):
    if request.method == 'POST':
        pi = Data.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This Function is Used for Edit Data
def update_data(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pi = Data.objects.get(pk=id)
            fm = UserDataInsert(request.POST, instance=pi)
            if fm.is_valid():
                usr = request.user
                fm.save()
    else:
        pi = Data.objects.get(pk=id)
        fm = UserDataInsert(instance=pi)
    return render(request, 'app/update.html', {'form': fm})
