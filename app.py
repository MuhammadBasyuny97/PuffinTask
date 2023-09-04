from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from QuotesScraper import db_params
from database import connect_to_database
from QuotesScraper import db_params


    
app = FastAPI()
handler = Mangum(app)

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for filtering
class FilterParams(BaseModel):
    column_name: str
    filter_value: str

# Connect to the PostgreSQL database
conn = connect_to_database(db_params)

# Define a route to retrieve data with optional filtering
@app.get("/data")
async def get_data(column_name: str = None, filter_params: FilterParams = None):
    if conn is None:
        return {"message": "Database connection error"}

    cursor = conn.cursor()
    
    if filter_params:
        # Perform filtering if filter_params are provided
        query = f"SELECT * FROM \"TB1\" WHERE {filter_params.column_name} = %s;"
        cursor.execute(query, (filter_params.filter_value,))
    elif column_name:
        # Retrieve data for a specific column if column_name is provided
        query = f"SELECT \"{column_name}\" FROM \"TB1\";"
        cursor.execute(query)
    else:
        # Retrieve all data if no filters or column_name are provided
        query = "SELECT * FROM \"TB1\" ;"
        cursor.execute(query)

    # Fetch the results
    data = cursor.fetchall()
    cursor.close()

    return {"data": data}

