''' Constructor and Destructor 
 - isisstance : check whether object was create from class
 - dir : show attr and method
 - __class__ : show class name of object '''

#%% Create class
class Employee:

    # Method Constructor
    def __init__(self, name, salary, department):
        self.name =  name # name
        self.salary = salary #salary
        self.department = department #department

    # Method show data
    def show_data(self):
        print(f"Employee name {self.name}")
        print(f"Employee salary {self.salary}")
        print(f"Employee Department {self.department} ")