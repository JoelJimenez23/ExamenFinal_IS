import unittest
import json  # Importar json para manejar respuestas JSON
from app import app

class TestMensajeria(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Pruebas de éxito (4)
    def test_listar_contactos_exito(self):
        response = self.app.get("/mensajeria/contactos?mialias=cpaz")
        self.assertEqual(response.status_code, 200)
        self.assertIn("lmunoz", response.get_json())

    def test_agregar_contacto_exito(self):
        response = self.app.post("/mensajeria/contactos/cpaz", json={"contacto": "nuevo", "nombre": "Nuevo Usuario"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Contacto agregado exitosamente", response.get_data(as_text=True))

    def test_enviar_mensaje_exito(self):
        response = self.app.post(
            "/mensajeria/enviar", 
            json={"usuario": "cpaz", "contacto": "mgrau", "mensaje": "Hola, Miguel!"}
        )
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data.get("mensaje"), "Mensaje enviado exitosamente")

    def test_mensajes_recibidos_exito(self):
        response = self.app.get("/mensajeria/recibidos?mialias=mgrau")
        self.assertEqual(response.status_code, 200)

    # Pruebas de error (3)
    def test_agregar_contacto_existente_error(self):
        response = self.app.post("/mensajeria/contactos/cpaz", json={"contacto": "lmunoz", "nombre": "Luisa"})
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data.get("error"), "El contacto ya existe")

    def test_enviar_mensaje_contacto_invalido_error(self):
        response = self.app.post(
            "/mensajeria/enviar", 
            json={"usuario": "cpaz", "contacto": "desconocido", "mensaje": "Hola"}
        )
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data.get("error"), "El contacto no está en la lista")

    def test_listar_contactos_usuario_inexistente_error(self):
        response = self.app.get("/mensajeria/contactos?mialias=inexistente")
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data.get("error"), "Usuario no encontrado")

if __name__ == "__main__":
    unittest.main()
