from alt import App, Window, Label, Button, TextBox, VBox
import time

# Usuários cadastrados (pode ser um dicionário ou depois um sistema com banco)
USUARIOS = {
    "usuario": "1234",
    "admin": "admin"
}

# Tela principal
class Jogo:
    def __init__(self, janela):
        self.janela = janela
        self.pontos = 0

        self.label = Label(f"Pontos: {self.pontos}")
        self.botao = Button("Clique aqui!", on_click=self.aumentar_pontos)

        layout = VBox([self.label, self.botao])
        janela.content = layout

    def aumentar_pontos(self, _):
        self.pontos += 1
        self.label.text = f"Pontos: {self.pontos}"

# Tela de login
class Login:
    def __init__(self, janela):
        self.janela = janela

        self.usuario_input = TextBox(placeholder="Usuário")
        self.senha_input = TextBox(password=True, placeholder="Senha")
        self.msg = Label("")
        botao_login = Button("Entrar", on_click=self.fazer_login)

        layout = VBox([
            Label("Login do Jogo"),
            self.usuario_input,
            self.senha_input,
            botao_login,
            self.msg
        ])

        janela.content = layout

    def fazer_login(self, _):
        usuario = self.usuario_input.text
        senha = self.senha_input.text

        if USUARIOS.get(usuario) == senha:
            self.msg.text = "Login bem-sucedido!"
            time.sleep(0.5)
            Jogo(self.janela)
        else:
            self.msg.text = "Usuário ou senha inválidos."

# App
app = App()
janela = Window(title="Jogo com Login", width=300, height=200)

Login(janela)

app.run(janela)
