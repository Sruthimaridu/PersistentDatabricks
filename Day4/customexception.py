class CustomError(Exception):
    pass
class ValidationError(Exception):
    def __init__(self,msg,code=None):
        super().__init__(msg)
        self.code=code
def validate_age(age):
    if age<0:
        raise ValidationError("age cannot be negative",code="NEGATIVE AGE")
    if age>150:
        raise ValidationError("age seems unreal",code="UNREALISTIC_AGE")
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"validation failed: {e}")
        print(f"error code:{e.code}")