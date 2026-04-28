"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"    - Add a task to the list.   
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)
        if len(sys.argv) == 2:
            return

        commands = sys.argv[2:]
        changed = False
        i = 0
        


        while i < len(commands):
            cmd = commands[i]
            if cmd == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1
            elif cmd == "add":
                if i + 1 >= len(commands):
                    raise IndexError('Task description required for "add".')
                task_desc = commands[i + 1]
                tasks.append(task_desc)
                print(f'Task "{task_desc}" added.')
                changed = True
                i += 2
            
            elif cmd == "remove":
                if i + 1 >= len(commands):
                    raise IndexError('Task description required for "remove".')
                task_desc = commands[i + 1]
                try:
                    tasks.remove(task_desc)
                    print(f'Task "{task_desc}" removed.')
                    changed = True
                except ValueError:
                    print(f'Task "{task_desc}" not found.')
                i += 2
            else:
                raise ValueError("Command not found!")

        if changed:
            write_todo_file(file_path, tasks)
    except (IndexError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()