# main.py

from module_b import func_b
from module_c import func_c

def func_a():
    print("Function A")
    func_b()
    func_c()

if __name__ == "__main__":
    func_a()
