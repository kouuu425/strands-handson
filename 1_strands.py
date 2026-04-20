from strands import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent("us.anthropic.claude-sonnet-4-5-20250929-v1:0")
agent("Strandsってどういう意味？")