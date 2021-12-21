import pytest
from api import application
import mysql.connector


class BaseTests:

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
    sql = f"DELETE FROM users WHERE email = 'test@varejao.com.br'"
    mycursor.execute(sql)
    mydb.commit()