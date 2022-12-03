from conf import variables as varmongo
from mongodb import Pymongo


##Jesus Morgado Marquez
# 18420469


def insertar_estudiante():
    obj_Pymongo = Pymongo(varmongo)
    productos = [{"idProducto": 1850, "productoNombreCorto": "William Lawsons Std",
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

    for est in productos:
        json = {
            "idProducto": est['idProducto'],
            "productoNombreCorto": est["productoNombreCorto"],
            "productoNombreLargo": est["productoNombreLargo"],
            "productoDescripcion": est["productoDescripcion"],
            "productoTipo": est["productoTipo"],
            "productoPresentacion": est["productoPresentacion"],
            "productoCosto": est["productoCosto"],
            "productoGanancia": est["productoGanancia"],
            "productoDescuento": est["productoDescuento"],
            "productoExistencia": est["productoExistencia"],
            "productoImagen": est["productoImagen"]

        }

        obj_Pymongo.conectar_mongodb()
        obj_Pymongo.insertar("producto",json)
        obj_Pymongo.desconectar_mongodb()
        print("Datos insertados Correctamente")

insertar_estudiante()