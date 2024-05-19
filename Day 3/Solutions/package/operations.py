def add_lead(name, email):
    """
    Add a new lead to Salesforce.
    :param name: Lead's name
    :param email: Lead's email
    :return: Confirmation message
    """
    # Here you would have the code to add a lead to Salesforce
    return f"Lead {name} with email {email} added successfully!"

def update_contact(contact_id, name=None, email=None):
    """
    Update an existing contact in Salesforce.
    :param contact_id: Contact ID
    :param name: Updated name (optional)
    :param email: Updated email (optional)
    :return: Confirmation message
    """
    # Here you would have the code to update a contact in Salesforce
    return f"Contact {contact_id} updated successfully!"
