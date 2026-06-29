import SessionCard from "./components/SessionCard";
import { useEffect, useState } from "react";
function App() {
  const [sessions , setSession] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/sessions")
        .then(response => response.json())
        .then(data => {
          console.log(data);
            setSession(data);
        });
}, []);
  return (
    <div>
      <h1>AgentViz Dashboard</h1>
       {sessions.map((session)=>(
        <SessionCard
        key = {session.session_id}
        session_id={session.session_id}
        user_query = {session.user_query}
        status = {session.status}
        created_at={session.created_at}
        >
        </SessionCard>
       ))}
    </div>
  );
}

function MyName(){
  return(<h2>Amey</h2>)
}

export default App;