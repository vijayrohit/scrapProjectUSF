from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import Context, loader
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post





def RecentPosts(request):
    pass


class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'delivery/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-datePosted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    # fields = ['orderSource','houseAccount', 'name', 'address', 'mobile', 'deliverydriver', 'deliverytime', 'specialInstruction', 'cateringAmount', 'deliveryFee', 'tips', 'salesTax', 'customerFeedBack', 'onTime', 'deliveryStatus', 'customerPaymentStatus', 'employeePaymentStatus', 'cateringDate', 'commissionAmount', 'commissionStatus', 'estimatedDelivery']
    fields = ['title', 'zip', 'email', 'name', 'description', 'author']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = ['title', 'category',  'condition', 'description', 'price', 'images', 'zip', 'email', 'name']

    def form_valid(self, form):
        form.instance.userId = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'price', 'email', 'name', 'zip', 'description']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.userId:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.userId:
            return True
        return False




@login_required()
def search(request):
    if not request.method == 'POST':
        if 'user_query' in request.session:
            request.POST = request.session['user_query']
            request.method = 'POST'
            searchQuery = request.POST.get('user_query')
            queryResult = Post.objects.filter(title__icontains=searchQuery)
            paginator = Paginator(queryResult, 5)
            page_number = request.GET.get('page', 1)
            page_obj = paginator.page(page_number)
            return render(request, 'delivery/search_results.html', {'page_obj': page_obj})
    if request.method == 'POST':
        searchQuery = request.POST.get('user_query')
        request.session['user_query'] = request.POST
        queryResult = Post.objects.filter(title__icontains=searchQuery)
        paginator = Paginator(queryResult, 5)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.page(page_number)
        print(page_number)
        return render(request, 'delivery/search_results.html', {'page_obj': page_obj})


def about(request):
    return render(request, 'delivery/about.html', {'title': 'About'})
