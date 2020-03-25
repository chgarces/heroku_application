from contact_preparation import *
from contact_mapper import *

# CREATION INDIVIDUAL
def create_individual(sc_dict):
    """-----------------------------------------------------------
    Description: creates individual objects
    Argument: (1)stage contacts dictionary
    Return: list of individual 
    -----------------------------------------------------------"""
    # print("CHECK create_individual")
    ind_list = []
    for k in sc_dict.keys():
        if sc_dict.get(k).is_obfuscated__c:
            ind_list.append(obfuscated_individual(sc_dict.get(k)))
        else:
            ind_list.append(generic_individual(sc_dict.get(k)))

    return ind_list


# CREATION CONTACT
def create_contact(sc_dict, ind_dict):
    """-----------------------------------------------------------
    Description: creates contact objects
    Argument:  (1)stage contacts dictionary (2) individual dictionary
    Return: list of contact objects 
    -----------------------------------------------------------"""
    # print("CHECK create_contact")
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


# CREATION CONTACT SOURCE
def create_contact_source(sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: creates contact source objects
    Argument:  (1)stage contacts dictionary (2) contact dictionary
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    # print("CHECK create_contact_source")
    cont_source_list = []
    for k in cont_dict.keys():
        for c in cont_dict.get(k):
            cont_source_list.append(contact_source(sc_dict.get(k), c.contact_id_ext__c))
    return cont_source_list


# CREATION CONTACT IDENTIFIER
def create_contact_identifier(sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: creates contact identifier objects
    Argument:  (1)stage contacts dictionary (2) contact dictionary
    Return: list of contact source objects 
    -----------------------------------------------------------"""
    # print("CHECK create_contact_identifier")
    cont_ident_list = []
    for k in cont_dict.keys():
        for c in cont_dict.get(k):
            cont_ident_list.append(master_identifier(sc_dict.get(k), c))
            if not is_empty(sc_dict.get(k).source_id__c):
                cont_ident_list.append(source_id_identifier(sc_dict.get(k), c))
            if not sc_dict.get(k).is_obfuscated__c:
                if not is_empty(sc_dict.get(k).email__c):
                    cont_ident_list.append(email_identifier(sc_dict.get(k), c))
                if not is_empty(sc_dict.get(k).phone__c):
                    cont_ident_list.append(phone_identifier(sc_dict.get(k), c))
                if not is_empty(sc_dict.get(k).mobile__c):
                    cont_ident_list.append(mobile_identifier(sc_dict.get(k), c))
                if not is_empty(sc_dict.get(k).dealer_code__c):
                    cont_ident_list.append(dealer_code_identifier(sc_dict.get(k), c))
                if (
                    not is_empty(sc_dict.get(k).dealer_customer_number__c)
                    and sc_dict.get(k).is_dealer__c
                ):
                    cont_ident_list.append(
                        dealer_customer_number_identifier(sc_dict.get(k), c)
                    )

    return cont_ident_list


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
            cont_sou_ident_list.append(
                contact_source_identifier(ci, contact_source_dict.get(cid))
            )
    return cont_sou_ident_list


# CREATION CONTACT POINTS
def filter_contact_identifier(cont_identifier_list, indentifier_group):
    """-----------------------------------------------------------
    Description: filter contact points by type Email, Phone, and Mobile
    Argument: (1)list of contact identifiers (2) indentifier_group
    Return: list of contact points
    -----------------------------------------------------------"""
    cont_point_list = []
    for ci in cont_identifier_list:
        if ci.identifier_group__c == indentifier_group:
            cont_point_list.append(ci)

    return cont_point_list


# CREATION CONTACT POINT EMAIL
def create_contact_point_email(cont_identifier_list, sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: Build the contact point email objects
    Argument: (1)list of email contact identifiers 
    Return: list of contact point email
    -----------------------------------------------------------"""
    # print("create_contact_point_email")

    cont_point_email_list = []
    for ci in cont_identifier_list:
        cont_point_email_list.append(
            contact_point_email(
                ci,
                sc_dict.get(ci.stage_contact_id_ext__c),
                cont_dict.get(ci.contact_id_ext__c),
            )
        )
    return cont_point_email_list


# CREATION CONTACT POINT PHONE
def create_contact_point_phone(cont_identifier_list, sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: Build the contact point phone objects
    Argument: (1)list of phone contact identifiers (2)
    Return: list of contact point phone
    -----------------------------------------------------------"""
    # print("CHECK create_contact_point_phone")

    cont_point_phone_list = []
    for ci in cont_identifier_list:
        cont_point_phone_list.append(
            contact_point_phone(
                ci,
                sc_dict.get(ci.stage_contact_id_ext__c),
                cont_dict.get(ci.contact_id_ext__c),
            )
        )
    return cont_point_phone_list


# CREATION CONTACT POINT MOBILE
def create_contact_point_mobile(cont_identifier_list, sc_dict, cont_dict):
    """-----------------------------------------------------------
    Description: Build the contact point mobile objects
    Argument: (1)list or mobile contact identifiers (2)
    Return: list of contact point mobile
    -----------------------------------------------------------"""
    # print("CHECK create_contact_point_mobile")

    cont_point_mobile_list = []
    for ci in cont_identifier_list:
        cont_point_mobile_list.append(
            contact_point_mobile(
                ci,
                sc_dict.get(ci.stage_contact_id_ext__c),
                cont_dict.get(ci.contact_id_ext__c),
            )
        )
    return cont_point_mobile_list


# CREATION CONTACT POINT CONSENT EMAIL
def create_contact_consent_email(cont_point_list, sc_dict, cont_id_dict):
    """-----------------------------------------------------------
    Description: mange the creation of contact consent for email
    Argument:(1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    email_consent_list = []
    for cp in cont_point_list:
        email_consent_list.append(
            email_contact_point_consent(
                cp,
                sc_dict.get(cp.stage_contact_id_ext__c),
                cont_id_dict.get(cp.contact_id_ext__c),
            )
        )
    return email_consent_list


# CREATION CONTACT POINT CONSENT MOBILE
def create_contact_consent_mobile(cont_point_list, sc_dict, cont_id_dict):
    """-----------------------------------------------------------
    Description: mange the creation of contact consent for mobile
    Argument:(1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    mobile_consent_list = []
    for cp in cont_point_list:
        mobile_consent_list.append(
            mobile_contact_point_consent(
                cp,
                sc_dict.get(cp.stage_contact_id_ext__c),
                cont_id_dict.get(cp.contact_id_ext__c),
            )
        )
    return mobile_consent_list


# CREATION CONTACT POINT CONSENT PHONE
def create_contact_consent_phone(cont_point_list, sc_dict, cont_id_dict):
    """-----------------------------------------------------------
    Description: mange the creation of contact consent for phone
    Argument:(1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    phone_consent_list = []
    for cp in cont_point_list:
        phone_consent_list.append(
            phone_contact_point_consent(
                cp,
                sc_dict.get(cp.stage_contact_id_ext__c),
                cont_id_dict.get(cp.contact_id_ext__c),
            )
        )
    return phone_consent_list


# GENERIC
def manage_create_records(session, stage_contacts):
    """-----------------------------------------------------------
    Description: Will manage the creation of all the consent model
    Argument:(1)session (2)list of stage contacts
    Return: 
    -----------------------------------------------------------"""
    # print("CHECK manage_create_records")
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
    # ContactPoint EMAIL
    cont_id_dict = contact_dictionary(cont_list)
    email_cont_ident_list = filter_contact_identifier(cont_identifier_list, EMAIL)
    cont_point_email_list = create_contact_point_email(
        email_cont_ident_list, sc_dict, cont_id_dict
    )
    add_objects_to_session(session, cont_point_email_list)
    # ContactPoint MOBILE
    mobile_cont_ident_list = filter_contact_identifier(cont_identifier_list, MOBILE)
    cont_point_mobile_list = create_contact_point_mobile(
        mobile_cont_ident_list, sc_dict, cont_id_dict
    )
    add_objects_to_session(session, cont_point_mobile_list)
    # ContactPoints PHONE
    phone_cont_ident_list = filter_contact_identifier(cont_identifier_list, PHONE)
    cont_point_phone_list = create_contact_point_phone(
        phone_cont_ident_list, sc_dict, cont_id_dict
    )
    add_objects_to_session(session, cont_point_phone_list)
    # MOBILE CONSENT
    mobile_consent_list = create_contact_consent_mobile(
        cont_point_mobile_list, sc_dict, cont_id_dict
    )
    add_objects_to_session(session, mobile_consent_list)
    # PHONE CONSENT
    phone_consent_list = create_contact_consent_phone(
        cont_point_phone_list, sc_dict, cont_id_dict
    )
    add_objects_to_session(session, phone_consent_list)
    # EMAIL CONSENT
    email_consent_list = create_contact_consent_email(
        cont_point_email_list, sc_dict, cont_id_dict
    )
    add_objects_to_session(session, email_consent_list)

    if session.new:
        dml_submit_to_database(session)
        # update StageContacts status
        add_objects_to_session(session, update_stage_contacts(stage_contacts))
        dml_submit_to_database(session)


# TODO VALIDATE THE RECORD MAPPING AND CREATION
# MAIN
if __name__ == "__main__":
    session = loadSession()
    # DEBUG

    # SEQUENCE
    query_limit = 100
    # CONTACT PREPARATION
    stage_contact_list = query_stage_contacts(
        session,
        query_limit,
        process_status__c=["NOT STARTED"],
        status__c=["NOT STARTED"],
    )
    if stage_contact_list.count() > 0:
        update_stage_contact_with_org_source(
            session,
            stage_contact_list,
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
    else:
        print("No records to prepare at this time")

    # CONTACT PROCESSING
    ready_stage_contact_list = query_stage_contacts(
        session,
        query_limit,
        process_status__c=["MOBILE FIELDS"],
        status__c=["IN PROGRESS"],
        is_matched_completed=[True],
    )
    if ready_stage_contact_list.count() > 0:
        manage_create_records(
            session, ready_stage_contact_list,
        )
    else:
        print("No stage records to process")
