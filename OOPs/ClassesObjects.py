# In this python file, We implemented a simple class with a state and behavior using an object instance.

class PC: #Classes are created by keyword class.

    pcName = "Zebronics"

    print("PC Class Created Successfully.") 
   
    """ 
    def __init__(self):
        pass
        print("Basic Function Created") 
    """
    
    def MyMethod(self,pcName):
        print("PC Model & Manufacturer is '{}'".format(pcName));

obj = PC()
print("PC Model & Manufacturer is '{}'".format(obj.pcName));
obj1 = PC()
obj1.MyMethod("Lenovo")