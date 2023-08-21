import psycopg

cur=None

def create_table(table_name,contenido):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS  {table_name}({contenido}) 
                """);
        CONN_STRING.commit()
        print("Tabla creada")
    except Exception as error:
        print (error)
        print("hubo un error")
    finally:
        if cur is not None:
            cur.close()
        elif CONN_STRING is not None:
            CONN_STRING.close()



def insert(table_name,values):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        insert_query=f"""INSERT INTO {table_name}(
                    juego,
                    personaje,
                    jefe) 
                    VALUES (%s,%s,%s) 
                """
        for input in values:
            cur.execute(insert_query,input);
        CONN_STRING.commit()
        print("Valores añadidos")
    except Exception as error:
        print (error)
        print("hubo un error")
    finally:
        if cur is not None:
            cur.close()
        elif CONN_STRING is not None:
            CONN_STRING.close()

#create_table("ToDo", ("id SERIAL PRIMARY KEY, Titulo VARCHAR(255) NOT NULL, Descripcion VARCHAR(255) NOT NULL, Estado BOOL, fecha_de_creacion DATE"))
create_table("Autor", ("id SERIAL PRIMARY KEY, Nombre VARCHAR(255) NOT NULL, Apellido_P VARCHAR(255) NOT NULL, Apellido_M VARCHAR(255) NOT NULL, Correo_electronico VARCHAR(255) NOT NULL, contraseña VARCHAR(255) NOT NULL"))

#insert(("dark_souls"),[("ds3","Kikler","Midir")])
