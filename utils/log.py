import logging

logging.basicConfig(filename="./log_file.log",level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")

def get_log(text):
    try:
        logging.info(text)
    except Exception as e:
        logging.info("Exception in log_fun function occured.")
        logging.exception(str(e))
    