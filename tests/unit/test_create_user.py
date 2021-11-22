import pytest
from api import application
from api.config import DATABASE_URL
import mysql.connector


class TestCreateUser:

  @pytest.fixture(scope='module')
  def app(self):
    app = application()
    return app

  @pytest.fixture(autouse=True)
  def db_check(tmpdir):
    mydb = mysql.connector.connect(
      host="localhost",
      user="admin",
      password="admin",
      database="admin"
    )

    mycursor = mydb.cursor()
    sql = f"DELETE FROM users WHERE email = 'oscar@varejao.com.br'"
    mycursor.execute(sql)
    mydb.commit()


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

    assert response.json['email'] == 'oscar@varejao.com.br'

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

  def test_create_unvalid_user_no_name(self, app):
    user = {
      'email': '123123@1dwaskjd.com',
      'password': '123'
    }

    response = app.test_client().post(
      '/api/users',
      json=user
    )

    assert response.status_code == 400
    