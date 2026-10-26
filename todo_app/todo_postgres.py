import psycopg2

# Database connection configuration
# Update these details to match your local PostgreSQL setup
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "UDBATMAN",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    """Establish and return a database connection."""
    return psycopg2.connect(**DB_CONFIG)

def setup_database():
    """Create the todos table automatically if it does not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_task(task_description):
    """Add a new task to the PostgreSQL database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (task, completed) VALUES (%s, %s);",
        (task_description, False)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Task added successfully!")

def view_tasks():
    """Fetch and display all tasks from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, completed FROM todos ORDER BY id;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    if not rows:
        print("\n📂 No tasks found in the database.")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for row in rows:
        task_id, task_desc, completed = row
        status = "[X]" if completed else "[ ]"
        print(f"{task_id}. {status} {task_desc}")
    print("-" * 23)

def complete_task(task_id):
    """Mark a specific task as completed."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE todos SET completed = TRUE WHERE id = %s;",
        (task_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"🎉 Task {task_id} marked as completed!")

def delete_task(task_id):
    """Delete a task from the database by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s;", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"🗑️ Task {task_id} deleted successfully!")

def main():
    try:
        setup_database()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("Please check your database credentials in DB_CONFIG.")
        return

    while True:
        print("\n=== PYTHON POSTGRES TO-DO APP ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task description: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Task description cannot be empty.")
        elif choice == '3':
            view_tasks()
            try:
                task_id = int(input("Enter ID of task to complete: "))
                complete_task(task_id)
            except ValueError:
                print("⚠️ Please enter a valid numeric ID.")
        elif choice == '4':
            view_tasks()
            try:
                task_id = int(input("Enter ID of task to delete: "))
                delete_task(task_id)
            except ValueError:
                print("⚠️ Please enter a valid numeric ID.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()