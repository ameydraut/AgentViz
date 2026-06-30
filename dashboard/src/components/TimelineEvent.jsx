import "./TimelineEvent.css";

function TimelineEvent({ event }) {
    return (
        <div className="timeline-event">
            <h3 className="event-title">
                {event.event_type}
            </h3>

            <p className="event-time">
                {new Date(event.timestamp).toLocaleTimeString()}
            </p>
        </div>
    );
}

export default TimelineEvent;