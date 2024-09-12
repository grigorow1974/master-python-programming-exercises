# Your code here
class InputOutString:
    def __init__(self):
        self.cadena = "" 
    def get_string(self):
        self.cadena = input("Introduce un string: ") 
    def print_string(self):
        print(self.cadena.upper()) 