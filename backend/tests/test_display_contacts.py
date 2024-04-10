import pytest
from main import app, db 
from models import Contact

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for tests
    with app.app_context():
        db.create_all()
        
        new_contact = Contact(first_name="test_first_name", last_name="test_last_name", email="test_email", phone="T05848")
        db.session.add(new_contact)
        db.session.commit()
    
    yield app.test_client()
    
    with app.app_context():
        db.drop_all()
        
        
def test_read_contacts(client):
    """
    GIVEN a Contact model
    WHEN a the contact list is requested
    THEN check that the firstName, lastName, email, and phone are all in the response
    """

    response = client.get('/contacts_api/contacts')
    assert response.status_code == 200
    assert b'{"contacts":[{"email":"test_email","firstName":"test_first_name","id":1,"lastName":"test_last_name","phone":"T05848"}]}\n' in response.data
