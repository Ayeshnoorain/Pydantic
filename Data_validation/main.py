import csv
from typing import Optional, List
from pydantic import BaseModel, ValidationError, field_validator, Field
from testprogram import SurveyRecord

# Press the green button in the gutter to run the script.
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

    # # Example usage: Print the parsed records
    # for record in records:
    #     print(record)
