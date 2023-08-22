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

def insert(table_name,values,colums,mod):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        if mod==1:
            insert_query=f"""INSERT INTO {table_name}({colums}) 
                        VALUES (%s,%s,%s) 
                    """
        elif mod==2:
                insert_query=f"""INSERT INTO {table_name}({colums}) 
                        VALUES (%s,%s,%s,%s,%s) 
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

def update_todo(values):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        update_t=f"UPDATE ToDo SET Titulo=%s, Descripcion=%s, Estado=%s WHERE id=%s"
        cur.execute(update_t,values);
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

def update_autor(values):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        update_t=f"UPDATE Autor SET Nombre=%s, Apellido_P=%s, Apellido_M=%s, Correo_electronico=%s, contraseña=%s WHERE id=%s"
        cur.execute(update_t,values);
        CONN_STRING.commit()
        print("Datos actualizados")
    except Exception as error:
        print (error)
        print("hubo un error")
    finally:
        if cur is not None:
            cur.close()
        elif CONN_STRING is not None:
            CONN_STRING.close()

def update_estado(values):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        try:
            update_t=f"UPDATE ToDo SET Estado=%s WHERE id=%s"
        except Exception as error:
            print(error)
            print("Se detecto un error")
        cur.execute(update_t,values);
        CONN_STRING.commit()
        print("Cambio de estado realizado")
    except Exception as error:
        print (error)
        print("hubo un error")
    finally:
        if cur is not None:
            cur.close()
        elif CONN_STRING is not None:
            CONN_STRING.close()

def delete(table_name,value):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE id={value} ")
        CONN_STRING.commit()
        print("Fila borrada")
    except Exception as error:
        print (error)
        print("hubo un error")
    finally:
        if cur is not None:
            cur.close()
        elif CONN_STRING is not None:
            CONN_STRING.close()

def read(table_name,value):
    try:
        CONN_STRING=psycopg.connect("dbname=tareas user=postgres password= host=localhost")
        print("Conexion exitosa")
        cur=CONN_STRING.cursor()
        cur.execute(f"SELECT * FROM {table_name} WHERE id={value}")
        print(cur.fetchone())
    except Exception as error:
        print (error)
        print("hubo un error")
    finally:
        if cur is not None:
            cur.close()
        elif CONN_STRING is not None:
            CONN_STRING.close()


#create_table("ToDo", ("id SERIAL PRIMARY KEY, Titulo VARCHAR(255) NOT NULL, Descripcion VARCHAR(255) NOT NULL, Estado BOOL, fecha_de_creacion DATE DEFAULT CURRENT_DATE"))
#create_table("Autor", ("id SERIAL PRIMARY KEY, Nombre VARCHAR(255) NOT NULL, Apellido_P VARCHAR(255) NOT NULL, Apellido_M VARCHAR(255) NOT NULL, Correo_electronico VARCHAR(255) NOT NULL, contraseña VARCHAR(255) NOT NULL"))

#values_ToDo=("Titulo, Descripcion,Estado")
#values_autor=("Nombre, Apellido_P, Apellido_M, Correo_electronico, contraseña")

#insert(("ToDo"),[("Practica1","trabajo de postgres",True)],(values_ToDo),1)
#insert(("Autor"),[("Erwin","Romel","Guderian","guerra_relampago@hotmail.com","123")],(values_autor),2)


#update_todo(("Proyecto alfred1", "Proyecto en equipos con clases",True,"2"))
#update_autor(("Marcos", "Gutierrez","Gutierrez","marcos@gamil.com","123","4"))
#update_estado((False,"1"))

#delete("ToDo","3")

#read("ToDo","1")
read("Autor","3")