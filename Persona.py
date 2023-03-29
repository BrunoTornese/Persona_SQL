from conexion import log

class Persona: # clase persona
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None): # valores de la clase
        self._id_persona = id_persona
        self._nombre = nombre # los valores de la clase seran reemplazados por los recibidos
        self._apellido = apellido
        self.email = email
    
    def __str__(self):#  metodo str para devolver los valores de la clase
        return f''' 
        Id Persona: {self._id_persona} , Nombre: {self._nombre} ,
        Apellido: {self._apellido} , Email: {self._email}
        '''
    
    @property # metodo get para tomar los valores
    def id_persona(self):
        return self._id_persona

    @id_persona.setter # metodo setter para reemplazar los valores
    def id_persona(self, id_persona):
        self._id_persona = id_persona
    
    @property # metodo get para tomar los valores
    def nombre(self):
        return self._nombre

    @nombre.setter # metodo setter para reemplazar los valores
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property 
    def apellidos(self):
        return self._apellido
    
    @apellidos.setter
    def apellidos(self, apellido):
        self._apellidos = apellido
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    
if __name__ == '__main__':
    persona1 = Persona(1,'Juan', 'Perez', 'Jperez@email.com')
    log.debug(persona1)







