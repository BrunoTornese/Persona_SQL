import logging as log
from psycopg2 import pool
import sys

log.basicConfig(level=log.DEBUG,
                format= '%(asctime)s - %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                # aqui muestro la hora, el nivel del error la linea y el mensaje que le agrego al log
                datefmt = '%I:%M:%S %p', # aqui modifico la forma en que se muestra la fecha
                handlers= [ #configuro la informacion de la consola vaya a un archivo
                    log.FileHandler('capa_datos.log'), # el archivo que se va a mandar
                    log.StreamHandler() # se encarga de que los archivos se manden a la consola
                ])
class Conexion:
    _DATABASE = 'Test_bd' # le paso los valores de la database
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 0
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls): # clase para manejar el pool de conexiones
        if cls._pool is None: # si no se inicializo
            try:
                cls._pool = pool.SimpleConnectionPool (cls._MIN_CON, cls._MAX_CON,# se obtiene el pool de conexiones
                                        host = cls._HOST,
                                        user = cls._USERNAME, # Con los valores de la bd
                                        password = cls._PASSWORD,
                                        port = cls._DB_PORT,
                                       database = cls._DATABASE) 
                log.debug(f'Se creo el pool de manera exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(F'ocurrio un error al obtener el pool {e}')
                sys.exit() # se cierra el programa
        else: # si se inicializo el pool
            return cls._pool #retorna el pool
        
    @classmethod
    def obtener_conexion(cls): # funcion para obtener conexion
        log.debug(f'Obteniendo conexión del pool...') #envia un mensaje nivel debug de que esta obteniendo el pool
        conexion = cls.obtener_pool().getconn() # llama al metodo getconn para obtener una conexion de la piscina
        log.debug(f'Conexión obtenida del pool: {conexion}') #envia un mensaje nivel debug de que se obtuvo el pool
        return conexion

    
    @classmethod
    def liberar_conexion(cls, conexion): # metodo para liverar un pool
        log.debug(f'Liberando un pool')
        cls.obtener_pool().putconn(conexion) # con el metodo putconn regresa el pool al pool de conexiones
        log.debug(f'Pool liberado: {conexion}')
    
    @classmethod
    def cerrar_conexion(cls): # metodo cerrar todas las conexiones
        log.debug(f'Cerrando conexion')
        cls.obtener_pool().closeall() # cierra la conexion
        log.debug(f'Conexion cerrada {Conexion}')




    #@classmethod
    #def obtener_conexion(cls): # funcion para obtener conexion
      #  if cls._conexion is None:  # si no hay conecion
         #   try : # bloque try except para caputar un error
               # cls._conexion = bd.connect(host = cls._HOST, # le digo a que bd conectarme
                  #                      user = cls._USERNAME,
                  #                      password = cls._PASSWORD,
                  #                      port = cls._DB_PORT,
                  #                      database = cls._DATABASE) 
               # log.debug(f'Conexion exitosa: {cls._conexion}') 
               # return cls._conexion # manda un mensaje de exito al conectarse
           # except Exception as e: # si no se conecta muestra error
              #  log.error(f'Ocurrio un error al obtener la conexion {e}')
                #sys.exit() # cierra el programa
        #else: # si hay un metodo de conexion
            #return cls._conexion # retorna la conexion

    #@classmethod
    #def obtener_cursor(cls): # funcion para obtener el cursor
      #  if cls._cursor is None: # si no hay cursor
     #       try: # bloque try exept para captar el error
      #          cls._cursor = cls.obtener_conexion().cursor() # obtiene el cursor mediante la funcion de conexion
        #        log.debug(f'Se creo el cursor correctamente: {cls._cursor}')
       #         return cls._cursor # retorna el cursor
         #   except Exception as e:
        #        log.error(f'Ocurrio un error al obtener el cursor {e}')
         #       sys.exit() # si ocurrio un error cierra el programa
       # else: # si hay cursor
      #      return cls._cursor # lo retorna
    


if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    Conexion.cerrar_conexion()






