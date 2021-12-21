import pytest
from tests.unit.base import BaseTests


class TestUser(BaseTests):
  
  def create_user(self, app): 
    user = {
      'name': 'Test',
      'password': '123',
      'email': 'test@varejao.com.br'
    }

    response = app.test_client().post(
      '/api/users',
      json=user
    )

    return response

  def validate_user(self, app, user):
    user = {
      'email': 'test@varejao.com.br',
      'password': '123'
    }

    response = app.test_client().post(
      '/api/signin',
      json=user
    )

    return response

  def test_create_valid_user(self, app):
    response = self.create_user(app)
    assert response.json['email'] == 'test@varejao.com.br'

  def test_create_unvalid_user_no_email(self, app):
    user = {
      'name': 'Oscar',
      'password': '123'
    }

    response = app.test_client().post(
      '/api/users',
      json=user
    )

    assert response.status_code == 400

  def test_create_unvalid_user_no_pass(self, app):
    user = {
      'email': '123123@1dwaskjd.com',
      'name': 'Oscar',
    }

    response = app.test_client().post(
      '/api/users',
      json=user
    )

    assert response.status_code == 400

  def test_create_invalid_user_no_name(self, app):
    user = {
      'email': '123123@1dwaskjd.com',
      'password': '123'
    }

    response = app.test_client().post(
      '/api/users',
      json=user
    )

    assert response.status_code == 400

  def test_signin_with_invalid_credentials(self, app):
    user = {
      'email': 'test@varejao.com.br',
      'password': '123'
    }

    response = app.test_client().post(
      '/api/signin',
      json=user
    )

    assert response.status_code == 500

  def test_signin_with_valid_credentials(self, app):
    created_user = self.create_user(app)
    validated_user = self.validate_user(app, created_user)

    assert validated_user.status_code == 200 and validated_user.headers['authentication-token'] is not None
    
  def test_validate_token_with_invalid_token(self, app):
    response = app.test_client().post(
      '/api/token/validate',
      headers={'authentication-token': '123'}
    )

    assert response.status_code == 500

  def test_validate_token_with_valid_token(self, app):
    created_user = self.create_user(app)
    validated_user = self.validate_user(app, created_user)

    response = app.test_client().post(
      '/api/token/validate',
      headers={'authentication-token': validated_user.headers['authentication-token']}
    )

    assert response.status_code == 200 and response.json['email'] == 'test@varejao.com.br'
  