from .contact_model_engine import *
from .contact_utility import *
from .contact_variables import *
from .contact_mapper import *

#
# REQUIRED FIELDS
def client_type_required_fields(stage_contact):
    """-----------------------------------------------------------
    Description: determine the required fields based on client type
    Argument: (1)list of stage contacts
    Return: Tuple
    -----------------------------------------------------------"""
    if stage_contact.is_app__c == True:
        return app_required_fields()
    elif stage_contact.is_dealer__c == True:
        return dealer_required_fields()
    elif stage_contact.is_salesforce_org__c == True:
        return salesforce_org_required_fields()


# REQUIRED FIELDS
def object_as_dict(obj):
    """-----------------------------------------------------------
    Description: convert an object into a DICT
    Argument: object
    Return: dictionary with [key]=field and [value]=value
    -----------------------------------------------------------"""
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def validate_stage_contacts(session, stage_contacts):
    """-----------------------------------------------------------  
    Description: Manage the validation functions
    Argument: (1)session (2)list of stage contacts 
    Return: 
    -----------------------------------------------------------"""
    stage_contact_list = []
    req_dictionary = validate_required_fields(stage_contacts)
    email_dictionary = validate_required_fields(req_dictionary.get(PASSED))
    mobile_dictionary = validate_mobile_fields(email_dictionary.get(PASSED))

    stage_contact_list = (
        req_dictionary.get(FAILED)
        + email_dictionary.get(FAILED)
        + mobile_dictionary.get(FAILED)
        + mobile_dictionary.get(PASSED)
    )

    if len(stage_contact_list) > 0:
        dml_list_of_objects(
            session, stage_contact_list,
        )


# REQUIRED FIELDS
def validate_required_fields(stage_contacts):
    """-----------------------------------------------------------  
    Description:  validate required fields
    Argument: (1)list of stage contacts 
    Return: 
    -----------------------------------------------------------"""
    # print("CHECK validate_stage_contacts")
    rfv = dict()
    req_dictionary = {PASSED: [], FAILED: []}
    for sc in stage_contacts:
        rfv = required_field_validator(sc)
        sc.process_status__c = REQUIRED_FIELD_VALIDATION
        if rfv.get(HAS_ERROR):
            sc.status__c = FAILED
            sc.error_message__c = "REQUIRED FIELDS MISSING : {}".format(
                ", ".join(rfv.get(ERROR_FIELDS))
            )
            req_dictionary.get(FAILED).append(sc)
        else:
            sc.status__c = IN_PROGRESS
            sc.error_message__c = None
            req_dictionary.get(PASSED).append(sc)

    return req_dictionary


# REQUIRED FIELDS
def required_field_validator(obj):
    """-----------------------------------------------------------
    Description: will validate required fields from a given object
    Argument: (1)session (2)object
    Return: dict with error and fields that error 
    -----------------------------------------------------------"""
    # print("CHECK required_field_validator")
    required_errors = []
    rfv = dict()
    for rf in client_type_required_fields(obj):
        if is_empty(object_as_dict(obj).get(rf)):
            required_errors.append(rf)
    if len(required_errors) > 0:
        rfv[HAS_ERROR] = True
        rfv[ERROR_FIELDS] = required_errors

    return rfv


# REQUIRED FIELDS
def validate_email_fields(stage_contacts):
    """-----------------------------------------------------------  
    Description: if changed email is true old_email is required
    Argument: (1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    # print("CHECK validate_email_fields")
    email_dictionary = {PASSED: [], FAILED: []}
    for sc in stage_contacts:
        sc.process_status__c = EMAIL_VALIDATION
        if sc.change_email__c == True and is_empty(sc.old_email__c):
            sc.status__c = FAILED
            sc.error_message__c = "REQUIRED FIELDS MISSING : old_email__c"
            email_dictionary.get(FAILED).append(sc)
        sc.status__c = IN_PROGRESS
        sc.error_message__c = None
        email_dictionary.get(PASSED).append(sc)

    return email_dictionary


# REQUIRED FIELDS
def validate_mobile_fields(stage_contacts):
    """-----------------------------------------------------------  
    Description: if mobile phone is provided sms consent and date are required
    Argument: (1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    # print("CHECK validate_mobile_fields")
    mobile_dictionary = {PASSED: [], FAILED: []}
    for sc in stage_contacts:
        sc.process_status__c = MOBILE_VALIDATION
        if not is_empty(sc.mobile__c):
            if is_empty(sc.sms_consent_date__c):
                sc.error_message__c = " sms_consent_date__c,"
            if is_empty(sc.sms_data_use_purpose__c):
                if is_empty(sc.error_message__c):
                    sc.error_message__c = " sms_data_use_purpose__c,"
                else:
                    sc.error_message__c += " sms_data_use_purpose__c,"
            if not is_empty(sc.error_message__c):
                sc.error_message__c = "REQUIRED FIELDS MISSING : " + sc.error_message__c
                sc.status__c = FAILED
                mobile_dictionary.get(FAILED).append(sc)
        else:
            sc.status__c = IN_PROGRESS
            sc.error_message__c = None
            mobile_dictionary.get(PASSED).append(sc)

    return mobile_dictionary


# ORG SOURCE UPDATE
def update_stage_contact_with_org_source(session, stage_contacts, org_dict):
    """-----------------------------------------------------------
    Description: Update each stage contact with the organization source table attributes for processing
    Argument: (1)session (2)list of stage contacts (3)org source dictionary
    Return: 
    -----------------------------------------------------------"""
    # print("CHECK update_stage_contact_with_org_source")
    stage_contact_list = []
    for sc in stage_contacts:
        sc.process_status__c = CLIENT_TYPE_VALIDATION
        if sc.client_id__c in org_dict.keys():
            sc.status__c = IN_PROGRESS
            stage_contact_list.append(
                organization_source(sc, org_dict.get(sc.client_id__c))
            )
        else:
            sc.status__c = FAILED
            sc.error_message__c = CLIENT_DOES_NOT_EXIST
            stage_contact_list.append(sc)

    dml_list_of_objects(session, stage_contact_list)


# ORG SOURCE UPDATE
def query_stage_contacts(session, query_limit, **kwargs):
    """-----------------------------------------------------------
    Description: Will query all of the records from the StageContact table 
    Argument: (1)session (2)integer for query limit (3)query filters
    Return: list of org source objects 
    -----------------------------------------------------------"""
    # print("CHECK query_stage_contacts")
    try:
        q = session.query(StageContact)
        for key, value in kwargs.items():
            f = getattr(StageContact, key)
            q = q.filter(f.in_(value))
        stage_contacts = q.limit(query_limit)
        # TODO: CATCH ERRORS
    except expression as identifier:
        print("THERE WAS AN ERROR WHILE QUERYING STAGE CONTACTS")

    # for sc in stage_contacts:
    #     # print("CHECK SC {}".format(sc.process_status__c))
    return stage_contacts


# ORG SOURCE UPDATE
def query_organization_source(session, query_limit, **kwargs):
    """-----------------------------------------------------------
    Description: Will query all of the records from the OrganizationSource table 
    Argument: (1)session (2)integer for query limit (3)query filters
    Return: list of org source objects 
    -----------------------------------------------------------"""
    # print("CHECK query_organization_source")
    try:
        q = session.query(OrganizationSource)
        for key, value in kwargs.items():
            f = getattr(OrganizationSource, key)
            q = q.filter(f.in_(value))
        organization_sources = q.limit(query_limit)
        # TODO: CATCH ERRORS
    except expression as identifier:
        print("THERE WAS AN ERROR WHILE QUERYING ORG SOURCES")

    # for org in organization_sources:
    #     # print("CHECK ORG {}".format(org.client_id__c))
    return organization_sources


# ORG SOURCE UPDATE
def organization_source_dictionary(organization_sources):
    """-----------------------------------------------------------
    Description: create a dictionary with org sources
    Argument:(1)list of organization source
    Return: dictionary with the [key]=client_id [value]=obj
    -----------------------------------------------------------"""
    # print("CHECK organization_source")
    org_dict = dict()

    for org in organization_sources:
        org_dict[org.client_id__c] = org
    return org_dict


# # MAIN
# if __name__ == "__main__":
#     session = loadSession()
#     # DEBUG

#     # SEQUENCE
#     query_limit = 100
#     # CONTACT PREPARATION
#     stage_contact_list = query_stage_contacts(
#         session, query_limit, process_status__c=[NOT_STARTED], status__c=[NOT_STARTED],
#     )

#     if stage_contact_list.count() > 0:
#         update_stage_contact_with_org_source(
#             session,
#             stage_contact_list,
#             organization_source_dictionary(
#                 query_organization_source(session, query_limit, is_active__c=[True])
#             ),
#         )
#     else:
#         print("No stage records to update with organization source")

#     stage_contact_validate = query_stage_contacts(
#         session,
#         query_limit,
#         process_status__c=[CLIENT_TYPE_VALIDATION],
#         status__c=[IN_PROGRESS],
#     )
#     if stage_contact_validate.count() > 0:
#         validate_stage_contacts(
#             session, stage_contact_validate,
#         )
#     else:
#         print("No stage records to validate")
