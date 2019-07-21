import logging
import os
global app_name
app_name = 'hahaha'
logger = logging.getLogger(app_name)

logging.basicConfig(level=logging.DEBUG,
                    filename=log_path,
                    format='%(asctime)s - %(levelname)s : %(name)s - %(filename)s -%(funcName)s() -No.%(lineno)d - %(message)s')

msg = '这是一条只有调试时才输出的日志'
logger.debug(msg)


msg = '证明事件按预期工作，可以输出也可以不输出'
logger.info(msg)

msg = '现在没问题，但将来可能出现问题'
logger.warning(msg)

msg = '严重的问题，部分功能已不能执行'
logger.error(msg)

msg = '致命型问题，程序崩溃'
logger.critical(msg)
