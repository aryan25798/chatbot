import React, { useState } from "react";
import axios from "axios";

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    // Add user message to the chat
    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setInput("");
    setLoading(true);

    try {
      // Call the backend API
      const response = await axios.post("http://127.0.0.1:8000/chat", {
        query: input,
      });

      // Add bot response to the chat
      setMessages((prev) => [
        ...prev,
        { role: "bot", content: response.data.response || "No response provided." },
      ]);
    } catch (error) {
      console.error("Error fetching response:", error);
      setMessages((prev) => [
        ...prev,
        { role: "bot", content: "Sorry, I couldn't process your request. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div className="w-full max-w-md bg-white shadow-lg rounded-lg p-4 fixed bottom-16 right-4">
      <div className="h-64 overflow-y-auto border-b border-gray-300">
        {messages.map((msg, index) => (
          <div key={index} className="my-2">
            <div
              className={`font-bold ${
                msg.role === "user" ? "text-blue-500" : "text-green-500"
              }`}
            >
              {msg.role === "user" ? "You:" : "Bot:"}
            </div>
            <div className="text-gray-700">{msg.content}</div>
          </div>
        ))}
        {loading && (
          <div className="my-2 text-gray-500 italic">Bot is typing...</div>
        )}
      </div>
      <div className="mt-2 flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          className="flex-1 p-2 border rounded focus:outline-none focus:ring focus:ring-blue-300"
          placeholder="Type your message..."
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          className={`ml-2 bg-blue-500 text-white p-2 rounded ${
            loading ? "opacity-50 cursor-not-allowed" : "hover:bg-blue-600"
          }`}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;
