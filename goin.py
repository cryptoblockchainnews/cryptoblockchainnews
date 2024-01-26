from oauth2client.service_account import ServiceAccountCredentials 
import httplib2 
import os

SCOPES = [ "https://www.googleapis.com/auth/indexing" ] 

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish" 

 

# service_account_file.json is the private key that you created for your service account. 

JSON_KEY_FILE = "/root/cryptonewsletter.github.io/calm-bison-354711-79c5bce1461d.json" 

 

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES) 

 

http = credentials.authorize(httplib2.Http()) 

link = os.environ["LINK"]

content = """{ 

  "url": "${link}", 

  "type": "URL_UPDATED" 

}""" 

 

response, content = http.request(ENDPOINT, method="POST", body=content) 

print(response) 

print(content)
