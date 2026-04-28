"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""

def read_todo_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"File {file_path} not found! Returning an empty to-do list.")
        return []

def write_todo_file(file_path, tasks):
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
