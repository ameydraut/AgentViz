import { useNavigate } from "react-router-dom";
function SessionCard({ session_id,user_query, status, created_at}) {
  const navigate = useNavigate();
  return (
    <div
    onClick={()=> navigate(`/session/${session_id}`)}
      style={{
        border: "1px solid gray",
        borderRadius: "10px",
        padding: "20px",
        marginBottom: "15px",
        width: "350px",
        cursor: "pointer"
      }}
    >
      <h2>{user_query}</h2>
      <p>Status: {status}</p>
      <p>Created: {created_at}</p>
      <p>session_id:{session_id}</p>
    </div>
  );
}

export default SessionCard;