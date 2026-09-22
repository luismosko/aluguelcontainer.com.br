# aluguelcontainer.com.br — conteúdo v1.0.0
# Texto 100% próprio (não reaproveitar do campograndecontainers.com.br — evita conteúdo duplicado).
# Regras de conteúdo: sem prazo de entrega em horas, sem depoimentos inventados, sem "frota própria",
# alojamento só 6m e sem citar beliches/armários, prazo mínimo de locação 30 dias.

EMPRESA = dict(razao="TRM Serviços LTDA", cnpj="58.169.089/0001-02", tel="(67) 99241-4371", tel_num="67992414371",
               wa="5567992414371", rua="Rua Pernambuco, 1396", bairro="Monte Castelo", cidade="Campo Grande",
               uf="MS", cep="79010-040", lat=-20.4697, lng=-54.6201)

CIDADES = ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá", "Ponta Porã", "Naviraí", "Aquidauana", "Sidrolândia",
           "Nova Andradina", "Maracaju", "Coxim", "São Gabriel do Oeste", "Rio Brilhante", "Paranaíba", "Chapadão do Sul", "Terenos"]
LISTA_CIDADES = '<ul class="cidades">' + "".join(f"<li>{c}</li>" for c in CIDADES) + "</ul>"

def img(nome, w, h, alt, lazy=True):
    return f'<img src="/img/{nome}.webp" width="{w}" height="{h}" alt="{alt}"{" loading=lazy decoding=async" if lazy else ""}>'

PAGINAS = []

# ============================================================ HOME
PAGINAS.append(dict(
 slug="", migalha="Início",
 title="Aluguel de Container em Campo Grande - MS | Escritório, Obra e Almoxarifado",
 desc="Aluguel de container em Campo Grande e interior de MS: escritório com ar-condicionado, almoxarifado, banheiro e alojamento para obra. Contrato mensal e entrega com munck.",
 h1="Aluguel de container em Campo Grande",
 lead="Container escritório, almoxarifado, banheiro e alojamento para obra, empresa ou evento. Você paga por mês, usa enquanto precisar e a gente busca quando acabar.",
 hero_img=("aluguel-container-escritorio-campo-grande-ms", 1200, 903, "Container escritório branco para aluguel instalado em terreno em Campo Grande MS"),
 placa=[("Prazo mínimo", "30 dias"), ("Tamanhos", "6 m e 12 m"), ("Entrega", "Caminhão munck"), ("Cobertura", "Campo Grande e MS")],
 placa_tit="Condições de locação",
 corpo=f'''
<section><div class="wrap">
<div class="intro"><h2>Qual container você precisa alugar?</h2>
<p>Cada uso pede uma montagem diferente. Um escritório precisa de ar-condicionado e tomada; um almoxarifado precisa de porta larga e trava boa; um banheiro precisa de ponto de água e esgoto. Escolha pelo uso e a gente indica o modelo.</p></div>
<div class="tipos">
<div class="tipo"><div class="med">6 m ou 12 m · climatizado</div><h3>Container escritório</h3><p>Sala pronta com ar-condicionado, iluminação, tomadas, janela e porta com fechadura. Serve de escritório de obra, plantão de vendas ou base de atendimento.</p><a href="/aluguel-de-container-escritorio">Ver container escritório</a></div>
<div class="tipo"><div class="med">6 m ou 12 m · aço</div><h3>Container almoxarifado</h3><p>Depósito fechado para ferramenta, material e equipamento. Porta dupla na cabeceira e haspe para cadeado, direto no canteiro ou no pátio da empresa.</p><a href="/aluguel-de-container-almoxarifado">Ver almoxarifado</a></div>
<div class="tipo"><div class="med">Canteiro completo</div><h3>Container para obra</h3><p>Monte o canteiro com um ou mais containers: escritório do engenheiro, depósito, vestiário e sanitário, entregues na mesma programação.</p><a href="/aluguel-de-container-para-obra">Ver container para obra</a></div>
<div class="tipo"><div class="med">Água e esgoto no local</div><h3>Container banheiro</h3><p>Módulo sanitário para equipe de obra, evento ou área sem estrutura. Configuração definida pelo número de pessoas que vão usar.</p><a href="/aluguel-de-container-banheiro">Ver container banheiro</a></div>
<div class="tipo"><div class="med">6 m · climatizado</div><h3>Container alojamento</h3><p>Espaço climatizado para descanso de equipe em obra ou frente de trabalho. Para turmas maiores, entregamos mais de uma unidade.</p><a href="/aluguel-de-container-alojamento">Ver alojamento</a></div>
<div class="tipo"><div class="med">20 e 40 pés · dry</div><h3>Container marítimo</h3><p>O container padrão, sem adaptação, para guardar carga volumosa, estoque sazonal ou insumo agrícola por alguns meses.</p><a href="/aluguel-de-container-maritimo">Ver container marítimo</a></div>
</div></div></section>

<section class="sec-branca"><div class="wrap duas">
<div><h2>Alugar ou comprar? Quando o aluguel compensa</h2>
<p>A conta é simples: se o container vai ficar com você por um período definido, como a duração de uma obra, uma safra ou uma reforma, alugar costuma sair mais barato do que comprar e revender depois. Você não imobiliza dinheiro, não se preocupa com manutenção estrutural e devolve quando terminar.</p>
<p>Comprar passa a fazer sentido quando o uso é permanente, por vários anos, ou quando você quer fazer adaptações que não dá para desfazer. Nesses casos, veja a página de <a href="/venda-de-container">venda de container</a>.</p>
<ul class="lista"><li>Sem investimento inicial no equipamento</li><li>Mensalidade previsível, fácil de lançar no custo da obra</li><li>Troca de modelo se a necessidade mudar no meio do caminho</li><li>Retirada agendada no fim do contrato</li></ul></div>
<div>{img("container-escritorio-instalado-terreno-ms",1200,800,"Container escritório alugado instalado sobre base de brita em terreno de Mato Grosso do Sul")}</div>
</div></section>

<section><div class="wrap">
<div class="intro"><h2>Do pedido ao container no seu terreno</h2><p>O processo completo está detalhado em <a href="/como-funciona-o-aluguel">como funciona o aluguel</a>. Resumindo:</p></div>
<ol class="passos">
<li><b>Orçamento</b><span>Você informa uso, endereço e período. Respondemos com valor da locação e do frete.</span></li>
<li><b>Contrato</b><span>Contrato mensal, prazo mínimo de 30 dias, renovável sem precisar de nova entrega.</span></li>
<li><b>Entrega</b><span>Caminhão munck posiciona o container no ponto combinado, com data agendada.</span></li>
<li><b>Retirada</b><span>No fim do período, agendamos a busca. Quer ficar mais? É só avisar antes.</span></li>
</ol></div></section>

<section class="sec-branca"><div class="wrap duas">
<div><h2>Onde entregamos</h2>
<p>Estamos no Monte Castelo, em Campo Grande, e entregamos em todos os bairros da capital. No interior de Mato Grosso do Sul, o frete é calculado pela distância e pelo acesso ao local, e você recebe esse valor junto com o orçamento, antes de fechar.</p>
{LISTA_CIDADES}</div>
<div>{img("patio-containers-maritimos-campo-grande-ms",1200,900,"Pátio com containers marítimos disponíveis para locação em Campo Grande MS")}</div>
</div></section>
''',
 faq=[
  ("Quanto custa alugar um container em Campo Grande?", "O valor depende do tipo (escritório, almoxarifado, banheiro, alojamento ou marítimo), do tamanho, do tempo de contrato e do endereço de entrega. Mande essas informações pelo WhatsApp (67) 99241-4371 e você recebe o valor da mensalidade e do frete."),
  ("Qual o tempo mínimo de aluguel?", "O contrato mínimo é de 30 dias. Depois disso a locação segue mês a mês enquanto você precisar, sem necessidade de nova entrega."),
  ("Como o container é entregue?", "Com caminhão munck, que levanta o container e posiciona no ponto combinado. O local precisa ter acesso para o caminhão e espaço livre de fiação aérea no trajeto do içamento."),
  ("Em quanto tempo o container chega?", "A entrega é agendada conforme a disponibilidade do modelo e da agenda de transporte. Em Campo Grande costuma ser em poucos dias úteis após o contrato; para o interior, informamos o prazo real antes de fechar."),
  ("Vocês entregam fora de Campo Grande?", "Sim, atendemos o interior de Mato Grosso do Sul, como Dourados, Três Lagoas, Corumbá, Ponta Porã, Sidrolândia e Maracaju. O frete é calculado pela distância e aparece no orçamento."),
  ("Preciso preparar o terreno?", "O container precisa ficar sobre uma superfície firme e nivelada: piso de concreto, asfalto, brita compactada ou calços de concreto nos cantos. Antes da entrega passamos as orientações para o seu caso."),
  ("Posso alugar mais de um container para o mesmo lugar?", "Pode. É comum montar um canteiro com escritório, almoxarifado e banheiro. Os containers podem ser entregues na mesma programação."),
  ("Pessoa física pode alugar?", "Sim. Alugamos para pessoa física, empresa e órgão público. O contrato muda conforme o caso, mas o processo de orçamento é o mesmo."),
 ],
 faq_titulo="Dúvidas sobre aluguel de container",
))

# ============================================================ COMO FUNCIONA
PAGINAS.append(dict(
 slug="como-funciona-o-aluguel", migalha="Como funciona o aluguel",
 title="Como Funciona o Aluguel de Container | Prazo, Contrato e Entrega - Campo Grande MS",
 desc="Entenda o aluguel de container em Campo Grande - MS: prazo mínimo de 30 dias, o que entra no contrato, como é o frete, como preparar o local e como é a retirada.",
 h1="Como funciona o aluguel de container",
 lead="Tudo o que acontece entre o primeiro contato e a retirada do container: o que perguntamos, o que vai no contrato, como preparar o local e o que você paga.",
 hero_img=("container-escritorio-alugado-obra-campo-grande", 1200, 903, "Container escritório alugado posicionado em terreno de obra em Campo Grande"),
 placa=[("Contrato", "Mensal"), ("Mínimo", "30 dias"), ("Renovação", "Sem nova entrega"), ("Frete", "No orçamento")],
 placa_tit="Regras do contrato",
 wa_msg="Olá! Li como funciona o aluguel e quero um orçamento de container.",
 corpo='''
<section><div class="wrap texto">
<h2>1. O que você precisa informar no orçamento</h2>
<p>Para dar um valor fechado, precisamos de quatro informações. Quanto mais precisas, menos idas e vindas:</p>
<ul class="lista">
<li><b>Uso do container:</b> escritório, depósito, sanitário, alojamento ou só armazenagem. Isso define o modelo.</li>
<li><b>Endereço de entrega:</b> bairro em Campo Grande ou cidade no interior. Isso define o frete.</li>
<li><b>Período estimado:</b> mesmo que seja aproximado (3 meses, até o fim da obra, a safra).</li>
<li><b>Condição do acesso:</b> rua de terra, portão estreito, fiação baixa, declive. Uma foto do local ajuda muito.</li>
</ul>

<h2>2. O contrato</h2>
<p>O contrato é mensal, com prazo mínimo de 30 dias. Nele ficam descritos o container locado, o endereço de instalação, o valor da mensalidade, o valor de entrega e retirada e as responsabilidades de cada lado durante o uso.</p>
<p>Passados os 30 dias, a locação continua mês a mês. Para encerrar, você avisa com antecedência e agendamos a retirada. Para prorrogar, não é preciso fazer nada além de manter o pagamento em dia: o container não sai do lugar.</p>
<div class="nota"><p><b>Órgão público:</b> atendemos contratações por dispensa e licitação. A proposta segue o formato exigido pelo edital; peça pelo WhatsApp ou pelo formulário de contato.</p></div>

<h2>3. O que você paga</h2>
<p>São dois valores separados: a <b>mensalidade</b> da locação e o <b>frete</b> de entrega e retirada. O frete depende da distância e do tipo de acesso, e é informado no orçamento, antes de você assinar. Não existe cobrança surpresa na hora de buscar o container.</p>

<h2>4. Preparando o local</h2>
<p>A entrega é feita com caminhão munck, que levanta o container pelo guindaste e coloca no ponto combinado. Para dar certo na primeira tentativa, confira antes:</p>
<ul class="lista">
<li>Rua e portão com largura para o caminhão entrar e manobrar.</li>
<li>Nenhuma fiação elétrica ou galho baixo entre o caminhão e o ponto de instalação.</li>
<li>Base firme e nivelada: concreto, asfalto, brita compactada ou quatro calços de concreto nos cantos.</li>
<li>Para escritório e alojamento, um ponto de energia perto do container.</li>
<li>Para banheiro, ponto de água e ligação de esgoto ou fossa.</li>
</ul>
<p>Terreno com barro depois de chuva forte é o motivo mais comum de reagendamento. Se o acesso for de terra, vale combinar a data olhando a previsão.</p>

<h2>5. Durante a locação</h2>
<p>O container fica sob sua guarda no local combinado. Mudar de lugar dentro do mesmo terreno é possível, mas precisa do munck; não tente arrastar. Qualquer problema de porta, fechadura, elétrica ou vedação, avise pelo WhatsApp que a gente resolve.</p>

<h2>6. A retirada</h2>
<p>Deixe o container vazio, limpo e com acesso livre na data combinada. Fazemos a conferência do estado do container na retirada, comparando com a entrega.</p>
</div></section>
''',
 faq=[
  ("Posso devolver o container antes dos 30 dias?", "O prazo mínimo contratado é de 30 dias, então a mensalidade do primeiro mês é integral. Depois do primeiro mês, você pode encerrar a qualquer momento avisando com antecedência."),
  ("Como é feita a renovação?", "Automática, mês a mês. O container continua no local e você segue pagando a mensalidade até avisar que quer encerrar."),
  ("O frete é cobrado duas vezes?", "O frete cobre a entrega e a retirada. O orçamento mostra esse valor de forma separada da mensalidade, para você saber exatamente o custo total."),
  ("Preciso estar no local na entrega?", "Sim, ou alguém autorizado. É preciso indicar o ponto exato de instalação e conferir o container na chegada."),
  ("Posso mudar o container de lugar depois de instalado?", "Pode, mas só com caminhão munck. Arrastar ou tentar mover com outro equipamento danifica a estrutura e o piso. Combine a mudança com a gente."),
  ("E se o container der algum problema durante o uso?", "Fale pelo WhatsApp com foto do problema. Defeitos de uso normal, como porta, fechadura ou vedação, são atendidos por nós."),
  ("Vocês atendem licitação?", "Sim. Preparamos proposta no formato do edital e atendemos contratações de órgãos públicos em Campo Grande e no interior de MS."),
 ],
))

# ============================================================ ESCRITÓRIO
PAGINAS.append(dict(
 slug="aluguel-de-container-escritorio", migalha="Container escritório", servico="Aluguel de container escritório",
 title="Aluguel de Container Escritório em Campo Grande - MS | Com Ar-Condicionado",
 desc="Container escritório para alugar em Campo Grande - MS: ar-condicionado, elétrica, iluminação, janela e porta com fechadura. 6 m ou 12 m, contrato mensal, entrega com munck.",
 h1="Aluguel de container escritório em Campo Grande",
 lead="Uma sala pronta para trabalhar, entregue no seu terreno. Ar-condicionado instalado, elétrica, iluminação e porta com fechadura. É ligar na energia e ocupar.",
 hero_img=("container-escritorio-alugado-obra-campo-grande", 1200, 903, "Container escritório para aluguel com porta e janela em Campo Grande MS"),
 placa=[("Tamanhos", "6 m e 12 m"), ("Área útil 6 m", "≈ 13 m²"), ("Área útil 12 m", "≈ 27 m²"), ("Climatização", "Inclusa")],
 placa_tit="Container escritório",
 wa_msg="Olá! Quero orçamento de aluguel de container escritório.",
 corpo=f'''
<section><div class="wrap duas">
<div><h2>O que vem no container escritório</h2>
<p>O escritório sai do nosso pátio montado. Você não precisa contratar eletricista nem instalar ar-condicionado: basta ligar o cabo de energia no ponto do seu terreno.</p>
<ul class="lista">
<li>Ar-condicionado instalado e testado antes da entrega</li>
<li>Quadro de disjuntores, tomadas e interruptores</li>
<li>Iluminação interna em LED</li>
<li>Janela com veneziana e porta com fechadura</li>
<li>Paredes e forro com revestimento interno e isolamento térmico</li>
<li>Piso interno pronto para uso</li>
</ul>
<p>Móveis, divisórias e banheiro interno são opcionais. Consulte a disponibilidade de cada configuração quando pedir o orçamento.</p></div>
<div class="galeria" style="grid-template-columns:repeat(2,1fr)">
{img("interior-container-escritorio-janela-porta",903,1200,"Interior do container escritório com porta e janela veneziana")}
{img("container-escritorio-ar-condicionado-interno",675,1200,"Container escritório com ar-condicionado instalado na parede")}
{img("interior-container-escritorio-janela-veneziana",903,1200,"Parede interna revestida de container escritório com janela")}
{img("banheiro-interno-container-escritorio",675,1200,"Banheiro interno opcional em container escritório para locação")}
</div>
</div></section>

<section class="sec-branca"><div class="wrap">
<div class="intro"><h2>6 metros ou 12 metros?</h2><p>A escolha depende de quantas pessoas vão trabalhar ao mesmo tempo e se o escritório vai receber cliente ou só a equipe.</p></div>
<div class="tab-scroll"><table class="spec">
<thead><tr><th>Medida</th><th>Container 6 m (20 pés)</th><th>Container 12 m (40 pés)</th></tr></thead>
<tbody>
<tr><th>Área interna aproximada</th><td>≈ 13 m²</td><td>≈ 27 m²</td></tr>
<tr><th>Uso confortável</th><td>2 a 4 mesas de trabalho</td><td>até 8 mesas ou sala + recepção</td></tr>
<tr><th>Largura / altura externa</th><td>≈ 2,44 m / 2,59 m</td><td>≈ 2,44 m / 2,59 m</td></tr>
<tr><th>Espaço para instalar</th><td>Vaga de carro com folga</td><td>Área de ~13 × 3 m</td></tr>
<tr><th>Indicado para</th><td>Escritório de obra, portaria, plantão de vendas</td><td>Base administrativa, sala de reunião, atendimento ao público</td></tr>
</tbody></table></div>
<p style="margin-top:14px;color:#5E6B78;font-size:.95rem">Medidas aproximadas; variam conforme o acabamento interno.</p>
</div></section>

<section><div class="wrap duas">
<div><h2>Onde o container escritório costuma ser usado</h2>
<p><b>Escritório de obra:</b> o engenheiro e o mestre de obras ficam no canteiro, com projeto aberto na mesa, sem depender de imóvel alugado perto.</p>
<p><b>Plantão de vendas:</b> loteamentos e condomínios em lançamento usam o container como ponto de atendimento no próprio terreno.</p>
<p><b>Expansão temporária:</b> empresa que cresceu e ainda não mudou de sede instala um container no pátio por alguns meses.</p>
<p><b>Base de campo:</b> agronegócio, mineração e obras de rodovia no interior de MS usam como escritório em local sem estrutura.</p></div>
<div><h2>Calor de Campo Grande</h2>
<p>Container sem isolamento vira estufa no verão sul-mato-grossense. Por isso o nosso escritório vai com revestimento interno, forro e ar-condicionado dimensionado para o tamanho da sala.</p>
<p>Para aliviar ainda mais o consumo, vale posicionar o container com a porta e a janela longe do sol da tarde e, se der, embaixo de uma cobertura ou sombra de árvore. Na hora da entrega, a gente ajuda a escolher o melhor ponto.</p></div>
</div></section>
''',
 faq=[
  ("O ar-condicionado já vem instalado?", "Sim. Todo container escritório é entregue com ar-condicionado instalado e testado. Você só precisa de um ponto de energia no local para ligar."),
  ("Qual a voltagem do container escritório?", "Informe a voltagem disponível no seu terreno no orçamento. A instalação elétrica é preparada de acordo com o ponto de energia do local."),
  ("Quantas pessoas cabem em um container escritório de 6 metros?", "Com conforto, de 2 a 4 pessoas trabalhando em mesa. Para mais gente ou para ter uma área de atendimento separada, o de 12 metros é mais indicado."),
  ("O container escritório tem banheiro?", "O modelo padrão não tem. Há configuração com banheiro interno, que depende de disponibilidade e exige ponto de água e esgoto no local."),
  ("Vem com móveis?", "O padrão é entregue vazio, com a estrutura, a elétrica e a climatização. Mobiliário pode ser consultado no orçamento."),
  ("Posso colocar a logo da minha empresa no container?", "Adesivos removíveis podem ser aplicados desde que não danifiquem a pintura. Combine antes para que fique registrado no contrato."),
  ("Quanto custa alugar um container escritório?", "Depende do tamanho, do tempo de locação e do endereço de entrega. Mande essas informações pelo WhatsApp (67) 99241-4371 que respondemos com mensalidade e frete."),
  ("Dá para juntar dois containers e fazer um escritório maior?", "Dá para instalar lado a lado ou em L no mesmo terreno. A união interna entre dois containers exige adaptação específica e precisa ser avaliada caso a caso."),
 ],
 faq_titulo="Perguntas sobre container escritório",
))

# ============================================================ ALMOXARIFADO
PAGINAS.append(dict(
 slug="aluguel-de-container-almoxarifado", migalha="Container almoxarifado", servico="Aluguel de container almoxarifado",
 title="Aluguel de Container Almoxarifado em Campo Grande - MS | Depósito para Obra",
 desc="Container almoxarifado para alugar em Campo Grande - MS. Depósito em aço com porta dupla e haspe para cadeado, 6 m ou 12 m, para guardar ferramentas, material de obra e estoque.",
 h1="Container almoxarifado para alugar",
 lead="Um depósito de aço fechado no seu canteiro ou pátio. Guarda ferramenta, material e equipamento longe da chuva, do sol e de quem não deveria mexer.",
 hero_img=("aluguel-container-almoxarifado-obra-campo-grande", 1167, 778, "Container almoxarifado com portas duplas para aluguel em canteiro de obra em Campo Grande"),
 placa=[("Tamanhos", "6 m e 12 m"), ("Volume 6 m", "≈ 33 m³"), ("Volume 12 m", "≈ 67 m³"), ("Fechamento", "Haspe p/ cadeado")],
 placa_tit="Container almoxarifado",
 wa_msg="Olá! Quero orçamento de aluguel de container almoxarifado.",
 corpo='''
<section><div class="wrap duas">
<div><h2>Por que usar container como almoxarifado</h2>
<p>Barraco de madeira na obra dá trabalho para montar, apodrece com a chuva e é fácil de arrombar. O container chega pronto, é inteiro de aço e fecha com porta dupla e haspe para cadeado. No fim da obra, sai do terreno em uma manhã, sem entulho.</p>
<ul class="lista">
<li>Estrutura de aço, fechada nas quatro laterais e no teto</li>
<li>Porta dupla na cabeceira, com abertura total para entrar com carrinho e material comprido</li>
<li>Haspe para cadeado; você usa o cadeado da sua preferência</li>
<li>Piso resistente para peso de sacaria, ferramenta e equipamento</li>
<li>Ventilação natural para reduzir umidade</li>
</ul></div>
<div><h2>O que dá para guardar</h2>
<p><b>Na obra:</b> cimento, argamassa, ferragem, ferramentas elétricas, betoneira pequena, EPI e material de acabamento.</p>
<p><b>Na empresa:</b> estoque sazonal, arquivo morto, mercadoria de promoção, material de manutenção.</p>
<p><b>No campo:</b> sementes, defensivos e peças de máquina, com mais controle de acesso do que um galpão aberto.</p>
<div class="nota"><p>Produto inflamável, combustível ou químico perigoso tem regras próprias de armazenagem. Consulte antes de guardar esse tipo de material no container.</p></div>
</div>
</div></section>

<section class="sec-branca"><div class="wrap">
<div class="intro"><h2>Medidas do container almoxarifado</h2><p>Valores aproximados de container dry padrão. Para almoxarifado de obra de casa ou reforma, o de 6 metros costuma sobrar; o de 12 metros é para prédio, galpão e estoque grande.</p></div>
<div class="tab-scroll"><table class="spec">
<thead><tr><th>Medida</th><th>6 m (20 pés)</th><th>12 m (40 pés)</th></tr></thead>
<tbody>
<tr><th>Comprimento interno</th><td>≈ 5,90 m</td><td>≈ 12,0 m</td></tr>
<tr><th>Largura interna</th><td>≈ 2,35 m</td><td>≈ 2,35 m</td></tr>
<tr><th>Altura interna</th><td>≈ 2,39 m</td><td>≈ 2,39 m</td></tr>
<tr><th>Volume</th><td>≈ 33 m³</td><td>≈ 67 m³</td></tr>
<tr><th>Abertura da porta</th><td>≈ 2,34 × 2,28 m</td><td>≈ 2,34 × 2,28 m</td></tr>
</tbody></table></div>
</div></section>

<section><div class="wrap texto">
<h2>Dicas para o almoxarifado render mais</h2>
<p>Coloque o container sobre calços ou base de brita: além de nivelar, afasta o piso da umidade do chão e facilita o escoamento da chuva. Deixe a porta virada para o lado de onde o material chega, assim o caminhão de entrega descarrega perto.</p>
<p>Organize em corredor: prateleira ou palete dos dois lados, passagem no meio. Material mais usado perto da porta, estoque de reserva no fundo. Isso evita tirar tudo do container para achar uma ferramenta.</p>
<p>Em obra com muito material de valor, um cadeado de boa qualidade no haspe faz diferença. É o ponto mais visado em tentativa de furto.</p>
</div></section>
''',
 faq=[
  ("O container almoxarifado vem com cadeado?", "Não. Ele vem com haspe para cadeado e você usa o seu. Assim só você e sua equipe têm a chave."),
  ("Qual cabe mais: o de 6 ou o de 12 metros?", "O de 12 metros tem pouco mais que o dobro do volume: cerca de 67 m³ contra 33 m³ do de 6 metros. A largura e a altura são as mesmas."),
  ("O container almoxarifado esquenta muito?", "Sim, aço no sol esquenta. Para ferramenta e material de obra não costuma ser problema. Para produto sensível a calor, consulte a opção com ventilação reforçada ou use o container em local sombreado."),
  ("Entra água no container?", "O container é fechado e vedado. O cuidado é instalar sobre base nivelada e um pouco elevada, para que a água da chuva não empoce em volta da porta."),
  ("Tem prateleira dentro?", "O padrão é entregue vazio. Prateleiras podem ser consultadas no orçamento, ou você instala prateleiras soltas, sem furar a estrutura."),
  ("Posso usar o almoxarifado como vestiário também?", "Para vestiário é melhor usar um container com iluminação e ventilação, ou o container escritório. O almoxarifado padrão não tem elétrica."),
  ("Quanto tempo posso ficar com o container?", "O mínimo é 30 dias e depois segue mês a mês. Tem obra que fica com o almoxarifado mais de um ano."),
 ],
))

# ============================================================ OBRA
PAGINAS.append(dict(
 slug="aluguel-de-container-para-obra", migalha="Container para obra", servico="Aluguel de container para obra",
 title="Aluguel de Container para Obra em Campo Grande - MS | Canteiro Completo",
 desc="Monte o canteiro de obras com containers alugados em Campo Grande - MS: escritório, almoxarifado, banheiro e alojamento. Contrato pelo período da obra e entrega com munck.",
 h1="Container para obra: monte o canteiro inteiro",
 lead="Escritório, depósito, sanitário e área de descanso para a equipe, tudo em container alugado pelo tempo da obra. Entrega no início, retirada na limpeza final.",
 hero_img=("patio-containers-maritimos-campo-grande-ms", 1200, 900, "Containers disponíveis para aluguel de canteiro de obra em pátio de Campo Grande"),
 placa=[("Módulos", "Escritório, depósito, WC"), ("Contrato", "Período da obra"), ("Entrega", "Munck"), ("Mínimo", "30 dias")],
 placa_tit="Canteiro de obra",
 wa_msg="Olá! Quero montar um canteiro de obra com containers. Pode me passar orçamento?",
 corpo='''
<section><div class="wrap">
<div class="intro"><h2>Um canteiro por tamanho de obra</h2><p>Sugestões de ponto de partida. A quantidade certa depende do número de trabalhadores, da duração e de quanta coisa você precisa guardar no local.</p></div>
<div class="tipos">
<div class="tipo"><div class="med">Reforma ou casa térrea</div><h3>1 container</h3><p>Um almoxarifado de 6 metros para ferramenta e material. O dono da obra ou o mestre guardam tudo trancado no fim do dia.</p><a href="/aluguel-de-container-almoxarifado">Almoxarifado</a></div>
<div class="tipo"><div class="med">Sobrado, galpão pequeno</div><h3>2 containers</h3><p>Almoxarifado mais um escritório de 6 metros, onde o engenheiro trabalha, guarda projeto e recebe fornecedor.</p><a href="/aluguel-de-container-escritorio">Escritório</a></div>
<div class="tipo"><div class="med">Prédio, condomínio, obra pública</div><h3>3 ou mais</h3><p>Escritório, almoxarifado, banheiro e, se a equipe dorme perto, alojamento. Entregues na mesma programação.</p><a href="/aluguel-de-container-banheiro">Banheiro</a></div>
</div></div></section>

<section class="sec-branca"><div class="wrap duas">
<div><h2>Vantagens do container no canteiro</h2>
<ul class="lista">
<li><b>Sem obra dentro da obra:</b> não precisa construir barraco, que depois vira entulho.</li>
<li><b>Instalação em minutos:</b> o munck posiciona e está pronto para uso.</li>
<li><b>Muda de lugar:</b> se a obra avança sobre o ponto do container, dá para reposicionar com o munck.</li>
<li><b>Custo por mês:</b> entra no orçamento da obra como despesa, sem ativo para revender depois.</li>
<li><b>Segurança:</b> aço e cadeado são bem mais difíceis de violar do que madeira e compensado.</li>
</ul></div>
<div><h2>NR-18 e áreas de vivência</h2>
<p>A NR-18 exige, conforme o porte da obra, instalação sanitária, vestiário, local para refeição e, quando há trabalhadores alojados, alojamento com condições adequadas. Containers adaptados são uma forma comum de atender essas áreas de vivência sem construir.</p>
<p>A definição de quantos sanitários e qual área é necessária depende do número de trabalhadores e cabe ao responsável técnico da obra. Com esse número em mãos, indicamos a composição de containers.</p>
</div>
</div></section>

<section><div class="wrap texto">
<h2>Planejando o canteiro antes da entrega</h2>
<p>Separe no projeto do canteiro uma faixa com acesso de caminhão, longe do trecho onde vai ter escavação, fundação ou movimentação de guindaste. Container posicionado no lugar errado vai ter que mudar de novo, e cada mudança é uma diária de munck.</p>
<p>Deixe o escritório perto da entrada da obra, para receber visitante e fornecedor sem que eles circulem pelo canteiro. O almoxarifado vai perto de onde o material é descarregado. O banheiro depende do ponto de água e esgoto provisório.</p>
<p>Se a obra é longa, pense na retirada: no fim, o caminhão precisa chegar até os containers de novo, e muitas vezes a área já está com paisagismo ou calçada pronta.</p>
</div></section>
''',
 faq=[
  ("Quantos containers eu preciso na minha obra?", "Depende do número de trabalhadores e do que precisa guardar. Reforma costuma usar um almoxarifado; obra média usa almoxarifado e escritório; obra grande soma banheiro e alojamento. Conte seu caso no WhatsApp e indicamos a composição."),
  ("Os containers atendem a NR-18?", "Containers adaptados são usados para áreas de vivência previstas na NR-18, como sanitário, vestiário e alojamento. A quantidade e as condições exigidas dependem do porte da obra e devem ser definidas pelo responsável técnico."),
  ("Dá para receber todos os containers no mesmo dia?", "Normalmente sim, desde que o local comporte as manobras. Em canteiros grandes, a entrega pode ser feita em etapas, conforme o avanço da obra."),
  ("E se a obra atrasar?", "O contrato segue mês a mês depois dos 30 dias iniciais. Se a obra atrasar, os containers continuam lá; basta manter a locação."),
  ("Vocês atendem obra no interior de MS?", "Sim. Obras em Dourados, Três Lagoas, Corumbá, Ponta Porã e outras cidades são atendidas com frete calculado pela distância."),
  ("Posso trocar um container no meio da obra?", "Pode. Trocar um almoxarifado por um escritório, ou somar mais uma unidade, é comum quando a obra muda de fase. A troca envolve frete de ida e volta."),
  ("Atendem construtora e obra pública?", "Sim. Trabalhamos com construtoras, empreiteiros, pessoa física e órgãos públicos, inclusive com proposta para licitação."),
 ],
))

# ============================================================ BANHEIRO
PAGINAS.append(dict(
 slug="aluguel-de-container-banheiro", migalha="Container banheiro", servico="Aluguel de container banheiro",
 title="Aluguel de Container Banheiro em Campo Grande - MS | Sanitário para Obra",
 desc="Container banheiro e módulo sanitário para alugar em Campo Grande - MS. Para canteiro de obra, evento e área sem estrutura. Exige ponto de água e esgoto ou fossa.",
 h1="Container banheiro para alugar",
 lead="Sanitário de verdade, com vaso, pia e descarga, para equipe de obra ou área sem estrutura. É preciso ter água e esgoto no local; a gente cuida do resto.",
 hero_img=("aluguel-container-banheiro-canteiro-obra", 1200, 800, "Módulo sanitário container para aluguel instalado em canteiro de obra"),
 placa=[("Uso", "Obra, evento, campo"), ("Requer", "Água + esgoto"), ("Config.", "Por nº de usuários"), ("Mínimo", "30 dias")],
 placa_tit="Container banheiro",
 wa_msg="Olá! Quero orçamento de aluguel de container banheiro.",
 corpo=f'''
<section><div class="wrap duas">
<div><h2>Container banheiro ou banheiro químico?</h2>
<p>O banheiro químico é bom para evento de um dia. Para uma obra de meses, ele vira custo de limpeza semanal, cheiro e reclamação da equipe. O container banheiro funciona como um banheiro comum: vaso com descarga, pia com torneira, ligado na rede de água e no esgoto ou fossa.</p>
<p>Por isso ele é a escolha mais comum para canteiros de média e longa duração, obras públicas e frentes de trabalho fixas.</p>
<h2 style="margin-top:1.2em">O que precisa ter no local</h2>
<ul class="lista">
<li>Ponto de água com pressão (rede ou caixa elevada)</li>
<li>Ligação para esgoto, fossa séptica ou sistema provisório da obra</li>
<li>Ponto de energia, se o módulo tiver iluminação interna</li>
<li>Base nivelada, para o esgoto escoar direito</li>
</ul></div>
<div>{img("modulo-sanitario-container-obra-ms",600,900,"Módulo sanitário com vaso, pia e caixa de descarga para aluguel em obra em MS")}</div>
</div></section>

<section class="sec-branca"><div class="wrap texto">
<h2>Qual configuração escolher</h2>
<p>A configuração é definida pelo número de pessoas que vão usar. Na hora do orçamento, informe quantos trabalhadores ficam no local por turno e se há homens e mulheres na equipe. Com isso indicamos o modelo e a quantidade:</p>
<ul class="lista">
<li><b>Módulo individual:</b> uma cabine com vaso e pia, para equipe pequena ou apoio a um escritório.</li>
<li><b>Container com mais de uma cabine:</b> para equipes maiores, com vasos e lavatórios em quantidade.</li>
<li><b>Divisão masculino e feminino:</b> quando a equipe é mista.</li>
</ul>
<p>A disponibilidade de cada configuração varia; confirme no orçamento.</p>
<div class="nota"><p>Em canteiro de obra, a quantidade mínima de vasos, lavatórios e chuveiros segue a NR-18 e depende do número de trabalhadores. Quem define é o responsável técnico da obra; a gente monta a composição de containers a partir desse número.</p></div>
</div></section>
''',
 faq=[
  ("O container banheiro precisa de ligação de água?", "Sim. Ele funciona como um banheiro comum e precisa de ponto de água e de ligação para esgoto ou fossa séptica no local."),
  ("Quem faz a ligação de água e esgoto?", "O ponto de água e o destino do esgoto são do local de instalação. Com eles prontos, a ligação do container é simples; orientamos o que é necessário antes da entrega."),
  ("Qual a diferença para banheiro químico?", "O banheiro químico armazena os dejetos em um tanque e precisa de limpeza periódica. O container banheiro é ligado ao esgoto e funciona como banheiro normal, com descarga e pia."),
  ("Tem chuveiro?", "Depende da configuração. Se a equipe precisa de banho no local, informe no orçamento para indicarmos o modelo adequado."),
  ("Quantos banheiros minha obra precisa?", "A NR-18 define a quantidade conforme o número de trabalhadores. O responsável técnico calcula a necessidade e nós indicamos quantos containers ou cabines atendem."),
  ("Serve para evento?", "Serve para eventos com duração maior ou em locais com água e esgoto disponíveis. Lembre que o prazo mínimo de locação é de 30 dias."),
  ("Quem faz a limpeza durante a locação?", "A limpeza do dia a dia é de quem usa, como em qualquer banheiro. Na retirada, o container deve ser devolvido limpo."),
 ],
))

# ============================================================ ALOJAMENTO
PAGINAS.append(dict(
 slug="aluguel-de-container-alojamento", migalha="Container alojamento", servico="Aluguel de container alojamento",
 title="Aluguel de Container Alojamento em Campo Grande - MS | Para Equipes de Obra",
 desc="Container alojamento climatizado para alugar em Campo Grande e interior de MS. Modelo de 6 m com ar-condicionado, elétrica e iluminação, para descanso de equipes em obra.",
 h1="Container alojamento para equipes",
 lead="Espaço climatizado para a equipe descansar perto da frente de trabalho. Modelo de 6 metros com ar-condicionado, elétrica e iluminação, pronto para ocupar.",
 hero_img=("container-escritorio-instalado-terreno-ms", 1200, 800, "Container climatizado para alojamento de equipe instalado em terreno em Mato Grosso do Sul"),
 placa=[("Tamanho", "6 m (20 pés)"), ("Climatização", "Ar-condicionado"), ("Elétrica", "Tomadas + LED"), ("Mobiliário", "Sob consulta")],
 placa_tit="Container alojamento",
 wa_msg="Olá! Quero orçamento de aluguel de container alojamento.",
 corpo=f'''
<section><div class="wrap duas">
<div><h2>Quando o alojamento em container faz sentido</h2>
<p>Obra longe de casa, turma vinda de outra cidade, trabalho em fazenda ou em trecho de rodovia: nesses casos, alugar casa ou hotel para a equipe custa caro e ainda obriga a levar e buscar todo dia. O container alojamento fica no próprio local de trabalho.</p>
<p>No calor de Mato Grosso do Sul, a climatização não é luxo: equipe que não descansa direito à noite rende menos e se acidenta mais. Por isso o alojamento vai com ar-condicionado instalado.</p>
<ul class="lista">
<li>Container de 6 metros com revestimento interno e isolamento</li>
<li>Ar-condicionado instalado</li>
<li>Tomadas, quadro de disjuntores e iluminação LED</li>
<li>Janela e porta com fechadura</li>
</ul>
<p>O mobiliário interno é definido na hora do orçamento, conforme a disponibilidade.</p></div>
<div>{img("container-escritorio-ar-condicionado-interno",675,1200,"Interior de container climatizado com ar-condicionado e revestimento para alojamento")}</div>
</div></section>

<section class="sec-branca"><div class="wrap texto">
<h2>Equipe grande: combine unidades</h2>
<p>Trabalhamos com o modelo de 6 metros para alojamento. Para turmas maiores, a solução é instalar mais de uma unidade lado a lado, o que ainda permite separar equipes ou turnos.</p>
<p>O alojamento quase sempre vem acompanhado de <a href="/aluguel-de-container-banheiro">container banheiro</a>, e muitas vezes de um <a href="/aluguel-de-container-almoxarifado">almoxarifado</a> para guardar ferramentas fora da área de descanso. Tudo pode ser entregue na mesma programação.</p>
<div class="nota"><p>Alojamento em obra tem exigências na NR-18 (área por trabalhador, ventilação, iluminação, instalações sanitárias). A adequação ao número de pessoas alojadas é responsabilidade do empregador e do responsável técnico.</p></div>
</div></section>
''',
 faq=[
  ("O container alojamento tem ar-condicionado?", "Sim. Ele é entregue com ar-condicionado instalado, além de tomadas e iluminação. Você precisa de um ponto de energia no local."),
  ("Qual o tamanho do container alojamento?", "Trabalhamos com o modelo de 6 metros (20 pés) para alojamento. Para equipes maiores, instalamos mais de uma unidade."),
  ("Vem com mobília?", "O mobiliário é consultado no orçamento, conforme a disponibilidade. Informe quantas pessoas vão ficar alojadas."),
  ("Tem banheiro dentro do alojamento?", "O alojamento não tem banheiro interno. O mais comum é combinar com um container banheiro instalado ao lado."),
  ("O alojamento atende a NR-18?", "O container oferece estrutura climatizada, iluminada e ventilada. A quantidade de pessoas por unidade e as demais exigências da NR-18 devem ser verificadas pelo responsável técnico da obra."),
  ("Atendem fazenda e obra no interior?", "Sim. Levamos o alojamento para obras, fazendas e frentes de trabalho no interior de MS, com frete calculado pela distância."),
  ("Posso alugar por poucos meses?", "Pode. O mínimo é 30 dias e depois a locação segue mês a mês, até o fim do serviço."),
 ],
))

# ============================================================ MARÍTIMO
PAGINAS.append(dict(
 slug="aluguel-de-container-maritimo", migalha="Container marítimo", servico="Aluguel de container marítimo",
 title="Aluguel de Container Marítimo 20 e 40 Pés em Campo Grande - MS",
 desc="Container marítimo dry de 20 e 40 pés para alugar em Campo Grande - MS. Para armazenagem de estoque, insumo agrícola e carga volumosa. Contrato mensal e entrega com munck.",
 h1="Container marítimo 20 e 40 pés para alugar",
 lead="O container original de navio, sem adaptação. Para quem precisa de espaço fechado e resistente por alguns meses, sem pagar por elétrica ou acabamento que não vai usar.",
 hero_img=("containers-maritimos-usados-patio-campo-grande", 1200, 900, "Containers marítimos de 20 e 40 pés disponíveis para aluguel em pátio de Campo Grande"),
 placa=[("Tamanhos", "20 e 40 pés"), ("Tipo", "Dry, seminovo"), ("Material", "Aço"), ("Mínimo", "30 dias")],
 placa_tit="Container marítimo",
 wa_msg="Olá! Quero orçamento de aluguel de container marítimo.",
 corpo=f'''
<section><div class="wrap">
<div class="intro"><h2>20 pés ou 40 pés</h2><p>Medidas de referência do container dry padrão ISO. Podem variar alguns centímetros entre fabricantes.</p></div>
<div class="tab-scroll"><table class="spec">
<thead><tr><th>Medida</th><th>20 pés</th><th>40 pés</th></tr></thead>
<tbody>
<tr><th>Comprimento externo</th><td>≈ 6,06 m</td><td>≈ 12,19 m</td></tr>
<tr><th>Largura externa</th><td>≈ 2,44 m</td><td>≈ 2,44 m</td></tr>
<tr><th>Altura externa</th><td>≈ 2,59 m</td><td>≈ 2,59 m</td></tr>
<tr><th>Volume interno</th><td>≈ 33 m³</td><td>≈ 67 m³</td></tr>
<tr><th>Espaço para instalar</th><td>≈ 7 × 3 m livres</td><td>≈ 13 × 3 m livres</td></tr>
</tbody></table></div>
</div></section>

<section class="sec-branca"><div class="wrap duas">
<div><h2>Para que alugar um container marítimo</h2>
<p><b>Agronegócio:</b> guardar semente, adubo, peça de máquina e ferramenta na fazenda durante a safra, com cadeado e sem depender de galpão.</p>
<p><b>Comércio:</b> estoque extra para Black Friday e fim de ano, instalado no pátio da loja.</p>
<p><b>Mudança e reforma:</b> guardar móveis no próprio terreno enquanto a casa está em obra.</p>
<p><b>Indústria:</b> armazenagem temporária de matéria-prima, embalagem ou produto acabado.</p>
<p>Se o uso pede ar-condicionado ou tomada, o que você procura é um <a href="/aluguel-de-container-escritorio">container escritório</a>. Se é só depósito de obra, veja o <a href="/aluguel-de-container-almoxarifado">almoxarifado</a>.</p></div>
<div>{img("container-maritimo-40-pes-aluguel",650,400,"Container marítimo dry de 40 pés branco para aluguel")}
<h2 style="margin-top:1em">Seminovo: o que esperar</h2>
<p>O container seminovo já fez viagens de navio. Pode ter marcas de uso, amassados leves e pintura com desgaste, mas a estrutura, o piso e a vedação são conferidos antes da entrega. Para armazenagem, isso não faz diferença na prática.</p></div>
</div></section>
''',
 faq=[
  ("Qual a diferença entre container de 20 e de 40 pés?", "O de 40 pés tem o dobro do comprimento (cerca de 12 m contra 6 m) e pouco mais que o dobro do volume, com a mesma largura e altura."),
  ("O container marítimo é novo?", "É seminovo, ou seja, já foi usado em transporte. A estrutura, o piso, as portas e a vedação são inspecionados antes da entrega."),
  ("O container marítimo tem luz ou tomada?", "Não. É o container sem adaptação. Se precisar de elétrica, veja o container escritório ou pergunte por uma adaptação."),
  ("Serve para guardar grãos a granel?", "Não é indicado para grão a granel solto sem preparo. Para produtos ensacados, paletizados ou em caixas, funciona bem."),
  ("Qual o espaço necessário para instalar um de 40 pés?", "Além da área do próprio container (cerca de 12,2 × 2,5 m), é preciso espaço para o caminhão munck encostar e manobrar."),
  ("Posso comprar em vez de alugar?", "Pode. Se o uso vai ser permanente, veja a página de venda de container ou peça as duas cotações para comparar."),
  ("Tem container refrigerado (reefer)?", "Não trabalhamos com container refrigerado para locação. Nosso foco é container dry e containers adaptados."),
 ],
))

# ============================================================ VENDA
PAGINAS.append(dict(
 slug="venda-de-container", migalha="Venda de container", servico="Venda de container",
 title="Venda de Container em Campo Grande - MS | Marítimo e Adaptado",
 desc="Comprar container em Campo Grande - MS: container marítimo 20 e 40 pés seminovo e containers adaptados sob consulta. Entrega com munck em Campo Grande e interior de MS.",
 h1="Venda de container em Campo Grande",
 lead="Quando o uso é permanente, comprar pode sair melhor que alugar. Vendemos container marítimo de 20 e 40 pés e, sob consulta, containers adaptados.",
 hero_img=("patio-containers-maritimos-campo-grande-ms", 1200, 900, "Containers marítimos à venda em pátio em Campo Grande MS"),
 placa=[("Marítimo", "20 e 40 pés"), ("Adaptados", "Sob consulta"), ("Condição", "Seminovo"), ("Entrega", "Munck")],
 placa_tit="Venda",
 wa_msg="Olá! Quero orçamento para comprar um container.",
 cta_titulo="Peça o orçamento de compra",
 corpo='''
<section><div class="wrap duas">
<div><h2>Quando comprar em vez de alugar</h2>
<p>Faça a conta com o tempo de uso. Se a mensalidade somada durante o período que você vai usar chega perto do preço de compra, comprar compensa, e no fim o container ainda é seu.</p>
<ul class="lista">
<li>Uso por vários anos no mesmo lugar</li>
<li>Projeto com adaptação permanente (loja, casa, ateliê)</li>
<li>Depósito fixo em fazenda ou empresa</li>
<li>Você quer o container como patrimônio</li>
</ul>
<p>Se o prazo é de meses, ou a obra tem data para acabar, o <a href="/">aluguel</a> geralmente sai mais barato.</p></div>
<div><h2>O que vendemos</h2>
<p><b>Container marítimo 20 pés:</b> o tamanho mais versátil, fácil de posicionar e transportar.</p>
<p><b>Container marítimo 40 pés:</b> o dobro do espaço, para estoque grande ou projeto de construção.</p>
<p><b>Containers adaptados:</b> escritório, almoxarifado ou sanitário, conforme disponibilidade. Consulte o que está pronto no pátio.</p>
<div class="nota"><p>Antes de comprar para construir, verifique com a prefeitura as regras de uso do solo e aprovação de projeto para o seu terreno.</p></div></div>
</div></section>
''',
 faq=[
  ("Vocês vendem container novo?", "Trabalhamos com container seminovo, que já foi usado em transporte marítimo e é inspecionado antes da venda."),
  ("Quais tamanhos estão à venda?", "Container marítimo de 20 e 40 pés. Containers adaptados dependem de disponibilidade no pátio."),
  ("O frete está incluso no preço?", "O frete é calculado conforme o endereço de entrega e informado junto com o valor do container."),
  ("Posso ver o container antes de comprar?", "Pode. Combine uma visita pelo WhatsApp para ver o container no pátio em Campo Grande."),
  ("Dá para comprar um container já adaptado como escritório?", "Sob consulta. Informe o uso que você pretende e verificamos o que temos disponível."),
  ("Vocês entregam container vendido no interior de MS?", "Sim. Entregamos com munck em Campo Grande e em cidades do interior de Mato Grosso do Sul."),
  ("Container comprado pode virar casa?", "O container é uma base comum para projetos de construção, mas a obra exige projeto, isolamento, elétrica e hidráulica, além de aprovação na prefeitura."),
 ],
))

# ============================================================ SOBRE
PAGINAS.append(dict(
 slug="sobre", migalha="Sobre",
 title="Sobre a Aluguel Container | Locação de Container em Campo Grande - MS",
 desc="A Aluguel Container é uma marca da TRM Serviços LTDA, de Campo Grande - MS, especializada em locação de container para obra, empresa e agronegócio em Mato Grosso do Sul.",
 h1="Sobre a Aluguel Container",
 lead="Somos de Campo Grande e trabalhamos com uma coisa: colocar o container certo no lugar certo, pelo tempo que você precisar.",
 hero_img=("container-escritorio-instalado-terreno-ms", 1200, 800, "Container escritório da Aluguel Container instalado em Campo Grande MS"),
 placa=[("Empresa", "TRM Serviços LTDA"), ("CNPJ", "58.169.089/0001-02"), ("Base", "Monte Castelo, CG"), ("Atuação", "MS")],
 placa_tit="Dados da empresa",
 corpo='''
<section><div class="wrap texto">
<h2>Quem somos</h2>
<p>A Aluguel Container é uma marca da TRM Serviços LTDA, empresa de Campo Grande - MS que também opera a <a href="https://campograndecontainers.com.br" rel="noopener">Campo Grande Containers</a>. Nosso foco aqui é a locação: construtoras, empreiteiros, empresas, produtores rurais e órgãos públicos que precisam de espaço por um período e não querem comprar.</p>
<p>Você fala direto com quem conhece o produto e decide o orçamento, sem central de atendimento e sem passar por várias pessoas até ter resposta.</p>

<h2>Como trabalhamos</h2>
<ul class="lista">
<li><b>Inspeção antes de sair:</b> estrutura, piso, teto, portas, fechaduras e, nos adaptados, elétrica e ar-condicionado são conferidos antes da entrega.</li>
<li><b>Preço fechado:</b> mensalidade e frete informados no orçamento. Sem taxa que aparece na retirada.</li>
<li><b>Contrato direto:</b> prazo mínimo de 30 dias, renovação mês a mês, regras claras de uso e devolução.</li>
<li><b>Entrega com munck:</b> posicionamento no ponto que você escolheu, com orientação prévia sobre o acesso.</li>
</ul>

<h2>Onde estamos</h2>
<p>Rua Pernambuco, 1396, bairro Monte Castelo, Campo Grande - MS, CEP 79010-040. Atendimento de segunda a sexta das 07:30 às 18:00 e aos sábados das 08:00 às 12:00, pelo telefone e WhatsApp (67) 99241-4371.</p>
</div></section>
''',
))

# ============================================================ CONTATO
PAGINAS.append(dict(
 slug="contato", migalha="Contato",
 title="Contato | Orçamento de Aluguel de Container em Campo Grande - MS",
 desc="Peça orçamento de aluguel de container em Campo Grande - MS pelo WhatsApp (67) 99241-4371 ou pelo formulário. Rua Pernambuco, 1396, Monte Castelo.",
 h1="Fale com a gente",
 lead="O caminho mais rápido é o WhatsApp. Se preferir, deixe seus dados no formulário que retornamos no próximo horário de atendimento.",
 hero_img=("aluguel-container-escritorio-campo-grande-ms", 1200, 903, "Container para aluguel em Campo Grande MS"),
 placa=[("WhatsApp", "(67) 99241-4371"), ("Seg a sex", "07:30–18:00"), ("Sábado", "08:00–12:00"), ("Bairro", "Monte Castelo")],
 placa_tit="Atendimento",
 sem_cta=True,
 corpo='''
<section><div class="wrap duas">
<div>
<h2>Formulário de orçamento</h2>
<form class="form" action="https://formsubmit.co/luismosko@gmail.com" method="POST">
<input type="hidden" name="_subject" value="Novo orçamento - aluguelcontainer.com.br">
<input type="hidden" name="_next" value="https://aluguelcontainer.com.br/obrigado">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<div class="lin"><div><label for="f-nome">Nome</label><input id="f-nome" name="nome" required autocomplete="name"></div>
<div><label for="f-tel">WhatsApp</label><input id="f-tel" name="whatsapp" type="tel" required autocomplete="tel" inputmode="tel"></div></div>
<div class="lin"><div><label for="f-tipo">Container</label><select id="f-tipo" name="tipo" required>
<option value="">Selecione</option><option>Escritório</option><option>Almoxarifado</option><option>Banheiro</option><option>Alojamento</option><option>Marítimo 20/40 pés</option><option>Canteiro completo</option><option>Compra</option><option>Não sei, quero orientação</option></select></div>
<div><label for="f-cid">Cidade / bairro de entrega</label><input id="f-cid" name="local" required></div></div>
<label for="f-per">Por quanto tempo?</label><select id="f-per" name="periodo"><option>1 a 3 meses</option><option>3 a 6 meses</option><option>6 a 12 meses</option><option>Mais de 1 ano</option><option>Ainda não sei</option></select>
<label for="f-msg">Detalhes (acesso, energia, quantidade)</label><textarea id="f-msg" name="mensagem"></textarea>
<button class="btn btn-wpp" type="submit">Enviar pedido de orçamento</button>
<small>Usamos seus dados só para responder este pedido. Veja a <a href="/politica-de-privacidade">política de privacidade</a>.</small>
</form></div>
<div>
<h2>WhatsApp e telefone</h2>
<p>Mande o tipo de container, o endereço e o período. Se puder, uma foto do local de instalação.</p>
<div class="acoes"><a class="btn btn-wpp" href="{WA}" target="_blank" rel="noopener">Chamar no WhatsApp</a></div>
<h2 style="margin-top:1.4em">Endereço</h2>
<p>Rua Pernambuco, 1396<br>Monte Castelo · Campo Grande - MS<br>CEP 79010-040</p>
<h2 style="margin-top:1.4em">Dados da empresa</h2>
<p>TRM Serviços LTDA<br>CNPJ 58.169.089/0001-02</p>
</div>
</div></section>
''',
 faq=[
  ("Qual o jeito mais rápido de receber orçamento?", "Pelo WhatsApp (67) 99241-4371, informando o tipo de container, o endereço de entrega e o período de uso."),
  ("Vocês atendem aos sábados?", "Sim, das 08:00 às 12:00. De segunda a sexta, das 07:30 às 18:00."),
  ("Posso visitar o pátio?", "Pode, com horário combinado pelo WhatsApp. Estamos na Rua Pernambuco, 1396, no Monte Castelo."),
  ("Atendem órgão público?", "Sim. Enviamos proposta no formato solicitado e participamos de licitações de locação de container."),
  ("Quais informações devo mandar?", "Tipo de container, endereço ou cidade de entrega, tempo estimado de uso e, se possível, uma foto do local e do acesso."),
  ("Vocês emitem nota fiscal?", "Sim, a locação é faturada pela TRM Serviços LTDA, CNPJ 58.169.089/0001-02."),
  ("Atendem fora do horário comercial?", "Mensagens enviadas fora do horário são respondidas no próximo período de atendimento."),
 ],
))

# ============================================================ LEGAIS / UTILITÁRIAS
PAGINAS.append(dict(
 slug="politica-de-privacidade", migalha="Política de privacidade", sem_cta=True,
 title="Política de Privacidade | Aluguel Container",
 desc="Como a Aluguel Container (TRM Serviços LTDA) trata os dados enviados pelo site, em conformidade com a LGPD.",
 corpo='''
<section class="sec-branca"><div class="wrap texto">
<nav class="trilha" aria-label="Você está em"><a href="/">Início</a><span>/</span>Política de privacidade</nav>
<h1>Política de privacidade</h1>
<p>Esta política explica como a TRM Serviços LTDA (CNPJ 58.169.089/0001-02), responsável pelo site aluguelcontainer.com.br, trata dados pessoais, conforme a Lei 13.709/2018 (LGPD).</p>
<h2>Dados coletados</h2>
<p>Coletamos apenas o que você envia pelo formulário ou pelo WhatsApp: nome, telefone, local de entrega, tipo de container, período e a mensagem que você escrever. O site não usa cookies de rastreamento nem ferramentas de publicidade.</p>
<h2>Finalidade</h2>
<p>Os dados são usados exclusivamente para responder ao pedido de orçamento e, se houver contratação, para elaborar e executar o contrato de locação ou venda.</p>
<h2>Compartilhamento</h2>
<p>Não vendemos nem cedemos dados. O formulário é processado pelo serviço FormSubmit, que encaminha a mensagem para o nosso e-mail. Dados de contrato podem ser compartilhados com contabilidade e órgãos fiscais quando exigido por lei.</p>
<h2>Seus direitos</h2>
<p>Você pode pedir acesso, correção ou exclusão dos seus dados a qualquer momento pelo WhatsApp (67) 99241-4371.</p>
<h2>Retenção</h2>
<p>Pedidos de orçamento sem contratação são descartados quando deixam de ser necessários. Dados de contratos são mantidos pelo prazo exigido pela legislação fiscal.</p>
</div></section>
''',
))
PAGINAS.append(dict(
 slug="termos-de-uso", migalha="Termos de uso", sem_cta=True,
 title="Termos de Uso | Aluguel Container",
 desc="Termos de uso do site aluguelcontainer.com.br.",
 corpo='''
<section class="sec-branca"><div class="wrap texto">
<nav class="trilha" aria-label="Você está em"><a href="/">Início</a><span>/</span>Termos de uso</nav>
<h1>Termos de uso</h1>
<p>O site aluguelcontainer.com.br é mantido pela TRM Serviços LTDA (CNPJ 58.169.089/0001-02) e tem caráter informativo.</p>
<h2>Informações do site</h2>
<p>Medidas, configurações e imagens são de referência e podem variar conforme o modelo disponível. Preço, prazo de entrega e condições só valem depois de confirmados no orçamento e no contrato.</p>
<h2>Contratação</h2>
<p>A locação ou venda é regida pelo contrato assinado entre as partes, que prevalece sobre qualquer informação do site.</p>
<h2>Propriedade intelectual</h2>
<p>Textos e imagens do site não podem ser reproduzidos sem autorização.</p>
<h2>Contato</h2>
<p>Dúvidas: (67) 99241-4371 · Rua Pernambuco, 1396, Monte Castelo, Campo Grande - MS.</p>
</div></section>
''',
))
PAGINAS.append(dict(
 slug="obrigado", migalha="Obrigado", sem_cta=True, noindex=True,
 title="Pedido recebido | Aluguel Container", desc="Pedido de orçamento recebido.",
 corpo='''
<section class="sec-branca"><div class="wrap texto" style="min-height:45vh">
<h1>Pedido recebido</h1>
<p>Obrigado. Seu pedido de orçamento chegou e respondemos no próximo horário de atendimento (seg a sex 07:30–18:00, sáb 08:00–12:00).</p>
<p>Com pressa? Chame no WhatsApp:</p>
<div class="acoes"><a class="btn btn-wpp" href="{WA}" target="_blank" rel="noopener">Chamar no WhatsApp</a> <a class="btn btn-linha" href="/">Voltar ao início</a></div>
</div></section>
''',
))
PAGINAS.append(dict(
 slug="404", arquivo="404.html", migalha="Página não encontrada", sem_cta=True, noindex=True,
 title="Página não encontrada | Aluguel Container", desc="Página não encontrada.",
 corpo='''
<section class="sec-branca"><div class="wrap texto" style="min-height:45vh">
<h1>Essa página não existe</h1>
<p>O endereço pode ter mudado com o novo site. Veja os tipos de container para aluguel:</p>
<ul class="lista">
<li><a href="/aluguel-de-container-escritorio">Container escritório</a></li>
<li><a href="/aluguel-de-container-almoxarifado">Container almoxarifado</a></li>
<li><a href="/aluguel-de-container-para-obra">Container para obra</a></li>
<li><a href="/aluguel-de-container-banheiro">Container banheiro</a></li>
<li><a href="/aluguel-de-container-alojamento">Container alojamento</a></li>
<li><a href="/aluguel-de-container-maritimo">Container marítimo</a></li>
</ul>
<div class="acoes"><a class="btn btn-linha" href="/">Ir para o início</a></div>
</div></section>
''',
))
