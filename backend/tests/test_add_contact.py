import pytest
from main import app, db
from models import Contact

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for tests
    with app.app_context():
        db.create_all()
    yield app.test_client()  # This provides a test client for your tests
    with app.app_context():
        db.drop_all()
    
def test_create_contact_success(client):    
    """
    GIVEN a Contact model
    WHEN a new contact is created
    THEN check that the firstName, lastName, email, and phone
    """
    test_contact = {
        "firstName": "test_first_name",
        "lastName": "test_last_name",
        "email": "test_email",
        "phone": "T488545"
    }
    response = client.post("/add_contact", json = test_contact)
    assert response.status_code == 201
    assert b'{"Message":"User Created!"}' in response.data
    
def test_create_contact_LastName_fail(client):    
    """
    GIVEN a Contact model
    WHEN a new contact is created
    THEN check that an error appears when last name not entered
    """
    
    test_contact = {
        "firstName": "test_first_name",
        "lastName": "",
        "email": "test_email",
        "phone": "T488545"
    }
    response = client.post("/add_contact", json = test_contact)
    assert response.status_code == 400
    assert b'{"message":"Please include a first name, last name, and email"}\n' in response.data
    
def test_create_contact_FirstName_fail(client):    
    """
    GIVEN a Contact model
    WHEN a new contact is created
    THEN check that an error appears when last name not entered
    """
    
    test_contact = {
        "firstName": "",
        "lastName": "test_last_name",
        "email": "test_email",
        "phone": "T488545"
    }
    response = client.post("/add_contact", json = test_contact)
    assert response.status_code == 400
    assert b'{"message":"Please include a first name, last name, and email"}\n' in response.data
    
    
def test_create_contact_Email_fail(client):    
    """
    GIVEN a Contact model
    WHEN a new contact is created
    THEN check that an error appears when last name not entered
    """
    
    test_contact = {
        "firstName": "first_last_name",
        "lastName": "test_last_name",
        "email": "",
        "phone": "T488545"
    }
    response = client.post("/add_contact", json = test_contact)
    assert response.status_code == 400
    assert b'{"message":"Please include a first name, last name, and email"}\n' in response.data