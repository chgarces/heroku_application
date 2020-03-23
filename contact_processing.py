from session_loader import *
from utility_factory import *
from contact_preparation import *

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
