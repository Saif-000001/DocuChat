import img from "../assets/img.png"
/**
 * ChatMessage Component (WhatsApp style UI)
 * -----------------------------------------
 * - Renders a single chat message in a conversation
 * - Distinguishes between:
 *    • User messages → green bubbles (right aligned)
 *    • Bot messages → gray bubbles (left aligned, with avatar)
 *    • Error messages → red-tinted bubble
 * - Displays timestamp inside the bubble (bottom-right corner)
 * - Optionally shows a "Sources" section if provided in the message object
 */
const ChatMessage = ({ message, formatTime }) => {
  // Check if the current message is from the user
  const isUser = message.sender === "user";
  // Check if the message represents an error
  const isError = message.isError;
  return (
    // Outer wrapper → aligns message to left (bot) or right (user)
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-2 px-2`}>
      {/* Bot avatar (shown only for bot messages) */}
      {!isUser && (
        <div className="flex-shrink-0 mr-2">
          <div className="w-8 h-8 rounded-full bg-gradient-to-br from-gray-800 to-gray-700 flex items-center justify-center">
            {/* Avatar image → same for normal and error messages */}
            <img 
              src={img}
              alt="Bot" 
              className="w-8 h-8 rounded-full object-cover" 
            />
          </div>
        </div>
      )}
      {/* Chat bubble container */}
      <div
        className={`relative max-w-[70%] px-3 py-2 rounded-lg text-sm leading-relaxed shadow-sm break-words
          ${isUser ? "bg-gradient-to-br from-green-800 to-green-700 text-white rounded-br-none" : ""}
          ${!isUser && !isError ? "bg-gray-800 text-white rounded-bl-none" : ""}
          ${isError ? "bg-gray-800 text-red-800 border border-red-300 rounded-bl-none" : ""}
        `}
      >
        {/* Main message text */}
        <p className="pr-12">{message.text}</p>
        {/* Optional: Sources list (appears only if provided in message) */}
        {message.sources && message.sources.length > 0 && (
          <div className="mt-2 text-xs text-gray-600 border-l-2 border-gray-400 pl-2">
            <p className="font-medium">Sources:</p>
            <ul className="list-disc list-inside">
              {message.sources.map((src, i) => (
                <li key={i} className="truncate">{src}</li>
              ))}
            </ul>
          </div>
        )}
        {/* Timestamp → positioned inside bubble (bottom-right) */}
        <span className="absolute bottom-1 right-2 text-[10px] text-white">
          {formatTime(message.timestamp)}
        </span>
      </div>
    </div>
  );
};
export default ChatMessage;
