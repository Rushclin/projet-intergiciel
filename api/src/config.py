from utils import get_env_variable

POSTGRES_URL = get_env_variable('POSTGRES_URL')
POSTGRES_USER = get_env_variable('POSTGRES_USER')
POSTGRES_PASSWORD = get_env_variable('POSTGRES_PASSWORD')
POSTGRES_DB = get_env_variable('POSTGRES_DB')

class Config(object):
    DEBUG = False
    TESTING = False

    uri_template = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PASSWORD,
        url=POSTGRES_URL,
        db=POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_PAGINATION_PER_PAGE = 10

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass 

def get_config(env = None): 
    if env is None:
        try: 
            env = get_env_variable('ENV')
        except Exception: 
            env = 'development'
            print("Variable d'environnement non definie, on pass en mode developpement")

    if env == 'production':
        return ProductionConfig()
    elif env == 'test':
        return TestConfig()
    
    return DevelopmentConfig()