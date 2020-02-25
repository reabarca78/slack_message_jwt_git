import jwt
import json


class jwt_module:

    def __init__(self, jwt_public_key, jwt_algorithm, jwt_object):
        self.public_key = jwt_public_key
        self.algorithm = jwt_algorithm
        self.jwt_object = jwt_object

    def jwt_decode(self, value):
        try:
            Decode = jwt.decode(self.jwt_object, self.public_key, self.algorithm)
            Dictionary = json.dumps(Decode)
            jsonObjectInfo = json.loads(Dictionary)
            result = jsonObjectInfo[value]
        except:
            result = "401"
        return result

    def jwt_token(self):
        Token = self.jwt_decode("Token")
        return Token

