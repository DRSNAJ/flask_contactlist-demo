import React from "react";
import { useState } from "react";

// Define a functional component for the contact form with props for existing contact and a callback function
const ContactForm = ({ existingContact = {}, updateCallback }) => {
  // State hooks for managing form fields with default values from an existing contact or empty
  const [firstName, setFirstName] = useState(existingContact.firstName || "");
  const [lastName, setLastName] = useState(existingContact.lastName || "");
  const [email, setEmail] = useState(existingContact.email || "");
  const [phone, setPhone] = useState(existingContact.phone || "");

  // Determine if we are updating an existing contact based on the presence of any properties in existingContact
  const updating = Object.entries(existingContact).length !== 0;

  // Handle form submission
  const onSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission behavior

    // Data object containing all form field values
    const data = {
      firstName,
      lastName,
      email,
      phone,
    };

    // Construct the API URL based on whether updating or adding a new contact
    const url =
      `/contacts_api/` +
      (updating ? `update_contact/${existingContact.id}` : "add_contact");
    const options = {
      method: updating ? "PATCH" : "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };

    // Make the HTTP request and await the response
    const response = await fetch(url, options);
    if (response.status !== 201 && response.status !== 200) {
      const data = await response.json();
      alert(data.message); // Alert the user if there was an error
    } else {
      updateCallback(); // Call the updateCallback if the operation was successful
    }
  };

  // Render the form with inputs for firstName, lastName, email, and phone
  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="firstName">First Name: </label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => {
            setFirstName(e.target.value);
          }}
        ></input>
      </div>
      <div>
        <label htmlFor="lastName">Last Name: </label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => {
            setLastName(e.target.value);
          }}
        ></input>
      </div>
      <div>
        <label htmlFor="email">Email: </label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        ></input>
      </div>
      <div>
        <label htmlFor="phone">Phone: </label>
        <input
          type="text"
          id="phone"
          value={phone}
          onChange={(e) => {
            setPhone(e.target.value);
          }}
        ></input>
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default ContactForm;
