import { useState, useRef, useEffect } from "react";

export function useEmoji(onEmojiSelect) {
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);
  const pickerRef = useRef(null);

  const toggleEmojiPicker = () => setShowEmojiPicker(prev => !prev);

  const handleEmojiSelect = (emoji) => {
    if (onEmojiSelect) onEmojiSelect(emoji);
    setShowEmojiPicker(false);
  };

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (pickerRef.current && !pickerRef.current.contains(e.target)) {
        setShowEmojiPicker(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return { showEmojiPicker, toggleEmojiPicker, pickerRef, handleEmojiSelect };
}
