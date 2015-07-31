import sys

from oslo_config import cfg
from oslo_log import log


def bootstrap():
    log.register_options(cfg.CONF)
    cfg.CONF(sys.argv[1:], project='clapton', validate_default_values=True)
    log.setup(cfg.CONF, 'clapton')
