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
