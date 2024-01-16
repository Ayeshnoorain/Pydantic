import csv
from datetime import datetime, date, time
from typing import Optional, List

from pydantic import BaseModel, ValidationError, field_validator
from pydantic.fields import Field


# Step 1: Define the Pydantic model
def valueError(param):
    pass


class SurveyRecord(BaseModel):
    ID: int
    user_id: str
    survey_id: int = Field(alias='survey_i')
    mid: Optional[int]
    mid2: Optional[str]
    sessionid: Optional[str]
    dayMonth: int
    weekday: int
    weeknum: int
    month: int
    quarter: int
    year: int
    date: date
    time: time
    q888811_2 : str

    @field_validator("date")
    def parse_date(cls, value):
        if value:
            return datetime.strptime(value, '%d/%m/%Y').date()
        return value

    @field_validator("time")
    def parse_time(cls, value):
        if value:
            return datetime.strptime(value, '%H:%M:%S').time()
        return value

    @field_validator("q888811_2")
    def parse_q888811_2(cls, value):
        if "“in the know”"in value:
            raise valueError("Column value cannot have double quotes")
        return value

# Step 2: Function to read and parse the CSV file
file_path = r'C:\Users\ayesha.noorain\PycharmProjects\PydanticProject\Dataset.csv'
def read_csv(file_path: str) -> List[SurveyRecord]:
    records = []
    with open(file_path, mode='r', encoding='cp1252') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                record = SurveyRecord(**row)
                records.append(record)
            except ValidationError as e:
                print(f"Error parsing record: {e}")
    return records

# Step 3: Read the file and process records
records = read_csv(file_path)

# Example usage: Print the parsed records
for record in records:
    print(record)
