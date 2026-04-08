import logging 
from config import LOG_PATH

occurence = 1

logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(filename)s | %(funcName)s | %(message)s",
  filename=LOG_PATH,
  filemode='a'
  )

def setup_logger (logger_name: str):
  logger = logging.getLogger(logger_name)
  return logger

if occurence == 1:
  log = setup_logger('logging')
  log.info("\n\nInitialising loging.", "-"*20)
  occurence += 10
