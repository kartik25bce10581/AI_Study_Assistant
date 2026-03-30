from chatbot import chatbot_response
from task_manager import load_tasks, save_tasks
from analytics import show_stats

def display_menu():
    print("\n📚 AI Study Assistant")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Ask AI")
    print("6. Show Analytics")
    print("7. Exit")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n📝 Tasks:")
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added successfully.")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"❌ Removed: {removed}")
                else:
                    print("Invalid task number.")

        elif choice == "4":
            tasks.clear()
            save_tasks(tasks)
            print("🗑 All tasks cleared.")

        elif choice == "5":
            q = input("Ask your study question: ")
            print("💡", chatbot_response(q))

        elif choice == "6":
            show_stats(tasks)

        elif choice == "7":
            print("👋 Exiting application.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()