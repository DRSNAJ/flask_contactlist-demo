import pytest
from main import app, db
from models import Contact

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.app_context():
        db.create_all()
        
        for i in range(1, 21):
            new_contact = Contact(first_name=f"test_first_name_{i}", last_name=f"test_last_name_{i}", email=f"test_email_{i}", phone=f"T05848_{i}")
            db.session.add(new_contact)
        db.session.commit()
        
    yield app.test_client()
    
    with app.app_context():
        db.drop_all()
        

def test_update_contact(client):
    """
    GIVEN a Contact model
    WHEN a the contact ID is specified
    THEN check that that firstName, lastName, email, and phone can be edited
    """
    
    for i in [1,7,8,11,5]:
        edited_contact = {
        "firstName": f"first_last_name_{i}_E",
        "lastName": f"test_last_name_{i}_E",
        "email": f"email_{i}_E",
        "phone": f"T48_{i}_E"
        }
        response = client.patch(f'/update_contact/{i}', json = edited_contact)
        
        with app.app_context():
            db_edited = db.session.query(Contact).filter_by(id = i).first().to_json()
            edited_contact["id"] = i
            assert edited_contact == db_edited