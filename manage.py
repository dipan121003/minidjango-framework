# manage.py
import sys
from minidjango_project.database import init_db
from minidjango_project.models import Post

def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command == "initdb":
        init_db()
    elif command == "seeddb":
        print("Seeding database with sample posts...")
        # Create some posts and save them
        post1 = Post(title="First Post", content="This is the content of the first post.")
        post1.save()
        
        post2 = Post(title="Second Post", content="Here is another post about MiniDjango.")
        post2.save()
        print("Database seeded.")
    else:
        print("Unknown command. Available commands: initdb, seeddb")

if __name__ == "__main__":
    main()