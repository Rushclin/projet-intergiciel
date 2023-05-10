import os 

def get_env_variable(name) -> str: 
    try: 
        return os.environ[name]
    except KeyError:
        message = "La variable d'environement ('{}') demandée n'existe pas ".format(name)
        raise Exception(message)