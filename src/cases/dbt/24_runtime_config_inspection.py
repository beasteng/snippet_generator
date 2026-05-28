"""Parse dbt_project.yml into typed Python config objects."""
from dbt.config.project import PartialProject
from dbt.config.renderer import DbtProjectYamlRenderer
from dbt.flags import set_from_args
from pathlib import Path
from argparse import Namespace
import os

# Set minimal flags
set_from_args(Namespace(
    profiles_dir=str(Path.home() / ".dbt"),
    project_dir=os.getcwd(),
), None)

project_root = Path(os.getcwd())
partial = PartialProject.from_project_root(str(project_root))

renderer = DbtProjectYamlRenderer(None, None)
project = partial.render(renderer)

print(f"Project name   : {project.project_name}")
print(f"Version        : {project.version}")
print(f"Config version : {project.config_version}")
print(f"Model paths    : {project.model_paths}")
print(f"Seed paths     : {project.seed_paths}")
print(f"Test paths     : {project.test_paths}")
print(f"Snapshot paths : {project.snapshot_paths}")
