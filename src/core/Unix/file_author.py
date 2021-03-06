import pwd
import logging
from src.core.FileInfo import FileInfo


def file_author(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: tuple - owner name with user id
    """
    assert isinstance(file_info, FileInfo)
    try:
        owner_id = file_info.stat.st_uid
        owner_name = pwd.getpwuid(owner_id)[0]
        return owner_name, owner_id
    except AttributeError as err:
        logging.error(err)
