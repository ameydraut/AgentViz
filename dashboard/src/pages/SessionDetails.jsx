import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Timeline from "../components/Timeline";

function SessionDetails(){
    const { session_id } = useParams()
    const [summary , setSummary] = useState(null);
    const [timeline, setTimeline] = useState(null);
    useEffect(()=> {
        fetch(`http://127.0.0.1:8000/sessions/${session_id}/summary`)
        .then(res => res.json())
        .then(data=> setSummary(data));
    }, [session_id])

    useEffect(
        ()=> {
            fetch(`http://127.0.0.1:8000/session/${session_id}/timelinedata`)
            .then(res=>res.json())
            .then(data=>setTimeline(data));
        },[session_id]
    )

    if (!summary) {
    return <h2>Loading...</h2>;
}
    if(!timeline){
        return <h2>Loading....</h2>
    }
    return(
        <div>
            <h1>Session Details</h1>
            <p>Status: {summary.status}</p>
            <p>User Query: {summary.user_query}</p>
            <p>Response: {summary.response}</p>
            <p>Duration in ms: {summary.duration_ms}</p>
            <p>Total Events: {summary.total_events}</p>
            <p>Tool Calls: {summary.tool_calls}</p>
            <p>LLM Calls: {summary.llm_calls}</p>
            <p>Tools Used: {summary.tools_used.join(",")}</p>
            <p>First Event: {summary.first_event}</p>
            <p>Last Event: {summary.last_event}</p>

            <Timeline events={timeline} ></Timeline>

        </div>
    );
}
export default SessionDetails;