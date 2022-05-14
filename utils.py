import logging 
import functools
import os, time

class CustomFormatter(logging.Formatter):

    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)

def create_logger(log_file_name):
    """
    Creates a logging object and returns it
    """

    log_dir = './logs_dir/'
    log_dir = os.path.join(log_dir)

    # Create Log file directory if not exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Build Log File Full Path
    logPath = log_file_name if os.path.exists(log_file_name) else os.path.join(log_dir, (str(log_file_name) + '.log'))
     # Create logger object and set the format for logging and other attributes
    logger = logging.Logger(log_file_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(logPath, 'a+')
    """ Set the formatter of 'CustomFormatter' type as we need to log base function name and base file name """
    handler.setFormatter(CustomFormatter('%(asctime)s - %(levelname)-10s - %(filename)s - %(funcName)s - %(message)s'))
    logger.addHandler(handler)
    
    stream_hanlder = logging.StreamHandler()
    stream_hanlder.setFormatter(CustomFormatter('%(asctime)s - %(levelname)-10s - %(filename)s - %(funcName)s - %(message)s'))
    logger.addHandler(stream_hanlder)

    
    return logger

def exception(logger):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
    
    @param logger: The logging object
    """
    
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception
                err = "[EXECPTION] in  "
                err += func.__name__
                logger.exception(err)
                # re-raise the exception
                raise 
            
            
        return wrapper
    return decorator

def timed(logger):
    def decorator(func):
        """This decorator prints the execution time for the decorated function."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.debug("{} ran in {}s".format(func.__name__, round(end - start, 2)))
            return result

        return wrapper
    
    return decorator