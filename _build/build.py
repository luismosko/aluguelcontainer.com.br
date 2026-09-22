#!/usr/bin/env python3
# aluguelcontainer.com.br — gerador estático v1.0.0
# Uso: python3 _build/build.py  -> escreve HTML em public/
# Edite o conteúdo em _build/paginas.py; cabeçalho/rodapé/schema ficam aqui.
import json, os, html, datetime
from urllib.parse import quote
from paginas import PAGINAS, EMPRESA

VERSAO = "1.0.0"
RAIZ = os.path.join(os.path.dirname(__file__), "..", "public")
URL = "https://aluguelcontainer.com.br"
HOJE = datetime.date.today().isoformat()

def wa(msg="Olá! Vim pelo site Aluguel Container e quero um orçamento."):
    return f"https://wa.me/{EMPRESA['wa']}?text={quote(msg)}"

ICO_WPP = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.8.4 3.5 3.5 0 0 0-1.1 2.6 6 6 0 0 0 1.3 3.2 13.8 13.8 0 0 0 5.3 4.7c2 .8 2.7.9 3.7.8.6-.1 1.8-.8 2.1-1.5s.3-1.3.2-1.5-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.3-1.7a11.8 11.8 0 0 0 5.6 1.4 11.8 11.8 0 0 0 8.4-20.1z"/></svg>'

LOGO = '''<svg width="46" height="30" viewBox="0 0 46 30" aria-hidden="true"><rect x="1" y="3" width="44" height="24" rx="1.5" fill="#22578F" stroke="#C9D1D8" stroke-width="1.5"/><g stroke="#C9D1D8" stroke-opacity=".55" stroke-width="1.6"><path d="M8 7v16M13 7v16M18 7v16M23 7v16M28 7v16M33 7v16M38 7v16"/></g><rect x="36.5" y="9" width="6" height="12" fill="#E8702A"/></svg>'''

MENU = [("/", "Início"), ("/como-funciona-o-aluguel", "Como funciona"),
        ("/aluguel-de-container-escritorio", "Escritório"), ("/aluguel-de-container-almoxarifado", "Almoxarifado"),
        ("/aluguel-de-container-para-obra", "Obra"), ("/sobre", "Sobre"), ("/contato", "Contato")]

def cabecalho(slug):
    itens = "".join(f'<a href="{h}"{" aria-current=page" if h.strip("/")==slug else ""}>{t}</a>' for h, t in MENU)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="topo"><div class="wrap">
<a class="marca" href="/" aria-label="Aluguel Container, página inicial">{LOGO}<span>Aluguel Container<small>Campo Grande · MS</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
<nav class="menu" id="menu" aria-label="Principal">{itens}<a class="tel" href="tel:+55{EMPRESA['tel_num']}">{EMPRESA['tel']}</a></nav>
</div></header>'''

def rodape():
    e = EMPRESA
    return f'''<footer class="rodape"><div class="wrap"><div class="cols">
<div><h2>Aluguel Container</h2><p>Locação de container para escritório, almoxarifado, obra, banheiro e alojamento em Campo Grande e no interior de Mato Grosso do Sul.</p></div>
<div><h2>Aluguel</h2><ul>
<li><a href="/aluguel-de-container-escritorio">Container escritório</a></li>
<li><a href="/aluguel-de-container-almoxarifado">Container almoxarifado</a></li>
<li><a href="/aluguel-de-container-para-obra">Container para obra</a></li>
<li><a href="/aluguel-de-container-banheiro">Container banheiro</a></li>
<li><a href="/aluguel-de-container-alojamento">Container alojamento</a></li>
<li><a href="/aluguel-de-container-maritimo">Container marítimo</a></li></ul></div>
<div><h2>Empresa</h2><ul>
<li><a href="/como-funciona-o-aluguel">Como funciona</a></li>
<li><a href="/venda-de-container">Venda de container</a></li>
<li><a href="/sobre">Sobre</a></li><li><a href="/contato">Contato</a></li></ul></div>
<div><h2>Atendimento</h2><address>
<a href="tel:+55{e['tel_num']}">{e['tel']}</a> (telefone e WhatsApp)<br>
{e['rua']}, {e['bairro']}<br>{e['cidade']}/{e['uf']} · CEP {e['cep']}<br>
Seg a sex 07:30–18:00 · Sáb 08:00–12:00</address></div>
</div>
<div class="base"><span>© {datetime.date.today().year} Aluguel Container · {e['razao']} · CNPJ {e['cnpj']}</span>
<span><a href="/politica-de-privacidade">Privacidade</a> · <a href="/termos-de-uso">Termos de uso</a></span></div>
</div></footer>
<a class="wpp-fixo" href="{wa()}" target="_blank" rel="noopener" aria-label="Chamar no WhatsApp"><span style="color:#fff">{ICO_WPP.replace('20','28',2)}</span></a>
<script>
(function(){{var b=document.querySelector('.menu-btn'),m=document.getElementById('menu');if(!b)return;
b.addEventListener('click',function(){{var a=m.classList.toggle('aberto');b.setAttribute('aria-expanded',a)}});}})();
</script>'''

def negocio():
    e = EMPRESA
    return {"@type": "LocalBusiness", "@id": URL + "/#empresa", "name": "Aluguel Container",
            "legalName": e["razao"], "taxID": e["cnpj"], "url": URL + "/", "telephone": "+55" + e["tel_num"],
            "image": URL + "/img/aluguel-container-escritorio-campo-grande-ms.webp", "priceRange": "$$",
            "address": {"@type": "PostalAddress", "streetAddress": e["rua"], "addressLocality": e["cidade"],
                        "addressRegion": e["uf"], "postalCode": e["cep"], "addressCountry": "BR"},
            "geo": {"@type": "GeoCoordinates", "latitude": e["lat"], "longitude": e["lng"]},
            "areaServed": [{"@type": "City", "name": "Campo Grande"}, {"@type": "State", "name": "Mato Grosso do Sul"}],
            "openingHoursSpecification": [
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "07:30", "closes": "18:00"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00"}]}

def schema(p):
    g = [negocio()]
    if p["slug"]:
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": URL + "/"},
            {"@type": "ListItem", "position": 2, "name": p["migalha"], "item": URL + "/" + p["slug"]}]})
    if p.get("servico"):
        g.append({"@type": "Service", "name": p["servico"], "serviceType": "Locação de container",
                  "provider": {"@id": URL + "/#empresa"}, "areaServed": {"@type": "State", "name": "Mato Grosso do Sul"},
                  "url": URL + "/" + p["slug"]})
    if p.get("faq"):
        g.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":"))

def bloco_faq(p):
    if not p.get("faq"): return ""
    itens = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in p["faq"])
    return f'<section class="sec-branca"><div class="wrap"><h2>{p.get("faq_titulo","Perguntas frequentes")}</h2><div class="faq">{itens}</div></div></section>'

def cta(p):
    msg = p.get("wa_msg", "Olá! Vim pelo site Aluguel Container e quero um orçamento.")
    return f'''<section class="corrugado"><div class="wrap">
<h2>{p.get("cta_titulo","Peça o orçamento do seu container")}</h2>
<p>Mande pelo WhatsApp o tipo de container, o endereço de entrega e por quanto tempo vai precisar. Com isso já dá para calcular locação e frete.</p>
<div class="acoes"><a class="btn btn-wpp" href="{wa(msg)}" target="_blank" rel="noopener">{ICO_WPP} Orçamento pelo WhatsApp</a>
<a class="btn btn-linha" style="color:#fff" href="tel:+55{EMPRESA['tel_num']}">Ligar {EMPRESA['tel']}</a></div>
</div></section>'''

def placa(p):
    if not p.get("placa"): return ""
    linhas = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in p["placa"])
    return f'<div class="placa" role="note" aria-label="Resumo da locação"><span class="rb"></span><div class="tit"><span>{p.get("placa_tit","Locação")}</span><b>AC-MS</b></div><dl>{linhas}</dl></div>'

def hero(p):
    if not p.get("hero_img"): return ""
    msg = p.get("wa_msg", "Olá! Vim pelo site Aluguel Container e quero um orçamento.")
    trilha = "" if not p["slug"] else f'<nav class="trilha" aria-label="Você está em"><a href="/">Início</a><span>/</span>{p["migalha"]}</nav>'
    img, w, h, alt = p["hero_img"]
    srcset = ""
    if p["slug"] == "":
        srcset = f' srcset="/img/{img}-720.webp 720w, /img/{img}.webp 1200w" sizes="(max-width:860px) 92vw, 560px"'
    return f'''<section class="hero" style="padding:0"><div class="wrap">
<div>{trilha}<h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p>
<div class="acoes"><a class="btn btn-wpp" href="{wa(msg)}" target="_blank" rel="noopener">{ICO_WPP} Pedir orçamento</a>
<a class="btn btn-linha" href="tel:+55{EMPRESA['tel_num']}">{EMPRESA['tel']}</a></div></div>
<div class="hero-foto"><img src="/img/{img}.webp"{srcset} width="{w}" height="{h}" alt="{alt}" fetchpriority="high">{placa(p)}</div>
</div></section>'''

def montar(p):
    canon = URL + "/" + p["slug"]
    pre = f'<link rel="preload" as="image" href="/img/{p["hero_img"][0]}.webp">' if p.get("hero_img") and p["slug"] else ""
    if p["slug"] == "" and p.get("hero_img"):
        i = p["hero_img"][0]
        pre = f'<link rel="preload" as="image" href="/img/{i}.webp" imagesrcset="/img/{i}-720.webp 720w, /img/{i}.webp 1200w" imagesizes="(max-width:860px) 92vw, 560px">'
    og_img = URL + "/img/" + (p["hero_img"][0] if p.get("hero_img") else "aluguel-container-escritorio-campo-grande-ms") + ".webp"
    robots = '<meta name="robots" content="noindex">' if p.get("noindex") else ""
    corpo = p["corpo"].replace("{WA}", wa(p.get("wa_msg", "Olá! Vim pelo site Aluguel Container e quero um orçamento.")))
    return f'''<!DOCTYPE html>
<!-- aluguelcontainer.com.br v{VERSAO} · gerado por _build/build.py em {HOJE} -->
<html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{canon}">{robots}
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Aluguel Container">
<meta property="og:title" content="{p["title"]}"><meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{og_img}">
<meta name="theme-color" content="#14212F">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/barlow-condensed-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/barlow-400.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/site.css?v={VERSAO}">
<script type="application/ld+json">{schema(p)}</script>
</head><body>
{cabecalho(p["slug"])}
<main id="conteudo">
{hero(p)}
{corpo}
{bloco_faq(p)}
{"" if p.get("sem_cta") else cta(p)}
</main>
{rodape()}
</body></html>
'''

def main():
    urls = []
    for p in PAGINAS:
        nome = p.get("arquivo") or ((p["slug"] or "index") + ".html")
        with open(os.path.join(RAIZ, nome), "w", encoding="utf-8") as f:
            f.write(montar(p))
        if not p.get("noindex"):
            urls.append((URL + "/" + p["slug"], "1.0" if p["slug"] == "" else "0.8"))
        print("ok", nome)
    sm = "".join(f"<url><loc>{u}</loc><lastmod>{HOJE}</lastmod><priority>{pr}</priority></url>" for u, pr in urls)
    with open(os.path.join(RAIZ, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')

if __name__ == "__main__":
    main()
