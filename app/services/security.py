from werkzeug.security import generate_password_hash, check_password_hash

class Security:
    
    @staticmethod
    def generate_password(text: str ) -> str:
        return generate_password_hash(text)

    @staticmethod
    def check_password( text1:str, text2: str) -> bool:
        return check_password_hash(text1, text2)