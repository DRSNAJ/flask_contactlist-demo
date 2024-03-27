from flask import request, jsonify      # importing library to send HTTP API requests (GET, POST, PUT/PATCH, DELETE, ...) and json formatter
from config import app, db      # importing our app and db objects created in our config file
from models import Contact      # importing our database model from models files

@app.route("/contacts", methods=["GET"]) # modifier 
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x:x.to_json(), contacts))# using a lambda function to map to map all of the contacts into a json object 
    # a lambda function is a one line function in python   
    return jsonify({"contacts": json_contacts})

@app.route("/add_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email") 
    phone = request.json.get("phone") 
    
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
        return jsonify({str(e)}), 400
    
    return jsonify({"Message": "User Created!"}), 201


@app.route("/update_contact/<int:cnt_id>", methods=["PATCH"])
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
            jsonify({"Message":"Record not found"}), 404
        )
    
    contact.first_name = request.json.get("firstName",  contact.first_name)
    contact.last_name = request.json.get("lastName",  contact.first_name)
    contact.email = request.json.get("email",  contact.first_name) 
    contact.phone = request.json.get("phone",  contact.first_name) 
    
    db.session.commit()
    return (
        jsonify({"Message":"Record updated"}), 200
        )   
    
@app.route("/delete_contact/<int:cnt_id>", methods=["DELETE"])
def delete_record(cnt_id):
    """Function used to delete contacts in the db based on ID

    Args:
        cnt_id (int): id, the primary key of the contact record to be updated

    Returns:
        _type_: json object spesifying if the record was successfully deleted or not
    """
    contact = Contact.query.get(cnt_id)
    if not contact:
        return (
            jsonify({"Message":"Record not found"}), 404
        )
    
    db.session.delete(contact)
    db.session.commit()
    
    return (
        jsonify({"Message":"Record successfully deleted"}), 200
    )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)