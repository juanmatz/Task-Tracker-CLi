import json
from Task import Task
from datetime import datetime


class Todo:
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)
        print(f"tarea añadida {task.description}")

    def set_task_in_progress(self, id_task):
        if not self.todo_list:
            print("la lista esta vacia")
            return
        found = False
        for task in self.todo_list:
            if task.id == id_task:
                task.update_status_in_progress()
                print(f"Tarea actualizada: {task}")
                found = True
                return

        if not found:
            print(f"No se encontró ninguna tarea con el id {id_task}")

    def set_task_done(self, id_task):
        if not self.todo_list:
            print("la lista esta vacia")
            return
        found = False
        for task in self.todo_list:
            if task.id == id_task:
                task.update_status_done()
                print(f"Tarea actualizada: {task}")
                found = True
                return

        if not found:
            print(f"No se encontró ninguna tarea con el id {id_task}")

    def delete_task(self, task_id):
        if not self.todo_list:
            print("la lista esta vacia")
            return
        tarea_encontrada = False

        for task in self.todo_list:
            if task.id == task_id:
                self.todo_list.remove(task)
                print(f"tarea con ID {task_id} eliminada")
                tarea_encontrada = True
                break

        if not tarea_encontrada:
            print("tarea no encontrada")

    def show_tasks(self):
        if not self.todo_list:
            print("la lista esta vacia")
        else:
            for self.task in self.todo_list:
                print(self.task)

    def show_task_in_progress(self):
        if not self.todo_list:
            print("la lista esta vacia")
        else:
            for self.task in self.todo_list:
                if self.task.status == "in-progress":
                    print(self.task)

    def show_task_done(self):
        if not self.todo_list:
            print("la lista esta vacia")
        else:
            for self.task in self.todo_list:
                if self.task.status == "done":
                    print(self.task)

    # Guarda la lista de tareas en el archivo JSON
    def save_task_json(self):
        with open("datos.json", "w") as archivo:
            list_task = [task.to_dict() for task in self.todo_list]
            json.dump(list_task, archivo, indent=4, ensure_ascii=False)

    # Carga las tareas desde el archivo JSON al iniciar
    def load_task_json(self):
        try:
            with open("datos.json", "r") as archivo:
                datos = json.load(archivo)
                self.todo_list = []
                for dato in datos:
                    t = Task()
                    t.id = dato["id"]
                    t.description = dato["description"]
                    t.status = dato["status"]
                    t.created_at = datetime.fromisoformat(dato["created_at"])
                    t.updated_at = datetime.fromisoformat(dato["updated_at"])
                    t.formato = t.created_at.strftime("%d/%m/%Y %H:%M:%S")
                    self.todo_list.append(t)
                if self.todo_list:
                    max_id = 0
                    for task in self.todo_list:
                        if task.id > max_id:
                            max_id = task.id

                    Task.id = max_id

        except FileNotFoundError:
            self.todo_list = []
