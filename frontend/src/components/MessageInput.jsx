import { Send, Smile } from "lucide-react";
import EmojiPicker from "./EmojiPicker";

const MessageInput = ({
  inputMessage,
  setInputMessage,
  sendMessage,
  isLoading,
  handleKeyPress,
  showEmojiPicker,
  setShowEmojiPicker,
  pickerRef,
  handleEmojiSelect,
}) => {
  return (
    <div className="flex items-center px-4 py-2 bg-gray-900 space-x-3 relative">
      
      {/* Input */}
      <div className="flex-1 relative">
        <textarea
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask Medical Chatbot…"
          className="w-full px-4 py-2 pr-12 text-white bg-transparent focus:outline-none resize-none"
          rows={1}
          style={{ minHeight: "40px", maxHeight: "100px" }}
          disabled={isLoading}
        />

        {/* Emoji button */}
        <button
          type="button"
          onClick={() => setShowEmojiPicker(!showEmojiPicker)}
          className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-200 transition-colors duration-200"
          disabled={isLoading}
        >
          <Smile className="w-8 h-8 text-center" />
        </button>

        {/* Emoji picker */}
        {showEmojiPicker && (
          <EmojiPicker
            pickerRef={pickerRef}
            handleEmojiSelect={handleEmojiSelect}
          />
        )}
      </div>

      {/* Send button */}
<button
  onClick={sendMessage}
  disabled={!inputMessage.trim() || isLoading}
  className="w-10 h-10 bg-green-600 hover:bg-green-500 active:bg-green-700 rounded-full 
             flex items-center justify-center shadow-md transition-all duration-200 
             disabled:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed"
>
  <Send className="w-5 h-5 text-white transition-colors duration-500" />
</button>

    </div>
  );
};

export default MessageInput;
