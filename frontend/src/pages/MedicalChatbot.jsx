import { AlertCircle, Bot } from 'lucide-react';
import Header from '../components/Header';
import ChatMessage from '../components/ChatMessage';
import MessageInput from '../components/MessageInput';

import { useChat } from '../hooks/useChat';
import { useEmoji } from '../hooks/useEmoji';
import { useScroll } from '../hooks/useScroll';
import { useFormatTime } from '../hooks/useFormatTime';

const MedicalChatbot = () => {
  const { messages, isLoading, error, inputMessage, setInputMessage, sendMessage, handleKeyPress} = useChat();
  const { showEmojiPicker, toggleEmojiPicker, handleEmojiSelect } = useEmoji();
  const messagesEndRef = useScroll(messages);
  const formatTime = useFormatTime();

  return (
    <div className="flex flex-col h-screen relative">
    {/* Background (Radial Grid) */}
    <div className="absolute top-0 left-0 z-[-1] h-full w-full bg-[#000000] bg-[radial-gradient(#ffffff33_1px,#00091d_1px)] bg-[size:20px_20px]" />
    
    <Header />

    {error && (
      <div className="bg-gray-800 border-l-4 border-red-400 p-4 m-4 flex">
        <AlertCircle className="w-5 h-5 text-red-400" />
        <p className="ml-3 text-sm text-red-700">{error}</p>
      </div>
    )}

    <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
      {messages.map((msg) => (
        <ChatMessage key={msg.id} message={msg} formatTime={formatTime} />
      ))}

      {isLoading && (
        <div className="flex items-center space-x-2 text-gray-500">
          <Bot className="w-5 h-5 animate-pulse" />
          <p className="text-sm">Thinking...</p>
        </div>
      )}
      <div ref={messagesEndRef} />
    </div>

    <MessageInput
      inputMessage={inputMessage}
      setInputMessage={setInputMessage}
      sendMessage={() => sendMessage(inputMessage)}
      isLoading={isLoading}
      handleKeyPress={handleKeyPress}
      showEmojiPicker={showEmojiPicker}
      setShowEmojiPicker={toggleEmojiPicker}
      handleEmojiSelect ={handleEmojiSelect}
    />
  </div>
  );
};

export default MedicalChatbot;
