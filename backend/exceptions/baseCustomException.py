class baseException(Exception):
    message = "baseCaseException"
    errorCode = 400
    def __init__(self,message = None, errorCode = None):
        if message:
            self.message = message
        if errorCode:
            self.errorCode =errorCode
        super().__init__(self.message)
        