list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 0]
dict1 = {"PASSED": list_1, "FAILED": list_2}

print("CHECK : {}".format(dict1))

dict2 = {"key": [], "key2": []}
for sc in dict1.get("PASSED"):
    if sc == 1:
        dict1.get("PASSED").remove(sc)
        dict1.get("FAILED").append(sc)


print("CHECK : {}".format(dict1))
print("CHECK : {}".format(dict2))

for k in dict2.keys():
    for kid in dict2.get(k):
        print("CHECK VALUES : {}".format(kid))



stage_contact_list = []
    email_dictionary = dict()
    mobile_dictionary = dict()
    req_dictionary = validate_required_fields(stage_contacts)
    if len(req_dictionary.get(FAILED)) > 0:
        stage_contact_list.extend(
            update_stage_contact_status(
                req_dictionary.get(FAILED), REQUIRED_FIELD_VALIDATION, FAILED
            )
        )
    if len(req_dictionary.get(PASSED)) > 0:
        email_dictionary = validate_email_fields(req_dictionary.get(PASSED))
    if len(email_dictionary.get(FAILED)) > 0:
        stage_contact_list.extend(
            update_stage_contact_status(
                email_dictionary.get(FAILED), EMAIL_VALIDATION, FAILED
            )
        )
    if len(email_dictionary.get(PASSED)) > 0:
        mobile_dictionary = validate_mobile_fields(email_dictionary.get(PASSED))
    if len(mobile_dictionary.get(FAILED)) > 0:
        stage_contact_list.extend(
            update_stage_contact_status(
                mobile_dictionary.get(FAILED), MOBILE_VALIDATION, FAILED
            )
        )
    if len(mobile_dictionary.get(PASSED)) > 0:
        stage_contact_list.extend(
            update_stage_contact_status(
                mobile_dictionary.get(PASSED), VALIDATION_COMPLETED, IN_PROGRESS
            )
        )