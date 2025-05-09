import './App.css';
import ChatWindow from './components/ChatWindow'; // Import your chatbot component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the Chatbot Application</h1>
        <p>Your AI assistant is ready to help you!</p>
      </header>
      <main>
        <ChatWindow /> {/* Include the Chatbot component here */}
      </main>
    </div>
  );
}

export default App;
