# Lab 1: Calling, Building, and Securing APIs
In homework I1 you will use third-party machine learning APIs and in the group project you will develop your own APIs. In this lab, you will experiment with both, connecting to the Azure Vision API and providing your own API endpoint. 

## Deliverables
- [x] Create an account and connected to the Azure Vision API
- [x] Explained why hard-coding credentials is a bad idea. Commit your code to GitHub without committing your credentials.
- [x] Run the API endpoint with the starter code and demonstrate that it works with an example invocation (e.g., using curl).

## Getting started

1. **Clone the Repository:**
    - Clone the starter code into this folder.

2. **Create a Virtual Environment:**
   - Create a virtual environment using the command:
     ```bash
     python -m venv mlp
     ``` 
   - Activate the virtual environment with:
     ```bash
     source mlp/bin/activate
     ```

3. **Install Dependencies:**
   - Install the required dependencies listed in the `requirements.txt` file by running:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application:**
   - Start the API by executing:
     ```bash
     python3 app.py
     ```
   - Navigate to `http://localhost:3000/` to access the API instructions.

## Connecting to the Azure Vision API

1. **Sign Up for a Student Account:**
    - Sign up for a student account for Microsoft Azure: https://azure.microsoft.com/en-us/free/students/

2. **Create an Instance of the Computer Vision Service:**
    - Click 'Create new' in the Resource Group field and name it 'test_group'.
    - Choose 'East US' in the Region field
    - Enter 'cv-testing-3' in the Name field
    - Choose 'Free F0' in the Pricing tier field

3. **Get the API Endpoint and Subscription Key:**
    - Retrieve the API endpoint and subscription key under the "Manage keys" section.

4. **Update `analyze.py` with Your Credentials:**
    - Paste the endpoint and subscription key into the appropriate fields in the `analyze.py` file.


## Secure your Credentials
The starter code hardcodes credentials in the code. This is a bad practice. Here’s how to securely store and manage your credentials:

1. **Configure an `.env` File:**
   - Create an `.env` file to store your credentials using the following format:
     ```bash
     AZURE_ENDPOINT=YOUR_ENDPOINT
     AZURE_KEY=YOUR_KEY
     ```

2. **Update the `analyze.py`:**
   - Remove the hardcoded credentials from the `analyze.py`.
   - Load the envoirnment variables from the `.env` file by adding the following code:
       ```bash
       from dotenv import load_dotenv
       import os

       # Load environment variables from .env file
       load_dotenv()

       # Get credentials from environment variables
       endpoint = os.getenv('AZURE_ENDPOINT')
       key = os.getenv('AZURE_KEY')
       ```


2. **Add `.env` to `.gitignore`:**
    - Add `.env` to your `.gitignore` file to prevent committing the credentials to GitHub.

## Calling your own API
The starter code comes with a flask server that serves the website at http://localhost:3000/. It also exposes an own API at http://localhost:3000/api/v1/analysis/ accepting a GET request with a JSON object with a single field “uri” pointing to an image to analyze.

To call the AP, execute the following command in the terminal:
```bash
curl --get "http://localhost:3000/api/v1/analysis/" --data-urlencode "uri=https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/images/handwritten-note.jpg"
```

This would return a result similar to:
```bash
{
"text": "- You must be the change you Wish to see in the world ! Everything has its beauty, but not everyone sees it !"
}
```


## Additional resources 
- [Redhat article on API](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces)
- [Azure Computer Vision](https://learn.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python)
- [API Design Best Practices](https://blog.stoplight.io/crud-api-design?_ga=2.223919515.1813989671.1674077556-1488117179.1674077556)
- [API Endpoint Best Practices](https://www.telerik.com/blogs/7-tips-building-good-web-api)
- The file seai-azure-cv-ocr-api.json has the structure to test calls to the Azure Vision API with Postman.

