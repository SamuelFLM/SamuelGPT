import openai

class GPT:
    def __init__(self) -> None:
        self.api_key = openai.api_key = "sua_chave_api"
        self.model = "text-davinci-003"
    
    def executar(self,mensagem):
        completar = openai.Completion.create(
        engine=self.model,
        prompt=mensagem,
        max_tokens=1024,
        temperature=0.5,
        )
        resposta = completar.choices[0].text    
        return resposta


if __name__ == "__main__":
    t = GPT()
    t.executar("")
        