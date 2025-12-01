from google.adk.memory import InMemoryMemoryService
# later you could switch to VertexAiMemoryBankService, etc.

def get_memory_service():
    # Shared long-term memory service used by all agents
    return InMemoryMemoryService()