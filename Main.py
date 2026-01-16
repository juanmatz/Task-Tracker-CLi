import time
from Task import Task
from Todo import Todo


def Main():
    def mostrar_menu():
        print("""===== Menu de Opciones =====
1. Agregar Tarea
2. Borrar Tarea
3. Iniciar Tarea
4. Finalizar Tarea
5. Mostrar Todas las Tareas
6. Mostrar Tareas en progreso
7. Mostrar Tareas finalizadas
8. Salir""")

    task_list = Todo()
    opcion = ""
    task_list.load_task_json()  # Cargar tareas guardadas al inicio
    while True:
        mostrar_menu()
        opcion = int(input("ingresa el numero de la opcion: "))
        if opcion == 8:  # Terminar Flujo
            return False
        elif opcion == 1:  # Agregar Tarea
            task = Task()
            task.description = input("Ingresa la descripcion de la tarea: ")
            task_list.add_task(task)
            task_list.save_task_json()
        elif opcion == 2:  # Borrar Tarea
            task_list.show_tasks()
            if task_list.todo_list:
                try:
                    id_borrar = int(
                        input("Ingresa el id de la tarea que deseas borrar: ")
                    )
                    task_list.delete_task(id_borrar)
                    task_list.save_task_json()
                except ValueError:
                    print("Asegurate que el id sea correcto")
        elif opcion == 3:  # Actualizar tarea -> in progress
            task_list.show_tasks()
            if task_list.todo_list:
                try:
                    id_task = int(
                        input("Ingresa el id de la tarea que deseas iniciar: ")
                    )
                    task_list.set_task_in_progress(id_task)
                    task_list.save_task_json()

                except ValueError:
                    print("Asegurate que el id sea correcto")
        elif opcion == 4:  # Actualizar Tarea -> completar
            task_list.show_tasks()
            if task_list.todo_list:
                try:
                    id_task = int(
                        input("Ingresa el id de la tarea que deseas completar: ")
                    )
                    task_list.set_task_done(id_task)
                    task_list.save_task_json()

                except ValueError:
                    print("Asegurate que el id sea correcto")
        elif opcion == 5:
            task_list.show_tasks()

        elif opcion == 6:  # Mostrar Tareas
            task_list.show_task_in_progress()
        elif opcion == 7:
            task_list.show_task_done()

        time.sleep(1)


if __name__ == "__main__":
    Main()
