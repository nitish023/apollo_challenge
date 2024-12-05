from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Qwerty_105@localhost/apollo')
try:
    connection = engine.connect()
    print("Database connected!")
    connection.close()
except Exception as e:
    print("Database connection failed:", e)