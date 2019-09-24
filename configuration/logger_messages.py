from datetime import datetime


def incorrect_flag_state_message() -> str:
    return str(datetime.utcnow()) + "|Incorrect|Flag:%s|Host:%s|Enabled:%s"


def correct_flag_state_message() -> str:
    return str(datetime.utcnow()) + "|Correct|Flag:%s|Host:%s|Enabled:%s"
