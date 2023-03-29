from conexion import log
from conexion import Conexion

# Se define la clase "Cursor"
class Cursor_del_pool:
    
    # Se define el constructor de la clase
    def __init__(self):
        self._cursor = None
        self._cursor = None
    
    # Se define el método "__enter__", que se ejecuta al inicio del bloque de contexto
    def __enter__(self): 
        # Se registra un mensaje 
        log.debug('Inicio del metodo __enter__')
        # Se establece la conexión con la base de datos
        self._conexion = Conexion.obtener_conexion()
        # Se crea un cursor 
        self._cursor = self._conexion.cursor()
        # Se devuelve el cursor 
        return self._cursor

    # Se define el método "__exit__", que se ejecuta al final del bloque
    def __exit__(self, tipo_exepcion, valor_exepcion, detalle_exepcion):
        # Se registra un mensaje 
        log.debug('Se ejecuta el metodo __exit__')
        # Si se produce alguna excepción  utiliza rollback de la conexión para deshacer los cambios
        if valor_exepcion: 
            self._conexion.rollback
            # Se registra un mensaje de error 
            log.error(f'Ocurrio un error: {valor_exepcion}, {tipo_exepcion}, {detalle_exepcion}')
        # Si no se produce ninguna excepción  se hace commit
        else: 
            self._conexion.commit()
            # Se registra un mensaje de depuración utilizando el objeto "log"
            log.debug('Se realizo un commit')
        # se cierra el cursor
        self._cursor.close()
        # se cierra la conexion
        Conexion.liberar_conexion(self._conexion)
    
if __name__ == "__main__":
    with Cursor_del_pool() as cursor:
        log.debug('Dentro del with') # manda un mensaje para saber que esta dentro del with
        cursor.execute('SELECT * FROM persona') # ejecuta la sentencia SQL select
        log.debug(cursor.fetchall()) # muestra todos los registros de la tabla



