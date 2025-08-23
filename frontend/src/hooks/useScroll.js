import { useEffect, useRef } from "react";

export const useScroll = (deps) => {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [deps]);

  return messagesEndRef;
};
