class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        """Возвращает информацию о сотруднике"""
        return f"Имя: {self.name}, ID: {self.employee_id}"


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def manage_project(self, project_name):
        """Управление проектом"""
        return f"{self.name} управляет проектом: {project_name}"

    def get_info(self):
        """Переопределение метода get_info для вывода дополнительной информации"""
        base_info = super().get_info()
        return f"{base_info}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, employee_id, specialization):
        super().__init__(name, employee_id)
        self.specialization = specialization

    def perform_maintenance(self):
        """Выполнение технического обслуживания"""
        return f"{self.name} выполняет техническое обслуживание по специализации: {self.specialization}"

    def get_info(self):
        """Переопределение метода get_info для вывода дополнительной информации"""
        base_info = super().get_info()
        return f"{base_info}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, employee_id, department, specialization):
        Manager.__init__(self, name, employee_id, department)  # Инициализация от Manager
        Technician.__init__(self, name, employee_id, specialization)  # Инициализация от Technician
        self.team = []  # Список подчинённых сотрудников

    def add_employee(self, employee):
        """Добавление сотрудника в команду"""
        self.team.append(employee)

    def get_team_info(self):
        """Вывод информации о всей команде"""
        team_info = "Информация о команде:\n"
        for employee in self.team:
            team_info += f"{employee.get_info()}\n"
        return team_info


# Создание объектов сотрудников
employee1 = Employee("Иван Иванов", 211)
manager1 = Manager("Олег Петров", 222, "IT")
technician1 = Technician("Иван Смирнов", 233, "Сетевой администратор")
tech_manager1 = TechManager("Сергей Ковалёв", 244, "IT", "Системный администратор")

# Технический менеджер добавляет сотрудников в свою команду
tech_manager1.add_employee(manager1)
tech_manager1.add_employee(technician1)

# Проверка функциональности
print(employee1.get_info())  # Информация о сотруднике
print(manager1.manage_project("Проект по внедрению CRM"))  # Управление проектом
print(technician1.perform_maintenance())  # Выполнение обслуживания
print(tech_manager1.manage_project("Проект по оптимизации сети"))  # Управление проектом
print(tech_manager1.perform_maintenance())  # Выполнение обслуживания
print(tech_manager1.get_team_info())  # Информация о команде
