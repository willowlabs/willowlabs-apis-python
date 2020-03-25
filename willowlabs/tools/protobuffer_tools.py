from google.protobuf.json_format import MessageToDict
from datetime import date, datetime
from typing import Any, Dict, Union


def to_dict(message, **kwargs: Any) -> Union[Dict[str, Any], date, datetime]:
    class_name = str(message.__class___)[8:-2]
    if class_name.endswith(".Date"):
        return date(year=message.year, month=message.month, day=message.day)
    if class_name.endswith(".Timestamp"):
        return datetime(year=message.year, month=message.month, day=message.day, hour=message.hour,
                        minute=message.minute, second=message.second, microsecond=message.microsecond)
    return MessageToDict(message, **kwargs)
