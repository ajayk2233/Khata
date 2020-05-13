from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Customer
from .forms import CustomerForm
from accounts.models import Account
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# To Calculate Total Balance Amount to be given or to be taken.
def total_b(request):
    all_queryset = Account.objects.filter(customer__user=request.user)
    got,gave = 0,0
    for i in all_queryset:
        got = got + i.got
        gave = gave + i.gave
    balance = gave - got
    try:
        return balance
    except:
        return 0

@login_required(login_url='/users/signin')
def show_customer(request,id=None):
    total_balance = total_b(request)
    customer = Customer.objects.filter(user=request.user)
    
    return render(request,'customer/show_customer.html',{'customer':customer,'total_balance':total_balance})

class Add_Customer(CreateView):
    form_class = CustomerForm
    template_name = 'customer/add_customer.html'
    success_url = '/'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Update_Customer(UpdateView):
    form_class = CustomerForm
    template_name = 'customer/update_customer.html'
    success_url = '/'

    def form_valid(self,form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

    def get_success_url(self):
        success = self.request.session['previous_url']
        return success

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Customer.objects.filter(pk=pk)

    def get_context_data(self, **kwargs):
        self.request.session['previous_url_del_cust'] = self.request.path
        context = super(Update_Customer, self).get_context_data(**kwargs)
        context['previous_url'] = self.request.session['previous_url']
        pk = self.kwargs['pk']
        context['cust_pk'] = pk
        return context

class Delete_Customer(DeleteView):
    model = Customer
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Delete_Customer, self).get_context_data(**kwargs)
        context['previous_url_del_cust'] = self.request.session['previous_url_del_cust']
        return context