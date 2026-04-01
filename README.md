# MCP + LangGraph AI Agent Demo

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-orange)
![MCP](https://img.shields.io/badge/MCP-MultiServer-lightgrey)

A conversational AI agent built using LangGraph's ReAct architecture, seamlessly integrated with **Model Context Protocol (MCP)** servers. 

This repository demonstrates how to orchestrate multiple external tools and APIs dynamically via MCP within a seamless interactive terminal loop.

## 🌟 Features

- **Multi-Server MCP Setup:** Easily configure and adapt multiple remote or local MCP servers all within a `MultiServerMCPClient`.
- **Preconfigured Tools:**
  - `Context7` - Context and code documentation.
  - `Met Museum` - Access to the rich Met Museum artwork database over standard I/O (stdio).
- **Intelligent ReAct Agent:** Powered by LangGraph and OpenAI, handling multi-step reasoning with access to tools.
- **Persistent Conversation Memory:** Employs an `InMemorySaver` checkpointer so the agent remembers previous steps during the active session.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- [Node.js](https://nodejs.org/) (Required for running `npx` commands in standard I/O for the Met Museum MCP server)
- An active OpenAI API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mukkandi-Sridhar/langgraph-mcp-agent-demo.git
   cd langgraph-mcp-agent-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your environment variables:
   Create a `.env` file or export your OpenAI credentials directly:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

### Usage

Start the interactive agent loop by running the main Python script:

```bash
python main.py
```

You'll be greeted by the agent introducing itself and its capabilities. From there, you can enter `1` to ask questions or interact with the programming documentation and Met Museum archives seamlessly!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/Mukkandi-Sridhar/langgraph-mcp-agent-demo/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.