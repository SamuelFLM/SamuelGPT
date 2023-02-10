import PySimpleGUI as sg


class Home_page():
    def __init__(self) -> None:
         pass
     
    def executar(self):
            sg.theme_background_color("white")
            cabecalho = [sg.Image(filename="img//cabecalho1.png",background_color="white", pad=(0,(0,0)))]
            digitando = [sg.Image(filename="img//Digitando.....png", background_color="white", visible=False, k="digitando")]
            resposta = [sg.Multiline("",
                s=(60,30),background_color="white",
                sbar_width=0,
                sbar_arrow_color="white" ,
                sbar_background_color="white",
                sbar_frame_color="white",
                sbar_relief=None,
                sbar_trough_color="white",
                sbar_arrow_width=0,
                border_width=0,
                auto_refresh=True,
                disabled=True,
                autoscroll=True,
                font="Inter 10 bold",
                k="resposta"
                )]
            mensagem = [[sg.Input("", focus=True,background_color="white",s=(40,0), pad=(10,(10,0)), text_color="black", font="Inter 10 bold", border_width=0, k="pergunta"), sg.Image(filename="img//paper-airplane-24.png", background_color="white",pad=(0,(10,0)), enable_events=True, k="enviar")],
                        [sg.Image(filename="img//Line 1 (4).png", background_color="white", pad=(20,(0,0)))]]
            rodape = [sg.Text("0 caracteres", background_color="white", font="Inter 10 bold", text_color="#696969", k="tamanho_mensagem")]
            layout = [cabecalho,resposta,digitando,mensagem,rodape]
            window = sg.Window("SamuelGPT", layout=layout, size=(369, 700), margins=(0,0),element_justification='c', icon="") 
            return window

            
if __name__ == "__main__":
    t = Home_page()
    t.executar()
        