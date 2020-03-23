from contact_model_engine import *
from contact_utility import *


# CREATION INDIVIDUAL
def generic_individual(stage_contact):
    """-----------------------------------------------------------
    Description: Individual mapper
    Argument: (1)stage contacts
    Return: Individual object
    -----------------------------------------------------------"""
    ind = Individual()
    ind.firstname = stage_contact.first_name__c
    ind.lastname = stage_contact.last_name__c
    ind.individual_id_ext__c = get_unique_id()
    ind.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return ind


# CREATION INDIVIDUAL
def obfuscated_individual(stage_contact):
    """-----------------------------------------------------------
    Description: Obfuscated Individual mapper
    Argument: (1)stage contacts
    Return: Individual Object 
    -----------------------------------------------------------"""
    ind = Individual()
    ind.firstname = stage_contact.source_name__c + "FirstName"
    ind.lastname = stage_contact.source_name__c + "LastName"
    ind.individual_id_ext__c = get_unique_id()
    ind.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return ind


# CREATION CONTACT
def generic_contact(stage_contact, ind_id):
    """-----------------------------------------------------------
    Description: Contact mapper :: Caterpillar/MA General 
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
    Description: Source Contact mapper :: This is the client type contact (Solar, CatFi)
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
    Description: Obfuscated Contact mapper
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
def contact_source(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description:  Contact Source mapper
    Argument:  (1)stage contact
    Return: contact source object 
    -----------------------------------------------------------"""
    print("CHECK contact_source")
    cs = ContactSource()
    cs.contact_id_ext__c = cont_id
    cs.firstname = stage_contact.first_name__c
    cs.lastname = stage_contact.last_name__c
    cs.contact_source_id_ext__c = get_unique_id()
    cs.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return cs


# CREATION CONTACT IDENTIFIER
def master_identifier(stage_contact, cont_id):
    """-----------------------------------------------------------
    Description: Salesforce Id contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: CRMI Id contact identifier object
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
    Description: Source Id contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Source Id contact identifier object
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
    Description: Phone contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Phone contact identifier object
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
    Description: Mobile contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Mobile contact identifier object
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
    Description: Email contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Email contact identifier object
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
    Description: Dealer contact identifier Mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Dealer contact identifier object  
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
    Description: Dealer Customer Number contact identifier Mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: dealer customer number contact identifier object
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
def contact_source_identifier(cont_ident, cont_sour):
    """-----------------------------------------------------------
    Description: Contact Source identifier Mapper
    Argument:  (1)contact identifier object (2) contact identifier object
    Return: contact source identifier object
    -----------------------------------------------------------"""
    csi = ContactSourceIdentifier()
    csi.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c
    csi.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    csi.contact_source_id_ext__c = cont_sour.contact_source_id_ext__c
    csi.contact_source_identifier_id_ext__c = get_unique_id()
    return csi


# CREATION CONTACT POINT EMAIL
def contact_point_email(cont_ident):
    """-----------------------------------------------------------
    Description: Contact Point Email Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Email object
    -----------------------------------------------------------"""
    cpe = ContactPointEmail()
    cpe.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpe.contact_point_email_id_ext__c = get_unique_id()
    cpe.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return cpe


# CONTACT POINT MOBILE
def contact_point_phone(cont_ident):
    """-----------------------------------------------------------
    Description: Contact Point Phone Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Phone object
    -----------------------------------------------------------"""
    cpp = ContactPointPhone()
    cpp.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpp.contact_point_phone_id_ext__c = get_unique_id()
    cpp.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return cpp


# CONTACT POINT MOBILE
def contact_point_mobile(cont_ident):
    """-----------------------------------------------------------
    Description: Contact Point Mobile Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Mobile object
    -----------------------------------------------------------"""
    cpm = ContactPointPhone()
    cpm.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpm.contact_point_phone_id_ext__c = get_unique_id()
    cpm.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return cpm


# CONTACT POINT CONSENT
def contact_point_consent(cont_point, ind_id):
    """-----------------------------------------------------------
    Description: Contact Point Consent Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Consent object
    -----------------------------------------------------------"""
    cpc = ContactPointConsent()
    cpc.contact_point_consent_id_ext__c = get_unique_id()
    cpc.stage_contact_id_ext__c = cont_point.stage_contact_id_ext__c
    cpc.individual_id_ext__c = ind_id

    return cpc
