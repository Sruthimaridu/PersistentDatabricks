import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("hello")
logging.info("hello info")
logging.warning("hello warning")
logging.error("hello error")
logging.critical("hello critical")

##############################
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s- %(levelname)s-%(message)s'
)
logging.debug("hello")
logging.info("hello info")
logging.warning("hello warning")
logging.error("hello error")
logging.critical("hello critical")