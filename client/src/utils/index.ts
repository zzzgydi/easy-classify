// Utils

function padStart(num: number): string {
  return num.toString().padStart(2, "0");
}

export function formatTime(time: number): string {
  if (!time || time < 0) return "-";

  const date = new Date(time);
  const year = date.getFullYear();
  const month = padStart(date.getMonth() + 1);
  const day = padStart(date.getDate());
  const hour = padStart(date.getHours());
  const min = padStart(date.getMinutes());
  const sec = padStart(date.getSeconds());

  return `${year}-${month}-${day} ${hour}:${min}:${sec}`;
}
