import unittest
from unittest.mock import patch

from flask_testing import TestCase

from modules.config.config import cfg

# update config according to the tests, we use sqlite in the memory to simulate database, (Not really a standard works very well ;) )
cfg.DB_URI = 'sqlite:///:memory:'

import modules.api.app
from modules.api.app import app, db, User, init_db, github, check_auth


class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        init_db()
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRoutes(TestBase):

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_create_user(self, mock_check_auth):
        mock_check_auth.return_value = True
        response = self.client.post('/user', json={'name': 'test', 'email': 'test@test.com', 'location': 'test'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()

        self.assertEqual(type(data), int)
        self.assertGreaterEqual(data, 1)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_create_user_invalid_request(self, mock_check_auth):
        mock_check_auth.return_value = True
        response = self.client.post('/user', json={'name': 'test', 'email': 'test@test.com', 'location': 'test',
                                                   'alma': 'apple'})
        data = response.get_json()
        self.assertIn("error", data)
        self.assertIn("Additional properties are not allowed", data['error'])
        self.assertEqual(response.status_code, 400)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_create_user_empty_request(self, mock_check_auth):
        mock_check_auth.return_value = True
        response = self.client.post('/user', json={})
        data = response.get_json()
        self.assertIn("error", data)
        self.assertIn("'name' is a required property", data['error'])
        self.assertEqual(response.status_code, 400)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_create_user_without_name(self, mock_check_auth):
        mock_check_auth.return_value = True
        response = self.client.post('/user', json={"email": "example@exmaple.com", "location": "test"})
        data = response.get_json()
        self.assertIn("error", data)
        self.assertIn("'name' is a required property", data['error'])
        self.assertEqual(response.status_code, 400)

    @patch.object(modules.api.app, 'check_auth', return_value=False)
    def test_without_auth_create_user(self, mock_check_auth):
        mock_check_auth.return_value = False
        response = self.client.post('/user', json={'name': 'test', 'email': 'test@test.com', 'location': 'test'})
        self.assertEqual(response.status_code, 401)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_get_user(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/user/{user.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'test')
        self.assertEqual(data['email'], 'test@test.com')

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_get_users(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/users')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data[0]['name'], 'test')
        self.assertEqual(data[0]['email'], 'test@test.com')

    @patch.object(modules.api.app, 'check_auth', return_value=False)
    def test_get_users_auth(self, mock_check_auth):
        mock_check_auth.return_value = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/users')
        self.assertEqual(response.status_code, 401)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_get_user_invalid_id(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/user/32333')
        self.assertEqual(response.status_code, 404)

    @patch.object(modules.api.app, 'check_auth', return_value=False)
    def test_without_auth_get_user(self, mock_check_auth):
        mock_check_auth.return_value = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/user/{user.id}')
        self.assertEqual(response.status_code, 401)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_update_user(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.put(f'/user/{user.id}', json={'name': 'updated'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'updated')

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_update_user_invalid_request(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.put(f'/user/{user.id}', json={'test': 'updated'})
        data = response.get_json()
        self.assertIn("error", data)
        self.assertIn("Additional properties are not allowed", data['error'])
        self.assertEqual(response.status_code, 400)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_update_user_empty_request(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.put(f'/user/{user.id}', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'test')

    @patch.object(modules.api.app, 'check_auth', return_value=False)
    def test_without_auth_update_user(self, mock_check_auth):
        mock_check_auth.return_value = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.put(f'/user/{user.id}', json={'name': 'updated'})
        self.assertEqual(response.status_code, 401)

    @patch.object(modules.api.app, 'check_auth', return_value=True)
    def test_delete_user(self, mock_check_auth):
        mock_check_auth.return_value = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.delete(f'/user/{user.id}')
        self.assertEqual(response.status_code, 204)

    @patch.object(modules.api.app, 'check_auth', return_value=False)
    def test_delete_user_without_login(self, mock_check_auth):
        mock_check_auth.return_value = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        user = User(name='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.delete(f'/user/{user.id}')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
