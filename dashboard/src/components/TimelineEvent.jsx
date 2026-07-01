import "./TimelineEvent.css";
import { useState } from "react";
import { useParams } from "react-router-dom";

function getEventInfo(eventType) {
    switch (eventType) {
        case "llm_call":
            return {
                icon: "🤖",
                label: "LLM Call",
                color: "#4A90E2"
            };

        case "tool_call":
            return {
                icon: "🛠",
                label: "Tool Call",
                color: "#F39C12"
            };

        case "final_response":
            return {
                icon: "✅",
                label: "Final Response",
                color: "#2ECC71"
            };

        default:
            return {
                icon: "📄",
                label: eventType,
                color: "#888888"
            };
    }
}

function TimelineEvent({ event }) {

    const { session_id } = useParams();

    const [expanded, setExpanded] = useState(false);
    const [eventData, setEventData] = useState(null);
    const [loading, setLoading] = useState(false);

    const eventInfo = getEventInfo(event.event_type);

    function loadEvent() {

        if (eventData) return;

        setLoading(true);

        fetch(`http://127.0.0.1:8000/sessions/${session_id}/event/${event.id}`)
            .then((res) => {
                if (!res.ok) {
                    throw new Error("Failed to fetch event");
                }
                return res.json();
            })
            .then((data) => {
                console.log(data);
                setEventData(data);
            })
            .catch((err) => {
                console.error(err);
            })
            .finally(() => {
                setLoading(false);
            });
    }

    function handleClick() {

        const nextState = !expanded;

        setExpanded(nextState);

        if (nextState && !eventData) {
            loadEvent();
        }
    }

    return (
        <div className="timeline-item">

            <div className="timeline-column">
                <div className="timeline-dot"></div>
                <div className="timeline-connector"></div>
            </div>

            <div
                className="timeline-event"
                onClick={handleClick}
            >

                <h3
                    className="event-title"
                    style={{ color: eventInfo.color }}
                >
                    {eventInfo.icon} {eventInfo.label}
                </h3>

                <p className="event-time">
                    {new Date(event.timestamp).toLocaleTimeString()}
                </p>

                {expanded && (

                    <div className="event-details">

                        <hr />

                        {loading ? (

                            <p>Loading...</p>

                        ) : eventData ? (

                            <>

                                <p>
                                    <strong>Event Type:</strong>{" "}
                                    {eventData.event_type}
                                </p>

                                <p>
                                    <strong>Payload</strong>
                                </p>

                                <pre>
                                    {JSON.stringify(eventData.payload ?? {}, null, 2)}
                                </pre>

                                <p>
                                    <strong>Response</strong>
                                </p>

                                <pre>
                                    {JSON.stringify(eventData.response ?? {}, null, 2)}
                                </pre>

                                <p>
                                    <strong>Token Usage:</strong>{" "}
                                    {eventData.token_usage ?? "N/A"}
                                </p>

                                <p>
                                    <strong>Duration:</strong>{" "}
                                    {eventData.duration_ms ?? "N/A"} ms
                                </p>

                                <p>
                                    <strong>Timestamp:</strong>{" "}
                                    {eventData.timestamp
                                        ? new Date(eventData.timestamp).toLocaleString()
                                        : "N/A"}
                                </p>

                            </>

                        ) : (

                            <p>Unable to load event.</p>

                        )}

                    </div>

                )}

            </div>

        </div>
    );
}

export default TimelineEvent;