import requests
from bs4 import BeautifulSoup
from database import connect_to_database, execute_sql_query, close_database_connection


# Database connection parameters 
db_params = {
    'dbname': 'task',
    'user': 'postgres',
    'password': '0552594782',
    'host': 'task-postgres.cp0fyahnpwk3.us-east-1.rds.amazonaws.com',  # Endpoint provided by Amazon RDS
    'port': '5432'   
}

# Establish a connection to the PostgreSQL database
conn = connect_to_database(db_params)
if not conn:
    exit()

# Define the base URL
base_url = 'http://quotes.toscrape.com'
page_url = '/page/1'


quotes = []
authors = []


# web scraping code
while page_url:
    try:
        # Construct the URL for the current page
        url = base_url + page_url

        # Send an HTTP GET request to the current page
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and scrape the quotes and authors on the current page
            for quote in soup.find_all('span', class_='text'):
                quotes.append(quote.text)

            for author in soup.find_all('small', class_='author', itemprop='author'):
                authors.append(author.text)

            # Check if there is a "Next" button for the next page
            next_button = soup.find('li', class_='next')
            if next_button:
                page_url = next_button.find('a')['href']
            else:
                # No more pages to scrape
                page_url = None

        else:
            print(f'Error: Unable to fetch data. Status code: {response.status_code}')
            break

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        break

    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        break


# Store the scraped data in the PostgreSQL database using SQL
try:
    for i in range(len(quotes)):
        query = "INSERT INTO \"TB1\" (\"Quote\", \"Author\") VALUES (%s, %s);"
        data = (quotes[i], authors[i])
        execute_sql_query(conn, query, data)

    print("Data successfully inserted into the database.")

finally:
    # Close the database connection
    close_database_connection(conn)

# Display the scraped data
for i in range(len(quotes)):
    print(f'Quote: {quotes[i]}')
    print(f'Author: {authors[i]}\n')