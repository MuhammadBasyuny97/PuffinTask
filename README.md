# PuffinTask

# Database Design
- SQL
   <br/>
   <br/>
   CREATE TABLE Quotes <br/>
   (<br/>
    ID SERIAL PRIMARY KEY,<br/>
    Quote TEXT NOT NULL,<br/>
    Author TEXT NOT NULL<br/>
   );


- Table Name: Quotes

|   ID   |            Quote            |  Author   |
|--------|---------------------------- |-----------|
|   1    | "To be or not to be..."     |  Shakespeare |
|   2    | "The only thing we have..." |  Albert Einstein |
|   3    | "In three words I can sum up..." |  Robert Frost |
|   ...  | ...                         | ...       |
----------------------------------------------


# Deployment 

- Deploying the Database on AWS RDS
  ```bash
     task-postgres.cp0fyahnpwk3.us-east-1.rds.amazonaws.com
  ```

- Deploying FastAPI and Scrapper on AWS Lambda
  ```bash
    https://lrwzxenqtquo2qhu6vhh3n6ggi0acrqq.lambda-url.us-east-1.on.aws/
  ```

- Testing the API
  ```bash
     Fetch All Data: https://lrwzxenqtquo2qhu6vhh3n6ggi0acrqq.lambda-url.us-east-1.on.aws/data
  ```
  ```bash
     Fetch Data of a Column: https://lrwzxenqtquo2qhu6vhh3n6ggi0acrqq.lambda-url.us-east-1.on.aws/data?column_name=Quote
  ```
  ```bash
     Fetch Data with filtered values: https://lrwzxenqtquo2qhu6vhh3n6ggi0acrqq.lambda-url.us-east-1.on.aws/data? 
      column_name=Quote&filter_params{"column_name":Author,"filter_value":Mark Twain}
  ```
------------------------------------------
# How to Run the Server Manually on the local Machine
- 1.Clone the Repo
- 2.Install the dependencies
     ```
      pip install -r requirements.txt
     ```
- 3.Run the server
     ```bash
         cd app
         python -m uvicorn app:app --reload
     ```
- 4.Open Postman-Collection and test the API.

- 5.Test the APIs
     ```bash
      -Fetch All Data: https:http://127.0.0.1:8000/data
      -Fetch Data of a Column: http://127.0.0.1:8000/data?column_name=Quote
      -Fetch Data with filtered values: http://127.0.0.1:8000/data?column_name=Quote&filter_params={"column_name":Author,"filter_value":Mark Twain}
     ```

