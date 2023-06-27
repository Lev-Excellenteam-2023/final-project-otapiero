# create an enum
import enum


class FileStatus(enum.Enum):
    """
    Enum class for the status of the file.
    """
    DONE = 0
    PENDING = 1
    NOT_FOUND = 2

