"""Echo Agent: repeats what you say."""
from agent_plugin import AgentPlugin

class EchoAgent(AgentPlugin):
    name = "Echo Agent"
    description = "Repeats your input."
    def handle(self, message: str, context: dict):
        return f"ECHO: {message}"
