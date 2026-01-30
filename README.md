# 🤖 Chatbot Discord com Respostas Inteligentes

Bot Discord desenvolvido em Python com sistema de perguntas frequentes e respostas personalizadas para servidores.

## 📋 Sobre o Projeto

Este é um chatbot completo para Discord que permite interação natural com usuários através de comandos e menções. O bot foi desenvolvido com foco em facilidade de uso e personalização.

## ✨ Funcionalidades

- 💬 Respostas automáticas para perguntas frequentes
- 🎯 Sistema de comandos customizáveis
- 🔔 Responde quando mencionado no servidor
- 📝 Interface amigável com embeds formatados
- 🛡️ Sistema de permissões para administradores
- ⚙️ FAQ dinâmico que pode ser atualizado em tempo real

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **discord.py** - Biblioteca para integração com Discord
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 🚀 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `!comandos` | Lista todos os comandos disponíveis |
| `!faq` | Mostra as perguntas frequentes |
| `!pergunta [texto]` | Faz uma pergunta ao bot |
| `!adicionar_faq [pergunta] [resposta]` | Adiciona nova FAQ (apenas admins) |

## 📦 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- Conta no Discord Developer Portal
- Token de bot do Discord

### Instalação Local

1. Clone o repositório
```bash
git clone https://github.com/SEU-USUARIO/chatbot-discord.git
cd chatbot-discord
```

2. Crie um ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:
```env
DISCORD_BOT_TOKEN=seu_token_aqui
```

5. Execute o bot
```bash
python discord_bot.py
```

## 🌐 Deploy no Render

Este bot está configurado para deploy automático no Render.

1. Faça fork deste repositório
2. Crie uma conta no [Render](https://render.com)
3. Crie um novo Web Service
4. Conecte seu repositório GitHub
5. Adicione a variável de ambiente `DISCORD_BOT_TOKEN`
6. Deploy automático!

## 🎨 Personalização

Para adicionar novas respostas, edite o dicionário `FAQ` em `discord_bot.py`:
```python
FAQ = {
    'sua_pergunta': 'Sua resposta aqui',
    'exemplo': 'Exemplo de resposta',
    # Adicione mais perguntas aqui
}
```

## 📝 Estrutura do Projeto
```
chatbot-discord/
├── discord_bot.py          # Código principal do bot
├── requirements.txt        # Dependências do projeto
├── runtime.txt            # Versão do Python para Render
├── .env.example           # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Seu Nome**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil)

## 🙏 Agradecimentos

- Discord.py pela excelente biblioteca
- Comunidade Python
- Anthropic Claude pela assistência no desenvolvimento

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
