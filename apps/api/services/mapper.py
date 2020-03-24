from ..models.db_models import ContactStagingTable
from datetime import datetime


def map_staging_contact_data(
    contact: dict, error_message=None, error=False, index=1, status="INSERTED"
):
    """
    Function to map contact-data in request to Contact Staging Table.

    """

    contact_data = ContactStagingTable(
        contact_source_most_recent__c=contact["contact-source-most-recent"],
        mobile__c=contact["mobile"],
        mailing_postal_code__c=contact["mailing-postal-code"],
        language__c=contact["language"],
        last_name__c=contact["last-name"],
        state_code__c=contact["state-code"],
        dealer_customer_number__c=contact["dcn"],
        first_name__c=contact["first-name"],
        sms_consent_date__c=datetime.strptime(
            contact["sms-consent-date"], "%Y-%m-%dT%H:%M:%S"
        ),
        email_consent_date__c=datetime.strptime(
            contact["email-consent-date"], "%Y-%m-%dT%H:%M:%S"
        ),
        bu_name__c=contact["bu-name"],
        email__c=contact["email"],
        country_code__c=contact["country-code"],
        mailing_city__c=contact["mailing-city"],
        data_processing__c=contact["data-processing"],
        mailing_street__c=contact["mailing-street"],
        heroku_cms_processing__c=contact["heroku-cms-processing"],
        form_name__c=contact["form-name"],
        campaign_most_recent__c=contact["campaign-most-recent"],
        dealer_code__c=contact["dealer-code"],
        email_opt_in_status__c=contact["email-opt-in-status"],
        sms_opt_in_status__c=contact["sms-opt-in-status"],
        crmi_master_contact_id__c=contact["crmi-master-contact-id"],
        ingestion_point__c=contact["form-name"],
        contact_source_most_recent_details__c=contact[
            "contact-source-most-recent-details"
        ],
        phone__c=contact["phone"],
        company_name__c=contact["company-name"],
        source_id__c=contact["source-id"],
        change_email__c=contact["change-email"],
        sms_data_use_purpose__c=contact["sms_data_use_purpose"],
        job_role__c=contact["job-role"],
        level_of_interest__c=contact["level-of-interest"],
        purchase_timeframe__c=contact["purchase-timeframe"],
        industry__c=contact["industry"],
        industry_level_2__c=contact["industry-level-2"],
        product_of_interest__c=contact["product-of-interest"],
        product_of_interest_text__c=contact["product-of-interest-text"],
        client_id__c=contact["client-id"],
        return_contact_id__c=contact["return-contact-id"],
        process_status__c="NOT STARTED",
        status__c="NOT STARTED",
    )
    print(contact_data)
    return contact_data
