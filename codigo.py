# Título Hashzap
# Botão de iniciar chat
    # Clicou no botão
        # Aparece um popup / modal
            #Titulo: Bem vindo ao Hashzap
            # campo: Escreva seu nome no chat
            # Botão: Entrar no chat
# Chat
# Embaixo do chat
    # campo: Digite sua mensagem
    # Botão: enviar

# Flet -> Framework do Python
# pip intall flet

import flet as ft

def main(pagina): # Criar a funcção main
    texto = ft.Text("Hashzap")

    chat = ft.Column()
    
    def enviar_mensagem(evento):
        print("Enviar mensagem")


    mensagem = ft. TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):
        popup.open=False # Fechar o popup
        pagina.remove(botao_iniciar) # Tirar o botão iniciar chat
        pagina.remove(texto) # Titar o titulo Hashzap
        pagina.add(chat) # Criar o Chat
        pagina.add(mensagem) # colocar o campo de digitar mensagem
        pagina.add(botao_enviar) # criar o botão de enviar
        pagina.update() # Atualizar Página

    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva o seu nome no chat")
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        # Sempre que editar a página, tem que fazer um update
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main) # Criar o app chamando a função principal
