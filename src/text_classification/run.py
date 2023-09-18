from kedro.framework.context import KedroContext
import os
from kedro.framework.project import settings

src_path = os.path.dirname(os.path.dirname(__file__))
project_path = os.path.dirname(src_path)
conf_path = os.path.join(project_path, settings.CONF_SOURCE)

class ProjectContext(KedroContext):
    CONF_ROOT = conf_path
