import sys

from oslo_config import cfg
import oslo_i18n
from oslo_log import log
import oslo_messaging

import pbr.version


PROJECT_NAME = 'clapton'
version_info = pbr.version.VersionInfo(PROJECT_NAME)


def prepare_service(argv=None, config_files=None):
    oslo_i18n.enable_lazy()
    log.register_options(cfg.CONF)
    if argv is None:
        argv = sys.argv
    cfg.CONF(argv[1:], project=PROJECT_NAME, validate_default_values=True,
             version=version_info.version_string(),
             default_config_files=config_files)
    log.setup(cfg.CONF, PROJECT_NAME)
    oslo_messaging.set_transport_defaults(PROJECT_NAME)
