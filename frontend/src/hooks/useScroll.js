import { useEffect, useRef } from 'react';

export function useScroll(deps) {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [deps]);

  return messagesEndRef;
}
