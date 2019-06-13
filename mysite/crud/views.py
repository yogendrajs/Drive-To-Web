from django.shortcuts import render
# Creating my views here.
from django.http import HttpResponse
import pickle
import os.path
import os, pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors


def index(request): # one of the endpoints method-name

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 15 files the user has access to.
    You can increase the files you want to access by changing the value of pageSize parameter.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    

    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=15, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', []) # appending all the details of the images in a list by calling 'files' key of 'results'
    # pprint.pprint(items)
    total_url_list = [] # taking this list to pass all the images link to html.
    if not items:
        print('No files found.') # it would be printed if no files would be in the list
    else:
        print('Files:')
        for item in items:
            if item['name'] == 'Images': # accessing the public 'Images' folder from my Drive.
                
                # The following 'query' variable has the 'id' of the parent folder to get access to 'children' of the folder.
                query = "'{}' in parents".format(item['id'])
                # pprint.pprint(query)

                children = service.files().list(q=query, 
                                fields='nextPageToken, files(id, name)').execute() # accessing the child images of 'Images' folder.

                all_images = children['files'] # list of all the images
                # pprint.pprint(all_images) # all the child images of the folder showing up in a list with particular dictionaries having their data.
                for i in all_images:
                    # appending and printing the urls of all the images while looping through the children image files.
                    print ('link is https://drive.google.com/uc?export=view&id={}'.format(i['id']))
                    total_url_list.append('https://drive.google.com/uc?export=view&id={}'.format(i['id'])) 

        return render(request, 'first.htm', {"data": total_url_list}) # passing the total urls-object of images to render on html.

# ...

def first(request): # tried 'first' endpoint to render a html file on the browser
    return render(request, 'trial.htm')