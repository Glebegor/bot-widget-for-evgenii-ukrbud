
class ManagerModel:

    def __init__(self, manager_id: int, manager_name: str, manager_email: str, manager_phone: str, manager_position: str):
        self.manager_id = manager_id
        self.manager_name = manager_name
        self.manager_email = manager_email
        self.manager_phone = manager_phone
        self.manager_position = manager_position

    def __str__(self):
        return f'{self.manager_id} {self.manager_name} {self.manager_email} {self.manager_phone} {self.manager_position}'