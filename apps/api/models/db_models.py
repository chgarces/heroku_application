from sqlalchemy import Table, MetaData
from ..utilities.config import Base, engine

# Base = declarative_base()
# engine = create_engine("sqlite:///hcms_db")


class ContactStagingTable(Base):
    __table__ = Table(
        "salesforce.stage_contact__c", MetaData(), autoload=True, autoload_with=engine,
    )
