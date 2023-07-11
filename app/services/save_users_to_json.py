import json
import pathlib

from app.config import FILES_OUTPUT_DIR
from app.loggers.loggers import get_custom_logger
from app.services.generate_users import User


def save_users_to_json(users: list[User], json_file_path: pathlib.Path = None) -> pathlib.Path:
    logger = get_custom_logger("save_users_to_json")

    logger.info(msg="start")

    if json_file_path is None:
        json_file_path = FILES_OUTPUT_DIR.joinpath("users.json")

    serialized_users = {"users": [user.get_dict() for user in users]}

    with json_file_path.open("w") as json_file:
        json.dump(serialized_users, json_file, indent=2)

    logger.info(f"end. json_file_path={json_file_path.as_uri()}")

    return json_file_path
