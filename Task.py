from datetime import datetime


class Task:
    id = 0

    def __init__(self):
        Task.id += 1
        self.id = Task.id
        self.description = ""
        self.status = "ToDo"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.formato = self.created_at.strftime("%d/%m/%Y %H:%M:%S")

    def update_status_in_progress(self):
        self.status = "in-progress"
        self.updated_at = datetime.now()
        self.formato = self.updated_at.strftime("%d/%m/%Y %H:%M:%S")

    def update_status_done(self):
        self.status = "done"
        self.updated_at = datetime.now()
        self.formato = self.updated_at.strftime("%d/%m/%Y %H:%M:%S")

    # Convierte el objeto a diccionario para guardarlo en JSON
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __str__(self):
        return f"Estado: [{self.status.upper()}] id: {self.id} {self.description} (Actualizada el: {self.formato})"
