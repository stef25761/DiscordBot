
class Validation():
    # TODO: validate gw2 api key
    def validateToken(self,token):
        if len(token) == 59:
            if token[24] == "." and token[31] == ".":
                return True


