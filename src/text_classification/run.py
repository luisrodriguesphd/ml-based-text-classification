"""https://docs.kedro.org/en/0.16.2/04_user_guide/03_configuration.html#local-and-base-configuration"""

from kedro.framework.context import KedroContext
import os
from kedro.framework.project import settings

src_path = os.path.dirname(os.path.dirname(__file__))
project_path = os.path.dirname(src_path)
conf_path = os.path.join(project_path, settings.CONF_SOURCE)

conf_path = os.path.join("text-classification", "text-classification", "conf")

class ProjectContext(KedroContext):
    CONF_ROOT = conf_path
