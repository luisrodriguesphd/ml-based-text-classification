import os

from kedro.config import ConfigLoader, MissingConfigException
from kedro.framework.project import pipelines, settings
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from kedro.runner import SequentialRunner

src_path = os.path.dirname(os.path.dirname(__file__))
project_path = os.path.dirname(src_path)
conf_path = os.path.join(project_path, settings.CONF_SOURCE)
conf_loader = ConfigLoader(conf_source=conf_path)

try:
    parameters = conf_loader["parameters"]
except MissingConfigException:
    parameters = {}

bootstrap_project(project_path)
package_name = os.path.split(project_path)[-1].replace("-", "_")
with KedroSession.create(package_name=package_name) as session:
    context = session.load_context()
    catalog = context.catalog

predict_pipeline = pipelines["prediction"]

runner = SequentialRunner()

# # Alternative way to set the ConfigLoader
#
# # Set the current working directory as project root
# src_path = os.path.dirname(os.path.dirname(__file__))
# root_path = os.path.join(*os.path.split(src_path)[:-1])
# os.chdir(root_path)
#
# conf_path = os.path.join(settings.CONF_SOURCE)
# conf_loader = ConfigLoader(conf_source=conf_path)
#
# project_path = os.path.dirname(src_path)