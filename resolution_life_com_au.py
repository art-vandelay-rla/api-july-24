import requests
import sys

# Credentials for the API
auth = requests.auth.HTTPBasicAuth('philippa.hawk@resolutionlife.co.nz','fecf6e30-449e-11ef-b3fc-7a67b0c07e2e')

def main() -> int:
  # API endpoint
  url = 'https://resolutionlife.com.au/'
  
  # Retrieve data
  response = requests.get(url, auth=auth)
  
  print(response.text)
  return 0

if __name__ == '__main__':
  sys.exit(main())
