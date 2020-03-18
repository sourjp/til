''' Loggingについて

import logging
https://docs.python.org/ja/3/library/logging.html
https://docs.python.org/ja/3/howto/logging-cookbook.html#logging-cookbook


logging.basicConfig:
    level: DEFAULTのレベルはWARNINGまで
        CRITICAL, ERROR, WARNING, INFO, DEBUG

    filename: ログファイルの出力を指定
        logging.basicConfig(filename='log.log', format=formatter)

    format: 出力されるログのフォーマットを変更できる

logger:
    logging以下で個別のログ設定を管理できる

handler:
    logのhandler


Reference: https://qiita.com/shotakaha/items/0fa2db1dc8253c83e2bb
    下記は良い感じ。
    ・fhにてファイル書き込みの内容を指定
    ・chにてコンソール用の内容を管理

    def setup_logger(name, logfile='LOGFILENAME.txt'):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # create file handler which logs even DEBUG messages
        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.DEBUG)
        fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
        fh.setFormatter(fh_formatter)

        # create console handler with a INFO log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        ch.setFormatter(ch_formatter)

        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    これをlogging.pyなどで用意し、importしてsetup_logger(__name__)で一元管理できる

'''

import logging

formatter = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logger = logging.getLogger(__name__)
logger.info('This log from main')


from logtest import do_something
do_something()
