import pytest
from api import application
from sqlalchemy import create_engine
from api.config import DATABASE_URL
from sqlalchemy.orm import Session


class TestCreateUser:

  @pytest.fixture(scope='module')
  def app(self):
    app = application()
    return app

  def test_create_valid_user(self, app):
    user = {
      'name': 'Oscar',
      'password': '123',
      'email': 'oscar@varejao.com.br'
    }

    response = app.test_client().post(
      '/api/users',
      json=user
    )

    User = db.session.query(db.User).filter_by(email=user['email']).first()

    assert response.json['email'] == 'oscar@varejao.com.br'