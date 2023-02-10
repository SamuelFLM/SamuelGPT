from page.home_page import Home_page
from Auth.gpt import GPT
import PySimpleGUI as sg
import pyautogui as bot

janela = Home_page()
gpt = GPT()

class Main:
    def __init__(self) -> None:
        self.window = janela.executar()
        
    def executar(self):
        while True:
            event,values = self.window.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                break
            
            tamanho_texto = len(values["pergunta"])
            self.window["tamanho_mensagem"].update(f"{tamanho_texto} caracteres")
                
            if event == "enviar" and bool(values["pergunta"]):
                mensagem = str(values["pergunta"])
                resposta_gpt = gpt.executar(mensagem=mensagem)
                self.window["resposta"].update(resposta_gpt)
                
            if event == "enviar" and (bool(values["pergunta"]) == False):
                bot.confirm(title="Aviso", text="Preencher o campo de mensagem", buttons=["OK"])    
if __name__ == "__main__":
    t = Main()
    t.executar()
        