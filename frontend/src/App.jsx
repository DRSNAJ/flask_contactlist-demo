import { useEffect, useState } from "react";
import "./App.css";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import loadConfig from "./configLoader";

function App() {
  const [contacts, setContacts] = useState([]);
  const [appConfig, setAppConfig] = useState({});

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentContact, setCurrentContact] = useState({});

  useEffect(() => {
    if (appConfig.CONTACTS_API_URL) {
      fetchContacts();
    }
  }, [appConfig.CONTACTS_API_URL]);

  useEffect(() => {
    loadConfig().then((config) => {
      setAppConfig(config);
      console.log("API URL: ", appConfig.CONTACTS_API_URL);
    });
  }, []);

  const fetchContacts = async () => {
    const response = await fetch(
      ` http://${appConfig.CONTACTS_API_URL}/contacts`
    );

    const data = await response.json();
    setContacts(data.contacts);
    console.log(data.contacts);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentContact({});
  };
  const openCreateModal = () => {
    if (!isModalOpen) {
      setIsModalOpen(true);
    }
  };

  const openEditModal = (contact) => {
    if (isModalOpen) return;
    setCurrentContact(contact);
    setIsModalOpen(true);
  };

  const onUpdate = () => {
    closeModal();
    fetchContacts();
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

export default App;
