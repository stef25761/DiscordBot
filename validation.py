
class Validation():

    def validateToken(self,token):
        if len(token) == 59:
            if token[24:25] == "." and token[31:32] == ".":
                return True


