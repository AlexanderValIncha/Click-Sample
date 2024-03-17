import uuid

class Client: 
    
    def __init__(self,name, company, email, position, uid=None):
        self.name = name 
        self.company = company
        self.email = email 
        self.position = position
        self.uid = uid or uuid.uuid4()
        
    def to_dict(self):
        return vars(self) 
    #El metodo vars nos permite acceder a una representación como diccionario de nuestro objeto o instancia
    
    #Un metodo estatico es un metodo que se puede ejecutar sin necesidad de una instancia de clase
    #No necesita el self porque no necesita de una instancia, definimos la representación columnar de nuestro objeto
    @staticmethod
    def schema():
        return['name','company','email','position','uid']