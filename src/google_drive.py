"""Google Drive helper utilities."""

from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import os

SCOPES=["https://www.googleapis.com/auth/drive"]


def drive_service():
    info=json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
    creds=service_account.Credentials.from_service_account_info(info,scopes=SCOPES)
    return build("drive","v3",credentials=creds)


def create_folder(name,parent_id=None):
    service=drive_service()
    metadata={"name":name,"mimeType":"application/vnd.google-apps.folder"}
    if parent_id:
        metadata["parents"]= [parent_id]
    folder=service.files().create(body=metadata,fields="id,name").execute()
    return folder["id"]


def move_file(file_id,folder_id):
    service=drive_service()
    service.files().update(fileId=file_id,addParents=folder_id,fields="id,parents").execute()
