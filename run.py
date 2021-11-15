import os
from api import application
from dotenv import load_dotenv
from api.utils.scripts import create_databases, create_tables

load_dotenv(os.path.join('./.env')) 

create_databases()
create_tables()

app = application()

if __name__ == '__main__':
    app.run(debug=False)