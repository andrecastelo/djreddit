from django.shortcuts import render
from core.models import Post


def index_view(request):
    posts = Post.objects.order_by('-created_at').all()
    return render(request, 'index.html', {'posts': posts})