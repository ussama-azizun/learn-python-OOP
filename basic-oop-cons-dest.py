''' Constructor and Destructor 
 - Constructor initial atrr when object has created (optional)
 - Object which made from Template, Prototype '''

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
    
    

#%% Create object
obj1 = Employee('Linda', 25000, 'Developer')
obj2 = Employee('Loren', 50000, 'Manager')

# %% Call method  show data
obj1.show_data()

# %% Change salary value (there is no encapsulation)
obj1.salary = 40000

# %%
