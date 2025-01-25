import ollama

#Generate entire response NO BYTE BY BYTE GENERATION
def generate_response(inp):
    resp=ollama.generate(model="victor", prompt=inp)
    return resp["response"]
