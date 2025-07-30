from My_logger import logging

def add(a,b):
    logging.debug("Addition operation is taking place`")
    return a+b

logging.debug("Addition function called")
add(12,1)