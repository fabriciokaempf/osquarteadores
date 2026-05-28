from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from textwrap import wrap

CARBON   = colors.HexColor("#1A1714")
BRANCO   = colors.HexColor("#EDE4D3")
VERMELHO = colors.HexColor("#8B2A1A")
VERDE    = colors.HexColor("#3F4E2E")
COURO    = colors.HexColor("#6E4B2F")
TRIGO    = colors.HexColor("#C49B47")

OUTPUT = r"C:\Users\nasci\Documents\Kaempf Business\Jobs 2026\Os Quarteadores\OsQuarteadores_Brandbook.pdf"

W, H = A4
ML = MR = 2.5 * cm
MB = 1.8 * cm

# ------------------------------------------------------------------ helpers

def bloco_texto(c, text, y, w, size=10, color=CARBON, italic=False, leading_mult=1.75):
    c.setFillColor(color)
    c.setFont("Times-Italic" if italic else "Times-Roman", size)
    usable = w - ML - MR
    chars = int(usable / (size * 0.48))
    linhas = wrap(text, chars)
    leading = size * leading_mult
    for l in linhas:
        c.drawString(ML, y, l)
        y -= leading
    return y

def titulo_secao(c, text, y, w):
    c.setFillColor(VERMELHO)
    c.setFont("Times-Bold", 11)
    c.drawString(ML, y, text.upper())
    y -= 0.38*cm
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(0.4)
    c.line(ML, y, w - MR, y)
    return y

def bullet(c, text, y, w, size=10):
    c.setFillColor(VERMELHO)
    c.setFont("Times-Bold", size)
    c.drawString(ML, y, "•")
    c.setFillColor(CARBON)
    c.setFont("Times-Roman", size)
    usable = w - ML - MR - 0.5*cm
    chars = int(usable / (size * 0.48))
    linhas = wrap(text, chars)
    leading = size * 1.7
    for l in linhas:
        c.drawString(ML + 0.5*cm, y, l)
        y -= leading
    return y - 0.25*cm

def rodape(c, w):
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(0.8)
    c.line(ML, MB + 0.8*cm, w - MR, MB + 0.8*cm)
    c.setFillColor(COURO)
    c.setFont("Times-Roman", 8)
    c.drawCentredString(w/2, MB + 0.3*cm,
        "fabriciokaempf.github.io/osquarteadores   |   instagram.com/osquarteadores")

# ------------------------------------------------------------------ pagina 1

def pagina1(c, w, h):
    # Faixa superior
    c.setFillColor(CARBON)
    c.rect(0, h - 3.8*cm, w, 3.8*cm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Times-Bold", 26)
    c.drawCentredString(w/2, h - 2.0*cm, "OS QUARTEADORES")
    c.setFillColor(VERMELHO)
    c.setFont("Times-Roman", 11)
    c.drawCentredString(w/2, h - 2.8*cm, "Brandbook  |  Identidade do coletivo")
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(2.5)
    c.line(0, h - 3.8*cm, w, h - 3.8*cm)

    y = h - 4.9*cm

    # ---- 1. Essencia ----
    y = titulo_secao(c, "1. Essência", y, w)
    y -= 0.4*cm
    y = bloco_texto(c,
        "Os Quarteadores são um coletivo de homens, compositores, intérpretes e "
        "tradicionalistas que se reúnem uma vez por ano com um único propósito: criar canção nativa. "
        "O encontro chama-se Quarteada. O grupo chama-se Os Quarteadores.",
        y, w, size=10)

    y -= 0.2*cm
    y = bloco_texto(c,
        "Quartear é engatar o próprio cavalo ao do companheiro para vencer um atoleiro, uma ladeira, "
        "uma carga pesada. É ajudar a passar. É revezar a força. É puxar junto. "
        "Os pássaros voam em V pela mesma razão: um abre o vento, os outros seguem, "
        "quando o da frente cansa, outro assume. Ninguém atravessa sozinho.",
        y, w, size=10)

    # ---- 2. Manifesto ----
    y -= 0.7*cm
    y = titulo_secao(c, "2. Manifesto", y, w)
    y -= 0.45*cm

    manifesto = [
        "A gente se ajunta uma vez por ano.",
        "Acende o fogo, escuta o silêncio do campo, e espera o tema chegar.",
        "Quando chega, a roda se forma.",
        "Um abre a frente. Outro pega o vento. A canção vai nascendo no revezamento.",
        "",
        "Não viemos disputar festival. Viemos compor.",
        "Não viemos brilhar. Viemos puxar junto.",
        "Não viemos atrás de palco. Viemos atrás de canção.",
        "",
        "Quarteador é quem engata seu cavalo no do outro pra vencer a ladeira.",
        "Quarteador é quem segura a frente do bando pra que a tropa chegue inteira.",
        "",
        "Nós somos isso. Os Quarteadores.",
    ]
    c.setFillColor(COURO)
    c.setFont("Times-Italic", 9.5)
    leading = 9.5 * 1.65
    for linha in manifesto:
        if linha == "":
            y -= 9.5 * 0.8
        else:
            c.drawString(ML + 0.5*cm, y, linha)
            y -= leading

    # ---- 3. Posicionamento ----
    y -= 0.65*cm
    y = titulo_secao(c, "3. Posicionamento", y, w)
    y -= 0.4*cm

    c.setFillColor(VERMELHO)
    c.setFont("Times-Bold", 11)
    c.drawCentredString(w/2, y, '"Onde a canção nasce."')
    y -= 0.6*cm

    items_pos = [
        ("Categoria", "Coletivo cultural de canção nativa."),
        ("Promessa", "Um lugar de criação, não de competição."),
        ("Diferencial", "Anual, íntimo (cerca de 300 pessoas), com tema lançado e composição em campo. É laboratório, não vitrine."),
        ("Propósito digital", "Não disputar espaço. Fortalecer a excelência do encontro, as amizades que viram querência e as canções que nascem quando a roda se fecha."),
    ]
    for label, val in items_pos:
        c.setFillColor(COURO)
        c.setFont("Times-Bold", 9.5)
        c.drawString(ML, y, label + ":")
        label_w = c.stringWidth(label + ":  ", "Times-Bold", 9.5)
        c.setFillColor(CARBON)
        c.setFont("Times-Roman", 9.5)
        usable = w - ML - MR - label_w
        chars = int(usable / (9.5 * 0.48))
        linhas = wrap(val, chars)
        for i, l in enumerate(linhas):
            if i == 0:
                c.drawString(ML + label_w, y, l)
            else:
                c.drawString(ML + label_w, y, l)
            y -= 9.5 * 1.65
        y -= 2

    rodape(c, w)

# ------------------------------------------------------------------ pagina 2

def pagina2(c, w, h):
    # Faixa superior fina
    c.setFillColor(CARBON)
    c.rect(0, h - 1.4*cm, w, 1.4*cm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Times-Bold", 11)
    c.drawString(ML, h - 0.95*cm, "OS QUARTEADORES")
    c.setFillColor(VERMELHO)
    c.setFont("Times-Roman", 9)
    c.drawRightString(w - MR, h - 0.95*cm, "Brandbook, continuação")
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(2)
    c.line(0, h - 1.4*cm, w, h - 1.4*cm)

    y = h - 2.3*cm

    # ---- Bloco de pertencimento ----
    box_h = 2.0*cm
    bx = ML
    bw = w - ML - MR
    c.setFillColor(CARBON)
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(0.8)
    c.roundRect(bx, y - box_h, bw, box_h, 4, fill=1, stroke=1)

    c.setFillColor(VERMELHO)
    c.setFont("Times-Bold", 9.5)
    c.drawString(bx + 0.4*cm, y - 0.48*cm, "PERTENCIMENTO")

    c.setFillColor(BRANCO)
    c.setFont("Times-Italic", 9)
    frase_pert = (
        "A porteira não está aberta para qualquer um. "
        "Novos membros entram por convite e passam pelo crivo da diretoria e do grupo. "
        "Quem entra, entra porque tem o perfil, o respeito e o propósito que o grupo exige."
    )
    usable = bw - 0.8*cm
    chars = int(usable / (9 * 0.48))
    linhas = wrap(frase_pert, chars)
    ty = y - 0.85*cm
    for l in linhas:
        c.drawString(bx + 0.4*cm, ty, l)
        ty -= 9 * 1.6

    y = y - box_h - 0.8*cm

    # ---- 4. Personalidade ----
    y = titulo_secao(c, "4. Personalidade", y, w)
    y -= 0.4*cm
    y = bloco_texto(c,
        "Como pessoa, Os Quarteadores seria: homem de campo, gente que sabe escutar. "
        "Fala pouco, mas o que fala é certeiro. Respeita quem veio antes, "
        "abre porteira pra quem vem depois. Tem leitura, sem precisar mostrar que sabe. "
        "Bom humor de galpão, sem deboche. Hospitaleiro. Recebe.",
        y, w, size=10)
    y -= 0.3*cm
    cinco = ["Hospitaleiro", "Coletivo", "Criador", "Tradicional", "Discreto"]
    c.setFillColor(COURO)
    c.setFont("Times-Bold", 9)
    c.drawString(ML, y, "Cinco adjetivos:")
    c.setFillColor(CARBON)
    c.setFont("Times-Roman", 9)
    c.drawString(ML + 3.3*cm, y, "  ".join(f"{i+1}. {a}" for i, a in enumerate(cinco)))
    y -= 0.55*cm

    # ---- 5. Tom de voz ----
    y = titulo_secao(c, "5. Tom de voz", y, w)
    y -= 0.4*cm
    tom_items = [
        "Primeira pessoa do plural: nós, a gente. Nunca primeira do singular.",
        "Presente. Frases curtas. Registro tradicional clássico.",
        "Convida, não vende. Mostra, não explica demais.",
        "Humor de galpão quando vier, com generosidade, nunca por cima de ninguém.",
        "Palavras do campo quando a palavra é a certa, não como enfeite.",
    ]
    for item in tom_items:
        y = bullet(c, item, y, w, size=9.5)
    y -= 0.2*cm

    # ---- 6. Identidade visual ----
    y = titulo_secao(c, "6. Identidade visual", y, w)
    y -= 0.45*cm

    # Paleta de cores (swatches visuais)
    c.setFillColor(COURO)
    c.setFont("Times-Bold", 9)
    c.drawString(ML, y, "Paleta:")
    y -= 0.35*cm

    paleta = [
        (CARBON,   "Carbón",       "#1A1714", "Texto, fundos sólidos"),
        (BRANCO,   "Branco lã",    "#EDE4D3", "Fundos neutros"),
        (VERMELHO, "Vermelho pala","#8B2A1A", "Destaque, títulos"),
        (VERDE,    "Verde azevém", "#3F4E2E", "Suporte"),
        (COURO,    "Couro baio",   "#6E4B2F", "Texto secundário"),
    ]
    sw = 1.2*cm
    sh = 0.7*cm
    gap = (w - ML - MR - len(paleta) * sw) / (len(paleta) - 1)
    for i, (cor, nome, hex_val, uso) in enumerate(paleta):
        bx = ML + i * (sw + gap)
        c.setFillColor(cor)
        c.setStrokeColor(COURO)
        c.setLineWidth(0.3)
        c.rect(bx, y - sh, sw, sh, fill=1, stroke=1)
        c.setFillColor(CARBON)
        c.setFont("Times-Bold", 7.5)
        c.drawString(bx, y - sh - 0.38*cm, nome)
        c.setFont("Times-Roman", 7)
        c.drawString(bx, y - sh - 0.7*cm, hex_val)
    y -= sh + 1.1*cm

    # Tipografia
    c.setFillColor(COURO)
    c.setFont("Times-Bold", 9)
    c.drawString(ML, y, "Tipografia:")
    y -= 0.35*cm
    tipo_items = [
        "Display: serifa clássica com presença. Recomendado: Cormorant Garamond ou Source Serif Pro.",
        "Texto corrido: Lora ou Source Serif Pro.",
        "Apoio: manuscrita legível com moderação (Caveat). Nunca fontes western ou góticas.",
    ]
    for item in tipo_items:
        y = bullet(c, item, y, w, size=9.5)
    y -= 0.45*cm

    # Simbolo
    c.setFillColor(COURO)
    c.setFont("Times-Bold", 9)
    c.drawString(ML, y, "Símbolo:")
    y -= 0.4*cm
    y = bloco_texto(c,
        "O V dos pássaros em formação: sete traços diagonais orgânicos formando o V. "
        "Funciona como assinatura, ícone e bordado em pala. "
        "Acompanha a marca tipográfica principal.",
        y, w, size=9.5)
    y -= 0.2*cm

    # ---- 7. Nao fazer ----
    y -= 0.3*cm
    y = titulo_secao(c, "7. O que não fazer", y, w)
    y -= 0.4*cm
    donts = [
        "Estampar bandeira do RS, chimarrão, bota ou esporas como ícones decorativos.",
        "Cair na estética de cartaz de rodeio: gradiente, letras de outline, ouro brilhante.",
        "Usar gauchês forçado, regionalismo pra inglês ver, adjetivos vazios.",
    ]
    for item in donts:
        y = bullet(c, item, y, w, size=9.5)

    rodape(c, w)

# ------------------------------------------------------------------ main

def main():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Os Quarteadores, Brandbook")
    c.setAuthor("Fabricio")
    c.setSubject("Identidade do coletivo")
    pagina1(c, W, H)
    c.showPage()
    pagina2(c, W, H)
    c.save()
    print(f"PDF gerado: {OUTPUT}")

if __name__ == "__main__":
    main()
