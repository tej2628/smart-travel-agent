from tools import weather_tool, budget_tool, attraction_tool, full_guide_tool
import subprocess

user_input = input("Ask the Travel Agent: ")

decision_prompt = f"""
You are a travel agent.

Available tools:

weather_tool
budget_tool
attraction_tool
full_guide_tool

Rules:

- Weather questions -> weather_tool
- Budget questions -> budget_tool
- Places to visit, restaurants -> attraction_tool
- Complete travel guide -> full_guide_tool

Reply ONLY with the tool name.

User Question:
{user_input}
"""

decision = subprocess.run(
    ["ollama", "run", "llama3.2", decision_prompt],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

tool_name = decision.stdout.strip().lower()

location = user_input

if "weather_tool" in tool_name:
    tool_result = weather_tool(location)

elif "budget_tool" in tool_name:
    tool_result = budget_tool(location)

elif "attraction_tool" in tool_name:
    tool_result = attraction_tool(location)

else:
    tool_result = full_guide_tool(location)


final_prompt = f"""
You are an expert travel guide.

User Question:
{user_input}

Tool Context:
{tool_result}

Answer the user's question naturally.

Give useful information for the location mentioned.

Do not mention the tool name.
"""  

final_response = subprocess.run(
    ["ollama", "run", "llama3.2", final_prompt],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

print("\nTravel Agent:\n")
print(final_response.stdout)
