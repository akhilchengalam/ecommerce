from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import SubscribersForm
from applications.subscription.models import Subscribers

class SubscriberView(FormView):
    model_form = SubscribersForm
    model = Subscribers
    fields = ['email',]
    template_name ="subscription/subscribe_form.html"
    success_url = '/'

    def form_invalid(self,form):
        return render(self.request, {'form':self.model_form(form)})

    def post(self, request, *args, **kwargs):
        form = self.model_form(request.POST)
        if form.is_valid():
            print('form valid')
            email = form['email'].value()

            msg=" ";
            email_exist = Subscribers.objects.filter(email=email)
            if email_exist:
                msg = 'You Are Already Subscribed To our NewsLetter.'
                msg = "<div><b>STATUS :</b> %s</div>"%(msg)
            else:
                newsubscriber = Subscribers()
                newsubscriber.email = email
                newsubscriber.is_active=True
                newsubscriber.save()
                msg = 'Successfully Subscribed!'
                msg = "<div><b>STATUS :</b> %s</div>"%(msg)
            print(msg)

        else:
            print('form_invalid')
            msg="Invalid Email"
            msg = "<div><b>STATUS :</b> %s</div>"%(msg)
        return HttpResponse(msg)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.model_form()})