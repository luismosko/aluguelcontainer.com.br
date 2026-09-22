# aluguelcontainer.com.br — v1.0.0

Site estático de **aluguel de container** (marca Aluguel Container · TRM Serviços LTDA).
Site-irmão do campograndecontainers.com.br, com **texto 100% próprio** (não copiar conteúdo de lá: conteúdo duplicado derruba os dois no Google).

## Estrutura
- `public/` → o que vai para o Cloudflare Pages (output dir). Nada fora daqui é publicado.
- `_build/paginas.py` → **conteúdo** de todas as páginas (texto, FAQ, placa-resumo).
- `_build/build.py` → template (topo, rodapé, schema LocalBusiness/Service/FAQPage/Breadcrumb, sitemap).
- `public/site.css` → estilo único. Identidade: azul-container, Barlow Condensed + Barlow, "placa de identificação" com rebites.

## Editar
1. Altere `_build/paginas.py` (ou `build.py` para topo/rodapé).
2. `python3 _build/build.py` → regrava `public/*.html` e `sitemap.xml`.
3. Bump `VERSAO` em build.py (o `?v=` do CSS vai junto). Commit + push = deploy.

## Regras de conteúdo
Sem prazo de entrega em horas · sem depoimentos inventados · sem "frota própria" · alojamento só 6 m, sem citar beliche/armário · mínimo 30 dias · FAQ ≥ 7 perguntas por página de serviço.

## Formulário
FormSubmit → luismosko@gmail.com. O 1º envio a partir do domínio novo dispara e-mail de ativação do FormSubmit (clicar para liberar).
