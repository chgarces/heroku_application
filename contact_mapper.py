from contact_model_engine import *
from contact_utility import *
from contact_variables import *
from datetime import datetime, date


# STAGE CONTACT

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

    # ID's
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

    # ID's
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

    # TODO Consent level summary
    # c.consent_date__c = stage_contact.consent_date__c
    # c.consent_level_summary__c = stage_contact.consent_level_summary__c
    c.company_name__c = stage_contact.company_name__c
    c.email = stage_contact.email__c
    c.email_matching_id__c = stage_contact.email__c
    c.firstname = stage_contact.first_name__c
    c.heroku_cms_processing_source__c = stage_contact.heroku_cms_processing__c
    c.industry__c = stage_contact.industry__c
    c.industry_level_2__c = stage_contact.industry_level_2__c
    c.isoname__c = stage_contact.language__c
    c.job_role__c = stage_contact.job_role__c
    c.language__c = stage_contact.language__c
    c.lastname = stage_contact.last_name__c
    c.level_of_interest__c = stage_contact.level_of_interest__c
    c.mailingcity = stage_contact.mailing_city__c
    c.mailingcountrycode = stage_contact.country_code__c
    c.mailingpostalcode = stage_contact.mailing_postal_code__c
    c.mailingstatecode = stage_contact.state_code__c
    c.mailingstreet = stage_contact.mailing_street__c
    c.matm_owner__c = CATERPILLAR
    c.mobile = stage_contact.mobile__c
    c.original_ingestion_point__c = stage_contact.ingestion_point__c
    c.product_of_interest__c = stage_contact.product_of_interest__c
    c.product_of_interest_text__c = stage_contact.product_of_interest_text__c
    c.purchase_timeframe__c = stage_contact.purchase_timeframe__c
    c.recordtypeid = stage_contact.generic_record_type_id__c
    c.status__c = ACTIVE

    # ID's
    c.contact_id_ext__c = get_unique_id()
    c.individual_id_ext__c = ind_id
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

    # TODO Consent level summary
    # c.consent_date__c = stage_contact.consent_date__c
    # c.consent_level_summary__c = stage_contact.consent_level_summary__c
    c.company_name__c = stage_contact.company_name__c
    c.email = stage_contact.email__c
    c.email_matching_id__c = stage_contact.email__c
    c.firstname = stage_contact.first_name__c
    c.heroku_cms_processing_source__c = stage_contact.heroku_cms_processing__c
    c.industry__c = stage_contact.industry__c
    c.industry_level_2__c = stage_contact.industry_level_2__c
    c.isoname__c = stage_contact.language__c
    c.job_role__c = stage_contact.job_role__c
    c.language__c = stage_contact.language__c
    c.lastname = stage_contact.last_name__c
    c.level_of_interest__c = stage_contact.level_of_interest__c
    c.mailingcity = stage_contact.mailing_city__c
    c.mailingcountrycode = stage_contact.country_code__c
    c.mailingpostalcode = stage_contact.mailing_postal_code__c
    c.mailingstatecode = stage_contact.state_code__c
    c.mailingstreet = stage_contact.mailing_street__c
    c.matm_owner__c = stage_contact.source_name__c
    c.mobile = stage_contact.mobile__c
    c.original_ingestion_point__c = stage_contact.ingestion_point__c
    c.product_of_interest__c = stage_contact.product_of_interest__c
    c.product_of_interest_text__c = stage_contact.product_of_interest_text__c
    c.purchase_timeframe__c = stage_contact.purchase_timeframe__c
    c.recordtypeid = stage_contact.generic_record_type_id__c
    c.status__c = ACTIVE

    # ID'S
    c.contact_id_ext__c = get_unique_id()
    c.individual_id_ext__c = ind_id
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

    c.bu_name__c = stage_contact.bu_name__c
    c.email = (
        "{}".format(stage_contact.source_id__c)
        + AT
        + "{}".format(stage_contact.source_name__c)
    )
    c.firstname = stage_contact.source_name__c + FIRSTNAME
    c.lastname = stage_contact.source_name__c + LASTNAME
    c.recordtypeid = stage_contact.source_contact_record_type_id__c
    c.matm_owner__c = stage_contact.source_name__c

    # ID'S
    c.contact_id_ext__c = get_unique_id()
    c.individual_id_ext__c = ind_id
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

    # TODO
    # cs.consent_date__c = stage_contact.consent_date__c
    # cs.consent_level__c = stage_contact.consent_level__c
    cs.bu_name__c = stage_contact.bu_name__c
    cs.campaign_most_recent__c = stage_contact.campaign_most_recent__c
    cs.company_name__c = stage_contact.company_name__c
    cs.contact_source__c = stage_contact.source_name__c
    cs.contact_source_details_most_recent__c = (
        stage_contact.contact_source_most_recent_details__c
    )
    cs.contact_source_most_recent__c = stage_contact.contact_source_most_recent__c
    cs.data_processing_role__c = stage_contact.data_processing__c
    cs.dealer_code__c = stage_contact.dealer_code__c
    cs.email__c = stage_contact.email__c
    cs.email_matching_id__c = stage_contact.email__c
    cs.first_name__c = stage_contact.first_name__c
    cs.form_name__c = stage_contact.form_name__c
    cs.industry__c = stage_contact.industry__c
    cs.industry_level_2__c = stage_contact.industry_level_2__c
    cs.isoname__c = stage_contact.language__c
    cs.job_role__c = stage_contact.job_role__c
    cs.language__c = stage_contact.language__c
    cs.last_name__c = stage_contact.last_name__c
    cs.mailing_address_line_1__c = stage_contact.mailing_street__c
    cs.mailing_city__c = stage_contact.mailing_city__c
    cs.mailing_country__c = stage_contact.country_code__c
    cs.mailing_state_province__c = stage_contact.state_code__c
    cs.mailing_zip_postal_code__c = stage_contact.mailing_postal_code__c
    cs.mobile__c = stage_contact.mobile__c
    cs.original_ingestion_point__c = stage_contact.ingestion_point__c
    cs.phone__c = stage_contact.phone__c
    cs.processed_date__c = datetime.utcnow()
    cs.processed_details__c = TEST_PROCESSED
    cs.processed_status__c = PROCESSED
    cs.product_of_interest__c = stage_contact.product_of_interest__c
    cs.product_of_interest_text__c = stage_contact.product_of_interest_text__c
    cs.purchase_timeframe__c = stage_contact.purchase_timeframe__c
    cs.sms_consent_date__c = stage_contact.sms_consent_date__c
    cs.sms_opt_in_status__c = stage_contact.sms_opt_in_status__c
    cs.source_date_created__c = datetime.utcnow()
    cs.source_status__c = ACTIVE
    cs.status__c = ACTIVE

    # ID's
    cs.contact_source_id_ext__c = get_unique_id()
    cs.contact_id_ext__c = cont_id
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

    ci.identifier_type__c = COMMUNICATION_CHANNEL
    ci.identifier_group__c = EMAIL
    ci.Identifier__c = stage_contact.email__c
    ci.status_time__c = stage_contact.email_consent_date__c
    ci.status__c = ACTIVE
    ci.matm_owner__c = contact.matm_owner__c
    ci.status_reason__c = NEW_CONTACT_CREATED
    ci.status_source__c = stage_contact.source_name__c
    ci.last_known_activity__c = datetime.utcnow()

    # ID's
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.contact_id_ext__c = contact.contact_id_ext__c
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

    ci.Identifier__c = stage_contact.mobile__c
    ci.identifier_group__c = MOBILE
    ci.identifier_type__c = COMMUNICATION_CHANNEL
    ci.last_known_activity__c = datetime.utcnow()
    ci.matm_owner__c = contact.matm_owner__c
    ci.status__c = ACTIVE
    ci.status_reason__c = NEW_CONTACT_CREATED
    ci.status_source__c = stage_contact.contact_source__c
    ci.status_time__c = stage_contact.email_consent_date__c

    # ID's
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

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

    ci.Identifier__c = stage_contact.mobile__c
    ci.identifier_group__c = PHONE
    ci.identifier_type__c = COMMUNICATION_CHANNEL
    ci.last_known_activity__c = datetime.utcnow()
    ci.matm_owner__c = contact.matm_owner__c
    ci.status__c = ACTIVE
    ci.status_reason__c = NEW_CONTACT_CREATED
    ci.status_source__c = stage_contact.contact_source__c
    ci.status_time__c = stage_contact.email_consent_date__c

    # ID's
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

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

    ci.status_source__c = stage_contact.source_name__c
    ci.identifier_type__c = SALESFORCE_ID
    ci.identifier_group__c = CRMI_MASTER_CONTACT_ID
    ci.status__c = ACTIVE
    ci.status_reason__c = NEW_CONTACT_CREATED
    ci.matm_owner__c = contact.matm_owner__c
    ci.last_known_activity__c = datetime.utcnow()

    # ID'S
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

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

    ci.identifier_type__c = SALESFORCE_ID
    ci.identifier_group__c = stage_contact.source_name__c + MASTER_CONTACT_ID
    ci.Identifier__c = stage_contact.source_id__c
    ci.matm_owner__c = contact.matm_owner__c

    # ID's
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

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

    ci.identifier_type__c = OTHER_IDENTIFIER
    ci.identifier_group__c = DEALER_CODE
    ci.Identifier__c = stage_contact.dealer_code__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.status_reason__c = NEW_CONTACT_CREATED
    ci.matm_owner__c = contact.matm_owner__c
    ci.last_known_activity__c = datetime.utcnow()

    # ID's
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.contact_id_ext__c = contact.contact_id_ext__c
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c

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

    ci.identifier_type__c = OTHER_IDENTIFIER
    ci.identifier_group__c = DC_DCN
    ci.Identifier__c = (
        stage_contact.dealer_code__c + stage_contact.dealer_customer_number__c
    )
    ci.matm_owner__c = contact.matm_owner__c

    # ID's
    ci.contact_identifier_id_ext__c = get_unique_id()
    ci.stage_contact_id_ext__c = stage_contact.stage_contact_id_ext__c
    ci.contact_id_ext__c = contact.contact_id_ext__c

    return ci


# CREATION CONTACT SOURCE IDENTIFIER
def contact_source_identifier(cont_ident, cont_sour):
    """-----------------------------------------------------------
    Description: Contact Source identifier Mapper
    Argument:  (1)contact identifier object (2) contact identifier object
    Return: contact source identifier object
    -----------------------------------------------------------"""
    csi = ContactSourceIdentifier()

    # ID's
    csi.contact_source_identifier_id_ext__c = get_unique_id()
    csi.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    csi.contact_source_id_ext__c = cont_sour.contact_source_id_ext__c
    csi.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return csi


# CREATION CONTACT POINT EMAIL
def contact_point_email(cont_ident, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Contact Point Email Mapper
    Argument:  (1)contact identifier object (2)stage contact (3)comtact
    Return: Contact Point Email object
    -----------------------------------------------------------"""

    # print("CHECK stage_contact {}".format(stage_contact))
    # print("CHECK contact {}".format(contact))

    cpe = ContactPointEmail()

    cpe.emailaddress = stage_contact.email__c
    cpe.activefromdate = stage_contact.email_consent_date__c
    cpe.email_status_mc__c = cont_ident.status__c
    cpe.emailmailbox = stage_contact.email__c[0 : stage_contact.email__c.find("@")]
    cpe.emaildomain = stage_contact.email__c[
        stage_contact.email__c.find(AT) + 1 : len(stage_contact.email__c)
    ]
    cpe.matm_owner__c = contact.matm_owner__c

    # ID's
    cpe.contact_point_email_id_ext__c = get_unique_id()
    cpe.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpe.contact_id_ext__c = cont_ident.contact_id_ext__c
    cpe.individual_id_ext__c = contact.individual_id_ext__c
    cpe.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return cpe


# CONTACT POINT MOBILE
def contact_point_mobile(cont_ident, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Contact Point Mobile Mapper
    Argument:  (1)contact identifier object (2)stage contact (3)comtact
    Return: Contact Point Mobile object
    -----------------------------------------------------------"""
    cpm = ContactPointPhone()

    cpm.telephonenumber = stage_contact.mobile__c
    cpm.activefromdate = stage_contact.sms_consent_date__c
    cpm.matm_owner__c = contact.matm_owner__c
    cpm.issmscapable = True
    cpm.isbusiness = False
    # TODO
    # cpm.areacode =
    # cpm.formattednationalphonenumber =

    # ID's
    cpm.contact_point_phone_id_ext__c = get_unique_id()
    cpm.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpm.individual_id_ext__c = contact.individual_id_ext__c
    cpm.contact_id_ext__c = cont_ident.contact_id_ext__c
    cpm.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return cpm


# CONTACT POINT MOBILE
def contact_point_phone(cont_ident, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Contact Point Phone Mapper
    Argument:  (1)contact identifier object (2)stage contact (3)comtact
    Return: Contact Point Phone object
    -----------------------------------------------------------"""
    cpp = ContactPointPhone()

    cpp.telephonenumber = stage_contact.phone__c
    cpp.activefromdate = stage_contact.sms_consent_date__c
    cpp.matm_owner__c = contact.matm_owner__c
    cpp.issmscapable = False
    cpp.isbusiness = True

    # ID'S
    cpp.contact_point_phone_id_ext__c = get_unique_id()
    cpp.contact_identifier_id_ext__c = cont_ident.contact_identifier_id_ext__c
    cpe.contact_id_ext__c = contact.contact_id_ext__c
    cpe.individual_id_ext__c = contact.individual_id_ext__c
    cpp.stage_contact_id_ext__c = cont_ident.stage_contact_id_ext__c

    return cpp


# CONTACT EMAIL POINT CONSENT
def email_contact_point_consent(cont_point, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Email Contact Point Consent Mapper
    Argument:  (1)contact identifier object (2)stage contact (3)comtact
    Return: Contact Point Consent object
    -----------------------------------------------------------"""
    epc = ContactPointConsent()

    epc.effectivefrom = stage_contact.email_consent_date__c
    epc.capturedate = stage_contact.email_consent_date__c
    epc.matm_owner__c = cont_point.matm_owner__c
    epc.capturesource = (
        "{}".format(stage_contact.source_name__c)
        + " | "
        + "{}".format(stage_contact.campaign_most_recent__c)
        + " | "
        + "{}".format(stage_contact.form_name__c)
    )[0, 255]
    epc.capturecontactpointtype = EMAIL
    epc.name = (
        EMAIL_CONSENT
        + "{}".format(stage_contact.source_name__c)
        + " | "
        + "{}".format(stage_contact.email__c)
        + " | "
        + date
    )[0, 255]

    # ID'S
    epc.data_use_purpose_id_ext__c = stage_contact.email_data_use_purpose__c
    epc.contact_point_consent_id_ext__c = get_unique_id()
    epc.stage_contact_id_ext__c = cont_point.stage_contact_id_ext__c
    epc.contact_id_ext__c = contact.contact_id_ext__c
    epc.contact_point_id_ext__c = cont_point.contact_point_email_id_ext__c
    epc.authorization_form_id_ext__c = stage_contact.authorization_form_id_ext__c

    return epc


# CONTACT MOBILE POINT CONSENT
def mobile_contact_point_consent(cont_point, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Mobile Contact Point Consent Mapper
    Argument:  (1)contact identifier object (2)stage contact (3)comtact
    Return: Contact Point Consent object
    -----------------------------------------------------------"""
    mpc = ContactPointConsent()

    mpc.effectivefrom = stage_contact.sms_consent_date__c
    mpc.capturedate = stage_contact.sms_consent_date__c
    mpc.matm_owner__c = cont_point.matm_owner__c
    epc.capturesource = (
        "{}".format(stage_contact.source_name__c)
        + " | "
        + "{}".format(stage_contact.campaign_most_recent__c)
        + " | "
        + "{}".format(stage_contact.form_name__c)
    )[0, 255]
    epc.capturecontactpointtype = MOBILE
    epc.name = (
        SMS_CONSENT
        + "{}".format(stage_contact.source_name__c)
        + " | "
        + "{}".format(stage_contact.mobile__c)
        + " | "
        + date
    )[0, 255]

    # ID'S
    mpc.data_use_purpose_id_ext__c = stage_contact.sms_data_use_purpose__c
    mpc.contact_point_consent_id_ext__c = get_unique_id()
    mpc.stage_contact_id_ext__c = cont_point.stage_contact_id_ext__c
    mpc.contact_id_ext__c = contact.contact_id_ext__c
    mpc.contact_point_id_ext__c = cont_point.contact_point_phone_id_ext__c
    mpc.authorization_form_id_ext__c = stage_contact.authorization_form_id_ext__c

    return mpc


# CONTACT PHONE POINT CONSENT
def phone_contact_point_consent(cont_point, stage_contact, contact):
    """-----------------------------------------------------------
    Description: Phone Contact Point Consent Mapper
    Argument:  (1)contact identifier object (2)stage contact (3)comtact
    Return: Contact Point Consent object
    -----------------------------------------------------------"""
    ppc = ContactPointConsent()

    mpc.effectivefrom = stage_contact.sms_consent_date__c
    mpc.capturedate = stage_contact.sms_consent_date__c
    mpc.matm_owner__c = cont_point.matm_owner__c
    mpc.privacyconsentstatus = NOT_SEEN
    epc.capturesource = (
        "{}".format(stage_contact.source_name__c)
        + " | "
        + "{}".format(stage_contact.campaign_most_recent__c)
        + " | "
        + "{}".format(stage_contact.form_name__c)
    )[0, 255]
    epc.capturecontactpointtype = PHONE
    epc.name = (
        "{}".format(stage_contact.source_name__c)
        + " | "
        + "{}".format(stage_contact.phone__c)
        + " | "
        + date
    )[0, 255]

    # ID'S
    ppc.contact_point_consent_id_ext__c = get_unique_id()
    ppc.stage_contact_id_ext__c = cont_point.stage_contact_id_ext__c
    ppc.contact_id_ext__c = contact.contact_id_ext__c
    ppc.contact_point_id_ext__c = cont_point.contact_point_phone_id_ext__c

    return ppc
