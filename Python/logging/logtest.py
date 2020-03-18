''' logging.pyの説明補足用のファイル

mainプログラムから使われる時に、
Loggerを利用しておけばログの出どころと出力レベルが管理できる

'''

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def do_something():
    logger.info('from logtest')
    logger.debug('from logtest debug')
