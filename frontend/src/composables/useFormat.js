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