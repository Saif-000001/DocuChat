import { useState } from 'react';
import { API_BASE_URL } from '../config/config';

export function useChat() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      timestamp: new Date()
    }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [inputMessage, setInputMessage] = useState('');

  const sendMessage = async (messageText) => {
    if (!messageText.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      text: messageText,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError('');
    setInputMessage('');

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: messageText }),
      });

      if (!response.ok) throw new Error("Failed to get response");

      const data = await response.json();
      const botMessage = {
        id: Date.now() + 1,
        text: data.answer,
        sender: 'bot',
        timestamp: new Date(),
        sources: data.source_documents
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      setError(err.message);
      setMessages(prev => [...prev, {
        id: Date.now() + 1,
        text: "I'm sorry, I encountered an error processing your request. Please try again.",
        sender: 'bot',
        timestamp: new Date(),
        isError: true
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  // Handle Enter key for sending message
  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage(inputMessage);
    }
  };

  return { 
    messages, 
    setMessages, 
    isLoading, 
    error, 
    inputMessage, 
    setInputMessage, 
    sendMessage, 
    handleKeyPress 
  };
}
