import factory
import random
from django.contrib.auth.hashers import make_password

from .models import Post, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = 'pbkdf2_sha256$36000$lmzbMjkoMdR1$QDFA3KXbNacmepYyHaBQNCNQs2TY5voojgsdsbHcNno=' # 'secret'
    email = factory.Faker('email')


def random_post_type():
    """
    Returns a random post type from Post.POST_TYPE (link or text)
    """
    post_types = [choice[0] for choice in Post.POST_TYPES]
    return random.choice(post_types)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    user = factory.SubFactory(UserFactory)
    title = factory.Faker('text', max_nb_chars=140)
    body = factory.Faker('text', max_nb_chars=140)
    post_type = factory.LazyFunction(random_post_type)
