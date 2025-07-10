import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios
      .get(`${import.meta.env.VITE_API_URL}/`)  // Calls backend root endpoint
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error("API error:", error);
      });
  }, []);

  return (
    <div>
      <h1>MazeMind</h1>
      <p>API says: {message}</p>
    </div>
  );
}

export default App;
