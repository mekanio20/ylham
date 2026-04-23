export const createUsername = (email) => {
  let username = email.split("@")[0];
  username = username + Math.floor(Math.random() * 10000);
  return username.length > 30 ? username.slice(0, 30) : username;
};