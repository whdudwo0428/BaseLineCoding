class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name : ", self.name)
        print("Salauy : ", self.salary)


class Manager(Employee):
    team_list = []
    def add_team_member(self, employee):
        self.team_list.append(employee)

    def display_team(self):
        print("Team Member List: ", self.team_list)
        for emp in self.team_list:
            emp.display_info()


manager = Manager("GongJae")

go = Employee("Go", 50)
ng = Employee("ng", 30)
ja = Employee("Ja", 20)
ee = Employee("ee", 20)
manager.add_team_member(go)
manager.add_team_member(ng)
manager.add_team_member(ja)

manager.display_team()

