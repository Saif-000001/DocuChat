import { emojis } from "../config/config";

const EmojiPicker = ({ pickerRef, handleEmojiSelect }) => {
  return (
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
  );
};

export default EmojiPicker;
