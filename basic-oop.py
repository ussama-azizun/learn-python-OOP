''' Create class and object 
 - Class means Template, Prototype
 - Object which made from Template, Prototype '''

#%% Create class
class Employee:
    # Method details
    # Parameters which pass to details method
    def details(self, name, salary, department):
        # Self which means we config with object attr
        self.name =  name # name
        self.salary = salary #salary
        self.department = department #department

    # Method show data
    def show_data(self):
        print(f"Employee name {self.name}")
        print(f"Employee salary {self.salary}")
        print(f"Employee Department {self.department} ")


#%% Create object
obj1 = Employee() 
obj2 = Employee()

# %% Pass an parameter name and salary
obj1.details('John', 25000, 'Developer')
obj2.details('Xavier', 40000, 'Acountant')
# %% Show data methods
obj1.show_data()

# %%
