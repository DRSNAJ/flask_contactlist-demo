from flask import request, jsonify      # importing library to send HTTP API requests (GET, POST, PUT/PATCH, DELETE, ...) and json formatter
from config import createApp      # importing our app and db objects created in our config file
from models import Contact      # importing our database model from models files

app, db = createApp()

@app.route("/contacts_api/contacts", methods=["GET"]) # modifier 
def get_contacts():
    """Retrieve all contacts from the database and return them as a JSON list.

    Returns:
        Response: A Flask response object containing the JSON list of contact data.
    """    
    contacts = Contact.query.all()  # Query all contact records from the database
    json_contacts = list(map(lambda x:x.to_json(), contacts))# using a lambda function to map to map all of the contacts into a json object 

    return jsonify({"contacts": json_contacts}) # Return a JSON response with the list of contacts

@app.route("/contacts_api/add_contact", methods=["POST"])
def create_contact():
    """Create a new contact record from JSON data provided in the request.

    Returns:
        Response: A Flask response object with a JSON body indicating success or failure.
    """
    
    # Extract details from JSON request data
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email") 
    phone = request.json.get("phone") 
    
    # Validate mandatory fields
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "Please include a first name, last name, and email"}),
            400
        )

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({str(e)}), 400  # Return error if operation fails
    
    return jsonify({"Message": "User Created!"}), 201  # Return success message with HTTP status code 201


@app.route("/contacts_api/update_contact/<int:cnt_id>", methods=["PATCH"])
def update_contact(cnt_id):
    """This function is used to update existing contacts and then commit them to the db

    Args:
        cnt_id (int): id, the primary key of the contact record to be updated

    Returns:
        json: json object spesifying if the record was successfully updated or not
    """
    contact = Contact.query.get(cnt_id)
    if not contact:
        return (
            jsonify({"Message":"Record not found"}), 404  # Return error if contact is not found
        )
    # Update the contact's attributes if provided in the request
    contact.first_name = request.json.get("firstName",  contact.first_name)
    contact.last_name = request.json.get("lastName",  contact.first_name)
    contact.email = request.json.get("email",  contact.first_name) 
    contact.phone = request.json.get("phone",  contact.first_name) 
    
    db.session.commit()
    return (
        jsonify({"Message":"Record updated"}), 200  # Return success message
        )   
    
@app.route("/contacts_api/delete_contact/<int:cnt_id>", methods=["DELETE"])
def delete_record(cnt_id):
    """Function used to delete contacts in the db based on ID

    Args:
        cnt_id (int): id, the primary key of the contact record to be updated

    Returns:
        _type_: json object spesifying if the record was successfully deleted or not
    """
    contact = Contact.query.get(cnt_id)  # Retrieve the contact by ID
    if not contact:
        return (
            jsonify({"Message":"Record not found"}), 404   # Return error if contact is not found
        )
    
    db.session.delete(contact)  # Remove the contact from the session
    db.session.commit()  # Commit the deletion to the database
    
    return (
        jsonify({"Message":"Record successfully deleted"}), 200  # Return success message
    )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # Create database tables before starting the application
        
    app.run(debug=True, host="0.0.0.0", port=5000)  # Start the application with debugging enabled