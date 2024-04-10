import pytest
from main import app, db
from models import Contact
import random

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.app_context():
        db.create_all()
        
        for i in range(20):
            new_contact = Contact(first_name=f"test_first_name_{i}", last_name=f"test_last_name_{i}", email=f"test_email_{i}", phone=f"T05848_{i}")
            db.session.add(new_contact)
        db.session.commit()
        
    yield app.test_client()
    
    with app.app_context():
        db.drop_all()
        
def test_delete_contact(client):
    
    """
    GIVEN a Contact model
    WHEN a the contact ID is specified
    THEN check that that contact can be deleted
    """
    
    for i in [1, 10, 5, 7, 8]:
        reponse = client.delete(f'/contacts_api/delete_contact/{i}')
        assert reponse.status_code == 200
    
    with app.app_context():
        remaining_contacts = db.session.query(Contact).count()
        assert remaining_contacts == 15
