from .templating import render_template
from .models import Post

def home_view(environ):
    context = {'title': 'Welcome to MiniDjango!'}
    return render_template('home.html', context)

def post_detail_view(environ, post_id):
    post = Post.get(id=int(post_id))
    if post:
        context = {
            'post_title': post.title,
            'post_content': post.content
        }
        return render_template('post_detail.html', context)
    else:
        return None