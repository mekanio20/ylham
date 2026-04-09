export const getAccessToken = () => localStorage.getItem('ylham_access');
export const getRefreshToken = () => localStorage.getItem('ylham_refresh');
export const getUser = () => localStorage.getItem('ylham_user');

export const setAccessToken = (token) => localStorage.setItem('ylham_access', token);
export const setRefreshToken = (token) => localStorage.setItem('ylham_refresh', token);
export const setUser = (data) => localStorage.setItem('ylham_user', JSON.stringify(data));

export const clearTokens = () => {
  localStorage.removeItem('ylham_access');
  localStorage.removeItem('ylham_refresh');
  localStorage.removeItem('ylham_user')
};

export const isTokenExpired = (token) => {
  try {
    if (!token) return true; // No token means expired
    const payload = JSON.parse(atob(token.split('.')[1])); // Decode the JWT payload
    const exp = payload.exp; // Expiration time in seconds (Unix timestamp)
    const now = Math.floor(Date.now() / 1000); // Current time in seconds

    return exp < now; // Returns true if token is expired, false otherwise
  } catch (error) {
    console.error("Invalid token", error);
    return true; // Treat invalid tokens as expired
  }
}