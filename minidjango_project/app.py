import re
from minidjango_project.templating import render_template
from minidjango_project.models import Post
from . import views

# --- URL Router ---
# We're upgrading to a list of (regex, view) tuples for dynamic URLs

urls = [
    (r'^/$', views.home_view),
    (r'^/posts/(?P<post_id>\d+)/$', views.post_detail_view),
]

# --- Main Application (The Router) ---

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    
    # Find a matching view
    view, kwargs = None, {}
    for pattern, view_func in urls:
        match = re.search(pattern, path)
        if match:
            view = view_func
            kwargs = match.groupdict() # Captures named groups like 'post_id'
            break

    # Get the response from the view
    if view:
        html_string = view(environ, **kwargs)
        if html_string:
            status = '200 OK'
        else: # Handle case where post is not found in the view
            status = '404 Not Found'
            html_string = "<h1>404 Not Found</h1>"
    else:
        status = '404 Not Found'
        html_string = "<h1>404 Not Found</h1>"

    response_body = html_string.encode('utf-8')
    headers = [
        ('Content-type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, headers)
    return [response_body]