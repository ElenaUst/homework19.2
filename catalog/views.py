from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


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


# class ContactTemplateView(TemplateView):
#     template_name = 'contacts.html'

# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'Товары'
#     }
#     # print(f'{name}\n{description}\n{price}\n')
#     return render(request, 'catalog/product_detail.html', context)

class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Товары'
    }


