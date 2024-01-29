import pyodbc
from pydantic import BaseModel, ValidationError, field_validator

# Define your Pydantic model (similar to the one you provided)
class SurveyRecord(BaseModel):
    user_id: str
    gender: int
    age: int
    q65475: str
    # add other fields and validations as needed

    @field_validator("age")
    def check_q1234_1_exists(cls, v):
        if v is None:
            raise ValueError("Field is a required and it is missing")
        return v

    @field_validator("q65475")
    def check_q1230000003_non_empty(cls, v):
        if v == " ":
            raise ValueError("field is present but empty, which is not allowed")
        return v
# Database connection details
server = '10.190.30.51'
database = 'Asics_SportsMarketing_Dev'
username = 'jkhan'
password = 'jkhan'
driver = '{ODBC Driver 17 for SQL Server}'

# Establish a database connection
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)
cursor = conn.cursor()

# Fetch data from the database
cursor.execute("SELECT * FROM Asics_SM_2020_Dec_Set1")
rows = cursor.fetchall()
#print(rows)

# Apply validations
for row in rows:
    try:
        record = SurveyRecord(
            user_id=row.user_id,
            gender=row.gender,
            age=row.gender,
            q65475=row.q65475,
            # map other fields as necessary
        )
        # If necessary, perform additional operations with the validated record
    except ValidationError as e:
        print(f"Validation error for record {row}: {e}")

# Close the database connection
cursor.close()
conn.close()
