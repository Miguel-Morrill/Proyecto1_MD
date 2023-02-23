from schemas.user import User


class UserController:

    @staticmethod
    def create_user(rfc: str, curp: str, name: str, address: str, phone_number: int, email: str,
                    password: str) -> User:
        user = User(rfc=rfc,
                    curp=curp,
                    name=name,
                    address=address,
                    phone_number=phone_number,
                    email=email,
                    password=password)
        user.save()
        return user
