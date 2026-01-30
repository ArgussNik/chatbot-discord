<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Chatbot Discord com Respostas Inteligentes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>🤖 Chatbot Discord com Respostas Inteligentes</h1>

<p>
    Bot Discord desenvolvido em <strong>Python</strong> com sistema de perguntas frequentes (FAQ) e respostas personalizadas,
    ideal para servidores que buscam organização, automação e interação inteligente com os membros.
</p>

<hr>

<h2>📋 Sobre o Projeto</h2>

<p>
    Este projeto consiste em um chatbot completo para Discord, capaz de interagir de forma natural com usuários por meio
    de comandos, menções diretas e um sistema dinâmico de perguntas frequentes.
</p>

<p>
    O foco do desenvolvimento está na <strong>clareza</strong>, <strong>personalização</strong> e
    <strong>facilidade de manutenção</strong>, permitindo que administradores adaptem o bot à realidade do servidor
    sem complexidade técnica excessiva.
</p>

<hr>

<h2>✨ Funcionalidades</h2>

<ul>
    <li>💬 Respostas automáticas para perguntas frequentes (FAQ)</li>
    <li>🎯 Sistema de comandos customizáveis</li>
    <li>🔔 Responde automaticamente quando mencionado</li>
    <li>📝 Mensagens organizadas com embeds</li>
    <li>🛡️ Controle de permissões para administradores</li>
    <li>⚙️ FAQ dinâmico, atualizável em tempo real via comandos</li>
</ul>

<hr>

<h2>🛠️ Tecnologias Utilizadas</h2>

<ul>
    <li><strong>Python 3.11+</strong></li>
    <li><strong>discord.py</strong> – Integração com a API do Discord</li>
    <li><strong>python-dotenv</strong> – Gerenciamento seguro de variáveis de ambiente</li>
</ul>

<hr>

<h2>🚀 Comandos Disponíveis</h2>

<table border="1" cellpadding="8" cellspacing="0">
    <thead>
        <tr>
            <th>Comando</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>!comandos</code></td>
            <td>Exibe todos os comandos disponíveis</td>
        </tr>
        <tr>
            <td><code>!faq</code></td>
            <td>Lista as perguntas frequentes</td>
        </tr>
        <tr>
            <td><code>!pergunta [texto]</code></td>
            <td>Envia uma pergunta ao bot</td>
        </tr>
        <tr>
            <td><code>!adicionar_faq [pergunta] [resposta]</code></td>
            <td>Adiciona uma nova FAQ (somente administradores)</td>
        </tr>
    </tbody>
</table>

<hr>

<h2>📦 Como Usar</h2>

<h3>Pré-requisitos</h3>

<ul>
    <li>Python 3.8 ou superior</li>
    <li>Conta no Discord Developer Portal</li>
    <li>Token de bot do Discord</li>
</ul>

<h3>Instalação Local</h3>

<ol>
    <li>
        Clone o repositório:
        <pre><code>git clone https://github.com/ArgussNik/chatbot-discord.git
cd chatbot-discord</code></pre>
    </li>

    <li>
        Crie e ative um ambiente virtual:
        <pre><code>python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows</code></pre>
    </li>

    <li>
        Instale as dependências:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>

    <li>
        Configure as variáveis de ambiente:
        <pre><code>DISCORD_BOT_TOKEN=seu_token_aqui</code></pre>
    </li>

    <li>
        Execute o bot:
        <pre><code>python discord_bot.py</code></pre>
    </li>
</ol>

<hr>

<h2>🌐 Deploy no Render</h2>

<ol>
    <li>Faça fork do repositório</li>
    <li>Crie uma conta em <a href="https://render.com" target="_blank">https://render.com</a></li>
    <li>Crie um novo Web Service</li>
    <li>Conecte seu repositório do GitHub</li>
    <li>Adicione a variável de ambiente <code>DISCORD_BOT_TOKEN</code></li>
    <li>Inicie o deploy</li>
</ol>

<hr>

<h2>🎨 Personalização</h2>

<p>
    As respostas do bot são controladas por um dicionário de FAQ no arquivo
    <code>discord_bot.py</code>:
</p>

<pre><code>FAQ = {
    'sua_pergunta': 'Sua resposta aqui',
    'exemplo': 'Exemplo de resposta',
}</code></pre>

<hr>

<h2>📝 Estrutura do Projeto</h2>

<pre><code>chatbot-discord/
├── discord_bot.py
├── requirements.txt
├── runtime.txt
├── .env.example
├── .gitignore
└── README.md</code></pre>

<hr>

<h2>📄 Licença</h2>

<p>
    Este projeto está sob a <strong>MIT License</strong>.
    Consulte o arquivo <code>LICENSE</code> para mais detalhes.
</p>

<hr>

<h2>👤 Autor</h2>

<p><strong>Nicolas Henrique dos Santos de Lima</strong></p>

<ul>
    <li>GitHub: <a href="https://github.com/ArgussNik" target="_blank">@ArgussNik</a></li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/nicollas-lima/" target="_blank">Nicollas Lima</a></li>
</ul>

<p>⭐ Se este projeto foi útil, considere deixar uma estrela no repositório.</p>

</body>
</html>