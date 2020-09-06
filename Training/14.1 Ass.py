class Error(Exception):
    pass


class CustomException(Error):
    pass


try:
    print("Try Block")
    raise CustomException
except CustomException:
    print("Error Block")
