from uuid import uuid4
from sqlalchemy import exc
from contact_variables import *

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
        "phone__c",
        # "state_code__c",
        "mobile__c",
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
    # print("CHECK get_unique_id")
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
    # print("CHECK add_objects_to_session")
    for obj in obj_list:
        session.add(obj)

    return session


# GENERIC
def dml_submit_set_to_database(session, record_set_dictionary, sc_dict):
    """-----------------------------------------------------------
    Description: Manage DML operation in the database with the set of 
                    records and update the stage contact status
    Argument: db session
    Return: 
    -----------------------------------------------------------"""
    print("CHECK dml_submit_to_database")
    # TODO update stage contact with error message in case of error
    stage_contact_list = []
    for scid in record_set_dictionary.keys():
        for obj in record_set_dictionary.get(scid):
            session.add(obj)
        try:
            session.commit()
            sc_dict.get(scid).process_status__c = POSTGRES_COMPLETED
            sc_dict.get(scid).status__c = IN_PROGRESS
            stage_contact_list.append(sc_dict.get(scid))
        # TODO: CATCH ERRORS
        except exc.SQLAlchemyError as e:
            print("THERE WAS AN ERROR WHILE CREATING SET OF RECORDS ")
            sc_dict.get(scid).process_status__c = POSTGRES_FAILED
            sc_dict.get(scid).status__c = FAILED
            stage_contact_list.append(sc_dict.get(scid))

    if len(stage_contact_list) > 0:
        dml_list_of_objects(session, stage_contact_list)


# GENERIC
def dml_list_of_objects(session, obj_list):
    """-----------------------------------------------------------
    Description: Commit a list of object to db
    Argument:(1)list of stage contacts
    Return: return a list of stage contacts
    -----------------------------------------------------------"""
    print("CHECK dml_list_of_objects ")

    for obj in obj_list:
        session.add(obj)
    try:
        session.commit()
    except Exception as e:
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
    # print("CHECK create_dictionary")
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
    # print("CHECK create_dictionary")
    dict_list = dict()
    for obj in objects:
        if obj.stage_contact_id_ext__c in dict_list.keys():
            dict_list.get(obj.stage_contact_id_ext__c).append(obj)
        else:
            dict_list[obj.stage_contact_id_ext__c] = [obj]
    return dict_list


# CREATION CONTACT SOURCE IDENTIFIER
def contact_identifier_dictionary(cont_identifier_list):
    """-----------------------------------------------------------
    Description: Will create a dictionary with a list of objects
    Argument:(1)list of objects
    Return: dictionary with the [key]=contact_id_ext__c [value]=[obj]
    -----------------------------------------------------------"""
    # print("CHECK contact_identifier_dictionary")
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
    # print("CHECK contact_source_dictionary")
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
    # print("CHECK contact_dictionary")
    cont_dict = dict()
    for c in cont_list:
        cont_dict[c.contact_id_ext__c] = c
    return cont_dict


# GENERIC
def build_record_sets_dictionary(obj_list, record_set_dictionary):
    """-----------------------------------------------------------
    Description: Group the object to be inserted into db by stage_contact_id_ext__c
    Argument:(1)list of objects (2) dict() [key]= stage_contact_id_ext__c [value]= [obj]
    Return: dict()
    -----------------------------------------------------------"""
    for obj in obj_list:
        if obj.stage_contact_id_ext__c in record_set_dictionary.keys():
            record_set_dictionary.get(obj.stage_contact_id_ext__c).append(obj)
        else:
            record_set_dictionary[obj.stage_contact_id_ext__c] = [obj]

    return record_set_dictionary
