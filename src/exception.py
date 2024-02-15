import sys
import logging

#whenever exception gets raised, custom message is displayed
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #gives very specific info like which file, which line
    file_name = exc_tb.tb_frame.f_code.co_filename #to get file name
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
        
    
class CustomException(Exception):
    def __init__ ( self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail) #gettig populated from the abaove function

    def __str__(self):
        return self.error_message

    