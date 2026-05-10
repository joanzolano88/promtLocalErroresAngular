import json
from groq import Groq

# Configuración de Groq
client = Groq(api_key="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")

def explorar():
    try:
        with open("ErroresBasicosAngular.json",encoding="utf-8") as f:
            nodo = json.load(f)
    except FileExistsError:
        print("Error: No se encontró el archivo 'ErroresBasicosAngular.json'")
        return
    camino = []
    while True:
        camino.append(nodo["valor"])
        hijos = nodo.get("hijos",[])

        if not hijos:
            prompt = f"Explicame que es{nodo['valor']} en el contexto de {camino[0]}."
            print(f"\n[Groq] Generando explicación...")
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role":"system","content": "Eres un experto en algoritmos. Da respuestas claras y breves"},
                        {"role":"user","content": prompt}
                    ],
                    temperature=0.5
                )
                print("\nExplicación")
                print(completion.choices[0].message.content)
            except Exception as e:
                print(f"\nError al conectar con Groq: {e}")
            break
        print(f"Seleccione una Categoria: ")
        for i, h in enumerate(hijos,1):
            print(f"{i}.{h['valor']}")
        
        while True:
            idx = input("\nNúmero > ")
            if idx.isdigit() and 1 <=int(idx) <=len(hijos):
                nodo = hijos[int(idx)-1]
                break
            print ("Opción Invalida")

explorar()
