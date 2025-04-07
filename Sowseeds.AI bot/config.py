"""
Orignal Author: Eric Kella Mwinwule

"""

class Config:
    PAGE_TITLE = "Sowseeds AI Assistant "

    OLLAMA_MODELS = ( 'llama3.2','codellama:7b', 'codellama:13b', ' deepseek-r1', 
                    'llama2:7b', 'llama2:13b', 'mistral', 'mixtral')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic."""
    