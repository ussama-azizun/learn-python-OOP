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
        self._name =  name # Name
        self.__salary = salary #Private salary
        self.__department = department #Private department
        self.__show_data() # Within class can access show_data

    # Method show data change to private 
    def __show_data(self):
        print(f"Employee name {self._name}")
        print(f"Employee salary {self.__salary}")
        print(f"Employee Department {self.__department} ")



# %% Create object
obj1 = Employee('Linda', 25000, 'Developer')
obj2 = Employee('Loren', 50000, 'Manager')

# %% Show data


# %%
