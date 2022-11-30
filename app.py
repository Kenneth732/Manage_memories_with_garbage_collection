import gc
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True

    return False

class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')
class B:
    def __init__(self):
        self.a = a 
        print(f"B: {hex(id(self))}, A{hex(id(self.a))}")
        
        
gc.disable()

a = A()

a_id = id(a)
b_id = id(a.b)

print(ref_count(a_id)) 
print(ref_count(b_id)) 

print(object_exists(a_id))
print(object_exists(b_id)) 


a = None
print(ref_count(a_id)) 
print(ref_count(b_id))

print(object_exists(a_id)) 
print(object_exists(b_id))

gc.collect()

print(object_exists(a_id))
print(object_exists(b_id))  
print(ref_count(a_id))
print(ref_count(b_id)) 