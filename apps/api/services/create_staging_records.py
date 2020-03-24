from .mapper import map_staging_contact_data
from ..utilities.config import session

# engine = create_engine("sqlite:///hcms_db")


def create_staging_records(request):
    contact_records = request["contact-data"]
    print("=====contact_data====")
    print(contact_records)
    staging_records_list = [
        map_staging_contact_data(record) for i, record in enumerate(contact_records)
    ]
    # staging_records_list = map_staging_contact_data(contact_records)

    print("========staging_records_list=========")
    print(staging_records_list)
    session.add_all(staging_records_list)
    session.commit()
