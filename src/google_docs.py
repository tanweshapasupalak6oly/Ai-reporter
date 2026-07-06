"""Create a Google Doc for the weekly AI report."""

from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]


def get_services():
    info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    docs = build("docs", "v1", credentials=creds)
    drive = build("drive", "v3", credentials=creds)
    return docs, drive


def create_report(title: str, body: str):
    docs, _ = get_services()
    doc = docs.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]
    docs.documents().batchUpdate(documentId=doc_id, body={"requests":[{"insertText":{"location":{"index":1},"text":body}}]}).execute()
    return doc_id
