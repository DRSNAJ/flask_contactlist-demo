import React from "react";

// Define a React functional component 'ContactList' that receives props for managing contacts
const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const onDelete = async (id) => {
    try {
      // Define the DELETE request options
      const options = {
        method: "DELETE",
      };
      const response = await fetch(
        `/contacts_api/delete_contact/${id}`,
        options
      );
      // If the response is successful (status 200), call the update callback
      if (response.status == 200) {
        updateCallback();
      } else {
        // Log error if deletion is not successful
        console.error("Failed to delete");
      }
    } catch (error) {
      // Alert the user if an error occurs in the fetch operation
      alert(error);
    }
  };

  // Render the component
  return (
    <div>
      <h2>Contacts</h2>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id}>
              <td>{contact.firstName}</td>
              <td>{contact.lastName}</td>
              <td>{contact.email}</td>
              <td>{contact.phone}</td>
              <td>
                <button
                  onClick={() => {
                    updateContact(contact); // Call 'updateContact' with the contact object when clicked
                  }}
                >
                  Update
                </button>
                <button
                  onClick={() => {
                    onDelete(contact.id); // Call 'onDelete' with the contact's id when clicked
                  }}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

// Export the 'ContactList' component
export default ContactList;
