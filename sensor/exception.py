import sys,os

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() #print(_,_,exc_tb) nothing is printed.
    file_name = exc_tb.tb_frame.f_code.co_filename
    print(file_name) #print(file_name) nothing is printed.
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message #print(error_message)



class SensorException(Exception):

    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message