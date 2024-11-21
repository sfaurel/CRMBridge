from flask import request
from flask_restx import Resource, marshal, fields

from ..models.leads_models import LeadsModel

from ..services.crm_service import CRMService

leads_ns = LeadsModel.api
lead_model = LeadsModel.lead_model
lead_payload_model = LeadsModel.lead_payload_model
error_model = LeadsModel.error_model


@leads_ns.route('/')
class Leads(Resource):
    @leads_ns.response(code=200, description='Success', model=fields.List(fields.Nested(lead_model)))
    @leads_ns.response(code=500, description='Internal Server Error', model=error_model)
    def get(self):
        """Return a leads list."""
        response = CRMService.get_leads()
        if 'status' in response and response['status'] == 'error':
            return marshal(response, error_model), 500
        return marshal(response, lead_model, envelope=[]), 201

    @leads_ns.expect(lead_payload_model, validate=True)
    @leads_ns.response(code=500, description='Internal Server Error', model=error_model)
    @leads_ns.response(code=200, description='Success', model=lead_model)
    def post(self):
        """Creates a lead."""
        data = request.json
        response = CRMService.create_lead(data)
        if 'status' in response and response['status'] == 'error':
            return marshal(response, error_model), 500
        return marshal(response, lead_model), 201


@leads_ns.route('/<box_key>')
@leads_ns.doc(params={'box_key': 'The unique identifier of a lead'})
class Lead(Resource):
    @leads_ns.response(code=200, description='Success', model=lead_model)
    @leads_ns.response(code=500, description='Internal Server Error', model=error_model)
    def get(self, box_key):
        """Return a specific lead based on the key (box_key) you provide."""
        crm_service = CRMService()
        response = crm_service.get_lead(box_key)
        if 'status' in response and response['status'] == 'error':
            return marshal(response, error_model), 500
        return marshal(response, lead_model), 200
