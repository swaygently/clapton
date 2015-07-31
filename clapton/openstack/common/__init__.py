import sys

from oslo_config import cfg
from oslo_log import log

log.register_opts(cfg)
cfg.CONF(sys.argv[1:], project='clapton', validate_default_values=True)
log.setup(cfg.CONF, 'clapton')
