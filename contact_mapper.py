from contact_model_engine import *
from contact_utility import *
from contact_variables import *
from datetime import datetime


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
    ind.firstname = stage_contact.source_name__c + FIRSTNAME
    ind.lastname = stage_contact.source_name__c + LASTNAME
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

    c.company_name__c = stage_contact.company_name__c
    c.consent_date__c = stage_contact.consent_date__c
    # TODO Consent level summary
    # c.consent_level_summary__c = stage_contact.consent_level_summary__c
    c.contact_id_ext__c = get_unique_id()
    c.email = stage_contact.email
    c.email_matching_id__c = stage_contact.email
    c.firstname = stage_contact.first_name__c
    c.heroku_cms_processing_source__c = stage_contact.heroku_cms_processing_source__c
    c.individual_id_ext__c = ind_id
    c.industry__c = stage_contact.industry__c
    c.industry_level_2__c = stage_contact.industry_level_2__c
    c.isoname__c = stage_contact.language__c
    c.job_role__c = stage_contact.job_role__c
    c.language__c = stage_contact.language__c
    c.lastname = stage_contact.last_name__c
    c.level_of_interest__c = stage_contact.level_of_interest__c
    c.mailingcity = stage_contact.mailingcity
    c.mailingcountrycode = stage_contact.mailingcountrycode
    c.mailingpostalcode = stage_contact.mailingpostalcode
    c.mailingstatecode = stage_contact.mailingstatecode
    c.mailingstreet = stage_contact.mailingstreet
    c.matmowner__c = CATERPILLAR
    c.mobile = stage_contact.mobile__c
    c.original_ingestion_point__c = stage_contact.original_ingestion_point__c
    c.product_of_interest__c = stage_contact.product_of_interest__c
    c.product_of_interest_text__c = stage_contact.product_of_interest_text__c
    c.purchase_timeframe__c = stage_contact.purchase_timeframe__c
    c.recordtypeid = stage_contact.generic_record_type_id__c
    c.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    c.status__c = ACTIVE

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

    c.company_name__c = stage_contact.company_name__c
    c.consent_date__c = stage_contact.consent_date__c
    # TODO Consent level summary
    # c.consent_level_summary__c = stage_contact.consent_level_summary__c
    c.contact_id_ext__c = get_unique_id()
    c.email = stage_contact.email
    c.email_matching_id__c = stage_contact.email
    c.firstname = stage_contact.first_name__c
    c.heroku_cms_processing_source__c = stage_contact.heroku_cms_processing_source__c
    c.individual_id_ext__c = ind_id
    c.industry__c = stage_contact.industry__c
    c.industry_level_2__c = stage_contact.industry_level_2__c
    c.isoname__c = stage_contact.language__c
    c.job_role__c = stage_contact.job_role__c
    c.language__c = stage_contact.language__c
    c.lastname = stage_contact.last_name__c
    c.level_of_interest__c = stage_contact.level_of_interest__c
    c.mailingcity = stage_contact.mailingcity
    c.mailingcountrycode = stage_contact.mailingcountrycode
    c.mailingpostalcode = stage_contact.mailingpostalcode
    c.mailingstatecode = stage_contact.mailingstatecode
    c.mailingstreet = stage_contact.mailingstreet
    c.matmowner__c = stage_contact.source_name__c
    c.mobile = stage_contact.mobile__c
    c.original_ingestion_point__c = stage_contact.original_ingestion_point__c
    c.product_of_interest__c = stage_contact.product_of_interest__c
    c.product_of_interest_text__c = stage_contact.product_of_interest_text__c
    c.purchase_timeframe__c = stage_contact.purchase_timeframe__c
    c.recordtypeid = stage_contact.generic_record_type_id__c
    c.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    c.status__c = ACTIVE

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
        + AT
        + "{}".format(stage_contact.source_name__c)
    )
    c.firstname = stage_contact.source_name__c + FIRSTNAME
    c.lastname = stage_contact.source_name__c + LASTNAME
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

    c.bu_name__c = stage_contact.bu_name__c
    c.campaign_most_recent__c = stage_contact.campaign_most_recent__c
    c.company_name__c = stage_contact.company_name__c
    c.consent_date__c = stage_contact.consent_date__c
    c.consent_level__c = stage_contact.consent_level__c
    c.contact_source__c = stage_contact.source_name__c
    c.contact_source_details_most_recent__c = (
        stage_contact.contact_source_details_most_recent__c
    )
    c.contact_source_most_recent__c = stage_contact.contact_source_most_recent__c
    c.data_processing_role__c = stage_contact.data_processing_role__c
    c.dealer_code__c = stage_contact.dealer_code__c
    c.email__c = stage_contact.email__c
    c.email_matching_id__c = stage_contact.email__c
    c.first_name__c = stage_contact.first_name__c
    c.form_name__c = stage_contact.form_name__c
    c.industry__c = stage_contact.industry__c
    c.industry_level_2__c = stage_contact.industry_level_2__c
    c.isoname__c = language__c
    c.job_role__c = stage_contact.job_role__c
    c.language__c = stage_contact.language__c
    c.last_name__c = stage_contact.last_name__c
    c.mailing_address_line_1__c = stage_contact.mailing_address_line_1__c
    c.mailing_city__c = stage_contact.mailing_city__c
    c.mailing_country__c = stage_contact.mailing_country__c
    c.mailing_state_province__c = stage_contact.mailing_state_province__c
    c.mailing_zip_postal_code__c = stage_contact.mailing_zip_postal_code__c
    c.mobile__c = stage_contact.mobile__c
    c.original_ingestion_point__c = stage_contact.original_ingestion_point__c
    c.phone__c = stage_contact.phone__c
    c.processed_date__c = datetime.utcnow()
    c.processed_details__c = TEST_PROCESSED
    c.processed_status__c = PROCESSED
    c.product_of_interest__c = stage_contact.product_of_interest__c
    c.product_of_interest_text__c = stage_contact.product_of_interest_text__c
    c.purchase_timeframe__c = stage_contact.purchase_timeframe__c
    c.sms_consent_date__c = stage_contact.sms_consent_date__c
    c.sms_opt_in_status__c = stage_contact.sms_opt_in_status__c
    c.source_date_created__c = datetime.utcnow()
    c.source_status__c = ACTIVE
    c.status__c = ACTIVE
    cs.contact_id_ext__c = cont_id
    cs.contact_source_id_ext__c = get_unique_id()
    cs.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return cs


# CREATION CONTACT IDENTIFIER
def email_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Email contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Email contact identifier object
    -----------------------------------------------------------"""
    print("CHECK email_identifier")
    ci = ContactIdentifier()

    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.identifier_type__c = COMMUNICATION CHANNEL
    ci.identifier_group__c = EMAIL
    ci.Identifier__c = stage_contact.email__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.status_time__c = stage_contact.email_consent_date__c
    ci.status__c = ACTIVE
    ci.matm_owner__c = contact.matm_owner__c
    ci.status_reason__c = NEW CONTACT CREATED
    ci.status_source__c = stage_contact.contact_source__c
    ci.last_known_activity__c = datetime.utcnow()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

    return ci


# CREATION CONTACT IDENTIFIER
def mobile_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Mobile contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Mobile contact identifier object
    -----------------------------------------------------------"""
    print("CHECK phone_identifier")
    ci = ContactIdentifier()

    # TODO MATMOWNER
    ci.Identifier__c = stage_contact.mobile__c
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.identifier_group__c = MOBILE
    ci.identifier_type__c = COMMUNICATION CHANNEL
    ci.last_known_activity__c = datetime.utcnow()
    ci.matm_owner__c = contact.matm_owner__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.status__c = ACTIVE
    ci.status_reason__c = 
    ci.status_source__c = stage_contact.contact_source__c
    ci.status_time__c = stage_contact.email_consent_date__c

    return ci


# CREATION CONTACT IDENTIFIER
def phone_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Phone contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Phone contact identifier object
    -----------------------------------------------------------"""
    print("CHECK phone_identifier")
    ci = ContactIdentifier()

    # TODO MATMOWNER
    ci.Identifier__c = stage_contact.mobile__c
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.identifier_group__c = PHONE
    ci.identifier_type__c = COMMUNICATION CHANNEL
    ci.last_known_activity__c = datetime.utcnow()
    ci.matm_owner__c = contact.matm_owner__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.status__c = ACTIVE
    ci.status_reason__c = NEW CONTACT CREATED
    ci.status_source__c = stage_contact.contact_source__c
    ci.status_time__c = stage_contact.email_consent_date__c

    return ci


# CREATION CONTACT IDENTIFIER
def master_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Salesforce Id contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: CRMI Id contact identifier object
    -----------------------------------------------------------"""
    print("CHECK master_identifier")
    ci = ContactIdentifier()

    # TODO MATMOWNER
    ci.status_source__c = stage_contact.contact_source__c
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.identifier_type__c = SALESFORCE_ID
    ci.identifier_group__c = CRMI_MASTER_CONTACT_ID
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.status__c = ACTIVE
    ci.status_reason__c = NEW CONTACT CREATED
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.matm_owner__c = contact.matm_owner__c
    ci.last_known_activity__c = datetime.utcnow()

    return ci


# CREATION CONTACT IDENTIFIER
def source_id_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Source Id contact identifier mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Source Id contact identifier object
    -----------------------------------------------------------"""
    print("CHECK source_id_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.identifier_type__c = SALESFORCE_ID
    ci.identifier_group__c = stage_contact.source_name__c + MASTER_CONTACT_ID
    ci.Identifier__c = stage_contact.source_id__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.matm_owner__c = contact.matm_owner__c

    return ci


# CREATION CONTACT IDENTIFIER
def dealer_code_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Dealer contact identifier Mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: Dealer contact identifier object  
    -----------------------------------------------------------"""
    print("CHECK dealer_code_identifier")
    ci = ContactIdentifier()

    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.identifier_type__c = OTHER_IDENTIFIER
    ci.identifier_group__c = DEALER_CODE
    ci.Identifier__c = stage_contact.dealer_code__c
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.status_reason__c = NEW CONTACT CREATED
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.matm_owner__c = contact.matm_owner__c
    ci.last_known_activity__c = datetime.utcnow()

    return ci


# CREATION CONTACT IDENTIFIER
def dealer_customer_number_identifier(stage_contact, contact):
    """-----------------------------------------------------------
    Description: Dealer Customer Number contact identifier Mapper
    Argument:  (1)stage contacts dictionary (2) contact id
    Return: dealer customer number contact identifier object
    -----------------------------------------------------------"""
    print("CHECK dealer_code_identifier")
    ci = ContactIdentifier()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.identifier_type__c = OTHER_IDENTIFIER
    ci.identifier_group__c = DC_DCN
    ci.Identifier__c = (
        stage_contact.dealer_code__c + stage_contact.dealer_customer_number__c
    )
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.matm_owner__c = contact.matm_owner__c

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
def contact_point_email(cont_ident, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Contact Point Email Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Email object
    -----------------------------------------------------------"""
    cpe = ContactPointEmail()

    cpe.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpe.contact_point_email_id_ext__c = get_unique_id()
    cpe.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c
    cpe.emailaddress = stage_contact.email__c
    cpe.activefromdate = stage_contact.email_consent_date__c
    cpe.contact_id_ext__c = contact.contact_id_ext__c
    cpe.email_status_mc__c = cont_ident.status__c
    cpe.emailmailbox = stage_contact.email__c[0 : stage_contact.email__c.find("@")]
    cpe.emaildomain = stage_contact.email__c[
        stage_contact.email__c.find(AT) + 1 : len(stage_contact.email__c)
    ]
    cpe.matm_owner__c = contact.matm_owner__c

    return cpe


# CONTACT POINT MOBILE
def contact_point_mobile(cont_ident, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Contact Point Mobile Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Mobile object
    -----------------------------------------------------------"""
    cpm = ContactPointPhone()
    cpm.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpm.contact_point_phone_id_ext__c = get_unique_id()
    cpm.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    cpm.telephonenumber = stage_contact.mobile__c
    cpm.activefromdate = stage_contact.sms_consent_date__c
    cpe.matm_owner__c = contact.matm_owner__c
    cpm.issmscapable = True
    cpm.isbusiness = False
    # TODO
    # cpm.areacode =
    # cpm.formattednationalphonenumber =

    return cpm


# CONTACT POINT MOBILE
def contact_point_phone(cont_ident, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Contact Point Phone Mapper
    Argument:  (1)contact identifier object 
    Return: Contact Point Phone object
    -----------------------------------------------------------"""
    cpp = ContactPointPhone()
    cpp.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpp.contact_point_phone_id_ext__c = get_unique_id()
    cpp.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    cpp.telephonenumber = stage_contact.phone__c
    cpp.activefromdate = stage_contact.sms_consent_date__c
    cpp.matm_owner__c = contact.matm_owner__c
    cpp.issmscapable = False
    cpp.isbusiness = True

    return cpp


# CONTACT POINT CONSENT
def email_contact_point_consent(cont_point, ind_id):
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

    # TODO email contact point consents!!!
