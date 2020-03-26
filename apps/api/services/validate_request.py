def validate_request(request):
    client_id = request["contact-data"][0]["client-id"]
    print(client_id)
    if client_id == "SFSolarIsSepNIsObfY":
        required_fields_dict = {
            "required": [
                "phone",
                "campaign-most-recent",
                "company-name",
                "contact-source-most-recent",
                "data-processing",
                "email",
                "email-consent-date",
                "email-opt-in-status",
                "first-name",
                "heroku-cms-processing",
                "ingestion-point",
                "last-name",
                "state-code",
            ]
        }
    elif client_id == "591064a3608a41a39a3db19cd6b97843":
        required_fields_dict = {
            "required": [
                "phone",
                "campaign-most-recent",
                "company-name",
                "contact-source-most-recent",
                "data-processing",
                "email",
                "email-consent-date",
                "email-opt-in-status",
                "first-name",
                "heroku-cms-processing",
                "ingestion-point",
                "last-name",
                "state-code",
            ]
        }
    elif client_id == "fc9e75b31fe14d4d8656cc6570d82088":
        required_fields_dict = {
            "required": [
                "phone",
                "campaign-most-recent",
                "company-name",
                "contact-source-most-recent",
                "data-processing",
                "email",
                "email-consent-date",
                "email-opt-in-status",
                "first-name",
                "heroku-cms-processing",
                "ingestion-point",
                "last-name",
                "state-code",
            ]
        }
    try:
        for field in required_fields_dict.get("required"):
            missing_field = 0
            if (
                request["contact-data"][0][field] is None
                or request["contact-data"][0][field] == ""
            ):
                print(f"====Required field {field} missing====")
                missing_field += 1
                break

        if missing_field > 0:
            return field
        else:
            return "validated"
    except:
        return field
