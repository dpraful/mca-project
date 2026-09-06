import { useState, useRef, useEffect } from "react";
import "./App.css";

function App() {

  const [messages, setMessages] = useState([]);

  const [input, setInput] = useState("");

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);


  // Scroll to latest message
  useEffect(() => {

    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages]);


  const sendMessage = async () => {

    const userMessage = input.trim();

    if (!userMessage || loading) {
      return;
    }


    // Add user message
    setMessages(prev => [
      ...prev,
      {
        sender: "user",
        text: userMessage
      }
    ]);

    setInput("");
    setLoading(true);


    try {

      const response = await fetch(
        "http://127.0.0.1:8000/chatbot/",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            message: userMessage
          })
        }
      );


      const data = await response.json();


      if (!response.ok) {
        throw new Error(data.response || "Something went wrong");
      }


      // Add bot response
      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: data.response
        }
      ]);

    }

    catch (error) {

      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: "Sorry, something went wrong. Please try again."
        }
      ]);

      console.error(error);

    }

    finally {

      setLoading(false);

    }

  };


  // Send when Enter is pressed
  const handleKeyDown = (event) => {

    if (event.key === "Enter") {
      sendMessage();
    }

  };


  return (

    <div className="page">

      <div className="chatbot-container">


        {/* Header */}

        <div className="chatbot-header">

          <div className="header-title">

            <div className="bot-icon">
              🤖
            </div>

            <div>

              <h3>AI Chatbot</h3>

              <span>
                Online
              </span>

            </div>

          </div>


          <button
            className="close-button"
            onClick={() => setMessages([])}
          >
            ×
          </button>

        </div>


        {/* Messages */}

        <div className="chatbot-messages">


          {messages.length === 0 && (

            <div className="welcome-message">

              <div className="welcome-icon">
                🤖
              </div>

              <h3>
                Hello!
              </h3>

              <p>
                How can I help you today?
              </p>

            </div>

          )}


          {messages.map((message, index) => (

            <div
              key={index}
              className={`message ${message.sender}`}
            >

              {message.text}

            </div>

          ))}


          {loading && (

            <div className="message bot typing">

              <span></span>
              <span></span>
              <span></span>

            </div>

          )}


          <div ref={messagesEndRef}></div>

        </div>


        {/* Input */}

        <div className="chat-input-container">

          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type a message..."
            disabled={loading}
          />

          <button
            onClick={sendMessage}
            disabled={loading || !input.trim()}
          >

            {loading ? "..." : "Send"}

          </button>

        </div>


      </div>

    </div>

  );

}

export default App;