from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter,landscape
import report
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import scale
import os

def scale(drawing, scaling_factor):
    """
    scale a reportlab.graphics.shapes.drawing()
    object while maintaining the aspect ratio
    """
    scaling_x = scaling_factor
    scaling_y = scaling_factor

    drawing.width = drawing.minWidth() * scaling_x
    drawing.height = drawing.height * scaling_y
    drawing.scale(scaling_x, scaling_y)
    return drawing

def create_pdf():

    custom_size = (1497 , 1058)
    c = canvas.Canvas("hello_world.pdf", pagesize=landscape(custom_size))
    svg_blue_footer = "./blue-footer.svg"
    svg_blue_header = "./blue-header.svg"
    # png_logo = "./title.png"
    svg_title = "./title.svg"

    blue_footer = svg2rlg(svg_blue_footer )
    scaled_blue_footer = scale(blue_footer, 1.3)
    blue_header = svg2rlg(svg_blue_header)
    scaled_blue_header = scale(blue_header, 1.5)
    title = svg2rlg(svg_title)
    scaled_title = scale(title, 1.4)
    
    renderPDF.draw(scaled_blue_footer, c, 0, 0)
    renderPDF.draw(scaled_blue_header, c, 800, 900)
    renderPDF.draw(scaled_title, c, 210, 550)
    c.drawImage("./citsec.png", 200, 900)

    c.save()

if __name__ == "__main__":
    create_pdf()