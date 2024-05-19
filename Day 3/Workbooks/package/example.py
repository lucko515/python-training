from test_crm_utils import add_lead, update_contact

# Add a lead
print(add_lead("John Doe", "john.doe@example.com"))

# Update a contact
print(update_contact(1, name="Jane Doe", email="jane.doe@example.com"))
