''' Encapsulation
- Attribute permision 
- Acces modifier : access permision to Class, Attr, Method
  + Public : anyone can access data (public post)
  + Protected(_) : acces permision within class and child class that inherit (friend post)
  + Private(__) : can acces only its class (only me post) '''

#%% Create class
class Employee:

    # Method Constructor
    def __init__(self, name, salary, department):
        # Public attribute
        self._name =  name # name
        self._salary = salary #salary
        self._department = department #department

    # Method show data
    def _show_data(self):
        print(f"Employee name {self._name}")
        print(f"Employee salary {self._salary}")
        print(f"Employee Department {self._department} ")



# %% Create object
obj1 = Employee('Linda', 25000, 'Developer')
obj2 = Employee('Loren', 50000, 'Manager')

# %% Show data
obj1._show_data()

# %%
