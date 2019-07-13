import logging

# logging.basicConfig(level=logging.WARNING)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
# logging.getLogger().setLevel(logging.DEBUG)

logging.info('Info.....')
logging.warning('Warning ......')
logging.debug('Debug ........')