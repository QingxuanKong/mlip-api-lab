from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file

# Get credentials from environment variables
endpoint = os.getenv('AZURE_ENDPOINT')
key = os.getenv('AZURE_KEY')

if not endpoint or not key:
    raise ValueError("Azure endpoint and key must be set in environment variables.")

credentials = CognitiveServicesCredentials(key)

client = ComputerVisionClient(
    endpoint=endpoint,
    credentials=credentials
)

def read_image(uri):
    try:
        numberOfCharsInOperationId = 36
        maxRetries = 10

        # SDK call
        rawHttpResponse = client.read(uri, language="en", raw=True)

        # Get ID from returned headers
        operationLocation = rawHttpResponse.headers["Operation-Location"]
        operationId = operationLocation.split('/')[-1]

        # SDK call
        result = client.get_read_result(operationId)
        
        # Try API
        retry = 0
        
        while retry < maxRetries:
            if result.status.lower () not in ['notstarted', 'running']:
                break
            time.sleep(1)
            result = client.get_read_result(operationId)
            
            retry += 1
        
        if retry == maxRetries:
            return "max retries reached"

        if result.status == OperationStatusCodes.succeeded:
            res_text = " ".join([line.text for line in result.analyze_result.read_results[0].lines])
            return res_text
        else:
            return "error"
    except Exception as e:
        return f"Error occurred: {str(e)}"
