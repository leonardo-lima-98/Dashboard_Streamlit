from decouple import config
from sqlalchemy import create_engine

TIME_ZONE = 'America/Sao_Paulo'
USE_L10N = True
USE_TZ = True

SECRET_KEY = config('SECRET_KEY', default='')
DB_TYPE = config("DB_TYPE", default='')
DB_HOST = config("DB_HOST", default='')
DB_PORT = config("DB_PORT", default='1433')
DB_USER = config("DB_USER", default='')
DB_PASSWORD = config("DB_PASSWORD", default='')
DB_NAME = config("DB_NAME", default='')

# Criar a string de conexão
CONNECTION_STRING = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

try:
    # Criar a conexão
    engine = create_engine(CONNECTION_STRING)
    with engine.connect() as conn:
        # Testar uma consulta simples
        result = conn.execute("SELECT top 1 * from tarefa")
        print("Conexão bem-sucedida!")
        for row in result:
            print(f"Resultado: {row}")
except Exception as e:
    print("Erro ao conectar ao banco de dados:")
    print(e)
