from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Account
from customer_app.models import Customer
from .forms import GaveForm,GotForm
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# To Calculate Selected Customer Balance Amount to be given or to be taken.
def cust_balance(request,id):
    cust_queryset = Account.objects.filter(customer__user=request.user, customer=id)
    got,gave = 0,0
    for i in cust_queryset:
        got = got + i.got
        gave = gave + i.gave
        balance = gave - got
    try:
        return balance
    except:
        return 0

@login_required(login_url='/users/signin')
def show_account(request,id,name):
    cust_id =id
    cust_name = name
    cust_bal = cust_balance(request,id)
    entries = Account.objects.filter(customer=id)
    # Session
    request.session['previous_url'] = request.path
    context = {'cust_name':cust_name, 'cust_id':cust_id,
                'entries':entries,'balance':cust_bal}
    return render(request, 'accounts/show_account.html', context)

class Gave(CreateView):
    form_class = GaveForm
    template_name = 'accounts/gave.html'
    success_url = '/customer/'

    def form_valid(self,form):
        cust_id = self.request.GET.get('cust_id')
        form.instance.customer = Customer.objects.get(id=cust_id)
        return super().form_valid(form)

    def get_success_url(self):
        success = self.request.session['previous_url']
        return success
    
    def get_context_data(self, **kwargs):
        context = super(Gave, self).get_context_data(**kwargs)
        context['previous_url'] = self.request.session['previous_url']
        return context


class Update_Gave(UpdateView):
    form_class = GaveForm
    template_name = 'accounts/update_gave.html'
    success_url = '/customer/'

    def form_valid(self,form):
        # cust_id = self.request.GET.get('cust_id')
        cust_id = self.kwargs['cust_id']
        form.instance.customer = Customer.objects.get(id=cust_id)
        return super().form_valid(form)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Account.objects.filter(pk=pk)
    
    def get_success_url(self):
        success = self.request.session['previous_url']
        return success

    def get_context_data(self, **kwargs):
        self.request.session['previous_url_del_acc'] = self.request.path
        context = super(Update_Gave, self).get_context_data(**kwargs)
        account_pk = self.kwargs['pk']
        print(account_pk)
        context['previous_url'] = self.request.session['previous_url']
        context['account_pk'] = account_pk
        return context

class Got(CreateView):
    form_class = GotForm
    template_name = 'accounts/got.html'
    success_url = '/customer/'

    def form_valid(self,form):
        cust_id = self.request.GET.get('cust_id')
        form.instance.customer = Customer.objects.get(id=cust_id)
        return super().form_valid(form)
    
    def get_success_url(self):
        success = self.request.session['previous_url']
        return success
    
    def get_context_data(self, **kwargs):
        context = super(Got, self).get_context_data(**kwargs)
        context['previous_url'] = self.request.session['previous_url']
        return context

class Update_Got(UpdateView):
    form_class = GotForm
    template_name = 'accounts/update_got.html'
    success_url = '/customer/'

    def form_valid(self,form):
        # cust_id = self.request.GET.get('cust_id')
        cust_id = self.kwargs['cust_id']
        form.instance.customer = Customer.objects.get(id=cust_id)
        return super().form_valid(form)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Account.objects.filter(pk=pk)
    
    def get_success_url(self):
        success = self.request.session['previous_url']
        return success

    def get_context_data(self, **kwargs):
        self.request.session['previous_url_del_acc'] = self.request.path
        context = super(Update_Got, self).get_context_data(**kwargs)
        account_pk = self.kwargs['pk']
        print(account_pk)
        context['previous_url'] = self.request.session['previous_url']
        context['account_pk'] = account_pk
        return context

class Delete_Account(DeleteView):
    model = Account
    success_url = '/customer'

    def get_success_url(self):
        success = self.request.session['previous_url']
        return success

    def get_context_data(self, **kwargs):
        context = super(Delete_Account, self).get_context_data(**kwargs)
        context['previous_url_del_acc'] = self.request.session['previous_url_del_acc']
        return context










































# @login_required(login_url='/users/signin')
# def gave(request):
#     print(id)
#     form = GaveForm()
#     if request.method == 'POST':
#         form = GaveForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/customer/')
#         else:
#             return render(request,'accounts/gave.html',{'form':form})
#     return render(request,'accounts/gave.html',{'form':form})

# @login_required(login_url='/users/signin')
# def got(request):
#     forms = GotForm()
#     if request.method == 'POST':
#         forms = GotForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('/customer/')
#         else:
#             return render(request,'accounts/gave.html',{'forms':forms})
#     return render(request,'accounts/got.html',{'forms':forms})