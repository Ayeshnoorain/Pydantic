import csv
from datetime import date, time, datetime
from typing import Optional, List

from pydantic import BaseModel, ValidationError, field_validator
from pydantic.fields import Field


class SurveyRecord(BaseModel):
    user_id: str
    survey_id: int = Field(alias='survey_i')
    mid: Optional[str]
    mid2: Optional[str]
    sessionid: Optional[str]
    dayMonth: int
    weekday: int
    weeknum: int
    month: int
    quarter: int
    year: int
    date: date = Field(..., description="The date in a specific format (e.g., YYYY-MM-DD)")
    time: time
    q888811_2: str

    @field_validator("user_id")
    def validate_user_id(cls, value):
        if not all(char.isalnum() or char in {'_', '-'} for char in value):
            raise ValueError("User ID must be alphanumeric and can include underscores and hyphens")
        return value

    @field_validator("mid", "mid2", "sessionid")
    def validate_string_length(cls, value):
        if value and len(value) > 1:  # Example max length
            raise ValueError("String length exceeds maximum limit")
        return value

    @field_validator("q888811_2")
    def parse_q888811_2(cls, value):
        if "“in the know”" in value:
            raise ValueError("Column value cannot have double quotes")
        return value

    @field_validator("month")
    def validate_month(cls, value):
        if not 1 <= value <= 12:
            raise ValueError("Month value must be between 1 and 12")
        return value

    @field_validator("quarter")
    def validate_quarter(cls, value):
        if not 1 <= value <= 4:
            raise ValueError("Quarter value must be between 1 and 4")
        return value

    @field_validator("year")
    def validate_year(cls, value):
        if value < 2000:  # Assuming surveys started from the year 2000
            raise ValueError("Year is out of the valid range")
        return value

    @field_validator("date")
    def parse_date(cls, value):
        if isinstance(value, str):
            try:
                # Parse the string using the expected date format
                return datetime.strptime(value, '%d/%m/%Y').date()
                print('AAAA')
            except ValueError:
                # Raise a ValueError if the format does not match
                raise ValueError("Invalid date format, expected DD/MM/YYYY")
        elif not isinstance(value, date):
            # Additional check to ensure the value is a date if it's not a string
            raise ValueError("Invalid type for date")
        return value


if __name__ == '__main__':

    # Step 2: Function to read and parse the CSV file
    file_path = r'C:\Users\ayesha.noorain\PycharmProjects\PydanticProject\Dataset.csv'

    def read_csv(file_path: str) -> List[SurveyRecord]:
        records = []
        with open(file_path, mode='r', encoding='cp1252') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
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
