
import os
import pem


def check_env_variable(name):
    """This function checks for Env variables, it quits the code if not found."""
    if os.environ.get(name) is None:
        print('Variable {0} not found!'.format(name))
        quit()
    else:
        return os.environ.get(name)


def get_public_key(file):
    file_name = os.path.join(os.getcwd(), file)
    cert = pem.parse_file(file_name)
    return str(cert[0])


class Config:
    def __init__(self):
        self.jwt_algorithm = check_env_variable('JWT_ALG')
        self.public_key_file = check_env_variable('JWT_PK')
        self.slack_token = check_env_variable('SLACK_TOKEN')

    def get_jwt_algorithm(self):
        return self.jwt_algorithm

    def get_jwt_public_key(self):
        return get_public_key(self.public_key_file)

    def get_slack_token(self):
        return self.slack_token


