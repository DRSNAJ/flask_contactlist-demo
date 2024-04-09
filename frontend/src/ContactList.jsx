import React from "react";
import { useEffect, useState } from "react";
import loadConfig from "./configLoader";

const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const [appConfig, setAppConfig] = useState({});

  useEffect(() => {
    loadConfig().then((config) => {
      setAppConfig(config);
      console.log("API URL: ", appConfig.CONTACTS_API_URL);
    });
  }, []);

  const onDelete = async (id) => {
    try {
      const options = {
        method: "DELETE",
      };
      const response = await fetch(
        `http://${appConfig.CONTACTS_API_URL}//delete_contact/${id}`,
        options
      );
      if (response.status == 200) {
        updateCallback();
      } else {
        console.error("Failed to delete");
      }
    } catch (error) {
      alert(error);
    }
  };

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
                    updateContact(contact);
                    // updateCallback();
                  }}
                >
                  Update
                </button>
                <button
                  onClick={() => {
                    onDelete(contact.id);
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

export default ContactList;
