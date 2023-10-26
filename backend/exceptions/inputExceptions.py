from .baseCustomException import Base_exception


class Missing_field_exception(Base_exception):
    errorCode = 400
    def __init__(self,missing_args):
        super().__init__(f"missing {','.join(missing_args)}")
    
class Invalid_json_format_exception(Base_exception):
    message = "invalid json format"
    errorCode = 400