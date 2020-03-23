from session_loader import *
from uuid import uuid4

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


# REQUIRED FIELDS
def app_required_fields():
    """-----------------------------------------------------------  
    Description: This tuple determines the required fields for app
    Argument: 
    Return: Tuple
    -----------------------------------------------------------"""
    is_app_required_fields = (
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
    return is_app_required_fields


# REQUIRED FIELDS
def dealer_required_fields():
    """-----------------------------------------------------------  
    Description: This tuple determines the required fields
    Argument: 
    Return: Tuple
    -----------------------------------------------------------"""
    is_dealer_required_fields = (
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
    return is_dealer_required_fields


# REQUIRED FIELDS
def salesforce_org_required_fields():
    """-----------------------------------------------------------  
    Description: This tuple determines the required fields
    Argument: 
    Return: Tuple
    -----------------------------------------------------------"""
    is_salesforce_org_required_fields = (
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
    return is_salesforce_org_required_fields


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
def required_field_validator(session, obj):
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
        rfv["HAS_ERROR"] = True
        rfv["ERROR_FIELDS"] = required_errors
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
            sc.status__c = "FAILED"
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
                sc.status__c = "FAILED"
                sc.error_message__c = " sms_consent_date__c,"
            if is_empty(sc.sms_data_use_purpose__c):
                sc.status__c = "FAILED"
                sc.error_message__c += " sms_consent_date__c,"
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
        rfv = required_field_validator(session, sc)
        sc.process_status__c = "REQUIRED FIELDS"
        if rfv.get("HAS_ERROR"):
            sc.status__c = "FAILED"
            sc.error_message__c = "REQUIRED FIELDS MISSING : {}".format(
                ", ".join(rfv.get("ERROR_FIELDS"))
            )
            session.add(sc)
        else:
            sc.status__c = "IN PROGRESS"
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
            sc.process_status__c = "ORG SOURCE"
            sc.source_contact_record_type_id__c = org_dict.get(
                sc.client_id__c
            ).source_contact_record_type_id__c
            sc.generic_record_type_id__c = org_dict.get(
                sc.client_id__c
            ).generic_record_type_id__c
            sc.source_name__c = org_dict.get(sc.client_id__c).source_name__c
            sc.status__c = "IN PROGRESS"
            session.add(sc)
        else:
            sc.process_status__c = "ORG SOURCE"
            sc.status__c = "FAILED"
            sc.error_message__c = "CLIENT DOES NOT EXIST"
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


# CREATION INDIVIDUAL
def create_individual(sc_dict):
    """-----------------------------------------------------------
    Description: creates individual objects
    Argument: (1)stage contacts dictionary
    Return: list of indiviual objects 
    -----------------------------------------------------------"""
    print("CHECK create_individual")
    ind_list = []
    for k in sc_dict.keys():
        if sc_dict.get(k).is_obfuscated__c:
            ind_list.append(obfuscated_individual(sc_dict.get(k)))
        else:
            ind_list.append(generic_individual(sc_dict.get(k)))
    return ind_list


# CREATION INDIVIDUAL
def generic_individual(stage_contact):
    ind = Individual()
    ind.firstname = stage_contact.first_name__c
    ind.lastname = stage_contact.last_name__c
    ind.individual_id_ext__c = get_unique_id()
    ind.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return ind


# CREATION INDIVIDUAL
def obfuscated_individual(stage_contact):
    ind = Individual()
    ind.firstname = stage_contact.source_name__c + "FirstName"
    ind.lastname = stage_contact.source_name__c + "LastName"
    ind.individual_id_ext__c = get_unique_id()
    ind.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return ind


# CREATION CONTACT
def create_contact(sc_dict, ind_dict):
    """-----------------------------------------------------------
    Description: creates contact objects
    Argument:  (1)stage contacts dictionary (2) individual dictionary
    Return: list of contact objects 
    -----------------------------------------------------------"""
    print("CHECK create_contact")
    cont_list = []
    for k in ind_dict.keys():
        if sc_dict.get(k).is_obfuscated__c:
            cont_list.append(
                obfuscated_contact(sc_dict.get(k), ind_dict.get(k).individual_id_ext__c)
            )
        else:
            cont_list.append(
                generic_contact(sc_dict.get(k), ind_dict.get(k).individual_id_ext__c)
            )
        if sc_dict.get(k).is_separate_contact__c:
            cont_list.append(
                source_contact(sc_dict.get(k), ind_dict.get(k).individual_id_ext__c)
            )
    return cont_list


# CREATION CONTACT
def generic_contact(stage_contact, ind_id):
    """-----------------------------------------------------------
    Description: build contact objects :: Caterpillar/MA General 
    Argument:  (1)stage contact obj (2) individual id
    Return: contact object 
    -----------------------------------------------------------"""
    print("CHECK generic_contact")
    c = Contact()
    c.individual_id_ext__c = ind_id
    c.firstname = stage_contact.first_name__c
    c.lastname = stage_contact.last_name__c
    c.recordtypeid = stage_contact.generic_record_type_id__c
    c.contact_id_ext__c = get_unique_id()
    c.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return c


# CREATION CONTACT
def source_contact(stage_contact, ind_id):
    """-----------------------------------------------------------
    Description: build source contact objects :: This is the client type contact (Solar, CatFi)
    Argument:  (1)stage contact obj (2) individual id
    Return: contact object 
    -----------------------------------------------------------"""
    print("CHECK source_contact")
    c = Contact()
    c.individual_id_ext__c = ind_id
    c.firstname = stage_contact.first_name__c
    c.lastname = stage_contact.last_name__c
    c.contact_id_ext__c = get_unique_id()
    c.recordtypeid = stage_contact.source_contact_record_type_id__c
    c.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return c


# CREATION CONTACT
def obfuscated_contact(stage_contact, ind_id):
    """-----------------------------------------------------------
    Description: build obfustaced source contact objects 
    Argument:  (1)stage contact obj (2) individual id
    Return: contact object 
    -----------------------------------------------------------"""
    print("CHECK obfuscated_contact")
    c = Contact()
    c.individual_id_ext__c = ind_id
    c.bu_name__c = stage_contact.bu_name__c
    c.email = (
        "{}".format(stage_contact.source_id__c)
        + "@"
        + "{}".format(stage_contact.source_name__c)
    )
    c.firstname = stage_contact.source_name__c + "FirstName"
    c.lastname = stage_contact.source_name__c + "LastName"
    c.contact_id_ext__c = get_unique_id()
    c.recordtypeid = stage_contact.source_contact_record_type_id__c
    c.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return c


# CREATION CONTACT SOURCE
def create_contact_source(sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: creates contact source objects
    Argument:  (1)stage contacts dictionary (2) contact dictionary
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK create_contact_source")
    cont_source_list = []
    # print("DEBUG sources : {}".format(cont_dict))
    for k in cont_dict.keys():
        for c in cont_dict.get(k):
            cs = ContactSource()
            cs.contact_id_ext__c = c.contact_id_ext__c
            cs.firstname = sc_dict.get(k).first_name__c
            cs.lastname = sc_dict.get(k).last_name__c
            cs.contact_source_id_ext__c = get_unique_id()
            cs.stage_contact_id_ext__c = sc_dict.get(k).stage_contact_id_ext__c
            cont_source_list.append(cs)
    return cont_source_list


# CREATION CONTACT IDENTIFIER
def create_contact_identifier(sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: creates contact identifier objects
    Argument:  (1)stage contacts dictionary (2) contact dictionary
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK create_contact_identifier")
    cont_ident_list = []
    for k in cont_dict.keys():
        for c in cont_dict.get(k):
            cont_ident_list.append(
                master_identifier(sc_dict.get(k), c.contact_id_ext__c)
            )
            if not is_empty(sc_dict.get(k).source_id__c):
                cont_ident_list.append(
                    source_id_identifier(sc_dict.get(k), c.contact_id_ext__c)
                )
            if not sc_dict.get(k).is_obfuscated__c:
                if not is_empty(sc_dict.get(k).email__c):
                    cont_ident_list.append(
                        email_identifier(sc_dict.get(k), c.contact_id_ext__c)
                    )
                if not is_empty(sc_dict.get(k).phone__c):
                    cont_ident_list.append(
                        phone_identifier(sc_dict.get(k), c.contact_id_ext__c)
                    )
                if not is_empty(sc_dict.get(k).mobile__c):
                    cont_ident_list.append(
                        mobile_identifier(sc_dict.get(k), c.contact_id_ext__c)
                    )
                if not is_empty(sc_dict.get(k).dealer_code__c):
                    cont_ident_list.append(
                        dealer_code_identifier(sc_dict.get(k), c.contact_id_ext__c)
                    )
                if (
                    not is_empty(sc_dict.get(k).dealer_customer_number__c)
                    and sc_dict.get(k).is_dealer__c
                ):
                    cont_ident_list.append(
                        dealer_customer_number_identifier(
                            sc_dict.get(k), c.contact_id_ext__c
                        )
                    )

    return cont_ident_list


# CREATION CONTACT IDENTIFIER
def master_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Salesforce Id contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK master_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Salesforce ID"
    ci.identifier_group__c = "CRMI Master Contact ID"
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT IDENTIFIER
def source_id_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Source Id contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK source_id_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Salesforce ID"
    ci.identifier_group__c = stage_contact.source_name__c + "Master Contact ID"
    ci.Identifier__c = stage_contact.source_id__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT IDENTIFIER
def phone_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Phone contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK phone_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Comunication Channel"
    ci.identifier_group__c = "Phone"
    cd.Identifier__c = stage_contact.phone__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT IDENTIFIER
def mobile_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Mobile contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK phone_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Comunication Channel"
    ci.identifier_group__c = "Mobile"
    ci.Identifier__c = stage_contact.mobile__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT IDENTIFIER
def email_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Email contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK email_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Comunication Channel"
    ci.identifier_group__c = "Email"
    ci.Identifier__c = stage_contact.email__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT IDENTIFIER
def dealer_code_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Email contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK dealer_code_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Other Identifier"
    ci.identifier_group__c = "Dealer Code"
    ci.Identifier__c = stage_contact.dealer_code__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT IDENTIFIER
def dealer_customer_number_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: creates Email contact identifier object
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    print("CHECK dealer_code_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = cont_id
    ci.identifier_type__c = "Other Identifier"
    ci.identifier_group__c = "DC+DCN"
    ci.Identifier__c = (
        stage_contact.dealer_code__c + stage_contact.dealer_customer_number__c
    )
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    return ci


# CREATION CONTACT SOURCE IDENTIFIER
def create_contact_source_identifier(contact_source_dict, contact_identifier_dict):
    """-----------------------------------------------------------
    Description: Will create contact source identifier records
    Argument:(1)contact source dictionary (2)contact identifier dictionary
    Return: list of contact source identifier
    -----------------------------------------------------------"""
    cont_sou_ident_list = []
    for cid in contact_source_dict.keys():
        for ci in contact_identifier_dict.get(cid):
            csi = ContactSourceIdentifier()
            csi.stage_contact_id_ext__c = ci.stage_contact_id_ext__c
            csi.contact_identifier_id_ext__c = ci.contact_identifier_id_ext__c
            csi.contact_source_id_ext__c = contact_source_dict.get(
                cid
            ).contact_source_id_ext__c
            cont_sou_ident_list.append(csi)
            csi.contact_source_identifier_id_ext__c = get_unique_id()
    return cont_sou_ident_list


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


# CREATION CONTACT POINT
def create_contact_points(cont_identifier_list):
    """-----------------------------------------------------------
    Description: Build the contact point objects
    Argument: (1)list of contact identifiers (2)
    Return: list of contact points
    -----------------------------------------------------------"""
    print("CHECK create_contact_points")
    cont_point_list = []
    cont_point_email_list = []
    cont_point_phone_list = []
    cont_point_mobile_list = []
    for ci in cont_identifier_list:
        if ci.identifier_group__c == "Email":
            cont_point_email_list.append(ci)
        if ci.identifier_group__c == "Mobile":
            cont_point_mobile_list.append(ci)
        if ci.identifier_group__c == "Phone":
            cont_point_phone_list.append(ci)

    if len(cont_point_email_list) > 0:
        cont_point_list += create_contact_point_email(cont_point_email_list)
    if len(cont_point_mobile_list) > 0:
        cont_point_list += create_contact_point_mobile(cont_point_mobile_list)
    if len(cont_point_phone_list) > 0:
        cont_point_list += create_contact_point_phone(cont_point_phone_list)

    return cont_point_list


# CREATION CONTACT POINT
def create_contact_point_email(cont_identifier_list):
    """-----------------------------------------------------------
    Description: Build the contact point email objects
    Argument: (1)list of email contact identifiers (2)
    Return: list of contact point email
    -----------------------------------------------------------"""
    print("CHECK create_contact_point_email")

    cont_point_email_list = []
    for ci in cont_identifier_list:
        cpe = ContactPointEmail()
        cpe.contact_identifier_id_ext__c = ci.contact_identifier_id_ext__c
        cpe.contact_point_email_id_ext__c = get_unique_id()
        cpe.stage_contact_id_ext__c = ci.stage_contact_id_ext__c
        cont_point_email_list.append(cpe)
    return cont_point_email_list


# CREATION CONTACT POINT
def create_contact_point_phone(cont_identifier_list):
    """-----------------------------------------------------------
    Description: Build the contact point phone objects
    Argument: (1)list of phone contact identifiers (2)
    Return: list of contact point phone
    -----------------------------------------------------------"""
    print("CHECK create_contact_point_phone")

    cont_point_phone_list = []
    for ci in cont_identifier_list:
        cpp = ContactPointPhone()
        cpp.contact_identifier_id_ext__c = ci.contact_identifier_id_ext__c
        cpp.contact_point_phone_id_ext__c = get_unique_id()
        cpe.stage_contact_id_ext__c = ci.stage_contact_id_ext__c
        cont_point_phone_list.append(cpp)
    return cont_point_phone_list


# CREATION CONTACT POINT
def create_contact_point_mobile(cont_identifier_list):
    """-----------------------------------------------------------
    Description: Build the contact point mobile objects
    Argument: (1)list or mobile contact identifiers (2)
    Return: list of contact point mobile
    -----------------------------------------------------------"""
    print("CHECK create_contact_point_mobile")

    cont_point_mobile_list = []
    for ci in cont_identifier_list:
        cpm = ContactPointPhone()
        cpm.contact_identifier_id_ext__c = ci.contact_identifier_id_ext__c
        cpm.contact_point_phone_id_ext__c = get_unique_id()
        cpe.stage_contact_id_ext__c = ci.stage_contact_id_ext__c
        cont_point_mobile_list.append(cpm)
    return cont_point_mobile_list


# CREATION CONTACT POINT CONSENT
def create_contact_point_consent(cont_point_list, sc_dict, ind_dict):
    """-----------------------------------------------------------
    Description: Create contact point consent 
    Argument:(1)list of contact point (email/phone/mobile) (2)Stage contact dictionary (3)Individual dictionary
    Return: list of contact point consent 
    -----------------------------------------------------------"""
    print("CHECK create_contact_point_consent")
    cont_consent_list = []

    for cp in cont_point_list:
        cpc = ContactPointConsent()
        cpc.contact_point_consent_id_ext__c = get_unique_id()
        cpc.stage_contact_id_ext__c = cp.stage_contact_id_ext__c
        cpc.individual_id_ext__c = ind_dict.get(
            cp.stage_contact_id_ext__c
        ).individual_id_ext__c
        cont_consent_list.append(cpc)
    return cont_consent_list


# GENERIC
def manage_create_records(session, stage_contacts):
    """-----------------------------------------------------------
    Description: Will manage the creation of all the contact related records  
    Argument:(1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    print("CHECK manage_create_records")
    sc_dict = create_dictionary(stage_contacts)
    # Individual
    ind_list = create_individual(sc_dict)
    ind_dict = create_dictionary(ind_list)
    add_objects_to_session(session, ind_list)
    # Contact
    cont_list = create_contact(sc_dict, ind_dict)
    cont_dict = create_dictionary_list(cont_list)
    add_objects_to_session(session, cont_list)
    # ContactSource
    cont_source_list = create_contact_source(sc_dict, cont_dict)
    add_objects_to_session(session, cont_source_list)
    # ContactIdentifier
    cont_identifier_list = create_contact_identifier(sc_dict, cont_dict)
    add_objects_to_session(session, cont_identifier_list)
    # ContactSourceIdentifier
    contact_source_dict = contact_source_dictionary(cont_source_list)
    contact_identifier_dict = contact_identifier_dictionary(cont_identifier_list)
    cont_sou_ident_list = create_contact_source_identifier(
        contact_source_dict, contact_identifier_dict
    )
    add_objects_to_session(session, cont_sou_ident_list)
    # ContactPoint
    cont_point_list = create_contact_points(cont_identifier_list)
    add_objects_to_session(session, cont_point_list)
    # ContactPointConsent
    cont_consent_list = create_contact_point_consent(cont_point_list, sc_dict, ind_dict)
    add_objects_to_session(session, cont_consent_list)

    if session.new:
        dml_stage_contact(session)
        # update StageContacts status
        add_objects_to_session(session, update_stage_contacts(stage_contacts))
        dml_stage_contact(session)


if __name__ == "__main__":
    session = loadSession()
    # DEBUG

    # SEQUENCE
    query_limit = 100
    update_stage_contact_with_org_source(
        session,
        query_stage_contacts(
            session,
            query_limit,
            process_status__c=["NOT STARTED"],
            status__c=["NOT STARTED"],
        ),
        organization_source_dictionary(
            query_organization_source(session, query_limit, is_active__c=[True])
        ),
    )

    validate_required_fields(
        session,
        query_stage_contacts(
            session,
            query_limit,
            process_status__c=["ORG SOURCE"],
            status__c=["IN PROGRESS"],
        ),
    )
    validate_email_fields(
        session,
        query_stage_contacts(
            session,
            query_limit,
            process_status__c=["REQUIRED FIELDS"],
            status__c=["IN PROGRESS"],
        ),
    )
    validate_mobile_fields(
        session,
        query_stage_contacts(
            session,
            query_limit,
            process_status__c=["EMAIL FIELDS"],
            status__c=["IN PROGRESS"],
        ),
    )
    manage_create_records(
        session,
        query_stage_contacts(
            session,
            query_limit,
            process_status__c=["MOBILE FIELDS"],
            status__c=["IN PROGRESS"],
            is_matched_completed=[True],
        ),
    )
