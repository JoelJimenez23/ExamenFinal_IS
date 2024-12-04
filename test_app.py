import unittest
import json  # Importar json para manejar respuestas JSON
from app import app

class TestMensajeria(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_listar_contactos_exito(self):
        response = self.app.get("/mensajeria/contactos?mialias=cpaz")
        self.assertEqual(response.status_code, 200)
        self.assertIn("lmunoz", response.get_json())

    def test_agregar_contacto_exito(self):
        response = self.app.post("/mensajeria/contactos/cpaz", json={"contacto": "nuevo", "nombre": "Nuevo Usuario"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Contacto agregado exitosamente", response.get_data(as_text=True))

    def test_enviar_mensaje_contacto_invalido(self):
        response = self.app.post(
            "/mensajeria/enviar", 
            json={"usuario": "cpaz", "contacto": "desconocido", "mensaje": "Hola"}
        )
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_data(as_text=True))  # Convertir respuesta a diccionario
        self.assertEqual(response_data.get("error"), "El contacto no está en la lista")  # Comparar directamente

    def test_mensajes_recibidos_usuario_no_encontrado(self):
        response = self.app.get("/mensajeria/recibidos?mialias=inexistente")
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data(as_text=True))  # Convertir respuesta a diccionario
        self.assertEqual(response_data.get("error"), "Usuario no encontrado")  # Comparar directamente

if _name_ == "_main_":
    unittest.main()
