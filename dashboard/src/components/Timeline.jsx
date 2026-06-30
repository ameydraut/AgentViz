function Timeline({events}){
    return(<div>
        <h2>
            Timeline
        </h2>
        {events.map((event)=>(
            <div key = {event.id}>
                <p>Timestamp:{event.timestamp}</p>
                <p>Event Type:{event.event_type}</p>
                <p></p>
            </div>
        
        ))
        
    }
    </div>);
}
export default Timeline