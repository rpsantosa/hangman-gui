# Hangman GUI Game 🎮

Um jogo da forca interativo com interface gráfica construído em Python e Tkinter.

## 📋 Características

- 🎨 Interface gráfica colorida e intuitiva
- 📊 Sistema de pontuação e estatísticas
- 💾 Salvar e carregar jogos
- 📚 Versão educacional em Jupyter Notebook
- 🏆 Níveis de dificuldade
- 🎯 Feedback visual imediato

## 🗂️ Estrutura do Projeto

```
hangman-gui
├── src
│   ├── __init__.py           # Marca src como pacote Python
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── game
│   │   ├── __init__.py       # Módulos relacionados ao jogo
│   │   ├── engine.py         # Lógica principal do jogo
│   │   └── words.py          # Base de palavras
│   ├── ui
│   │   ├── __init__.py       # Módulos da interface
│   │   ├── app.py            # Janela principal da aplicação
│   │   └── components.py     # Componentes visuais
│   └── services
│       └── state_manager.py  # Gerenciador de estado do jogo
├── notebooks
│   └── hangman_tutorial.ipynb # Tutorial interativo para crianças
├── tests
│   └── test_game.py          # Testes unitários
├── requirements.txt           # Dependências do projeto
├── pyproject.toml            # Configuração do projeto
├── .gitignore                # Arquivos ignorados pelo Git
└── README.md                 # Documentação
```

## 🚀 Instalação

### Opção 1: Usando Conda (Recomendado)

```bash
# Clone o repositório
git clone git@github.com:rpsantosa/hangman-gui.git
cd hangman-gui

# Crie o ambiente virtual
conda create --name jogos python=3.11
conda activate jogos

# Instale as dependências
pip install -r requirements.txt
```

### Opção 2: Usando venv

```bash
# Clone o repositório
git clone git@github.com:rpsantosa/hangman-gui.git
cd hangman-gui

# Crie o ambiente virtual
python3 -m venv jogos
source jogos/bin/activate  # No Windows: jogos\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## 🎮 Como Usar

### Executar a Aplicação GUI

```bash
python -m src.main
```

### Executar o Notebook Educacional

```bash
jupyter notebook notebooks/hangman_tutorial.ipynb
```

Ou abra no VS Code com a extensão Jupyter.

## 🎯 Funcionalidades

- **Jogar**: Adivinhe a palavra letra por letra
- **Salvar Jogo**: Salve seu progresso a qualquer momento
- **Carregar Jogo**: Continue de onde parou
- **Estatísticas**: Veja seu desempenho (vitórias, derrotas, taxa de acerto)
- **Modo Tutorial**: Aprenda programação enquanto joga!

## 🧪 Executar Testes

```bash
pytest tests/
```

## 📚 Para Educadores

O notebook `hangman_tutorial.ipynb` foi desenvolvido especificamente para ensinar Python a crianças através de:

- ✅ Conceitos progressivos (variáveis → funções → classes)
- ✅ Exemplos visuais e interativos
- ✅ Desafios práticos
- ✅ Interface colorida e amigável

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autor

**Ricardo Santosa** - [@rpsantosa](https://github.com/rpsantosa)

## 🙏 Agradecimentos

- Comunidade Python
- Serrano
- Todos os contribuidores

---

⭐ Se este projeto te ajudou, considere dar uma estrela!