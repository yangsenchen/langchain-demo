from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

def load_prompt(path):
    with open( path, 'r', encoding='utf-8') as f:
        return f.read()
    
    
# Configure the LLM
llm = ChatOpenAI(
    model="glm-4", 
    temperature=0.95, 
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/",
    openai_api_key="xxx"
)

# Define the prompt template
prompt = ChatPromptTemplate.from_template(load_prompt("demo1.prompt"))

# Set up the JSON output parser
output_parser = JsonOutputParser()

# Create the LLMChain
chain =  prompt|llm|JsonOutputParser()

# Define input variables
role = "werewolf"
roles_str = "werewolf,villager"
history = "villager: I think player2 are a werewolf\n"



# Invoke the chain
output = chain.invoke({"role": role, "roles": roles_str, "history": history})


# Print the output
print(output)
