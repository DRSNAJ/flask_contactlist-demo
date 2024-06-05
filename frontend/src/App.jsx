import { useEffect, useState } from "react";
import "./App.css";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";

function App() {
  const [contacts, setContacts] = useState([]); // State for storing contacts

  const [isModalOpen, setIsModalOpen] = useState(false); // State to control modal visibility
  const [currentContact, setCurrentContact] = useState({}); // State to hold the current contact being edited or created

  useEffect(() => {
    fetchContacts(); // Fetch contacts on component mount
  }, []);

  const fetchContacts = async () => {
    const response = await fetch(`/contacts_api/contacts`); // Make an API call to fetch contacts
    const data = await response.json(); // Parse JSON response
    setContacts(data.contacts); // Update the contacts state with fetched data
    console.log(data.contacts); // Log the fetched contacts for debugging
  };

  const closeModal = () => {
    setIsModalOpen(false); // Close modal
    setCurrentContact({}); // Reset currentContact state to clear the form
  };
  const openCreateModal = () => {
    if (!isModalOpen) {
      setIsModalOpen(true); // Open modal if it's not already open
    }
  };

  const openEditModal = (contact) => {
    if (isModalOpen) return; // If modal is already open, return to prevent multiple modals
    setCurrentContact(contact); // Set the currentContact to the one provided (for editing
    setIsModalOpen(true); // Open the modal for editing
  };

  const onUpdate = () => {
    closeModal(); // Close the modal after update
    fetchContacts(); // Fetch all contacts again to reflect changes in the UI
  };

  return (
    <>
      <ContactList
        contacts={contacts}
        updateContact={openEditModal}
        updateCallback={onUpdate}
      ></ContactList>
      <button onClick={openCreateModal}>Create New Contact</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <ContactForm
              existingContact={currentContact}
              updateCallback={onUpdate}
            ></ContactForm>
          </div>
        </div>
      )}
    </>
  );
}

// Export the App component
export default App;
