from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import DemoForm
from .models import DemoDatabase
# Create your views here.

# def home(request):
#     return render(request, 'phishing/index.html')

# def home(request):
#     """Add new lead from the lead form"""
#     template = 'phishing/index.html'
#     data = DemoDatabase.objects.all()

#     if request.method == 'POST':
#         form = DemoForm()
#         form.save()
#         # if form.is_valid():
#         #     form.save()
#         #     form = DemoForm()
#         #     # latest_lead = Lead.objects.latest()
#         #     # messages.success(request, " '{}' added to the leads table".format(str(latest_lead)))   
#         # else:
#         #     # form.save()
#         #     form = DemoForm()
#         #     print(form.errors)
#         #     print(form.non_field_errors())
#         #     print('no')
#         return render(request, template, {'form': form, 'show_option':True, 'data':data})

#     else:
#         form = DemoForm()

#     return render(request, template, {'form': form, 'show_option':True, 'data':data})


def home(request):

    template = 'phishing/index.html'
    if request.method == 'POST':
        form = DemoForm(request.POST)
        # form = DemoForm(data=travelform1)
        print(form)
        if form.is_valid:
            form.save()
            form = DemoForm()
            return HttpResponseRedirect('/')
    else:
        form = DemoForm()
    return render(request, template, {'form':form})