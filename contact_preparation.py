from contact_model_engine import *
from contact_utility import *
from contact_variables import *

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


# REQUIRED FIELDS
def required_field_validator(obj):
    """-----------------------------------------------------------
    Description: will validate required fields from a given object
    Argument: (1)session (2)object
    Return: dict with error and fields that error 
    -----------------------------------------------------------"""
    print("CHECK required_field_validator")
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
def validate_email_fields(session, stage_contacts):
    """-----------------------------------------------------------  
    Description: if changed email is true old_email is required
    Argument: (1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    print("CHECK validate_email_fields")
    for sc in stage_contacts:
        sc.process_status__c = "EMAIL FIELDS"
        if sc.change_email__c == True and is_empty(sc.old_email__c):
            sc.status__c = FAILED
            sc.error_message__c = "REQUIRED FIELDS MISSING : old_email__c"

        session.add(sc)
    if session.dirty:
        dml_stage_contact(session)


# REQUIRED FIELDS
def validate_mobile_fields(session, stage_contacts):
    """-----------------------------------------------------------  
    Description: if mobile phone is provided sms consent and date are required
    Argument: (1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    print("CHECK validate_mobile_fields")
    for sc in stage_contacts:
        sc.process_status__c = "MOBILE FIELDS"
        if not is_empty(sc.mobile__c):
            if is_empty(sc.sms_consent_date__c):
                sc.status__c = FAILED
                sc.error_message__c = " sms_consent_date__c,"
            if is_empty(sc.sms_data_use_purpose__c):
                sc.status__c = FAILED
                sc.error_message__c += " sms_data_use_purpose__c,"
            if not is_empty(sc.error_message__c):
                sc.error_message__c = "REQUIRED FIELDS MISSING : " + sc.error_message__c
        session.add(sc)
    if session.dirty:
        dml_stage_contact(session)


# REQUIRED FIELDS
def validate_required_fields(session, stage_contacts):
    """-----------------------------------------------------------  
    Description:  validate required fields
    Argument: (1)session (2)list of stage contacts 
    Return: 
    -----------------------------------------------------------"""
    print("CHECK validate_stage_contacts")
    rfv = dict()
    for sc in stage_contacts:
        rfv = required_field_validator(sc)
        sc.process_status__c = REQUIRED_FIELDS
        if rfv.get(HAS_ERROR):
            sc.status__c = FAILED
            sc.error_message__c = "REQUIRED FIELDS MISSING : {}".format(
                ", ".join(rfv.get(ERROR_FIELDS))
            )
            session.add(sc)
        else:
            sc.status__c = IN_PROGRESS
            session.add(sc)
    if session.dirty:
        dml_stage_contact(session)


# ORG SOURCE UPDATE
def update_stage_contact_with_org_source(session, stage_contacts, org_dict):
    """-----------------------------------------------------------
    Description: Update each stage contact with the organization source table attributes for processing
    Argument: (1)session (2)list of stage contacts (3)org source dictionary
    Return: 
    -----------------------------------------------------------"""
    print("CHECK update_stage_contact_with_org_source")

    for sc in stage_contacts:
        if sc.client_id__c in org_dict.keys():
            if is_empty(sc.stage_contact_id_ext__c):
                sc.stage_contact_id_ext__c = get_unique_id()
            sc.authorization_form_email_consent__c = org_dict.get(
                sc.client_id__c
            ).authorization_form_email_consent__c
            sc.authorization_form_sms_consent__c = org_dict.get(
                sc.client_id__c
            ).authorization_form_sms_consent__c
            sc.is_active__c = org_dict.get(sc.client_id__c).is_active__c
            sc.is_app__c = org_dict.get(sc.client_id__c).is_app__c
            sc.is_cat_consent__c = org_dict.get(sc.client_id__c).is_cat_consent__c
            sc.is_dealer__c = org_dict.get(sc.client_id__c).is_dealer__c
            sc.is_obfuscated__c = org_dict.get(sc.client_id__c).is_obfuscated__c
            sc.is_salesforce_org__c = org_dict.get(sc.client_id__c).is_salesforce_org__c
            sc.is_separate_contact__c = org_dict.get(
                sc.client_id__c
            ).is_separate_contact__c
            sc.process_status__c = ORG_SOURCE
            sc.source_contact_record_type_id__c = org_dict.get(
                sc.client_id__c
            ).source_contact_record_type_id__c
            sc.generic_record_type_id__c = org_dict.get(
                sc.client_id__c
            ).generic_record_type_id__c
            sc.source_name__c = org_dict.get(sc.client_id__c).source_name__c
            sc.status__c = IN_PROGRESS
            session.add(sc)
        else:
            sc.process_status__c = ORG_SOURCE
            sc.status__c = FAILED
            sc.error_message__c = CLIENT_DOES_NOT_EXIST
            session.add(sc)
    if session.dirty:
        dml_stage_contact(session)


# ORG SOURCE UPDATE
def query_stage_contacts(session, query_limit, **kwargs):
    """-----------------------------------------------------------
    Description: Will query all of the records from the StageContact table 
    Argument: (1)session (2)integer for query limit (3)query filters
    Return: list of org source objects 
    -----------------------------------------------------------"""
    print("CHECK query_stage_contacts")
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
    #     print("CHECK SC {}".format(sc.process_status__c))
    return stage_contacts


# ORG SOURCE UPDATE
def query_organization_source(session, query_limit, **kwargs):
    """-----------------------------------------------------------
    Description: Will query all of the records from the OrganizationSource table 
    Argument: (1)session (2)integer for query limit (3)query filters
    Return: list of org source objects 
    -----------------------------------------------------------"""
    print("CHECK query_organization_source")
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
    #     print("CHECK ORG {}".format(org.client_id__c))
    return organization_sources


# ORG SOURCE UPDATE
def organization_source_dictionary(organization_sources):
    """-----------------------------------------------------------
    Description: create a dictionary with org sources
    Argument:(1)list of organization source
    Return: dictionary with the [key]=client_id [value]=obj
    -----------------------------------------------------------"""
    print("CHECK organization_source")
    org_dict = dict()

    for org in organization_sources:
        org_dict[org.client_id__c] = org
    return org_dict
