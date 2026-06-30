import TimelineEvent from "./TimelineEvent";
function Timeline({events}){
    return(<div>
        <h2>
            Timeline
        </h2>
        {events.map((event)=>(
            <TimelineEvent
        key={event.id}
        event={event}/>
        
        ))
        
    }
    </div>);
}
export default Timeline