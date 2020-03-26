from flask_restful import Resource
from flask import make_response, request, jsonify
from .create_staging_records import create_staging_records
from .validate_request import validate_request


class ContactManagement(Resource):
    def __init__(self):
        try:
            self.request = request.get_json(force=True)

        except Exception:
            pass

    def post(self):
        """
        Function to handle POST request recieved on this resource.
        """
        print("GOT POST REQUEST")
        print(self.request)
        self.contact_data_list = self.request["contact-data"]
        if len(self.contact_data_list) > 1:
            create_staging_records(self.request)
            return make_response(jsonify("Record Created successfully"))

        else:
            print("single record validation required")
            validation_output = validate_request(self.request)
            if validation_output == "validated":
                create_staging_records(self.request)
                return make_response(
                    jsonify("Request validated and record created successfully")
                )
            else:
                return make_response(
                    jsonify("Required Field '" + validation_output + "' is Missing")
                )
