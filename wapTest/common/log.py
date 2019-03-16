import logging
import logging.config
def logtest():
    CON_LOG='log.conf'
    logging.config.fileConfig(CON_LOG)
    logging.getLogger()

