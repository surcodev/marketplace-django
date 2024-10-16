from django.test import TestCase
from django.contrib.auth import get_user_model
from perfil.models import Cliente, Administrador
from geografia.models import Departamento, Provincia, Distrito

# Obtener el modelo User personalizado
User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        """Configuración de datos de prueba para usuarios"""
        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            username='richarq',
            email='richar@example.com',
            password='password123',
            is_admindisco=False
        )

    def test_user_creation(self):
        """Probar que el usuario se crea correctamente"""
        self.assertEqual(self.user.username, 'richarq')
        self.assertEqual(self.user.email, 'richar@example.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_admindisco)

    def test_email_unique(self):
        """Probar que el correo electrónico es único"""
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='duplicado',
                email='richar@example.com',
                password='password456'
            )

class ClienteModelTest(TestCase):
    def setUp(self):
        """Configuración de datos de prueba para clientes"""
        self.user = User.objects.create_user(
            username='mariaq',
            email='maria@example.com',
            password='password123'
        )
        self.cliente = Cliente.objects.create(
            user=self.user,
            telefono='999888777',
            direccion='Av. Lima 123'
        )

    def test_cliente_creation(self):
        """Probar que el cliente se crea correctamente y está relacionado con un usuario"""
        self.assertEqual(self.cliente.user.username, 'mariaq')
        self.assertEqual(self.cliente.telefono, '999888777')
        self.assertEqual(self.cliente.direccion, 'Av. Lima 123')

class AdministradorModelTest(TestCase):
    def setUp(self):
        """Configuración de datos de prueba para administradores"""
        # Crear instancias de geografía
        self.departamento = Departamento.objects.create(nombre='Lima')
        self.provincia = Provincia.objects.create(nombre='Lima', departamento=self.departamento)
        self.distrito = Distrito.objects.create(nombre='Miraflores', provincia=self.provincia)
        
        # Crear un usuario
        self.user = User.objects.create_user(
            username='adminq',
            email='admin@example.com',
            password='password123',
            is_admindisco=True
        )
        
        # Crear un administrador
        self.administrador = Administrador.objects.create(
            user=self.user,
            nombre_admin='Carlos Q.',
            nombre_discoteca='Discoteca XYZ',
            razon_social='Discoteca XYZ S.A.C.',
            ruc='12345678901',
            departamento=self.departamento,
            provincia=self.provincia,
            distrito=self.distrito,
            direccion='Av. Siempre Viva 742',
            telefono='987654321',
            correo_personal='admin@personal.com'
        )

    def test_administrador_creation(self):
        """Probar que el administrador se crea correctamente y está relacionado con un usuario"""
        self.assertEqual(self.administrador.user.username, 'adminq')
        self.assertEqual(self.administrador.ruc, '12345678901')
        self.assertEqual(self.administrador.nombre_admin, 'Carlos Q.')
        self.assertEqual(self.administrador.telefono, '987654321')

    def test_ruc_unique(self):
        """Probar que el RUC es único"""
        with self.assertRaises(Exception):
            Administrador.objects.create(
                user=self.user,
                nombre_admin='Otro Admin',
                nombre_discoteca='Otra Discoteca',
                razon_social='Otra Discoteca S.A.C.',
                ruc='12345678901',  # Mismo RUC que el anterior
                departamento=self.departamento,
                provincia=self.provincia,
                distrito=self.distrito,
                direccion='Otra dirección',
                telefono='999999999'
            )
