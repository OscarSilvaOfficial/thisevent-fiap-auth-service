import os

SECRET=os.getenv('SECRET', 'ashdfashdfuioahdeusifhjiaudhgvq390713984ryfuhif')
DATABASE_URL=os.getenv('DATABASE_URL', 'mysql+pymysql://admin:admin@localhost:3306/admin?charset=utf8mb4')