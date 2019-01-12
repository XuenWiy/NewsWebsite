from datetime import timedelta

import logging
from redis import StrictRedis

# 设置配置信息
class Config(object):
    # 调试信息
    DEBUG = True
    SECRET_KEY = "fjewief"
    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/secondnews"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置ｓｅｓｓｉｏｎ信息
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=2)

    # 默认日志级别
    LEVEL_NAME = logging.DEBUG


# 开发环境配置信息
class DevelopConfig(Config):
    pass



# 生产环境配置信息
class ProductConfig(Config):
    DEBUG = False

    LEVEL_NAME = logging.ERROR


# 测试环境配置信息
class TestConfig(Config):
    pass

# 提供一个统一的访问入口
config_dict = {
    "develop":DevelopConfig,
    "product":ProductConfig,
    "test":TestConfig

}