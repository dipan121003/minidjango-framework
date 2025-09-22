# orm.py
from .database import get_db_connection

class Model:
    """
    The base class for all models. It provides the core ORM functionality.
    """
    def __init__(self, **kwargs):
        # Store initial values. __dict__ holds the object's attributes.
        self.__dict__.update(kwargs)

    @classmethod
    def get(cls, id):
        """Fetches a single record from the database by its ID."""
        conn = get_db_connection()
        table_name = cls.__name__.lower() + 's' # e.g., Post -> posts
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            # Create an instance of the class (e.g., Post) with the fetched data
            return cls(**dict(row))
        return None

    def save(self):
        """Saves a model instance to the database (INSERT only for now)."""
        conn = get_db_connection()
        cursor = conn.cursor()
        table_name = self.__class__.__name__.lower() + 's'

        # Get columns and values from the instance's attributes
        cols = [key for key in self.__dict__ if key != 'id']
        vals = [self.__dict__[key] for key in cols]
        
        # Build the SQL query dynamically
        col_names = ', '.join(cols)
        placeholders = ', '.join(['?'] * len(vals))
        
        query = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"
        
        cursor.execute(query, vals)
        conn.commit()
        conn.close()