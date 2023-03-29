from conexion import log
from conexion import Conexion
from Persona import Persona
from cursor import Cursor_del_pool

class Manejo_dao: # funciones para realizar con la base de datos
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido= %s, email=%s WHERE id_persona=%s'
    _ELIMINAR= 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def selecionar(cls):  # con esta funcion voy a poder conectarme a la bd atravez del cursor
        with Cursor_del_pool() as cursor: # obtengo la conexion de cursor
                cursor.execute(cls._SELECCIONAR) # llamo a la variable de seleccionar
                registros = cursor.fetchall() # obtengo todos los registros
                personas = [] # creo una lista vacia
                for registro in registros: # para cada registro en registros
                    persona = Persona(registro[0], registro[1], registro[2], registro[3]) # va a devolver en cada registro los datos de la persona (id nombre apellido e email)
                    personas.append(persona) # y las agrego a esta lista
                return personas #retorna la lista de personas
        
    @classmethod
    def insertar(cls, persona): # funcion para insertar una persona
        with Cursor_del_pool() as cursor: # obtengo la conexion de cursor
            log.debug(f'Persona a agregar: {persona}') # muestra la persona a agregar
            valores = (persona._nombre, persona._apellido, persona._email) # aqui pido los valores atravez de los metodos getter
            cursor.execute(cls._INSERTAR,valores) # inserta la persona
            log.debug(f'Persona agregada: {persona}')  # muestra la persona agregada
            return cursor.rowcount # muestra la cantidad de persons agregadas

    @classmethod 
    def actualizar(cls, persona): # funcion para actulizar
        with Cursor_del_pool() as cursor: # obtengo la conexion de cursor
            valores = (persona._nombre, persona._apellido, persona._email, persona.id_persona) # aqui pido los valores atravez de los metodos getter
            cursor.execute(cls._ACTUALIZAR, valores) # paso los valores
            log.debug (f'Persona actualizada {persona}')
            return cursor.rowcount # cuenta los registros actualizados
    
    @classmethod
    def eliminar(cls, persona): # funcion para eliminar
        with Cursor_del_pool() as cursor: # obtengo la conexion de cursor
            valores = (persona.id_persona,) # valores de la persona a eliminar
            cursor.execute(cls._ELIMINAR,valores) # paso los valores y llama a la sentencia eliminar
            log.debug(f'Registro eliminado: {persona}') #muestra un mensaje a nivel debug de la persona eliminada
            return cursor.rowcount # cuenta los registros eliminados
            
if __name__ == '__main__':
    personas1 = Manejo_dao.selecionar()
    for persona in personas1:
        log.debug(persona)

   # persona2 = Persona(nombre='Pedro', apellido = 'Gutierrez', email='Pgutierrez@mail.com')
   # personas_agregadas = Manejo_dao.insertar(persona2)
    #log.debug(f'personas agregadas: {personas_agregadas}')

    #persona = Persona(8,'Carlos', 'Esparza', 'Cezperza@mail.com')
    #persona_actualizadas = Manejo_dao.actualizar(persona)
    #log.debug(f'personas actualizadas: {persona_actualizadas}')

    #persona = Persona(id_persona=11)
    #personas_eliminadas = Manejo_dao.eliminar(persona)
    #log.debug(f'Pesonas eliminadas: {personas_eliminadas}')


