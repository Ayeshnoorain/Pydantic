from datetime import date, time, datetime
from typing import Optional, List
from pydantic import BaseModel, field_validator, Field


class SurveyRecord(BaseModel):
    user_id: str
    survey_id: int = Field(alias='survey_i')
    mid: Optional[str]
    mid2: Optional[str]
    sessionid: Optional[str]
    #date: date = Field(..., description="The date in a specific format (e.g., YYYY-MM-DD)")
    dayMonth: int
    weekday: int
    weeknum: int
    month: int
    quarter: int
    year: int
    q888811_2: str
    missing_column: str
    present_empty: str


    @field_validator("user_id")
    def validate_user_id(cls, value):
        if not all(char.isalnum() or char in {'_', '-'} for char in value):
            raise ValueError("User ID must be alphanumeric and can include underscores and hyphens")
        # print(value)
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
        if value != 2023:  # Assuming surveys started from the year 2023
            raise ValueError("Year is out of the valid range")
        return value

    @field_validator("missing_column")
    def check_q1234_1_exists(cls, v):
        if v is None:
            raise ValueError("Field is a required and it is missing")
        return v


    @field_validator("present_empty")
    def check_q1230000003_non_empty(cls, v):
        if v == " ":
            raise ValueError("field is present but empty, which is not allowed")
        return v


    # @field_validator("date", pre=True)
    # def parse_date(cls, value):
    #     if isinstance(value, str):
    #         try:
    #             # Parse the string using the expected date format
    #             return datetime.strptime(value, '%d/%m/%Y').date()
    #         except ValueError:
    #             # Raise a ValueError if the format does not match
    #             raise ValueError("Invalid date format, expected DD/MM/YYYY")
    #     elif not isinstance(value, date):
    #         # Additional check to ensure the value is a date if it's not a string
    #         raise ValueError("Invalid type for date")
    #     print(value)
    #     return value

