# MiniDjango Framework

MiniDjango is a simple Python web framework for learning purposes. You can use it to build your own web applications and add new features on top of it.

## Features

- Basic MVC structure
- SQLite database integration
- Simple templating system

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd MiniDjango/minidjango_project
   ```

2. **Initialize the database:**
   ```sh
   python database.py
   ```

3. **Run the web application:**
   ```sh
   python app.py
   ```

4. **Open your browser:**
   Visit [http://localhost:8000](http://localhost:8000)

## Example Usage

```python
# models.py
class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=100)
```

## Customization

- Add new models in `models.py`
- Create new views in `views.py`
- Add HTML templates in the `templates/` folder

## License

For learning and educational use only.