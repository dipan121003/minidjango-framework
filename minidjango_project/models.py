from .orm import Model

class Post(Model):
    # The fields are implicitly defined by what you pass to the constructor,
    # e.g., Post(title="...", content="...").
    # A more advanced ORM would have explicit field definitions here.
    pass