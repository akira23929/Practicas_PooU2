import  mysql . conector

clase  Registro_datos ():
    def  __init__ ( auto ):
        uno mismo conexión  =  mysql . conector _ conectar ( anfitrión = 'localhost' ,
                                            base de datos  = 'base_datos' ,
                                            usuario  =  'raíz' ,
                                            contraseña  = 'administrador' )
    def  inserta_producto ( self , codigo , nombre , modelo , precio , cantidad ):
        cur  =  uno mismo . conexión _ cursor ()
        sql = '''INSERTAR EN productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD)
        VALORES('{}', '{}','{}', '{}','{}')''' . formato ( código , nombre , modelo , precio , cantidad )
        cur . ejecutar ( sql )
        uno mismo conexión _ cometer ()    
        cur . cerrar ()
    def  buscar_productos ( self ):
        cursor  =  uno mismo . conexión _ cursor ()
        sql  =  "SELECCIONAR * DE productos " 
        cursor _ ejecutar ( sql )
        registro  =  cursor . buscar ()
        volver  registro

    def  busca_producto ( self , nombre_producto ):
        cur  =  uno mismo . conexión _ cursor ()
        sql  =  "SELECT * FROM productos WHERE NOMBRE = {}" . formato ( nombre_producto )
        cur . ejecutar ( sql )
        nombrex  =  cur . buscar ()
        cur . cerrar ()     
        volver  nombrex

    def  elimina_productos ( self , nombre ):
        cur  =  uno mismo . conexión _ cursor ()
        sql = '''ELIMINAR DESDE productos WHERE NOMBRE = {}''' . formato ( nombre )
        cur . ejecutar ( sql )
        nom  =  cur . número de filas
        uno mismo conexión _ cometer ()    
        cur . cerrar ()
         nombre de retorno   
    def  actualiza_productos ( self , codigo , nombre , modelo , precio , cantidad ):
        cur  =  uno mismo . conexión _ cursor ()
        sql  = '''ACTUALIZAR productos SET CODIGO =' {}' , MODELO = '{}', PRECIO = '{}', CANTIDAD = '{}'
        WHERE NOMBRE = '{}' ''' . formato ( código ,   modelo , precio , cantidad , nombre )
        cur . ejecutar ( sql )
        acto  =  cur . número de filas
        uno mismo conexión _ cometer ()    
        cur . cerrar ()
         acto de regreso  
