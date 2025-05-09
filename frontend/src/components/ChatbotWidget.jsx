import React, { useState } from "react";
import ChatWindow from "./ChatWindow";

function ChatbotWidget() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="fixed bottom-4 right-4">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="p-4 bg-blue-500 rounded-full text-white shadow-lg"
      >
        {isOpen ? "Close" : "Chat"}
      </button>
      {isOpen && <ChatWindow />}
    </div>
  );
}

export default ChatbotWidget;
