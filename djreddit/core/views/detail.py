from django.views.generic import DetailView
from core.models import Post

class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'detail.html'
