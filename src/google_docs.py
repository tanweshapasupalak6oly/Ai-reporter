"""Create and format Google Docs reports."""

from google.oauth2 import service_account
from googleapiclient.discovery import build
import json, os

SCOPES=["https://www.googleapis.com/auth/documents","https://www.googleapis.com/auth/drive"]


def _services():
    info=json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'])
    creds=service_account.Credentials.from_service_account_info(info,scopes=SCOPES)
    return build('docs','v1',credentials=creds), build('drive','v3',credentials=creds)


def create_report(title:str, body:str):
    docs, drive = _services()
    doc=docs.documents().create(body={'title':title}).execute()
    doc_id=doc['documentId']
    docs.documents().batchUpdate(documentId=doc_id,body={'requests':[{'insertText':{'location':{'index':1},'text':body}}]}).execute()
    drive.permissions().create(fileId=doc_id,body={'type':'anyone','role':'reader'}).execute()
    return doc_id