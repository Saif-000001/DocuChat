import { Send, Smile } from "lucide-react";
import { emojis } from "../config/config";
const MessageInput = ({ inputMessage, setInputMessage, sendMessage, isLoading, handleKeyPress, showEmojiPicker, setShowEmojiPicker, handleEmojiSelect}) => {
  return (
    <div className="flex items-center px-4 py-2 bg-gray-900 space-x-3 relative">
      {/* Input */}
      <div className="flex-1 relative">
        <textarea
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your symptom…"
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
          <div
            ref={pickerRef}
            className="absolute bottom-full right-0 mb-2 w-80 h-48 bg-gray-800 rounded-lg shadow-lg overflow-hidden z-50"
          >
            <div className="p-2 bg-gray-700 text-white font-medium text-sm">
              Select an emoji
            </div>
            <div className="grid grid-cols-8 gap-1 p-3 overflow-y-auto h-40">
              {emojis.map((emoji, i) => (
                <button
                  key={i}
                  onClick={() => handleEmojiSelect(emoji)}
                  className="w-8 h-8 flex items-center justify-center text-lg hover:bg-gray-700 rounded transition-colors duration-150"
                >
                  {emoji}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Send button */}
      <button
        onClick={sendMessage}
        disabled={!inputMessage.trim() || isLoading}
        className="w-8 h-8 bg-blue-500 hover:bg-blue-600 rounded-full flex items-center justify-center transition-colors duration-200 disabled:bg-gray-500 disabled:cursor-not-allowed"
      >
        <Send className="w-4 h-4 text-center text-white" />
      </button>
    </div>
  );
};

export default MessageInput;
