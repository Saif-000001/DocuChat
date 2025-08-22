export function useFormatTime() {
  return (date) =>
    date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}
