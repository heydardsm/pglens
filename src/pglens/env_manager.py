import os

class EnvVariablesManager:

    @property
    def secret(self):
        secret_env = os.getenv('SECRET_KEY', None)
        if secret_env is None:
            raise Exception('SECRET_KEY is required')
        return secret_env
