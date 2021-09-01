from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm, UserDataInsert
from .models import Data
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView
from django.db.models import Max, Q


class DataView(ListView):
    model = Data


class HomeView(TemplateView):
    def get(self, request):
        q = Data.objects.filter(Time__in=Data.objects.values('user')
                                .annotate(Max('Time')).values_list('Time__max'))

        return render(request, 'app/home.html', {'data': q})


@login_required()
def add_show(request):
    if request.method == 'POST':
        form = UserDataInsert(request.POST)
        if form.is_valid():
            usr = request.user
            d = Data.objects.filter(user=request.user).order_by('-id')
            for m in d:
                print(m.id, m.user, m.Sample_pending)
            if d.exists():
                p = Data.objects.filter(user=request.user).order_by('-id')
                print(p)
                for i in p:
                    print(i.user)
                    l = i.Sample_pending
                    Sample_received = form.cleaned_data['Sample_received']
                    Sequence_last = form.cleaned_data['Sequence_last']
                    Sample_pending = l + Sample_received - Sequence_last
                    Sample_rejected = form.cleaned_data['Sample_rejected']
                    Reason = form.cleaned_data['Reason']
                    Remark = form.cleaned_data['Remark']
                    reg = Data(user=usr, Sample_received=Sample_received, Sequence_last=Sequence_last,
                               Sample_pending=Sample_pending, Sample_rejected=Sample_rejected,
                               Reason=Reason, Remark=Remark)
                    reg.save()
                    form = UserDataInsert()
                    messages.success(request, 'Data Saved Successfully!!!!')
                    return HttpResponseRedirect('/accounts/profile/')
            else:
                Sample_received = form.cleaned_data['Sample_received']
                Sequence_last = form.cleaned_data['Sequence_last']
                Sample_pending = Sample_received - Sequence_last
                Sample_rejected = form.cleaned_data['Sample_rejected']
                Reason = form.cleaned_data['Reason']
                Remark = form.cleaned_data['Remark']
                reg = Data(user=usr, Sample_received=Sample_received, Sequence_last=Sequence_last,
                           Sample_pending=Sample_pending, Sample_rejected=Sample_rejected,
                           Reason=Reason, Remark=Remark)
                reg.save()
                form = UserDataInsert()
                messages.success(request, 'Data Saved Successfully!!!!')
                return HttpResponseRedirect('/accounts/profile/')

    else:
        form = UserDataInsert()
    data = Data.objects.filter(user=request.user).order_by('-id')
    return render(request, 'app/profile.html', {'form': form, 'data': data})


# Registration
class CustomerRegView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'app/registration.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            form = UserRegistrationForm()
            return HttpResponseRedirect('/accounts/login/')
        else:
            form = UserRegistrationForm()
            messages.success(request, 'Registration Not Successful')
        return render(request, 'app/registration.html', {'form': form})


#  Update Function
@login_required()
def delete(request, id):
    if request.method == 'GET':
        emp = Data.objects.get(pk=id)
        emp.delete()
        return HttpResponseRedirect('/accounts/profile/')


# This Function is Used for Edit Data
@login_required()
def update_data(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pi = Data.objects.get(pk=id)
            o = pi.id
            l = Data.objects.filter(Q(id__lt=o) & Q(user=request.user)).values('Sample_pending').order_by('-id')
            
            if l.exists():
                form = UserDataInsert(request.POST, instance=pi)
                for i in l:
                    s = i['Sample_pending']
                    m = Data.objects.filter(Q(id__gt=o) & Q(user=request.user))
                    if form.is_valid():
                        pi.Sample_received = form.cleaned_data['Sample_received']
                        pi.Sequence_last = form.cleaned_data['Sequence_last']
                        pi.Sample_pending = s + pi.Sample_received - pi.Sequence_last
                        pi.save()
                        messages.success(request, 'Data Updated Successfully')
                        return HttpResponseRedirect('/accounts/profile/')
            else:
                form = UserDataInsert(request.POST, instance=pi)
                if form.is_valid():
                    pi.Sample_received = form.cleaned_data['Sample_received']
                    pi.Sequence_last = form.cleaned_data['Sequence_last']
                    pi.Sample_pending = 0 + pi.Sample_received - pi.Sequence_last
                    pi.save()
                    messages.success(request, 'Data Updated Successfully')
                    return HttpResponseRedirect('/accounts/profile/')
                    
    else:
        pi = Data.objects.get(pk=id)
        fm = UserDataInsert(instance=pi)
        return render(request, 'app/profile.html', {'form': fm})
      
