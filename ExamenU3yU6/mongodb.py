# clase para conectarnos a mongodb
import pymongo
from conf import variables as varmongo
class Pymongo:
    def __init__(self,variables): # host = 'localhost', db='opensource', port = '27017', timeout=1000, user='', password=''
        self.MONGO_DATABASE = variables["bd"]
        self.MONGO_URL = 'mongodb://' + variables["host"] + ':' + variables["port"]
        self.MONGO_CLIENT = None
        self.MONGO_RESPUESTA = None
        self.MONGO_TIMEOUT = variables["timeout"]

    documento = productos = [{"idProducto": 1850, "productoNombreCorto": "William Lawsons Std",
                  "productoNombreLargo": "Whisky William Lawsons Std 750 ml",
                  "productoDescripcion": "Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave.",
                  "productoTipo": 1, "productoPresentacion": "Botella", "productoCosto": 170.5, "productoGanancia": 15,
                  "productoDescuento": 0, "productoExistencia": 1000, "productoImagen": "Whisky-1850.webp"},
                 {"idProducto": 1450, "productoNombreCorto": "Outer Space",
                  "productoNombreLargo": "Vodka Outer Space 750 ml",
                  "productoDescripcion": "Es un vodka hecho con maíz 100% americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos.",
                  "productoTipo": 1, "productoPresentacion": "Botella", "productoCosto": 700.5, "productoGanancia": 15,
                  "productoDescuento": 0, "productoExistencia": 1000, "productoImagen": "Vodka-1450.webp"},
                 {"idProducto": 850, "productoNombreCorto": "Ron Antillano Blanco",
                  "productoNombreLargo": "Ron Antillano Blanco C/Vaso/Macerador 1L", "productoDescripcion": "",
                  "productoTipo": 1, "productoPresentacion": "Botella", "productoCosto": 150.5, "productoGanancia": 15,
                  "productoDescuento": 0, "productoExistencia": 1000, "productoImagen": "Ron-850.webp"}]

    def conectar_mongodb(self):
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_URL, serverSelectionTimeOutMS=self.MONGO_TIMEOUT)  # Conectado
        except Exception as error:
            print("Error" ,error)
        else:
            pass
            #print("Conexion al servidor de Mongodb realizado")
        #finally:

    def desconectar_mongodb(self):
        if self.MONGO_CLIENT:
            self.MONGO_CLIENT.close()


    def insertar(self,tabla,documento):
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self. MONGO_DATABASE][tabla].insert_one(documento)
        if self.MONGO_RESPUESTA:
            return self.MONGO_RESPUESTA
        else:
            return None





obj_mongo =Pymongo(varmongo)
obj_mongo.conectar_mongodb()
#obj_mongo.consulta_mongodb('estudiantes')
#obj_mongo.insertar_estudiante(alumno)
obj_mongo.desconectar_mongodb()
