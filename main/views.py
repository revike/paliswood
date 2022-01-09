from django.views.generic import TemplateView, ListView

from main.models import Product, Social, ProductCategory


class Index(ListView):
    """Index"""
    model = Product
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'главная'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context


class CatalogListView(ListView):
    """Catalog"""
    model = Product
    template_name = 'main/catalog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'каталог'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context


class CategoryListView(ListView):
    """Products for category"""
    model = Product
    template_name = 'main/catalog.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(category_id=self.kwargs['pk'],
                                             is_active=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ProductCategory.get_category().filter(
            id=self.kwargs['pk']).first().name
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context


class Buyers(TemplateView):
    """Information for buyers"""
    template_name = 'main/buyers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'покупателям'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context


class AboutMe(TemplateView):
    """About me"""
    template_name = 'main/about_me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'о нас'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context


class Error404(TemplateView):
    """Error 404"""
    template_name = 'main/404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'error 404'
        return context
