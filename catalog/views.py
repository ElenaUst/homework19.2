from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, Version


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('catalog:access_denied')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin,  UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def get_form_class(self):
        if self.request.user == self.object.user:
            return ProductForm
        elif self.request.user.has_perm('catalog.set_published'):
            return ModeratorProductForm
        else:
            raise Http404('Вы не имеете права на редактирование чужих товаров')




# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/product_list.html', context)

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }


def contact(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f'{name}\n{phone}\n{message}\n')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Товары'
    }


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('catalog:access_denied')
    template_name = 'catalog/product_form.html'


class AccessDeniedView(TemplateView):
    template_name = 'catalog/access_denied.html'
