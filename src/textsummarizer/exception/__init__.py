import sys


def error_message_format(error,error_detail)->str:
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message_form = 'Exception occured in "{0}" file at line number "{1}" and message "{2}"'.format(file_name,line_no,error)
    return error_message_form


class CustomException(Exception):

    def __init__(self,error,error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_format(error,error_detail)

    def __str__(self)->str:
        return self.error_message