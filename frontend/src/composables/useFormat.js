export const formatDateTk = (date) => {
  const d = date instanceof Date ? date : new Date(date);
  if (isNaN(d)) return "";

  const weekdays = [
    "ýekşenbe",
    "duşenbe",
    "sişenbe",
    "çarşenbe",
    "penşenbe",
    "anna",
    "şenbe",
  ];

  const months = [
    "ýanwar",
    "fewral",
    "mart",
    "aprel",
    "maý",
    "iýun",
    "iýul",
    "awgust",
    "sentýabr",
    "oktýabr",
    "noýabr",
    "dekabr",
  ];

  const dayName = weekdays[d.getDay()];
  const day = d.getDate();
  const monthName = months[d.getMonth()];
  const year = d.getFullYear();

  return `${dayName}, ${day} ${monthName} ${year}`;
};

export const formatTime = (seconds) => {
  if (!seconds || isNaN(seconds)) return '0:00'

  const min = Math.floor(seconds / 60)
  const sec = Math.floor(seconds % 60)

  return `${min}:${sec.toString().padStart(2, '0')}`
}