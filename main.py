import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI

async def main():
    """
    Runs a LangGraph ReAct agent connected to MCP servers.

    Available tools:
    - Context7 → programming documentation
    - Met Museum → museum artwork database
    """

    # -----------------------------
    # Configure MCP Servers
    # -----------------------------
    client = MultiServerMCPClient(
        {
            "context7": {
                "url": "https://mcp.context7.com/mcp",
                "transport": "streamable_http",
            },
            "met-museum": {
                "command": "npx",
                "args": ["-y", "metmuseum-mcp"],
                "transport": "stdio",
            },
        }
    )

    # -----------------------------
    # Initialize LLM
    # -----------------------------
    model = ChatOpenAI(
        model="gpt-4o",
        temperature=0
    )

    # -----------------------------
    # Load MCP Tools
    # -----------------------------
    print("Loading MCP tools...")
    tools = await client.get_tools()

    print(f"{len(tools)} tools loaded")

    # -----------------------------
    # Setup Conversation Memory
    # -----------------------------
    checkpointer = InMemorySaver()

    config = {
        "configurable": {
            "thread_id": "conversation_id"
        }
    }

    # -----------------------------
    # Create ReAct Agent
    # -----------------------------
    agent = create_react_agent(
        model=model,
        tools=tools,
        checkpointer=checkpointer
    )

    # -----------------------------
    # Initial Message
    # -----------------------------
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an intelligent AI assistant with access "
                        "to programming documentation and the Met Museum collection."
                    ),
                },
                {
                    "role": "user",
                    "content": "Introduce yourself and explain what tools you can access."
                },
            ]
        },
        config=config,
    )

    print("\nAgent:")
    print(response["messages"][-1].content)

    # -----------------------------
    # Interactive CLI Loop
    # -----------------------------
    while True:

        choice = input(
            """
=============================
Menu
1 - Ask a question
2 - Quit
========

Enter choice: """
        )

        if choice == "1":

            query = input("\nYour question:\n> ")

            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": query
                        }
                    ]
                },
                config=config,
            )

            print("\nAgent:")
            print(response["messages"][-1].content)

        elif choice == "2":

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    asyncio.run(main())
