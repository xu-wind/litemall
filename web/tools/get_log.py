import logging.handlers
import time


class GetLog:
    log = None

    def get_log(self):
        if self.log is None:
            # 获取logger
            self.log = logging.getLogger()
            # 设置级别
            self.log.setLevel(logging.INFO)
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/{}.log".format(time.strftime("%Y-%m-%d")),
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            th.setFormatter(fm)
            # 将处理器添加到logger日志器
            self.log.addHandler(th)
        return self.log
