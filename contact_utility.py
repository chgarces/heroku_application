from uuid import uuid4

#
# APP REQUIRED FIELDS
def app_required_fields():
    """-----------------------------------------------------------  
    Description: This tuple determines the required fields for app
    Argument: 
    Return: Tuple
    -----------------------------------------------------------"""
    app_required = (
        # "campaign_most_recent__c",
        # "client_id__c",
        # "company_name__c",
        # "contact_source_most_recent__c",
        # "data_processing__c",
        # "dealer_code__c",
        "email__c",
        "email_consent_date__c",
        "email_opt_in_status__c",
        "first_name__c",
        # "heroku_cms_processing__c",
        # "ingestion_point__c",
        "last_name__c",
        # "phone__c",
        # "state_code__c",
    )
    return app_required


# DEALER REQUIRED FIELDS
def dealer_required_fields():
    """-----------------------------------------------------------  
    Description: This tuple determines the required fields
    Argument: 
    Return: Tuple
    -----------------------------------------------------------"""
    dealer_required = (
        # "billing_zip_postal_code__c",
        # "billingcity__c",
        # "billingcountry__c",
        # "billingstate_province__c",
        # "billingstreet__c",
        # "campaign_most_recent__c",
        # "campign__c",
        # "client_id__c",
        # "company_name__c",
        # "contact_source_most_recent__c",
        # "data_processing__c",
        "dealer_code__c",
        "email__c",
        # "dealer_customer_number__c",
        # "email_consent_date__c",
        # "email_opt_in_status__c",
        "first_name__c",
        # "heroku_cms_processing__c",
        # "ingestion_point__c",
        "last_name__c",
        # "phone__c",
        # "state_code__c",
    )
    return dealer_required


# SALESFORCE REQUIRED FIELDS
def salesforce_org_required_fields():
    """-----------------------------------------------------------  
    Description: This tuple determines the required fields
    Argument: 
    Return: Tuple
    -----------------------------------------------------------"""
    salesforce_org_required = (
        # "campaign_most_recent__c",
        # "client_id__c",
        # "company_name__c",
        # "contact_source_most_recent__c",
        # "data_processing__c",
        # "dealer_code__c",
        "email__c",
        # "email_consent_date__c",
        # "email_opt_in_status__c",
        "first_name__c",
        # "heroku_cms_processing__c",
        # "ingestion_point__c",
        "last_name__c",
        # "phone__c",
        # "state_code__c",
    )
    return salesforce_org_required


# GENERIC
def get_unique_id():
    """-----------------------------------------------------------
    Description: creates a unique id
    Argument: 
    Return: unique id
    -----------------------------------------------------------"""
    print("CHECK get_unique_id")
    return uuid4().hex[:18]


# GENERIC
def is_empty(obj):
    """-----------------------------------------------------------
    Description: checks if field has values or is null/empty 
    Argument: (1)object
    Return: Boolean
    -----------------------------------------------------------"""
    if isinstance(obj, str):
        if not (obj and not obj.isspace()):
            return True
        else:
            return False
    elif obj == None:
        return True
    else:
        return False


# GENERIC
def add_objects_to_session(session, obj_list):
    """-----------------------------------------------------------
    Description: add object to session 
    Argument: (1)session (2)list of objects
    Return: session
    -----------------------------------------------------------"""
    print("CHECK add_objects_to_session")
    for obj in obj_list:
        session.add(obj)

    return session


# GENERIC
def dml_stage_contact(session):
    """-----------------------------------------------------------
    Description: Manage DML operation in the database
    Argument: db session
    Return: 
    -----------------------------------------------------------"""
    print("CHECK dml_stage_contact")
    try:
        session.commit()
        # TODO: CATCH ERRORS
    except expression as identifier:
        print("THERE WAS AN ERROR WHILE UPDATING STAGE CONTACTS")
    finally:
        session.close()


# GENERIC
def create_dictionary(objects):
    """-----------------------------------------------------------
    Description: Will create a dictionary with a list of objects
    Argument:(1)list of objects
    Return: dictionary with the [key]=stage_contact_id_ext__c [value]=obj
    -----------------------------------------------------------"""
    print("CHECK create_dictionary")
    sc_dict = dict()
    for obj in objects:
        sc_dict[obj.stage_contact_id_ext__c] = obj
    return sc_dict


# GENERIC
def create_dictionary_list(objects):
    """-----------------------------------------------------------
    Description: Will create a dictionary with a list of objects
    Argument:(1)list of objects
    Return: dictionary with the [key]=stage_contact_id_ext__c [value]=[obj]
    -----------------------------------------------------------"""
    print("CHECK create_dictionary")
    sc_dict = dict()
    for obj in objects:
        if obj.stage_contact_id_ext__c in sc_dict.keys():
            sc_dict.get(obj.stage_contact_id_ext__c).append(obj)
        else:
            sc_dict[obj.stage_contact_id_ext__c] = [obj]
    return sc_dict


# GENERIC
def update_stage_contacts(stage_contacts):
    """-----------------------------------------------------------
    Description: Will update the stage contacs status after the related record are created
    Argument:(1)list of stage contacts
    Return: return a list of stage contacts
    -----------------------------------------------------------"""
    stage_contact_list = []
    for sc in stage_contacts:
        sc.process_status__c = "POSTGRES COMPLETED"
        stage_contact_list.append(sc)
    return stage_contact_list


# CREATION CONTACT SOURCE IDENTIFIER
def contact_identifier_dictionary(cont_identifier_list):
    """-----------------------------------------------------------
    Description: Will create a dictionary with a list of objects
    Argument:(1)list of objects
    Return: dictionary with the [key]=contact_id_ext__c [value]=[obj]
    -----------------------------------------------------------"""
    print("CHECK contact_identifier_dictionary")
    contact_identifier_dict = dict()
    for ci in cont_identifier_list:
        if ci.contact_id_ext__c in contact_identifier_dict.keys():
            contact_identifier_dict.get(ci.contact_id_ext__c).append(ci)
        else:
            contact_identifier_dict[ci.contact_id_ext__c] = [ci]
    return contact_identifier_dict


# CREATION CONTACT SOURCE IDENTIFIER
def contact_source_dictionary(cont_source_list):
    """-----------------------------------------------------------
    Description: Will create a dictionary with a list of objects
    Argument:(1)list of cont_source_list
    Return: dictionary with the [key]=contact_id_ext__c [value]=contact_source_id_ext__c
    -----------------------------------------------------------"""
    print("CHECK contact_source_dictionary")
    contact_source_dict = dict()
    for cs in cont_source_list:
        contact_source_dict[cs.contact_id_ext__c] = cs
    return contact_source_dict


def contact_dictionary(cont_list):
    """-----------------------------------------------------------
    Description: Will create a dictionary with a list of objects
    Argument:(1)list of contact
    Return: dictionary with the [key]=contact_id_ext__c [value]=obj
    -----------------------------------------------------------"""
    print("CHECK contact_dictionary")
    cont_dict = dict()
    for c in cont_list:
        cont_dict[c.contact_id_ext__c] = c
    return cont_dict
