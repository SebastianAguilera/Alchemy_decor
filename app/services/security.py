from abc import ABC, abstractmethod
from passlib.hash import pbkdf2_sha256
from werkzeug.security import generate_password_hash, check_password_hash

class AbstractSecurity(ABC):
    
    @staticmethod
    def generate_password(self, password: str) -> str:
        pass

    @staticmethod
    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        pass
    
class WerkzeugSecurity(AbstractSecurity):
    
    def generate_password(self, password: str) -> str:
        return generate_password_hash(password)
        
    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        return check_password_hash(hashed_password, plain_password)
    
class PassLibSecurity(AbstractSecurity):
    
    def generate_password(self, password: str) -> str:
        return pbkdf2_sha256.hash(password)
    
    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        return pbkdf2_sha256.verify(plain_password, hashed_password)
    
class SecurityManager:
    
    def __init__(self, security: AbstractSecurity):
        self.__security = security

    def generate_password(self, password: str ) -> str:
        return self.__security.generate_password(password)
    
    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        return self.__security.check_password(hashed_password, plain_password)