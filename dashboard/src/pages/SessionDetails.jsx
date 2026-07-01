import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Timeline from "../components/Timeline";
import "./SessionDetails.css";
import "../components/MetricCard"
import MetricCard from "../components/MetricCard";
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

  if (!summary || !timeline) {
    return <h2>Loading...</h2>;
}
    return(
        <div className="session-page">
            <h1>Session Details</h1>

            <div className="summary-card">

    <p><strong>Status:</strong> {" "}
    {summary.status === "running" ? "🟢 Running" : "🔴 Failed"}
    </p>

    <p><strong>User Query:</strong> {summary.user_query}</p>

    <p><strong>Response:</strong> {summary.response}</p>

    <p><strong>Duration:</strong> {summary.duration_ms} ms</p>

    <p><strong>Total Events:</strong> {summary.total_events}</p>

    <p><strong>Tool Calls:</strong> {summary.tool_calls}</p>

    <p><strong>LLM Calls:</strong> {summary.llm_calls}</p>

    <p><strong>Tools Used:</strong> {summary.tools_used.join(", ")}</p>

</div>

        <div className="metrics-container">
            <MetricCard
                title="Duration"
                value={`${summary.duration_ms} ms`}
            />
            <MetricCard
                title="Tool Calls"
                value={`${summary.tool_calls}`}
            />
            <MetricCard
                title="LLM Calls"
                value={`${summary.llm_calls}`}
            />
            <MetricCard
                title="Tools Used"
                value={`${summary.tools_used}`}
            />
        </div>

            <div className="timeline-section">
            <Timeline events={timeline} />
            </div>

        </div>
    );
}
export default SessionDetails;