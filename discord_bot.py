import discord
from discord.ext import commands
import os
import re
from dotenv import load_dotenv
load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Respostas predefinidas (FAQ)
FAQ = {

    # ==========================
    # Interações comuns 
    # ==========================

    'olá': 'Olá! Seja bem-vindo.',
    'oi': 'Oi! Paz e graça.',
    'bom dia': 'Bom dia! Que o Senhor o conduza hoje.',
    'boa tarde': 'Boa tarde! Que a graça de Cristo esteja com você.',
    'boa noite': 'Boa noite! Que Deus lhe conceda descanso.',
    'tudo bem': 'Tudo bem, graças a Deus.',
    'obrigado': 'À disposição. Que Deus abençoe.',
    'tchau': 'Até logo. Soli Deo Gloria.',

    # ==========================
    # Cristologia
    # ==========================

    'quem é jesus': (
        'Jesus Cristo é o Filho eterno de Deus, verdadeiro Deus e verdadeiro homem. '
        'Segundo João 1:1,14: “No princípio era o Verbo, e o Verbo estava com Deus, '
        'e o Verbo era Deus… e o Verbo se fez carne”. '
        'A Confissão de Augsburgo (Art. III) ensina que Cristo assumiu a natureza humana '
        'para reconciliar o Pai conosco por meio de Sua morte e ressurreição.'
    ),

    'jesus é deus': (
        'Sim. A Escritura afirma claramente a divindade de Cristo (Jo 20:28; Cl 2:9). '
        'Ele não é um ser criado, mas possui a plenitude da divindade. '
        'O Catecismo Maior de Lutero confessa que Jesus Cristo é “verdadeiro Deus, '
        'gerado do Pai desde a eternidade”.'
    ),

    # ==========================
    # Escritura
    # ==========================

    'o que é a bíblia': (
        'A Bíblia é a Palavra inspirada de Deus, dada por revelação divina. '
        'Segundo 2 Timóteo 3:16–17, toda Escritura é inspirada por Deus e suficiente '
        'para ensinar, repreender e instruir na justiça. '
        'O princípio da Sola Scriptura afirma que somente a Escritura é a autoridade final '
        'em matéria de fé e doutrina.'
    ),

    'a bíblia é inspirada': (
        'Sim. A inspiração bíblica significa que Deus falou por meio de autores humanos '
        'sem erro em tudo aquilo que Ele quis revelar para a salvação. '
        '2 Pedro 1:21 afirma que homens falaram da parte de Deus movidos pelo Espírito Santo.'
    ),

    # ==========================
    # Soteriologia
    # ==========================

    'o que é salvação': (
        'Salvação é a libertação do pecado, da morte e da condenação eterna, '
        'realizada exclusivamente pela obra redentora de Cristo. '
        'Efésios 2:8–9 ensina que somos salvos pela graça, mediante a fé, '
        'e isso não vem de nós, é dom de Deus. '
        'O Catecismo Menor de Lutero afirma que Jesus nos redimiu “não com ouro ou prata, '
        'mas com Seu precioso sangue”.'
    ),

    'como ser salvo': (
        'A Escritura ensina que o ser humano é salvo unicamente pela fé em Cristo. '
        'Atos 16:31 diz: “Crê no Senhor Jesus Cristo e serás salvo”. '
        'Essa fé não é uma obra humana, mas dom do Espírito Santo, '
        'conforme ensina a Confissão de Augsburgo (Art. IV).'
    ),

    'justificação': (
        'Justificação é o ato forense de Deus pelo qual Ele declara o pecador justo '
        'por causa da justiça de Cristo imputada pela fé. '
        'Romanos 3:28 afirma que o homem é justificado pela fé, independentemente das obras da lei. '
        'A Confissão de Augsburgo chama essa doutrina de “artigo pelo qual a Igreja permanece ou cai”.'
    ),

    'fé': (
        'Fé é confiança viva e segura nas promessas de Deus em Cristo. '
        'Hebreus 11:1 descreve a fé como a certeza das coisas que se esperam. '
        'Segundo Lutero, fé é “um firme confiar do coração, pelo qual nos apoiamos em Cristo”.'
    ),

    # ==========================
    # Pecado e condição humana
    # ==========================

    'o que é pecado': (
        'Pecado não é apenas atos externos, mas uma condição interior do coração humano. '
        'Romanos 3:23 declara que todos pecaram e carecem da glória de Deus. '
        'O Catecismo Menor ensina que o ser humano, por natureza, '
        'não teme, não ama e não confia em Deus como deveria.'
    ),

    'pecado original': (
        'O pecado original é a corrupção herdada de Adão, '
        'pela qual toda a humanidade nasce espiritualmente morta. '
        'Salmo 51:5 e Romanos 5:12 testemunham essa condição. '
        'As confissões luteranas afirmam que o ser humano é incapaz de voltar-se a Deus por si mesmo.'
    ),

    # ==========================
    # Lei e Evangelho
    # ==========================

    'lei e evangelho': (
        'A distinção entre Lei e Evangelho é central na teologia luterana. '
        'A Lei revela o pecado e a ira de Deus (Rm 3:20), '
        'enquanto o Evangelho anuncia o perdão e a graça em Cristo (Rm 1:16). '
        'Misturar ambos destrói a correta compreensão da salvação.'
    ),

    # ==========================
    # Igreja e meios de graça
    # ==========================

    'igreja': (
        'A Igreja é a congregação dos santos, onde o Evangelho é corretamente pregado '
        'e os sacramentos são corretamente administrados. '
        'Essa definição vem da Confissão de Augsburgo (Art. VII) '
        'e está fundamentada em Efésios 2:19–22.'
    ),

    'batismo': (
        'O Batismo é um meio de graça instituído por Cristo. '
        'Segundo Marcos 16:16 e Tito 3:5, ele está ligado à promessa de salvação. '
        'O Catecismo Menor ensina que o Batismo “opera perdão dos pecados, '
        'livra da morte e do diabo e concede salvação eterna”.'
    ),

    'ceia': (
        'A Santa Ceia é o sacramento no qual Cristo entrega Seu verdadeiro corpo e sangue '
        'para o perdão dos pecados. '
        'Baseia-se nas palavras de Cristo em Mateus 26:26–28 '
        'e é confessada claramente no Livro de Concórdia.'
    ),

    # ==========================
    # Providência e escatologia
    # ==========================

    'providência': (
        'A providência divina ensina que Deus preserva e governa todas as coisas. '
        'Romanos 8:28 afirma que todas as coisas cooperam para o bem dos que amam a Deus. '
        'O Catecismo Maior ensina que nada acontece por acaso.'
    ),

    'escatologia': (
        'A esperança cristã aponta para a volta visível de Cristo, '
        'a ressurreição dos mortos e o juízo final. '
        'Conforme Apocalipse 22:12, Cristo virá para julgar e restaurar todas as coisas.'
    ),

    # ==========================
    # Solas
    # ==========================

    'sola scriptura': (
        'Sola Scriptura afirma que somente a Escritura é norma infalível da fé. '
        'Isaías 8:20 declara: “À lei e ao testemunho”. '
        'As confissões rejeitam qualquer autoridade que se coloque acima da Palavra.'
    ),

    'sola fide': (
        'Sola Fide ensina que a fé é o único instrumento da justificação. '
        'Romanos 5:1 declara: “Justificados pela fé, temos paz com Deus”.'
    ),

    'sola gratia': (
        'Sola Gratia afirma que a salvação é totalmente obra de Deus. '
        'Nada no ser humano coopera para merecê-la. '
        'Efésios 2:8 deixa isso explicitamente claro.'
    ),

}


# Respostas padrão quando não encontra correspondência
RESPOSTAS_PADRAO = [
    'Interessante! Conte-me mais sobre isso.',
    'Hmm, não tenho certeza sobre isso. Pode reformular a pergunta?',
    'Essa é uma boa pergunta! Infelizmente não tenho essa informação no momento.',
    'Desculpe, não entendi completamente. Pode tentar perguntar de outra forma?',
     'Boa pergunta! Podemos refletir sobre isso juntos.',
    'Interessante ponto de vista. Quer desenvolver melhor?',
    'Ainda estou aprendendo, mas posso tentar ajudar.',
    'Talvez possamos olhar para isso à luz da Bíblia.',
    'Não tenho certeza, mas vale uma boa reflexão.',
    'Essa questão exige um pouco mais de contexto.',
    'Você poderia explicar de outra forma?',
    'Essa é uma pergunta profunda.',
    'Nunca tinha pensado por esse ângulo.',
    'Vamos com calma, esse tema é importante.',
    'Talvez seja bom consultar as Escrituras sobre isso.',
    'Essa pergunta é válida e merece atenção.',
    'Não entendi totalmente, pode reformular?',
    'Isso pode ter mais de uma interpretação.',
    'Interessante… continue.',
    'Essa questão é comum entre cristãos.',
    'Podemos conversar mais sobre isso.',
    'Ainda não tenho uma resposta clara para isso.',
    'Essa é uma boa reflexão teológica.',
    'Vale a pena estudar mais esse assunto.',

    'Entendi. Quer explicar um pouco melhor?',
    'Pode reformular? Assim consigo ajudar melhor.',
    'Interessante, continue.',
    'Não peguei totalmente o que você quis dizer.',
    'Pode dar um exemplo?',
    'Vamos com calma 😄',
    'Isso parece importante.',
    'Boa observação.',
    'Nunca tinha pensado nisso.',
    'Faz sentido.',
    'Pode desenvolver mais?',
    'Essa conversa é válida.',
    'Vamos manter o respeito.',
    'Boa pergunta!',
    'Isso merece atenção.',
    'Ainda estou processando isso.',
    'Vamos por partes.',
    'Essa questão é comum.',
    'Interessante ponto.',
    'Quer continuar?',
    'Essa questão exige reflexão teológica.',
    'Podemos analisar isso à luz das Escrituras.',
    'Há diferentes interpretações dentro do cristianismo.',
    'Esse tema é debatido historicamente.',
    'A tradição reformada reflete bastante sobre isso.',
    'A teologia luterana trata esse ponto com cautela.',
    'Essa pergunta toca no mistério da fé.',
    'Nem tudo é plenamente compreensível pela razão.',
    'A Escritura deve ser nosso ponto de partida.',
    'Esse é um tema profundo.',
    'Vale estudar os teólogos clássicos.',
    'Essa questão envolve pressupostos filosóficos.',
    'Há tensão entre razão e revelação aqui.',
    'A resposta curta não faria justiça ao tema.',
    'Isso já foi discutido desde os Pais da Igreja.',
    'A confissão ajuda a organizar essa questão.',
    'Esse ponto exige humildade teológica.',
    'É um bom tema para estudo bíblico.',
    'A Bíblia responde direta ou indiretamente a isso.',
    'Essa reflexão é legítima.',


]



def encontrar_resposta(mensagem):
    """Procura por palavras-chave na mensagem e retorna uma resposta apropriada"""
    mensagem_lower = mensagem.lower().strip()
    
    # Busca exata primeiro
    if mensagem_lower in FAQ:
        return FAQ[mensagem_lower]
    
    # Busca por palavras-chave contidas na mensagem
    for chave, resposta in FAQ.items():
        if chave in mensagem_lower:
            return resposta
    
    # Se não encontrar nada, retorna uma resposta padrão
    import random
    return random.choice(RESPOSTAS_PADRAO)

@bot.event
async def on_ready():
    print(f'{bot.user} está online e pronto!')
    print(f'ID do bot: {bot.user.id}')
    print('------')

@bot.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == bot.user:
        return
    
    # Processa comandos primeiro
    await bot.process_commands(message)
    
    # Se a mensagem menciona o bot, responde
    if bot.user.mentioned_in(message):
        resposta = encontrar_resposta(message.content)
        await message.channel.send(resposta)

@bot.command(name='question')
async def question (ctx, *, texto):
    """Faz uma pergunta ao bot"""
    resposta = encontrar_resposta(texto)
    await ctx.reply(resposta)

@bot.command(name='comandos')
async def comandos(ctx):
    """Lista todos os comandos disponíveis"""
    embed = discord.Embed(
        title="📋 Comandos Disponíveis",
        description="Aqui estão os comandos que você pode usar:",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="!question [sua pergunta]",
        value="Faz uma pergunta ao bot",
        inline=False
    )
    embed.add_field(
        name="!comandos",
        value="Mostra esta lista de comandos",
        inline=False
    )
    embed.add_field(
        name="!faq",
        value="Mostra as perguntas frequentes",
        inline=False
    )
    embed.add_field(
        name="Menção ao bot",
        value="Você também pode me mencionar diretamente para conversar!",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='faq')
async def mostrar_faq(ctx):
    """Mostra as perguntas frequentes"""
    embed = discord.Embed(
        title="❓ Perguntas Frequentes",
        description="Aqui estão algumas coisas que você pode me perguntar:",
        color=discord.Color.green()
    )
    
    perguntas_exemplo = [
        "Olá / Oi",
        "Tudo bem?",
        "Como você está?",
        "Ajuda",
        "O que você faz?",
        "Quem criou você?",
    ]
    
    for pergunta in perguntas_exemplo:
        embed.add_field(name=f"• {pergunta}", value="\u200b", inline=False)
    
    embed.set_footer(text="Você também pode conversar naturalmente comigo!")
    await ctx.send(embed=embed)

@bot.command(name='adicionar_faq')
@commands.has_permissions(administrator=True)
async def adicionar_faq(ctx, pergunta: str, *, resposta: str):
    """Adiciona uma nova pergunta/resposta ao FAQ (apenas administradores)"""
    FAQ[pergunta.lower()] = resposta
    await ctx.send(f"✅ Pergunta adicionada! Agora quando alguém perguntar sobre '{pergunta}', responderei: {resposta}")

# Inicia o bot
if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    
    if not TOKEN:
        print("❌ ERRO: Token do Discord não encontrado!")
        print("Por favor, defina a variável de ambiente DISCORD_BOT_TOKEN")
    else:
        bot.run(TOKEN)
