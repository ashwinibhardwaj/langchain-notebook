from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a powerful open-source framework designed to simplify the development of applications powered by large language models (LLMs).
It provides a wide range of modular components such as chains, prompts, memory management, agents, and document loaders that allow developers to 
integrate LLMs with external data sources, APIs, and custom tools. LangChain enables the creation of advanced AI applications, including chatbots,
question-answering systems, recommendation engines, and multi-step reasoning agents. By providing utilities for text splitting, embedding generation, and 
structured output parsing, LangChain helps developers manage complex workflows and large volumes of data efficiently. Its flexible architecture makes it 
easy to experiment, iterate, and scale AI solutions, whether for research, prototyping, or production-grade systems.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)
