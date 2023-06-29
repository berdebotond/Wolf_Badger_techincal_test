import loguru
from modules.config.config import cfg

loguru.Level = cfg.LOG_LEVEL
Logger = loguru.logger
