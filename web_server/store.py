import requests  # Import the requests library to make HTTP requests.

def get_categories():
    # Send an HTTP GET request to the specified URL to fetch category data.
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    
    # Print the HTTP status code of the response (e.g., 200 for success).
    print(r.status_code)
    
    # Print the raw text content of the response (expected to be in JSON format).
    print(r.text)
    
    # Print the type of the response text (should be a string).
    print(type(r.text))
    
    # Parse the JSON response into a Python object (likely a list of dictionaries).
    categories = r.json()
    
    # Iterate over the list of categories and print the 'name' field of each category.
    for category in categories:
        print(category['name'])

