from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    Text,
    DateTime,
    Date,
    MetaData,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OrganizationSource(Base):
    __tablename__ = "salesforce.organization_source__c"

    id = Column(Integer, primary_key=True)

    authorization_form_email_consent__c = Column(String(18))
    authorization_form_sms_consent__c = Column(String(18))
    client_id__c = Column(String(200), unique=True)
    generic_record_type_id__c = Column(String(200))
    is_active__c = Column(Boolean)
    is_app__c = Column(Boolean)
    is_cat_consent__c = Column(Boolean)
    is_dealer__c = Column(Boolean)
    is_obfuscated__c = Column(Boolean)
    is_salesforce_org__c = Column(Boolean)
    is_separate_contact__c = Column(Boolean)
    source_contact_record_type_id__c = Column(String(200))
    source_name__c = Column(String(200))


class StageContact(Base):
    __tablename__ = "salesforce.stage_contact__c"

    id = Column(Integer, primary_key=True)

    authorization_form_email_consent__c = Column(String(18))
    authorization_form_sms_consent__c = Column(String(18))
    billing_zip_postal_code__c = Column(String(255))
    billingcity__c = Column(String(255))
    billingcountry__c = Column(String(255))
    billingstate_province__c = Column(String(255))
    billingstreet__c = Column(String(255))
    bu_name__c = Column(String(255))
    campaign_most_recent__c = Column(String(255))
    change_email__c = Column(Boolean)
    client_id__c = Column(String(255))
    company_name__c = Column(String(255))
    contact_source_most_recent__c = Column(String(255))
    contact_source_most_recent_details__c = Column(String(255))
    country_code__c = Column(String(255))
    crmi_master_contact_id__c = Column(String(255))
    data_processing__c = Column(String(255))
    dealer_code__c = Column(String(255))
    dealer_customer_number__c = Column(String(255))
    email__c = Column(String(255))
    email_consent_date__c = Column(DateTime)
    email_data_use_purpose__c = Column(String(255))
    email_opt_in_status__c = Column(Boolean)
    error_message__c = Column(String(255))
    first_name__c = Column(String(255))
    form_name__c = Column(String(255))
    generic_record_type_id__c = Column(String(200))
    heroku_cms_processing__c = Column(String(255))
    industry__c = Column(String(255))
    industry_level_2__c = Column(String(255))
    ingestion_point__c = Column(String(255))
    is_active__c = Column(Boolean)
    is_app__c = Column(Boolean)
    is_cat_consent__c = Column(Boolean)
    is_dealer__c = Column(Boolean)
    is_matched_completed = Column(Boolean)
    is_obfuscated__c = Column(Boolean)
    is_salesforce_org__c = Column(Boolean)
    is_separate_contact__c = Column(Boolean)
    job_role__c = Column(String(255))
    language__c = Column(String(255))
    last_name__c = Column(String(255))
    level_of_interest__c = Column(String(255))
    mailing_city__c = Column(String(255))
    mailing_postal_code__c = Column(String(255))
    mailing_street__c = Column(String(255))
    matched__c = Column(Boolean)
    matched_type__c = Column(String(255))
    mobile__c = Column(String(255))
    old_email__c = Column(String(255))
    phone__c = Column(String(255))
    process_id = Column(String(255), unique=True)
    process_status__c = Column(String(255))
    product_of_interest__c = Column(String(255))
    product_of_interest_text__c = Column(String(255))
    purchase_timeframe__c = Column(String(255))
    return_contact_id__c = Column(Boolean)
    send__c = Column(Boolean)
    sms_consent_date__c = Column(DateTime)
    sms_data_use_purpose__c = Column(String(255))
    sms_opt_in_status__c = Column(Boolean)
    source_contact_record_type_id__c = Column(String(200))
    source_id__c = Column(String(255))
    source_name__c = Column(String(200))
    state_code__c = Column(String(255))
    status__c = Column(String(255))

    # ID's
    stage_contact_id_ext__c = Column(String(255))


class Individual(Base):
    __tablename__ = "salesforce.individual"

    id = Column(Integer, primary_key=True)

    firstname = Column(String(40))

    lastname = Column(String(80))

    # ID'S
    individual_id_ext__c = Column(String(255), unique=True, nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class Contact(Base):
    __tablename__ = "salesforce.contact"

    id = Column(Integer, primary_key=True)

    bu_name__c = Column(String(255))
    company_name__c = Column(String(255))
    consent_date__c = Column(DateTime)
    consent_level_summary__c = Column(String(255))
    contact_id_match__c = Column(String(18))
    customer_master_id_match__c = Column(String(255))
    customuniqueid__c = Column(String(255))
    data_processing_role_summary__c = Column(String(255))
    dealer_code__c = Column(String(255))
    eloqua_contact_id__c = Column(String(255))
    email = Column(String(80))
    ent_legacy_id__c = Column(String(40))
    firstname = Column(String(40))
    heroku_cms_processing_source__c = Column(String(255))
    industry__c = Column(String(255))
    industry_level_2__c = Column(String(255))
    isdeleted = Column(Boolean)
    job_role__c = Column(String(255))
    language__c = Column(String(255))
    lastname = Column(String(80))
    mailingcity = Column(String(40))
    mailingcountrycode = Column(String(10))
    mailingpostalcode = Column(String(20))
    mailingstate = Column(String(80))
    mailingstatecode = Column(String(10))
    mailingstreet = Column(String(255))
    matm_owner__c = Column(String(100))
    mobilephone = Column(String(40))
    original_ingestion_point__c = Column(String(255))
    phone = Column(String(40))
    ps_legacy_contact_id__c = Column(String(40))
    recordtypeid = Column(String(18))
    sfid = Column(String(18))
    solar_contact_id__c = Column(String(255))
    status__c = Column(String(255))

    # ID's
    individual_id_ext__c = Column(String(18), nullable=False)
    contact_id_ext__c = Column(String(255), unique=True, nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class ContactSource(Base):
    __tablename__ = "salesforce.contact_source__c"

    id = Column(Integer, primary_key=True)

    account_id_match__c = Column(String(18))
    account_name__c = Column(String(255))
    affiliation_description__c = Column(String(255))
    bounce_description__c = Column(String(255))
    bounce_reason__c = Column(String(255))
    bounce_time__c = Column(DateTime)
    bu_name__c = Column(String(255))
    campaign_most_recent__c = Column(String(255))
    catrecid__c = Column(String(255))
    company_name__c = Column(String(255))
    consent_date__c = Column(DateTime)
    consent_expiration__c = Column(Date)
    consent_level__c = Column(String(255))
    consent_scope__c = Column(String(255))
    consent_usage__c = Column(String(255))
    contact_id__r__herokuid__c = Column(String(255))
    contact_id_match__c = Column(String(18))
    contact_source__c = Column(String(40))
    contact_source_details_most_recent__c = Column(String(255))
    contact_source_most_recent__c = Column(String(255))
    contact_source_reference_date__c = Column(DateTime)
    createddate = Column(DateTime)
    customer_master_id_match__c = Column(String(255))
    cws_id__c = Column(String(255))
    data_processing_role__c = Column(String(255))
    dcn__c = Column(String(255))
    dealer_code__c = Column(String(255))
    dealer_name__c = Column(String(255))
    eloqua_contact_id__c = Column(String(255))
    email__c = Column(String(80))
    email_matching_id__c = Column(String(80))
    erp_id__c = Column(String(255))
    first_name__c = Column(String(255))
    form_name__c = Column(String(255))
    fpd_contact_id__c = Column(String(255))
    herokuid__c = Column(String(255))
    industry__c = Column(String(255))
    industry_level_2__c = Column(String(255))
    industry_master__c = Column(String(255))
    isdeleted = Column(Boolean)
    isoname__c = Column(String(255))
    job_role__c = Column(String(255))
    language__c = Column(String(255))
    last_name__c = Column(String(255))
    mailing_address_line_1__c = Column(String(255))
    mailing_address_line_2__c = Column(String(255))
    mailing_city__c = Column(String(255))
    mailing_country__c = Column(String(255))
    mailing_state_province__c = Column(String(255))
    mailing_zip_postal_code__c = Column(String(255))
    mobile__c = Column(String(40))
    name = Column(String(80))
    original_ingestion_point__c = Column(String(255))
    phone__c = Column(String(40))
    processed_date__c = Column(DateTime)
    processed_details__c = Column(String(255))
    processed_status__c = Column(String(255))
    region__c = Column(String(255))
    sending_language__c = Column(String(255))
    serial_number__c = Column(String(255))
    sfid = Column(String(18))
    source_account_id__c = Column(String(255))
    source_date_created__c = Column(DateTime)
    source_detail__c = Column(String(255))
    source_id__c = Column(String(128))
    source_status__c = Column(String(255))
    source_user_id__c = Column(String(255))
    sourceexternalid__c = Column(String(250))
    status__c = Column(String(255))
    ucid__c = Column(String(255))

    # ID's
    contact_source_id_ext__c = Column(String(255), unique=True, nullable=False)
    contact_id_ext__c = Column(String(18), nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class ContactIdentifier(Base):
    __tablename__ = "salesforce.contact_identifier__c"

    id = Column(Integer, primary_key=True)

    connectionreceivedid = Column(String(18))
    connectionsentid = Column(String(18))
    contact_id__r__herokuid__c = Column(String(255))
    createdbyid = Column(String(18))
    createddate = Column(DateTime)
    expiration_date__c = Column(Date)
    herokuid__c = Column(String(255))
    identifier__c = Column(String(255))
    identifier_group__c = Column(String(255))
    identifier_hashed__c = Column(String(255))
    identifier_type__c = Column(String(255))
    identifierexternalid__c = Column(String(250))
    isdeleted = Column(Boolean)
    last_known_activity__c = Column(DateTime)
    matm_owner__c = Column(String(100))
    name = Column(String(80))
    sfid = Column(String(18))
    status__c = Column(String(255))
    status_description__c = Column(String(255))
    status_reason__c = Column(String(255))
    status_source__c = Column(String(255))
    status_time__c = Column(DateTime)

    # ID's
    contact_id_ext__c = Column(String(18), nullable=False)
    contact_identifier_id_ext__c = Column(String(255), unique=True, nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class ContactSourceIdentifier(Base):
    __tablename__ = "salesforce.contact_source_Identifier__c"

    id = Column(Integer, primary_key=True)

    # ID's
    contact_source_identifier_id_ext__c = Column(
        String(255), unique=True, nullable=False
    )
    contact_source_id_ext__c = Column(String(255), nullable=False)
    contact_id_ext__c = Column(String(18), nullable=False)
    contact_identifier_id_ext__c = Column(String(255), unique=True, nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class ContactPointEmail(Base):
    __tablename__ = "salesforce.contactpointemail"

    id = Column(Integer, primary_key=True)

    activefromdate = Column(Date)
    contact_identifier_for_email__c = Column(String(18))

    contact_record__c = Column(String(18))
    contact_record__r__herokuid__c = Column(String(255))
    createddate = Column(DateTime)
    datausepurpose__c = Column(String(255))
    email_address_hashed__c = Column(String(255))
    email_status_mc__c = Column(String(255))
    emailaddress = Column(String(80))
    herokuid__c = Column(String(255))
    isdeleted = Column(Boolean)
    matm_owner__c = Column(String(100))
    name = Column(String(255))
    parentid = Column(String(18))
    privacy_consent_status__c = Column(String(255))

    # ID's
    contact_point_email_id_ext__c = Column(String(255), unique=True, nullable=False)
    individual_id_ext__c = Column(String(18), nullable=False)
    contact_identifier_id_ext__c = Column(String(255), nullable=False)
    contact_id_ext__c = Column(String(18), nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class ContactPointPhone(Base):
    __tablename__ = "salesforce.contactpointphone"

    id = Column(Integer, primary_key=True)

    activefromdate = Column(Date)
    activetodate = Column(Date)
    contact_identifier_for_phone__c = Column(String(18))
    contact_record__c = Column(String(18))
    contact_record__r__herokuid__c = Column(String(255))
    createddate = Column(DateTime)
    datausepurpose__c = Column(String(255))
    herokuid__c = Column(String(250))
    isbusinessphone = Column(Boolean)
    isdeleted = Column(Boolean)
    issmscapable = Column(Boolean)
    matm_owner__c = Column(String(100))
    name = Column(String(255))
    parentid = Column(String(18))
    phonetype = Column(String(255))
    privacy_consent_status__c = Column(String(255))
    sfid = Column(String(18))
    systemmodstamp = Column(DateTime)
    telephonenumber = Column(String(40))

    # ID's
    contact_point_phone_id_ext__c = Column(String(255), unique=True, nullable=False)
    individual_id_ext__c = Column(String(18), nullable=False)
    contact_identifier_id_ext__c = Column(String(255), nullable=False)
    contact_id_ext__c = Column(String(18), nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


class ContactPointConsent(Base):
    __tablename__ = "salesforce.contactpointconsent"

    id = Column(Integer, primary_key=True)

    capturecontactpointtype = Column(String(255))
    capturedate = Column(DateTime)
    capturesource = Column(String(255))
    contact__c = Column(String(18))
    contact__herokuid__c = Column(String(255))
    contactpointid = Column(String(18))
    createddate = Column(DateTime)
    effectivefrom = Column(DateTime)
    individual__c = Column(String(18))
    individual__herokuid__c = Column(String(240))
    isdeleted = Column(Boolean)
    legacy_consent_level__c = Column(String(255))
    matm_owner__c = Column(String(100))
    name = Column(String(255))
    privacyconsentstatus = Column(String(255))
    sfid = Column(String(18))
    systemmodstamp = Column(DateTime)
    email_data_use_purpose__c = Column(String(255))
    sms_data_use_purpose__c = Column(String(255))

    # ID's
    contact_point_consent_id_ext__c = Column(String(255), unique=True, nullable=False)
    authorization_form_id_ext__c = Column(String(18), nullable=False)
    individual_id_ext__c = Column(String(18), nullable=False)
    capture_contact_point_id_ext__c = Column(String(18), nullable=False)
    data_use_purpose_id_ext__c = Column(String(18), nullable=False)
    stage_contact_id_ext__c = Column(String(255), nullable=False)


engine = create_engine("sqlite:///contact_database", echo=True)

# MAIN
if __name__ == "__main__":

    # Base.metadata.drop_all(bind=engine, tables=[StageContact.__table__])
    # Base.metadata.drop_all(bind=engine, tables=[OrganizationSource.__table__])

    Base.metadata.drop_all(bind=engine, tables=[Individual.__table__])
    Base.metadata.drop_all(bind=engine, tables=[Contact.__table__])
    Base.metadata.drop_all(bind=engine, tables=[ContactIdentifier.__table__])
    Base.metadata.drop_all(bind=engine, tables=[ContactSource.__table__])
    Base.metadata.drop_all(bind=engine, tables=[ContactSourceIdentifier.__table__])
    Base.metadata.drop_all(bind=engine, tables=[ContactPointEmail.__table__])
    Base.metadata.drop_all(bind=engine, tables=[ContactPointPhone.__table__])
    Base.metadata.drop_all(bind=engine, tables=[ContactPointConsent.__table__])

    Base.metadata.create_all(bind=engine)
