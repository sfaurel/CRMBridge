import base64
from dotenv import load_dotenv
import os
import requests

from ..utils.decorator import handle_request_errors

load_dotenv()


class CRMService:
    api_url = os.getenv("STREAK_API_URL")
    streak_api_key = os.getenv("STREAK_API_KEY")
    basic_token = base64.b64encode(streak_api_key.encode("utf-8")).decode("utf-8")
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "authorization": f"Basic {basic_token}"
    }
    lead_stage = 5001
    pipeline_key = 'agxzfm1haWxmb29nYWVyPAsSDE9yZ2FuaXphdGlvbiIVYm9kb3F1ZTAwNDlAZ21haWwuY29tDAsSCFdvcmtmbG93GICA-Zvb7c0JDA'

    @classmethod
    @handle_request_errors
    def get_leads(cls):
        """
        Fetches leads from the CRM.

        Returns:
            dict:
                On success:
                    A dictionary containing the new lead
                On error:
                    A dictionary with an error status and a description of the problem that occurred. 
        """

        boxes_url = f"{cls.api_url}/v1/pipelines/{cls.pipeline_key}/boxes?stageKey={cls.lead_stage}"

        response = requests.get(boxes_url, headers=cls.headers)
        response.raise_for_status()
        return response.json()

    @classmethod
    @handle_request_errors
    def get_lead(cls, box_key):
        """
        Fetches leads from the CRM.

        Returns:
            dict:
                On success:
                    A dictionary containing the response data from the CRM
                On error:
                    A dictionary with an error status and a description of the problem that occurred.
        """
        box_url = f"{cls.api_url}/v1/boxes/{box_key}"

        response = requests.get(box_url, headers=cls.headers)
        response.raise_for_status()
        return response.json()

    @classmethod
    @handle_request_errors
    def create_lead(cls, data):
        """
        Create a new lead in the CRM.

        Args:
            name (str): Name of the lead.
            notes (str): Notes of the lead.
            assignedToSharingEntries : .
        Returns:
            On success:
                A dictionary containing the response data from the CRM
            On error:
                A dictionary with an error status and a description of the problem that occurred.
        """
        url = f"{cls.api_url}/v2/pipelines/{cls.pipeline_key}/boxes"
        if ("assigneesEmails" in data):
            data["assignedToSharingEntries"] = [{"email": email} for email in data["assigneesEmails"]]
            data.pop("assigneesEmails")
        response = requests.post(url, json=data, headers=cls.headers)
        response.raise_for_status()
        return response.json()
