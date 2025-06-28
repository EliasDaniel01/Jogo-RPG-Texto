import tkinter as tk

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Simples - Grande Aventura")
        self.root.configure(bg='#23272f')
        # Título estilizado
        self.title_label = tk.Label(root, text="RPG Simples - Grande Aventura", bg='#23272f', fg='#4f8cff', font=('Arial Black', 22, 'bold'))
        self.title_label.pack(pady=(10, 0))
        self.story = tk.Text(root, height=10, width=60, state='disabled', wrap='word', bg='#1e222a', fg='#f8f8f2', font=('Consolas', 13), bd=0, highlightthickness=0)
        self.story.pack(pady=30, padx=30, expand=True, fill='both')
        self.story.config(height=18, width=80, font=('Consolas', 16), relief='groove', borderwidth=4, highlightbackground='#4f8cff', highlightcolor='#4f8cff', padx=20, pady=20)
        self.button_frame = tk.Frame(root, bg='#23272f')
        self.button_frame.pack(pady=20)
        # Botões maiores e arredondados
        style_btn = {'font': ('Arial', 13, 'bold'), 'bd': 0, 'activebackground': '#357ae8', 'activeforeground': '#fff', 'height': 2, 'width': 18, 'cursor': 'hand2'}
        self.start_button = tk.Button(self.button_frame, text="Iniciar Jogo", command=self.start_game, bg='#4f8cff', fg='white', borderwidth=0, highlightthickness=0)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.choice1_button = tk.Button(self.button_frame, text="Escolha 1", command=lambda: self.make_choice(1), state='disabled', bg='#23272f', fg='#f8f8f2', borderwidth=0, highlightthickness=0)
        self.choice2_button = tk.Button(self.button_frame, text="Escolha 2", command=lambda: self.make_choice(2), state='disabled', bg='#23272f', fg='#f8f8f2', borderwidth=0, highlightthickness=0)
        self.choice1_button.pack(side=tk.LEFT, padx=5)
        self.choice2_button.pack(side=tk.LEFT, padx=5)
        self.fase = 0
        self.fases = self.create_fases()
        self.nome_jogador = "Aventureiro"
        self.nome_entry = tk.Entry(root, bg='#1e222a', fg='#f8f8f2', insertbackground='#f8f8f2', font=('Consolas', 12), bd=1, relief='flat')
        self.nome_label = tk.Label(root, text="Digite seu nome:", bg='#23272f', fg='#f8f8f2', font=('Arial', 11))
        self.nome_label.pack(pady=(30, 5))
        self.nome_entry.pack(pady=5)
        self.confirmar_nome_button = tk.Button(root, text="Confirmar Nome", command=self.confirmar_nome, bg='#4f8cff', fg='white', borderwidth=0, highlightthickness=0)
        self.confirmar_nome_button.pack(pady=10)
        self.start_button.config(state='disabled')
        # Espaçamento extra na área de botões
        self.button_frame.pack_configure(pady=30)
        # Centralizar tudo
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # Efeito hover nos botões
        for btn in [self.start_button, self.choice1_button, self.choice2_button, self.confirmar_nome_button]:
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg='#357ae8'))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg='#4f8cff' if 'Iniciar' in b['text'] or 'Confirmar' in b['text'] else '#23272f'))

    def create_fases(self):
        return {
            1: {
                'texto': "Você acorda em uma floresta misteriosa. Dois caminhos estão à sua frente.",
                'opcoes': ["Caminho da esquerda", "Caminho da direita"],
                'proximas': [2, 3]
            },
            2: {
                'texto': "Você segue pelo caminho da esquerda e encontra um lago brilhante.",
                'opcoes': ["Beber água", "Explorar a floresta"],
                'proximas': [4, 8]
            },
            3: {
                'texto': "Você segue pelo caminho da direita e encontra um dragão adormecido.",
                'opcoes': ["Lutar", "Explorar a trilha ao redor"],
                'proximas': [6, 23]
            },
            4: {
                'texto': "A água estava envenenada! Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            5: {
                'texto': "Você encontra uma vila amigável e descansa em segurança. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            6: {
                'texto': "O dragão é muito forte e você perde a batalha. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            7: {
                'texto': "Você foge rapidamente e volta para o início da floresta.",
                'opcoes': ["Caminho da esquerda", "Caminho da direita"],
                'proximas': [2, 3]
            },
            8: {
                'texto': "Você encontra uma cabana abandonada coberta de musgo.",
                'opcoes': ["Entrar na cabana", "Ignorar e seguir"],
                'proximas': [9, 10]
            },
            9: {
                'texto': "Dentro da cabana, há um diário antigo com páginas rasgadas.",
                'opcoes': ["Ler o diário", "Sair da cabana"],
                'proximas': [11, 10]
            },
            10: {
                'texto': "Você segue pela floresta e encontra um lobo rosnando.",
                'opcoes': ["Acalmar o lobo", "Fugir"],
                'proximas': [12, 7]
            },
            11: {
                'texto': "O diário fala sobre um tesouro perdido na floresta.",
                'opcoes': ["Procurar o tesouro", "Ignorar"],
                'proximas': [13, 10]
            },
            12: {
                'texto': "O lobo aceita sua amizade e se torna seu aliado.",
                'opcoes': ["Seguir com o lobo", "Seguir sozinho"],
                'proximas': [14, 15]
            },
            13: {
                'texto': "Você encontra um baú trancado sob uma árvore.",
                'opcoes': ["Tentar abrir", "Procurar chave"],
                'proximas': [16, 17]
            },
            14: {
                'texto': "O lobo te guia até uma clareira secreta.",
                'opcoes': ["Explorar clareira", "Descansar"],
                'proximas': [18, 19]
            },
            15: {
                'texto': "Você se perde na floresta e precisa recomeçar.",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            16: {
                'texto': "O baú estava protegido por uma armadilha! Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            17: {
                'texto': "Você encontra uma chave dourada pendurada em um galho.",
                'opcoes': ["Voltar ao baú", "Seguir em frente"],
                'proximas': [20, 21]
            },
            18: {
                'texto': "Na clareira, há um portal mágico brilhando.",
                'opcoes': ["Entrar no portal", "Ignorar o portal"],
                'proximas': [22, 19]
            },
            19: {
                'texto': "Você adormece e sonha com aventuras passadas.",
                'opcoes': ["Acordar e seguir", "Dormir mais"],
                'proximas': [1, 0]
            },
            20: {
                'texto': "Você abre o baú e encontra um medalhão mágico. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            21: {
                'texto': "Você segue em frente e encontra uma ponte quebrada. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            22: {
                'texto': "Você atravessa o portal e chega a um reino distante. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            23: {
                'texto': "Um trovão ecoa ao longe, assustando os pássaros.",
                'opcoes': ["Procurar abrigo", "Ignorar e seguir"],
                'proximas': [24, 25]
            },
            24: {
                'texto': "Você encontra uma caverna para se abrigar da chuva.",
                'opcoes': ["Entrar na caverna", "Esperar do lado de fora"],
                'proximas': [26, 27]
            },
            25: {
                'texto': "Você segue pela trilha e encontra um mercador.",
                'opcoes': ["Conversar com o mercador", "Ignorar o mercador"],
                'proximas': [28, 29]
            },
            26: {
                'texto': "Dentro da caverna, há pinturas rupestres misteriosas.",
                'opcoes': ["Explorar mais fundo", "Sair da caverna"],
                'proximas': [30, 31]
            },
            27: {
                'texto': "A tempestade piora e você se molha todo. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            28: {
                'texto': "O mercador oferece uma poção misteriosa.",
                'opcoes': ["Aceitar poção", "Recusar poção"],
                'proximas': [32, 33]
            },
            29: {
                'texto': "Você ignora o mercador e segue viagem, mas sente que perdeu uma oportunidade.",
                'opcoes': ["Voltar", "Continuar"],
                'proximas': [25, 34]
            },
            30: {
                'texto': "Você encontra um esqueleto de aventureiro com uma mochila.",
                'opcoes': ["Vasculhar mochila", "Ignorar e sair"],
                'proximas': [35, 31]
            },
            31: {
                'texto': "Você sai da caverna e a tempestade já passou.",
                'opcoes': ["Seguir viagem", "Descansar um pouco"],
                'proximas': [34, 36]
            },
            32: {
                'texto': "Você bebe a poção e sente energia renovada!",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [37, 34]
            },
            33: {
                'texto': "Você recusa a poção e o mercador vai embora.",
                'opcoes': ["Seguir viagem", "Chamar o mercador de volta"],
                'proximas': [34, 28]
            },
            34: {
                'texto': "Você encontra um grupo de bandidos bloqueando o caminho.",
                'opcoes': ["Negociar", "Lutar"],
                'proximas': [38, 39]
            },
            35: {
                'texto': "Na mochila, há uma chave prateada e uma carta de despedida.",
                'opcoes': ["Ler carta", "Pegar chave e sair"],
                'proximas': [40, 41]
            },
            36: {
                'texto': "Você adormece e sonha com um reino distante.",
                'opcoes': ["Acordar e seguir", "Dormir mais"],
                'proximas': [34, 0]
            },
            37: {
                'texto': "O mercador sorri e te entrega um mapa antigo.",
                'opcoes': ["Estudar mapa", "Guardar mapa"],
                'proximas': [42, 34]
            },
            38: {
                'texto': "Os bandidos aceitam negociar e deixam você passar.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [43, 44]
            },
            39: {
                'texto': "Você luta bravamente, mas é capturado pelos bandidos. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            40: {
                'texto': "A carta fala sobre um portal escondido na floresta.",
                'opcoes': ["Procurar portal", "Ignorar carta"],
                'proximas': [45, 41]
            },
            41: {
                'texto': "Você encontra uma árvore oca com um baú trancado.",
                'opcoes': ["Usar chave prateada", "Tentar forçar o baú"],
                'proximas': [46, 47]
            },
            42: {
                'texto': "O mapa indica um tesouro escondido perto de um rio.",
                'opcoes': ["Ir até o rio", "Ignorar o mapa"],
                'proximas': [48, 34]
            },
            43: {
                'texto': "Você segue viagem e encontra uma ponte de pedra.",
                'opcoes': ["Atravessar ponte", "Descansar antes"],
                'proximas': [49, 50]
            },
            44: {
                'texto': "Você segue viagem e encontra uma clareira iluminada.",
                'opcoes': ["Explorar clareira", "Seguir caminho"],
                'proximas': [51, 52]
            },
            45: {
                'texto': "Você encontra o portal escondido atrás de uma cascata.",
                'opcoes': ["Entrar no portal", "Voltar para a floresta"],
                'proximas': [53, 54]
            },
            46: {
                'texto': "A chave prateada abre o baú, revelando um tesouro! Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            47: {
                'texto': "Você não consegue abrir o baú e desiste.",
                'opcoes': ["Voltar", "Tentar novamente"],
                'proximas': [41, 55]
            },
            48: {
                'texto': "Você chega ao rio e encontra um barco à deriva.",
                'opcoes': ["Usar o barco", "Construir uma jangada"],
                'proximas': [56, 57]
            },
            49: {
                'texto': "A ponte é segura e você a atravessa sem problemas.",
                'opcoes': ["Seguir viagem", "Voltar"],
                'proximas': [58, 34]
            },
            50: {
                'texto': "Você descansa um pouco e retoma suas forças.",
                'opcoes': ["Atravessar ponte", "Descansar mais"],
                'proximas': [49, 59]
            },
            51: {
                'texto': "Na clareira, você encontra um altar antigo.",
                'opcoes': ["Examinar altar", "Fazer uma oferenda"],
                'proximas': [60, 61]
            },
            52: {
                'texto': "Você segue por um caminho estreito e chega a uma caverna.",
                'opcoes': ["Entrar na caverna", "Contornar a caverna"],
                'proximas': [62, 63]
            },
            53: {
                'texto': "Dentro do portal, há um mundo cheio de criaturas mágicas.",
                'opcoes': ["Explorar o mundo mágico", "Voltar para casa"],
                'proximas': [64, 0]
            },
            54: {
                'texto': "Você volta para a floresta e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 65]
            },
            55: {
                'texto': "Você tenta novamente abrir o baú, mas sem sucesso.",
                'opcoes': ["Desistir", "Pedir ajuda ao lobo"],
                'proximas': [41, 66]
            },
            56: {
                'texto': "O barco leva você rio abaixo rapidamente.",
                'opcoes': ["Descer do barco", "Continuar no barco"],
                'proximas': [67, 68]
            },
            57: {
                'texto': "Você constrói uma jangada com troncos e cipós.",
                'opcoes': ["Navegar pelo rio", "Procurar por peixes"],
                'proximas': [69, 70]
            },
            58: {
                'texto': "Você encontra uma estalagem e decide passar a noite.",
                'opcoes': ["Dormir na estalagem", "Continuar viajando"],
                'proximas': [71, 34]
            },
            59: {
                'texto': "Você descansa mais e se sente revigorado.",
                'opcoes': ["Atravessar ponte", "Explorar a área"],
                'proximas': [49, 72]
            },
            60: {
                'texto': "O altar brilha intensamente ao seu toque.",
                'opcoes': ["Fazer um pedido", "Deixar uma oferenda"],
                'proximas': [73, 74]
            },
            61: {
                'texto': "A oferenda é aceita e você recebe uma bênção.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [75, 34]
            },
            62: {
                'texto': "Dentro da caverna, você encontra cristais brilhantes.",
                'opcoes': ["Coletar cristais", "Ignorar cristais"],
                'proximas': [76, 77]
            },
            63: {
                'texto': "Você contorna a caverna e encontra uma passagem secreta.",
                'opcoes': ["Entrar na passagem", "Ignorar a passagem"],
                'proximas': [78, 79]
            },
            64: {
                'texto': "As criaturas mágicas são amigáveis e te recebem bem.",
                'opcoes': ["Ficar no mundo mágico", "Voltar para a floresta"],
                'proximas': [80, 54]
            },
            65: {
                'texto': "Você encontra um lugar seguro e monta acampamento.",
                'opcoes': ["Descansar", "Procurar comida"],
                'proximas': [81, 82]
            },
            66: {
                'texto': "O lobo tenta ajudar, mas o baú continua fechado.",
                'opcoes': ["Desistir", "Tentar abrir com a chave dourada"],
                'proximas': [41, 83]
            },
            67: {
                'texto': "Você desce do barco e explora a margem do rio.",
                'opcoes': ["Procurar por tesouros", "Voltar para o barco"],
                'proximas': [84, 68]
            },
            68: {
                'texto': "Você continua no barco e ele chega a uma cachoeira.",
                'opcoes': ["Descer a cachoeira", "Parar o barco"],
                'proximas': [85, 86]
            },
            69: {
                'texto': "Você navega pelo rio e encontra uma ilha.",
                'opcoes': ["Explorar a ilha", "Continuar navegando"],
                'proximas': [87, 88]
            },
            70: {
                'texto': "Você procura por peixes e encontra um lago cheio deles.",
                'opcoes': ["Pescar", "Ignorar e continuar"],
                'proximas': [89, 90]
            },
            71: {
                'texto': "Na estalagem, você ouve rumores sobre um tesouro.",
                'opcoes': ["Investigar rumores", "Ignorar e descansar"],
                'proximas': [91, 92]
            },
            72: {
                'texto': "Você explora a área e encontra ervas medicinais.",
                'opcoes': ["Coletar ervas", "Ignorar ervas"],
                'proximas': [93, 94]
            },
            73: {
                'texto': "Seu pedido é atendido e você recebe uma missão.",
                'opcoes': ["Aceitar missão", "Recusar missão"],
                'proximas': [95, 96]
            },
            74: {
                'texto': "A oferenda é rejeitada e você se sente mal.",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            75: {
                'texto': "A bênção aumenta suas habilidades temporariamente.",
                'opcoes': ["Aproveitar bênção", "Ignorar bênção"],
                'proximas': [97, 34]
            },
            76: {
                'texto': "Os cristais são valiosos e você decide coletá-los.",
                'opcoes': ["Coletar cristais", "Deixar os cristais"],
                'proximas': [98, 34]
            },
            77: {
                'texto': "Você ignora os cristais e segue em frente.",
                'opcoes': ["Seguir em frente", "Voltar"],
                'proximas': [79, 62]
            },
            78: {
                'texto': "A passagem secreta leva a um tesouro escondido.",
                'opcoes': ["Pegar o tesouro", "Ignorar o tesouro"],
                'proximas': [99, 34]
            },
            79: {
                'texto': "Você ignora a passagem e continua pela caverna.",
                'opcoes': ["Explorar a caverna", "Sair da caverna"],
                'proximas': [62, 31]
            },
            80: {
                'texto': "Você é nomeado herói no mundo mágico.",
                'opcoes': ["Aceitar título", "Recusar título"],
                'proximas': [100, 54]
            },
            81: {
                'texto': "Você descansa e recupera suas energias.",
                'opcoes': ["Continuar viagem", "Explorar arredores"],
                'proximas': [34, 101]
            },
            82: {
                'texto': "Você encontra comida e se alimenta.",
                'opcoes': ["Descansar", "Continuar viagem"],
                'proximas': [34, 102]
            },
            83: {
                'texto': "A chave dourada abre o baú, revelando um artefato mágico.",
                'opcoes': ["Usar artefato", "Guardar artefato"],
                'proximas': [103, 34]
            },
            84: {
                'texto': "Você encontra um colar de pérolas na margem do rio.",
                'opcoes': ["Pegar colar", "Ignorar colar"],
                'proximas': [104, 34]
            },
            85: {
                'texto': "Você desce a cachoeira e cai em uma piscina natural.",
                'opcoes': ["Nadar até a margem", "Ficar na água"],
                'proximas': [105, 106]
            },
            86: {
                'texto': "Você para o barco e observa a cachoeira.",
                'opcoes': ["Descer do barco", "Continuar no barco"],
                'proximas': [107, 68]
            },
            87: {
                'texto': "Na ilha, você encontra um altar semelhante ao da clareira.",
                'opcoes': ["Fazer uma oferenda", "Examinar o altar"],
                'proximas': [108, 109]
            },
            88: {
                'texto': "Você continua navegando e encontra uma cidade flutuante.",
                'opcoes': ["Visitar a cidade", "Continuar navegando"],
                'proximas': [110, 111]
            },
            89: {
                'texto': "Você pesca um peixe gigante!",
                'opcoes': ["Cozinhar o peixe", "Comer cru"],
                'proximas': [112, 113]
            },
            90: {
                'texto': "Você ignora o lago e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 114]
            },
            91: {
                'texto': "Os rumores falam sobre um dragão guardião de um tesouro.",
                'opcoes': ["Investigar dragão", "Ignorar rumores"],
                'proximas': [115, 34]
            },
            92: {
                'texto': "Você descansa na estalagem e recupera suas energias.",
                'opcoes': ["Sair da estalagem", "Ficar mais um dia"],
                'proximas': [34, 116]
            },
            93: {
                'texto': "As ervas medicinais podem ser úteis mais tarde.",
                'opcoes': ["Coletar ervas", "Ignorar ervas"],
                'proximas': [117, 34]
            },
            94: {
                'texto': "Você ignora as ervas e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 118]
            },
            95: {
                'texto': "A missão é encontrar um artefato sagrado.",
                'opcoes': ["Aceitar missão", "Recusar missão"],
                'proximas': [119, 96]
            },
            96: {
                'texto': "Você recusa a missão e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 120]
            },
            97: {
                'texto': "Você se sente mais forte e confiante.",
                'opcoes': ["Aproveitar força", "Ignorar força"],
                'proximas': [121, 34]
            },
            98: {
                'texto': "Os cristais brilham intensamente e te cercam.",
                'opcoes': ["Tentar coletar mais cristais", "Sair da caverna"],
                'proximas': [122, 79]
            },
            99: {
                'texto': "O tesouro é uma caixa cheia de moedas de ouro.",
                'opcoes': ["Pegar as moedas", "Ignorar o tesouro"],
                'proximas': [123, 34]
            },
            100: {
                'texto': "Você se torna o herói do mundo mágico e é celebrado.",
                'opcoes': ["Voltar para a floresta", "Ficar no mundo mágico"],
                'proximas': [54, 124]
            },
            101: {
                'texto': "Você explora os arredores e encontra um caminho oculto.",
                'opcoes': ["Seguir o caminho oculto", "Voltar para o acampamento"],
                'proximas': [125, 34]
            },
            102: {
                'texto': "Você continua sua viagem e encontra um lago.",
                'opcoes': ["Nadar no lago", "Descansar à beira do lago"],
                'proximas': [126, 34]
            },
            103: {
                'texto': "O artefato mágico brilha intensamente em suas mãos.",
                'opcoes': ["Usar artefato", "Guardar artefato"],
                'proximas': [127, 34]
            },
            104: {
                'texto': "O colar de pérolas é mais valioso do que parece.",
                'opcoes': ["Pegar colar", "Ignorar colar"],
                'proximas': [128, 34]
            },
            105: {
                'texto': "Você nada até a margem e se sente renovado.",
                'opcoes': ["Continuar viagem", "Descansar à margem"],
                'proximas': [34, 129]
            },
            106: {
                'texto': "Você fica na água e relaxa.",
                'opcoes': ["Sair da água", "Ficar mais tempo"],
                'proximas': [130, 131]
            },
            107: {
                'texto': "Você desce do barco e explora a área ao redor.",
                'opcoes': ["Procurar por tesouros", "Voltar para o barco"],
                'proximas': [132, 68]
            },
            108: {
                'texto': "A oferenda é aceita e você recebe uma bênção.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [75, 34]
            },
            109: {
                'texto': "Você examina o altar e encontra um compartimento secreto.",
                'opcoes': ["Abrir compartimento", "Ignorar compartimento"],
                'proximas': [133, 34]
            },
            110: {
                'texto': "Na cidade flutuante, você encontra um velho conhecido.",
                'opcoes': ["Cumprimentar o conhecido", "Ignorar e seguir"],
                'proximas': [134, 135]
            },
            111: {
                'texto': "Você continua navegando e encontra uma ilha misteriosa.",
                'opcoes': ["Explorar a ilha", "Continuar navegando"],
                'proximas': [136, 111]
            },
            112: {
                'texto': "Você cozinha o peixe e prepara uma refeição deliciosa.",
                'opcoes': ["Comer a refeição", "Guardar a refeição"],
                'proximas': [137, 34]
            },
            113: {
                'texto': "Você come o peixe cru e passa mal.",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            114: {
                'texto': "Você encontra um lugar seguro e monta acampamento.",
                'opcoes': ["Descansar", "Procurar comida"],
                'proximas': [81, 82]
            },
            115: {
                'texto': "Você investiga os rumores e encontra o dragão.",
                'opcoes': ["Lutar contra o dragão", "Fugir do dragão"],
                'proximas': [138, 139]
            },
            116: {
                'texto': "Você passa mais um dia na estalagem e se recupera.",
                'opcoes': ["Sair da estalagem", "Ficar mais um dia"],
                'proximas': [34, 116]
            },
            117: {
                'texto': "Você coleta as ervas medicinais e as guarda.",
                'opcoes': ["Seguir viagem", "Descansar um pouco"],
                'proximas': [34, 140]
            },
            118: {
                'texto': "Você para para descansar e reflete sobre sua jornada.",
                'opcoes': ["Continuar viagem", "Voltar para a floresta"],
                'proximas': [34, 54]
            },
            119: {
                'texto': "Você aceita a missão e parte em busca do artefato.",
                'opcoes': ["Seguir o caminho", "Perguntar sobre o artefato"],
                'proximas': [141, 142]
            },
            120: {
                'texto': "Você continua sua jornada sem a missão.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 143]
            },
            121: {
                'texto': "Você se sente mais forte e confiante.",
                'opcoes': ["Aproveitar força", "Ignorar força"],
                'proximas': [121, 34]
            },
            122: {
                'texto': "Você tenta coletar mais cristais, mas eles estão protegidos.",
                'opcoes': ["Destruir proteção", "Sair da caverna"],
                'proximas': [144, 79]
            },
            123: {
                'texto': "As moedas de ouro podem ser usadas em sua jornada.",
                'opcoes': ["Pegar moedas", "Ignorar moedas"],
                'proximas': [145, 34]
            },
            124: {
                'texto': "Você é celebrado como herói e recebe recompensas.",
                'opcoes': ["Aceitar recompensas", "Recusar recompensas"],
                'proximas': [146, 54]
            },
            125: {
                'texto': "Você segue o caminho oculto e encontra um santuário.",
                'opcoes': ["Entrar no santuário", "Voltar para o acampamento"],
                'proximas': [147, 34]
            },
            126: {
                'texto': "Você nada no lago e se sente renovado.",
                'opcoes': ["Sair do lago", "Continuar nadando"],
                'proximas': [148, 149]
            },
            127: {
                'texto': "O artefato mágico brilha intensamente e emite uma energia poderosa.",
                'opcoes': ["Usar artefato", "Guardar artefato"],
                'proximas': [150, 34]
            },
            128: {
                'texto': "O colar de pérolas brilha intensamente e parece pulsar com energia.",
                'opcoes': ["Usar colar", "Guardar colar"],
                'proximas': [151, 34]
            },
            129: {
                'texto': "Você descansa à margem do rio e recupera suas energias.",
                'opcoes': ["Continuar viagem", "Pescar"],
                'proximas': [34, 89]
            },
            130: {
                'texto': "Você sai da água e se seca ao sol.",
                'opcoes': ["Continuar viagem", "Descansar mais um pouco"],
                'proximas': [34, 152]
            },
            131: {
                'texto': "Você fica mais tempo na água e se refresca.",
                'opcoes': ["Sair da água", "Ficar mais tempo"],
                'proximas': [130, 153]
            },
            132: {
                'texto': "Você procura por tesouros e encontra uma caixa misteriosa.",
                'opcoes': ["Abrir a caixa", "Guardar a caixa"],
                'proximas': [154, 34]
            },
            133: {
                'texto': "Dentro do compartimento, há um colar mágico.",
                'opcoes': ["Pegar colar", "Ignorar colar"],
                'proximas': [155, 34]
            },
            134: {
                'texto': "Você cumprimenta o conhecido e eles conversam sobre aventuras passadas.",
                'opcoes': ["Pedir informações", "Trocar histórias"],
                'proximas': [156, 157]
            },
            135: {
                'texto': "Você ignora o conhecido e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 158]
            },
            136: {
                'texto': "A ilha misteriosa é cercada por uma névoa estranha.",
                'opcoes': ["Entrar na névoa", "Contornar a ilha"],
                'proximas': [159, 160]
            },
            137: {
                'texto': "Você come a refeição e se sente revigorado.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 161]
            },
            138: {
                'texto': "Você luta bravamente contra o dragão.",
                'opcoes': ["Atacar", "Defender"],
                'proximas': [162, 163]
            },
            139: {
                'texto': "Você foge do dragão e consegue escapar.",
                'opcoes': ["Voltar para a floresta", "Seguir viagem"],
                'proximas': [54, 34]
            },
            140: {
                'texto': "Você encontra um eremita que te ensina habilidades especiais.",
                'opcoes': ["Aprender habilidades", "Ignorar eremita"],
                'proximas': [164, 34]
            },
            141: {
                'texto': "Você segue o caminho e encontra um grupo de aventureiros.",
                'opcoes': ["Juntar-se aos aventureiros", "Seguir sozinho"],
                'proximas': [165, 166]
            },
            142: {
                'texto': "Você pergunta sobre o artefato e recebe informações úteis.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [34, 167]
            },
            143: {
                'texto': "Você encontra um lugar seguro e monta acampamento.",
                'opcoes': ["Descansar", "Procurar comida"],
                'proximas': [81, 82]
            },
            144: {
                'texto': "Você destrói a proteção dos cristais e os coleta.",
                'opcoes': ["Seguir viagem", "Descansar um pouco"],
                'proximas': [34, 168]
            },
            145: {
                'texto': "Você pega as moedas e as guarda com cuidado.",
                'opcoes': ["Seguir viagem", "Contar as moedas"],
                'proximas': [34, 169]
            },
            146: {
                'texto': "Você aceita as recompensas e se despede do povo mágico.",
                'opcoes': ["Voltar para a floresta", "Explorar o mundo mágico"],
                'proximas': [54, 170]
            },
            147: {
                'texto': "Você entra no santuário e encontra um altar sagrado.",
                'opcoes': ["Fazer uma oferenda", "Examinar o altar"],
                'proximas': [171, 172]
            },
            148: {
                'texto': "Você nada até a margem e se sente renovado.",
                'opcoes': ["Continuar viagem", "Descansar à margem"],
                'proximas': [34, 173]
            },
            149: {
                'texto': "Você continua nadando e explora o fundo do lago.",
                'opcoes': ["Procurar tesouros", "Voltar para a superfície"],
                'proximas': [174, 175]
            },
            150: {
                'texto': "Você usa o artefato e sente um poder imenso.",
                'opcoes': ["Controlar o poder", "Desfazer o uso do artefato"],
                'proximas': [176, 177]
            },
            151: {
                'texto': "Você usa o colar e se sente protegido contra perigos.",
                'opcoes': ["Aproveitar proteção", "Remover colar"],
                'proximas': [178, 179]
            },
            152: {
                'texto': "Você descansa mais um pouco e se sente revigorado.",
                'opcoes': ["Continuar viagem", "Descansar mais um pouco"],
                'proximas': [34, 180]
            },
            153: {
                'texto': "Você fica mais tempo na água e explora o lago.",
                'opcoes': ["Sair da água", "Ficar mais tempo"],
                'proximas': [130, 181]
            },
            154: {
                'texto': "Você abre a caixa e encontra um mapa do tesouro.",
                'opcoes': ["Seguir o mapa", "Guardar o mapa"],
                'proximas': [182, 34]
            },
            155: {
                'texto': "Você pega o colar mágico e o coloca.",
                'opcoes': ["Sentir o poder do colar", "Remover o colar"],
                'proximas': [183, 34]
            },
            156: {
                'texto': "Você pede informações sobre o tesouro e recebe dicas valiosas.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [34, 184]
            },
            157: {
                'texto': "Você troca histórias de aventuras com o conhecido.",
                'opcoes': ["Pedir informações", "Despedir-se do conhecido"],
                'proximas': [185, 34]
            },
            158: {
                'texto': "Você segue viagem e encontra uma estrada desconhecida.",
                'opcoes': ["Seguir pela estrada", "Voltar para a floresta"],
                'proximas': [186, 54]
            },
            159: {
                'texto': "Você entra na névoa e se perde temporariamente.",
                'opcoes': ["Tentar sair da névoa", "Esperar a névoa dissipar"],
                'proximas': [187, 188]
            },
            160: {
                'texto': "Você contorna a ilha e encontra um barco ancorado.",
                'opcoes': ["Usar o barco", "Explorar a ilha"],
                'proximas': [189, 190]
            },
            161: {
                'texto': "Você continua sua viagem e encontra um vilarejo.",
                'opcoes': ["Visitar o vilarejo", "Ignorar o vilarejo"],
                'proximas': [191, 34]
            },
            162: {
                'texto': "Você ataca o dragão com todas as suas forças.",
                'opcoes': ["Continuar atacando", "Recuar"],
                'proximas': [192, 193]
            },
            163: {
                'texto': "Você defende os ataques do dragão e procura uma abertura.",
                'opcoes': ["Atacar agora", "Continuar defendendo"],
                'proximas': [194, 195]
            },
            164: {
                'texto': "Você aprende a habilidade de cura com o eremita.",
                'opcoes': ["Usar habilidade de cura", "Guardar habilidade de cura"],
                'proximas': [196, 34]
            },
            165: {
                'texto': "Você se junta aos aventureiros e forma um grupo forte.",
                'opcoes': ["Planejar a próxima aventura", "Explorar a área"],
                'proximas': [197, 198]
            },
            166: {
                'texto': "Você decide seguir sozinho e confia em suas habilidades.",
                'opcoes': ["Continuar a jornada", "Parar para descansar"],
                'proximas': [34, 199]
            },
            167: {
                'texto': "Você segue viagem e encontra um viajante solitário.",
                'opcoes': ["Conversar com o viajante", "Ignorar o viajante"],
                'proximas': [200, 34]
            },
            168: {
                'texto': "Você segue viagem e encontra uma cidade escondida.",
                'opcoes': ["Visitar a cidade", "Continuar viajando"],
                'proximas': [201, 202]
            },
            169: {
                'texto': "Você conta suas moedas e percebe que tem uma fortuna.",
                'opcoes': ["Guardar as moedas", "Gastar algumas moedas"],
                'proximas': [203, 34]
            },
            170: {
                'texto': "Você explora o mundo mágico e descobre novos lugares.",
                'opcoes': ["Visitar o castelo", "Explorar a floresta mágica"],
                'proximas': [204, 205]
            },
            171: {
                'texto': "Você faz uma oferenda no altar sagrado.",
                'opcoes': ["Pedir proteção", "Agradecer pela jornada"],
                'proximas': [206, 34]
            },
            172: {
                'texto': "Você examina o altar e encontra um diário antigo.",
                'opcoes': ["Ler o diário", "Guardar o diário"],
                'proximas': [207, 34]
            },
            173: {
                'texto': "Você descansa à margem do rio e reflete sobre sua jornada.",
                'opcoes': ["Continuar viagem", "Voltar para a floresta"],
                'proximas': [34, 54]
            },
            174: {
                'texto': "Você procura tesouros no fundo do lago.",
                'opcoes': ["Procurar por mais tempo", "Voltar para a superfície"],
                'proximas': [208, 175]
            },
            175: {
                'texto': "Você volta para a superfície e respira aliviado.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 209]
            },
            176: {
                'texto': "Você controla o poder do artefato e se torna mais forte.",
                'opcoes': ["Usar poder para o bem", "Usar poder para o mal"],
                'proximas': [210, 211]
            },
            177: {
                'texto': "Você desfaz o uso do artefato e retorna ao normal.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 212]
            },
            178: {
                'texto': "Você aproveita a proteção do colar e se sente seguro.",
                'opcoes': ["Explorar áreas perigosas", "Seguir o caminho normal"],
                'proximas': [213, 34]
            },
            179: {
                'texto': "Você remove o colar e guarda para usar depois.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 214]
            },
            180: {
                'texto': "Você continua sua viagem e encontra um novo desafio.",
                'opcoes': ["Enfrentar o desafio", "Evitar o desafio"],
                'proximas': [215, 34]
            },
            181: {
                'texto': "Você explora o lago e encontra uma caverna subaquática.",
                'opcoes': ["Entrar na caverna", "Ignorar a caverna"],
                'proximas': [216, 217]
            },
            182: {
                'texto': "Você segue o mapa e encontra um tesouro escondido.",
                'opcoes': ["Pegar o tesouro", "Ignorar o tesouro"],
                'proximas': [218, 34]
            },
            183: {
                'texto': "Você sente o poder do colar e se torna mais forte.",
                'opcoes': ["Usar poder para o bem", "Usar poder para o mal"],
                'proximas': [219, 220]
            },
            184: {
                'texto': "Você agradece ao viajante e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 221]
            },
            185: {
                'texto': "Você ouve histórias incríveis do conhecido.",
                'opcoes': ["Pedir mais histórias", "Despedir-se do conhecido"],
                'proximas': [222, 34]
            },
            186: {
                'texto': "Você segue pela estrada desconhecida e encontra um desafio.",
                'opcoes': ["Enfrentar o desafio", "Retornar para a floresta"],
                'proximas': [223, 54]
            },
            187: {
                'texto': "Você tenta sair da névoa e encontra um caminho.",
                'opcoes': ["Seguir o caminho", "Voltar para a névoa"],
                'proximas': [224, 159]
            },
            188: {
                'texto': "Você espera a névoga dissipar e vê um arco-íris.",
                'opcoes': ["Seguir o arco-íris", "Ignorar o arco-íris"],
                'proximas': [225, 34]
            },
            189: {
                'texto': "Você usa o barco e navega em direção à cidade.",
                'opcoes': ["Explorar a cidade", "Continuar navegando"],
                'proximas': [226, 227]
            },
            190: {
                'texto': "Você explora a ilha e encontra um templo antigo.",
                'opcoes': ["Entrar no templo", "Ignorar o templo"],
                'proximas': [228, 229]
            },
            191: {
                'texto': "No vilarejo, você ouve rumores sobre um dragão adormecido.",
                'opcoes': ["Investigar rumores", "Ignorar rumores"],
                'proximas': [230, 34]
            },
            192: {
                'texto': "Você ataca o dragão com todas as suas forças.",
                'opcoes': ["Continuar atacando", "Recuar"],
                'proximas': [162, 163]
            },
            193: {
                'texto': "Você defende os ataques do dragão e procura uma abertura.",
                'opcoes': ["Atacar agora", "Continuar defendendo"],
                'proximas': [194, 195]
            },
            194: {
                'texto': "Você encontra uma abertura e ataca o dragão.",
                'opcoes': ["Continuar atacando", "Recuar"],
                'proximas': [231, 232]
            },
            195: {
                'texto': "Você continua defendendo e espera o momento certo.",
                'opcoes': ["Atacar agora", "Continuar defendendo"],
                'proximas': [233, 234]
            },
            196: {
                'texto': "Você usa a habilidade de cura e se sente revigorado.",
                'opcoes': ["Continuar a jornada", "Descansar um pouco"],
                'proximas': [34, 235]
            },
            197: {
                'texto': "Você planeja a próxima aventura com os aventureiros.",
                'opcoes': ["Seguir o plano", "Mudar de ideia"],
                'proximas': [236, 34]
            },
            198: {
                'texto': "Você explora a área e encontra um baú escondido.",
                'opcoes': ["Abrir o baú", "Ignorar o baú"],
                'proximas': [237, 34]
            },
            199: {
                'texto': "Você segue sozinho e encontra um desafio inesperado.",
                'opcoes': ["Enfrentar o desafio", "Fugir do desafio"],
                'proximas': [238, 239]
            },
            200: {
                'texto': "Você conversa com o viajante e troca informações.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [34, 240]
            },
            201: {
                'texto': "Você visita a cidade escondida e encontra um mercado.",
                'opcoes': ["Comprar suprimentos", "Vender itens"],
                'proximas': [241, 242]
            },
            202: {
                'texto': "Você continua viajando e encontra uma estalagem.",
                'opcoes': ["Dormir na estalagem", "Continuar viajando"],
                'proximas': [34, 243]
            },
            203: {
                'texto': "Você guarda suas moedas com cuidado.",
                'opcoes': ["Continuar viagem", "Contar as moedas"],
                'proximas': [34, 244]
            },
            204: {
                'texto': "Você visita o castelo e conhece o rei.",
                'opcoes': ["Conversar com o rei", "Explorar o castelo"],
                'proximas': [245, 246]
            },
            205: {
                'texto': "Você explora a floresta mágica e encontra criaturas fantásticas.",
                'opcoes': ["Interagir com as criaturas", "Ignorar as criaturas"],
                'proximas': [247, 248]
            },
            206: {
                'texto': "Você pede proteção e recebe uma bênção poderosa.",
                'opcoes': ["Agradecer", "Usar a bênção"],
                'proximas': [249, 34]
            },
            207: {
                'texto': "Você lê o diário e descobre segredos antigos.",
                'opcoes': ["Seguir os segredos", "Ignorar os segredos"],
                'proximas': [250, 34]
            },
            208: {
                'texto': "Você procura tesouros no fundo do lago.",
                'opcoes': ["Procurar por mais tempo", "Voltar para a superfície"],
                'proximas': [208, 175]
            },
            209: {
                'texto': "Você volta para a superfície e respira aliviado.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 209]
            },
            210: {
                'texto': "Você usa o poder do artefato para ajudar os necessitados.",
                'opcoes': ["Continuar ajudando", "Usar poder para si mesmo"],
                'proximas': [251, 34]
            },
            211: {
                'texto': "Você usa o poder do artefato para conquistar o mundo.",
                'opcoes': ["Continuar conquistando", "Desfazer o uso do artefato"],
                'proximas': [252, 177]
            },
            212: {
                'texto': "Você descansa um pouco e recupera suas energias.",
                'opcoes': ["Continuar viagem", "Descansar mais um pouco"],
                'proximas': [34, 153]
            },
            213: {
                'texto': "Você explora áreas perigosas e encontra tesouros.",
                'opcoes': ["Pegar os tesouros", "Ignorar os tesouros"],
                'proximas': [253, 34]
            },
            214: {
                'texto': "Você remove o colar e guarda para usar depois.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 214]
            },
            215: {
                'texto': "Você enfrenta o desafio e se destaca.",
                'opcoes': ["Continuar enfrentando", "Recuperar-se do desafio"],
                'proximas': [254, 34]
            },
            216: {
                'texto': "Você entra na caverna subaquática e encontra um baú.",
                'opcoes': ["Abrir o baú", "Ignorar o baú"],
                'proximas': [255, 34]
            },
            217: {
                'texto': "Você ignora a caverna subaquática e continua nadando.",
                'opcoes': ["Voltar para a superfície", "Explorar o fundo do lago"],
                'proximas': [175, 208]
            },
            218: {
                'texto': "Você pega o tesouro e encontra uma joia rara.",
                'opcoes': ["Usar a joia", "Vender a joia"],
                'proximas': [256, 257]
            },
            219: {
                'texto': "Você usa o poder do colar para ajudar os necessitados.",
                'opcoes': ["Continuar ajudando", "Usar poder para si mesmo"],
                'proximas': [258, 34]
            },
            220: {
                'texto': "Você usa o poder do colar para conquistar o mundo.",
                'opcoes': ["Continuar conquistando", "Remover colar"],
                'proximas': [259, 179]
            },
            221: {
                'texto': "Você segue viagem e encontra um novo desafio.",
                'opcoes': ["Enfrentar o desafio", "Evitar o desafio"],
                'proximas': [215, 34]
            },
            222: {
                'texto': "Você pede mais histórias e aprende sobre o mundo.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [34, 184]
            },
            223: {
                'texto': "Você enfrenta o desafio e se destaca.",
                'opcoes': ["Continuar enfrentando", "Recuperar-se do desafio"],
                'proximas': [254, 34]
            },
            224: {
                'texto': "Você segue o caminho e encontra uma clareira.",
                'opcoes': ["Descansar na clareira", "Continuar pela clareira"],
                'proximas': [34, 260]
            },
            225: {
                'texto': "Você segue o arco-íris e encontra um pote de ouro.",
                'opcoes': ["Pegar o ouro", "Ignorar o ouro"],
                'proximas': [261, 34]
            },
            226: {
                'texto': "Você explora a cidade e encontra um velho amigo.",
                'opcoes': ["Cumprimentar o amigo", "Ignorar o amigo"],
                'proximas': [262, 263]
            },
            227: {
                'texto': "Você continua navegando e encontra uma ilha misteriosa.",
                'opcoes': ["Explorar a ilha", "Continuar navegando"],
                'proximas': [136, 111]
            },
            228: {
                'texto': "Você entra no templo e encontra um altar.",
                'opcoes': ["Fazer uma oferenda", "Examinar o altar"],
                'proximas': [264, 265]
            },
            229: {
                'texto': "Você ignora o templo e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 118]
            },
            230: {
                'texto': "Você investiga os rumores e encontra o dragão adormecido.",
                'opcoes': ["Atacar o dragão", "Fugir do dragão"],
                'proximas': [266, 267]
            },
            231: {
                'texto': "Você ataca o dragão com todas as suas forças.",
                'opcoes': ["Continuar atacando", "Recuar"],
                'proximas': [162, 163]
            },
            232: {
                'texto': "Você defende os ataques do dragão e procura uma abertura.",
                'opcoes': ["Atacar agora", "Continuar defendendo"],
                'proximas': [194, 195]
            },
            233: {
                'texto': "Você encontra uma abertura e ataca o dragão.",
                'opcoes': ["Continuar atacando", "Recuar"],
                'proximas': [231, 232]
            },
            234: {
                'texto': "Você continua defendendo e espera o momento certo.",
                'opcoes': ["Atacar agora", "Continuar defendendo"],
                'proximas': [233, 234]
            },
            235: {
                'texto': "Você usa a habilidade de cura e se sente revigorado.",
                'opcoes': ["Continuar a jornada", "Descansar um pouco"],
                'proximas': [34, 235]
            },
            236: {
                'texto': "Você planeja a próxima aventura com os aventureiros.",
                'opcoes': ["Seguir o plano", "Mudar de ideia"],
                'proximas': [197, 34]
            },
            237: {
                'texto': "Você abre o baú e encontra um mapa do tesouro.",
                'opcoes': ["Seguir o mapa", "Guardar o mapa"],
                'proximas': [182, 34]
            },
            238: {
                'texto': "Você enfrenta o desafio e se destaca.",
                'opcoes': ["Continuar enfrentando", "Recuperar-se do desafio"],
                'proximas': [254, 34]
            },
            239: {
                'texto': "Você foge do desafio e consegue escapar.",
                'opcoes': ["Voltar para a floresta", "Seguir viagem"],
                'proximas': [54, 34]
            },
            240: {
                'texto': "Você conversa com o viajante e troca informações.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [34, 240]
            },
            241: {
                'texto': "Você compra suprimentos e se prepara para a jornada.",
                'opcoes': ["Usar os suprimentos", "Guardar os suprimentos"],
                'proximas': [34, 268]
            },
            242: {
                'texto': "Você vende itens que não precisa mais.",
                'opcoes': ["Usar o dinheiro", "Guardar o dinheiro"],
                'proximas': [34, 269]
            },
            243: {
                'texto': "Você descansa na estalagem e recupera suas energias.",
                'opcoes': ["Sair da estalagem", "Ficar mais um dia"],
                'proximas': [34, 116]
            },
            244: {
                'texto': "Você conta suas moedas e percebe que tem uma fortuna.",
                'opcoes': ["Guardar as moedas", "Gastar algumas moedas"],
                'proximas': [34, 270]
            },
            245: {
                'texto': "Você conversa com o rei e recebe uma missão.",
                'opcoes': ["Aceitar a missão", "Recusar a missão"],
                'proximas': [271, 34]
            },
            246: {
                'texto': "Você explora o castelo e encontra um laboratório.",
                'opcoes': ["Examinar o laboratório", "Sair do castelo"],
                'proximas': [272, 34]
            },
            247: {
                'texto': "Você interage com as criaturas e aprende sobre o mundo mágico.",
                'opcoes': ["Agradecer", "Seguir viagem"],
                'proximas': [34, 184]
            },
            248: {
                'texto': "Você ignora as criaturas e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 118]
            },
            249: {
                'texto': "Você agradece pela bênção e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 54]
            },
            250: {
                'texto': "Você segue os segredos e encontra um tesouro escondido.",
                'opcoes': ["Pegar o tesouro", "Ignorar o tesouro"],
                'proximas': [218, 34]
            },
            251: {
                'texto': "Você ajuda os necessitados e ganha aliados.",
                'opcoes': ["Continuar ajudando", "Usar poder para si mesmo"],
                'proximas': [273, 34]
            },
            252: {
                'texto': "Você conquista o mundo e se torna um governante poderoso.",
                'opcoes': ["Continuar governando", "Desfazer o uso do artefato"],
                'proximas': [274, 177]
            },
            253: {
                'texto': "Você encontra tesouros e se torna rico.",
                'opcoes': ["Usar a riqueza para ajudar", "Guardar a riqueza"],
                'proximas': [275, 34]
            },
            254: {
                'texto': "Você se destaca e ganha fama como aventureiro.",
                'opcoes': ["Aproveitar a fama", "Ignorar a fama"],
                'proximas': [276, 34]
            },
            255: {
                'texto': "Você encontra um artefato poderoso dentro do baú.",
                'opcoes': ["Usar o artefato", "Guardar o artefato"],
                'proximas': [277, 34]
            },
            256: {
                'texto': "A joia rara brilha intensamente e parece pulsar com energia.",
                'opcoes': ["Usar a joia", "Vender a joia"],
                'proximas': [278, 34]
            },
            257: {
                'texto': "Você vende a joia e ganha muito dinheiro.",
                'opcoes': ["Usar o dinheiro", "Guardar o dinheiro"],
                'proximas': [34, 279]
            },
            258: {
                'texto': "Você ajuda os necessitados e ganha aliados.",
                'opcoes': ["Continuar ajudando", "Usar poder para si mesmo"],
                'proximas': [273, 34]
            },
            259: {
                'texto': "Você conquista o mundo e se torna um governante poderoso.",
                'opcoes': ["Continuar governando", "Remover colar"],
                'proximas': [274, 179]
            },
            260: {
                'texto': "Você descansa na clareira e recupera suas energias.",
                'opcoes': ["Continuar viagem", "Descansar mais um pouco"],
                'proximas': [34, 260]
            },
            261: {
                'texto': "Você pega o ouro e se torna rico.",
                'opcoes': ["Usar a riqueza para ajudar", "Guardar a riqueza"],
                'proximas': [275, 34]
            },
            262: {
                'texto': "Você cumprimenta o amigo e eles conversam sobre aventuras passadas.",
                'opcoes': ["Pedir informações", "Trocar histórias"],
                'proximas': [156, 157]
            },
            263: {
                'texto': "Você ignora o amigo e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 158]
            },
            264: {
                'texto': "Você faz uma oferenda no altar e recebe uma bênção.",
                'opcoes': ["Agradecer", "Usar a bênção"],
                'proximas': [249, 34]
            },
            265: {
                'texto': "Você examina o laboratório e encontra poções mágicas.",
                'opcoes': ["Usar uma poção", "Guardar as poções"],
                'proximas': [280, 34]
            },
            266: {
                'texto': "Você ataca o dragão e causa dano.",
                'opcoes': ["Continuar atacando", "Recuar"],
                'proximas': [231, 232]
            },
            267: {
                'texto': "Você foge do dragão e consegue escapar.",
                'opcoes': ["Voltar para a floresta", "Seguir viagem"],
                'proximas': [54, 34]
            },
            268: {
                'texto': "Você usa os suprimentos e se sente revigorado.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 161]
            },
            269: {
                'texto': "Você guarda o dinheiro e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 118]
            },
            270: {
                'texto': "Você guarda suas moedas com cuidado.",
                'opcoes': ["Continuar viagem", "Contar as moedas"],
                'proximas': [34, 244]
            },
            271: {
                'texto': "Você aceita a missão e parte em busca do dragão.",
                'opcoes': ["Seguir o caminho", "Pedir mais informações"],
                'proximas': [281, 282]
            },
            272: {
                'texto': "Você examina o laboratório e encontra um livro de feitiços.",
                'opcoes': ["Ler o livro", "Guardar o livro"],
                'proximas': [283, 34]
            },
            273: {
                'texto': "Você ajuda os necessitados e ganha aliados.",
                'opcoes': ["Continuar ajudando", "Usar poder para si mesmo"],
                'proximas': [273, 34]
            },
            274: {
                'texto': "Você continua governando e se torna um líder sábio.",
                'opcoes': ["Ajudar o povo", "Expandir o reino"],
                'proximas': [284, 285]
            },
            275: {
                'texto': "Você usa a riqueza para ajudar os necessitados.",
                'opcoes': ["Continuar ajudando", "Guardar a riqueza"],
                'proximas': [273, 34]
            },
            276: {
                'texto': "Você aproveita a fama e se torna um ícone.",
                'opcoes': ["Usar a fama para o bem", "Usar a fama para o mal"],
                'proximas': [286, 287]
            },
            277: {
                'texto': "Você usa o artefato e se torna um ser poderoso.",
                'opcoes': ["Controlar o poder", "Desfazer o uso do artefato"],
                'proximas': [288, 177]
            },
            278: {
                'texto': "Você usa a joia e se torna mais forte.",
                'opcoes': ["Aproveitar a força", "Ignorar a força"],
                'proximas': [121, 34]
            },
            279: {
                'texto': "Você guarda o dinheiro e continua sua jornada.",
                'opcoes': ["Seguir o caminho", "Parar para descansar"],
                'proximas': [34, 244]
            },
            280: {
                'texto': "Você usa uma poção e se sente revigorado.",
                'opcoes': ["Continuar viagem", "Descansar um pouco"],
                'proximas': [34, 161]
            },
            281: {
                'texto': "Você segue o caminho e encontra o covil do dragão.",
                'opcoes': ["Entrar no covil", "Esperar o dragão sair"],
                'proximas': [289, 34]
            },
            282: {
                'texto': "Você pede mais informações e se prepara melhor.",
                'opcoes': ["Seguir o plano", "Desistir da missão"],
                'proximas': [197, 34]
            },
            283: {
                'texto': "Você lê o livro de feitiços e aprende um novo feitiço.",
                'opcoes': ["Usar o feitiço", "Guardar o feitiço"],
                'proximas': [290, 34]
            },
            284: {
                'texto': "Você ajuda o povo e ganha respeito.",
                'opcoes': ["Continuar ajudando", "Expandir o reino"],
                'proximas': [284, 285]
            },
            285: {
                'texto': "Você expande o reino e conquista novas terras.",
                'opcoes': ["Governar as novas terras", "Voltar para o reino original"],
                'proximas': [291, 292]
            },
            286: {
                'texto': "Você usa a fama para o bem e se torna um herói.",
                'opcoes': ["Continuar ajudando", "Desistir da fama"],
                'proximas': [273, 34]
            },
            287: {
                'texto': "Você usa a fama para o mal e se torna um vilão.",
                'opcoes': ["Continuar com o plano", "Desistir do plano"],
                'proximas': [293, 34]
            },
            288: {
                'texto': "Você controla o poder e se torna um governante justo.",
                'opcoes': ["Ajudar o povo", "Expandir o reino"],
                'proximas': [284, 285]
            },
            289: {
                'texto': "Você entra no covil e encontra o dragão adormecido.",
                'opcoes': ["Atacar o dragão", "Fugir do dragão"],
                'proximas': [266, 267]
            },
            290: {
                'texto': "Você usa o feitiço e realiza uma mágica impressionante.",
                'opcoes': ["Continuar usando o feitiço", "Guardar o feitiço"],
                'proximas': [290, 34]
            },
            291: {
                'texto': "Você governa as novas terras e se torna um líder respeitado.",
                'opcoes': ["Ajudar os habitantes", "Explorar as novas terras"],
                'proximas': [294, 295]
            },
            292: {
                'texto': "Você volta para o reino original e é recebido como herói.",
                'opcoes': ["Agradecer pelo retorno", "Ignorar os súditos"],
                'proximas': [34, 296]
            },
            293: {
                'texto': "Você continua com o plano e se torna um vilão temido.",
                'opcoes': ["Expandir o plano", "Desistir do plano"],
                'proximas': [297, 34]
            },
            294: {
                'texto': "Você ajuda os habitantes e ganha aliados poderosos.",
                'opcoes': ["Continuar ajudando", "Usar aliados para conquistar"],
                'proximas': [273, 298]
            },
                       295: {
                'texto': "Você explora as novas terras e descobre segredos antigos.",
                'opcoes': ["Investigar segredos", "Ignorar segredos"],
                'proximas': [299, 34]
            },
            296: {
                'texto': "Você ignora os súditos e segue sozinho sua jornada.",
                'opcoes': ["Refletir sobre suas escolhas", "Continuar sozinho"],
                'proximas': [34, 34]
            },
            297: {
                'texto': "Você expande o plano e se torna uma lenda temida.",
                'opcoes': ["Continuar como vilão", "Buscar redenção"],
                'proximas': [34, 34]
            },
            298: {
                'texto': "Você usa seus aliados para conquistar novas terras.",
                'opcoes': ["Governar as novas terras", "Voltar para o reino original"],
                'proximas': [291, 292]
            },
            299: {
                'texto': "Você investiga os segredos e encontra um artefato lendário. Fim da aventura!",
                'opcoes': ["Recomeçar", "Sair"],
                'proximas': [1, 0]
            },
            0: {
                'texto': "Obrigado por jogar!",
                'opcoes': ["", ""],
                'proximas': [0, 0]
            }
        }

    def start_game(self):
        self.nome_jogador = self.nome_entry.get() or "Aventureiro"
        self.fase = 1
        self.update_story()
        self.enable_buttons()

    def confirmar_nome(self):
        self.nome_jogador = self.nome_entry.get()
        self.nome_label.config(text=f"Bem-vindo, {self.nome_jogador}!")
        self.nome_entry.pack_forget()
        self.confirmar_nome_button.pack_forget()
        self.start_button.config(state='normal')

    def update_story(self):
        self.story.config(state='normal')
        self.story.delete(1.0, tk.END)
        fase_atual = self.fases[self.fase]
        self.story.insert(tk.END, fase_atual['texto'] + "\n\n")
        for i, opcao in enumerate(fase_atual['opcoes'], 1):
            self.story.insert(tk.END, f"{i}. {opcao}\n")
        self.story.config(state='disabled')

    def enable_buttons(self):
        self.choice1_button.config(state='normal')
        self.choice2_button.config(state='normal')

    def disable_buttons(self):
        self.choice1_button.config(state='disabled')
        self.choice2_button.config(state='disabled')

    def make_choice(self, escolha):
        fase_atual = self.fases[self.fase]
        proxima_fase = fase_atual['proximas'][escolha - 1]
        if proxima_fase == 0:
            self.story.config(state='normal')
            self.story.insert(tk.END, "\n\nVocê chegou ao fim da aventura. Obrigado por jogar!")
            self.story.config(state='disabled')
            self.disable_buttons()
        else:
            self.fase = proxima_fase
            self.update_story()
            self.disable_buttons()A
            self.root.after(3000, self.enable_buttons)  # Reabilita botões após 3 segundos

if __name__ == "__main__":
    root = tk.Tk()
    jogo = RPGGame(root)
    root.mainloop()
