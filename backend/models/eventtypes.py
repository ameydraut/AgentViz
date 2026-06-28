from enum import Enum
class EventType(str,Enum):
    LLM_CALL="llm_call",
    TOOL_CALL="tool_call",
    TOOL_RESPONSE="tool_response",
    MEMORY_UPDATE="memory_update",
    FINAL_RESPONSE="final_response",
    ERROR="error"
