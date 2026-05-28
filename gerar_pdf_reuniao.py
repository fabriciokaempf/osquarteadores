from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# Paleta do brandbook
CARBON   = colors.HexColor("#1A1714")
BRANCO   = colors.HexColor("#EDE4D3")
VERMELHO = colors.HexColor("#8B2A1A")
VERDE    = colors.HexColor("#3F4E2E")
COURO    = colors.HexColor("#6E4B2F")
BRANCO_PURO = colors.white

OUTPUT = r"C:\Users\nasci\Documents\Kaempf Business\Jobs 2026\Os Quarteadores\OsQuarteadores_ReuniaoDigital.pdf"

W, H = A4  # 595 x 842 pts
ML = MR = 2.5 * cm
MT = 0
MB = 1.8 * cm

def draw_page(c, w, h):
    # ---- Faixa superior ----
    c.setFillColor(CARBON)
    c.rect(0, h - 3.8*cm, w, 3.8*cm, fill=1, stroke=0)

    # Titulo principal
    c.setFillColor(BRANCO)
    c.setFont("Times-Bold", 26)
    c.drawCentredString(w/2, h - 2.0*cm, "OS QUARTEADORES")

    # Subtitulo
    c.setFillColor(VERMELHO)
    c.setFont("Times-Roman", 11)
    c.drawCentredString(w/2, h - 2.8*cm, "Coletivo da canção nativa  |  Onde a canção nasce")

    # Linha fina vermelho abaixo da faixa
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(2.5)
    c.line(0, h - 3.8*cm, w, h - 3.8*cm)

    # ---- Bloco de identificacao ----
    y = h - 4.9*cm
    c.setFillColor(COURO)
    c.setFont("Times-Roman", 9)
    c.drawString(ML, y, "DOCUMENTO PARA PAUTA DE REUNIÃO")
    c.drawRightString(w - MR, y, "28 de maio de 2026")

    y -= 0.5*cm
    c.setFillColor(CARBON)
    c.setFont("Times-Roman", 9)
    c.drawString(ML, y, "Apresentado por: Fabricio")
    c.drawRightString(w - MR, y, "Para: Sr. Heraclides do Nascimento, Presidente 2026")

    y -= 0.45*cm
    c.setFillColor(COURO)
    c.setFont("Times-Italic", 9)
    c.drawString(ML, y, "Grupo Os Quarteadores")

    # Linha separadora
    y -= 0.4*cm
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(0.8)
    c.line(ML, y, w - MR, y)

    # ---- Secao: Contexto ----
    y -= 1.0*cm
    y = section_title(c, "O que está sendo feito", y, w)
    y -= 0.45*cm

    texto_intro = (
        "Fabricio iniciou a construção da presença digital de Os Quarteadores. "
        "O trabalho está organizado em três entregas já concluídas e um projeto em andamento."
    )
    y = texto(c, texto_intro, y, w, size=10.5)

    # ---- 3 colunas de entregas ----
    y -= 0.7*cm
    box_h = 4.2*cm
    bw = (w - ML - MR - 0.4*cm) / 3
    boxes = [
        ("BENCHMARKING",
         "Mapeamento dos 5 grandes festivais nativistas (Musicanto, Califórnia, "
         "Sapecada, Tafona, Tertúlia). Lacunas e oportunidades estratégicas para o coletivo."),
        ("BRANDBOOK",
         "Manifesto, posicionamento, tom de voz, paleta de cores, tipografia e "
         "pilares de conteúdo. Conceito visual ancorado no V dos pássaros em formação."),
        ("REPOSITÓRIO ONLINE",
         "Documentos publicados no GitHub. Site publicado via GitHub Pages, "
         "acessível publicamente. URL disponível no rodapé deste documento."),
    ]
    for i, (titulo_box, corpo_box) in enumerate(boxes):
        bx = ML + i * (bw + 0.2*cm)
        by = y - box_h
        # fundo
        c.setFillColor(BRANCO)
        c.setStrokeColor(VERMELHO)
        c.setLineWidth(0.6)
        c.roundRect(bx, by, bw, box_h, 3, fill=1, stroke=1)
        # titulo da box
        c.setFillColor(VERMELHO)
        c.setFont("Times-Bold", 8.5)
        c.drawString(bx + 0.3*cm, by + box_h - 0.55*cm, titulo_box)
        # linha fina sob titulo da box
        c.setStrokeColor(VERMELHO)
        c.setLineWidth(0.3)
        c.line(bx + 0.3*cm, by + box_h - 0.75*cm, bx + bw - 0.3*cm, by + box_h - 0.75*cm)
        # corpo da box
        c.setFillColor(CARBON)
        c.setFont("Times-Roman", 8)
        wrap_box(c, corpo_box, bx + 0.3*cm, by + box_h - 1.05*cm, bw - 0.6*cm, 8.5)

    y = y - box_h - 0.9*cm

    # ---- Secao: Site oficial ----
    y = section_title(c, "Projeto a viabilizar: site oficial do coletivo", y, w)
    y -= 0.45*cm

    c.setFillColor(VERDE)
    c.setFont("Times-Bold", 10)
    c.drawString(ML, y, "ENTREGA VOLUNTÁRIA  |  Valor de mercado estimado: R$ 1.600,00  |  Será entregue gratuitamente ao coletivo")

    y -= 0.65*cm
    texto_site = (
        "Fabricio desenvolverá o site oficial de Os Quarteadores como contribuição voluntária ao coletivo "
        "e à tradição da Quarteada. O site terá página de apresentação do coletivo e da Quarteada, "
        "cancioneiro (catálogo de canções nascidas no encontro), histórico de edições, informações para "
        "participação e integração com redes sociais."
    )
    y = texto(c, texto_site, y, w, size=10.5)

    y -= 0.4*cm
    c.setFillColor(COURO)
    c.setFont("Times-Italic", 9.5)
    c.drawString(ML, y, "Custo único para o coletivo: registro do domínio próprio, estimado em até R$ 100,00 por dois anos de uso e posse.")

    # ---- Secao: Instagram ----
    y -= 0.8*cm
    y = section_title(c, "Instagram", y, w)
    y -= 0.45*cm

    texto_ig = (
        "Perfil atual: @osquarteadores. Está em avaliação a criação de um novo perfil com identidade "
        "visual alinhada ao brandbook. Opções priorizadas: @quarteadores ou @aquarteada. "
        "A decisão será tomada pelo grupo."
    )
    y = texto(c, texto_ig, y, w, size=10.5)

    # ---- Linha de rodape ----
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(0.8)
    c.line(ML, MB + 0.8*cm, w - MR, MB + 0.8*cm)

    c.setFillColor(COURO)
    c.setFont("Times-Roman", 8)
    c.drawCentredString(w/2, MB + 0.3*cm,
        "fabriciokaempf.github.io/osquarteadores   |   instagram.com/osquarteadores")

def section_title(c, text, y, w):
    c.setFillColor(VERMELHO)
    c.setFont("Times-Bold", 11.5)
    c.drawString(ML, y, text.upper())
    y -= 0.4*cm
    c.setStrokeColor(VERMELHO)
    c.setLineWidth(0.4)
    c.line(ML, y, w - MR, y)
    return y

def texto(c, text, y, w, size=10.5):
    from textwrap import wrap
    c.setFillColor(CARBON)
    c.setFont("Times-Roman", size)
    max_w = w - ML - MR
    # approx chars per line
    chars_per_line = int(max_w / (size * 0.48))
    linhas = wrap(text, chars_per_line)
    leading = size * 1.75
    for linha in linhas:
        c.drawString(ML, y, linha)
        y -= leading
    return y

def wrap_box(c, text, x, y, bw, size=8):
    from textwrap import wrap
    chars = int(bw / (size * 0.48))
    linhas = wrap(text, chars)
    leading = size * 1.7
    for linha in linhas:
        if y < 1*cm:
            break
        c.drawString(x, y, linha)
        y -= leading

def main():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Os Quarteadores, Presenca Digital, Reuniao 2026-05-28")
    c.setAuthor("Fabricio Kaempf")
    c.setSubject("Pauta de Reuniao, Presenca Digital")
    draw_page(c, W, H)
    c.save()
    print(f"PDF gerado: {OUTPUT}")

if __name__ == "__main__":
    main()
