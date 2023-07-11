import pathlib

from ruamel.yaml import YAML

from app.config import FILES_OUTPUT_DIR
from app.loggers.loggers import get_custom_logger
from app.services.generate_users import User


def save_users_to_yaml(users: list[User], yaml_file_path: pathlib.Path = None) -> pathlib.Path:
    logger = get_custom_logger("save_users_to_yaml")

    logger.info(msg="start")

    if yaml_file_path is None:
        yaml_file_path = FILES_OUTPUT_DIR.joinpath("users.yaml")

    serialized_users = {"users": [user.get_dict() for user in users]}

    yaml = YAML(typ="safe")
    yaml.version = (1, 2)

    with yaml_file_path.open("w") as yaml_file:
        yaml.dump(serialized_users, yaml_file)

    logger.info(f"end. yaml_file_path={yaml_file_path.as_uri()}")

    return yaml_file_path
