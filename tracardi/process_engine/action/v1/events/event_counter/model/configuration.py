from pydantic import BaseModel, validator
from pytimeparse import parse

from tracardi.domain.named_entity import NamedEntity


class Configuration(BaseModel):
    event_type: NamedEntity
    time_span: str

    @validator("time_span")
    def valid_time_span(cls, value):
        if parse(value.strip("-")) is None:
            raise ValueError("Could not parse {} as time span".format(value))
        return value

