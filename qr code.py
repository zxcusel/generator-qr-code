import flet as ft
#pip install flet
import qrcode
#pip install qrcode
def main(page: ft.Page):
    page.title = "QR-code"
    page.window_width=500
    page.window_height=200
    def b_click(e):
        img = qrcode.make(tb.value)
        img.save("site.png")
        l.src="site.png"
        page.remove(t,tb,b)
        page.add(l)
        page.window_width=200
        page.window_height=215
        page.update()

    t = ft.Text("Generate QR-code")
    tb = ft.TextField(label="link", width=500,)
    l=ft.Image(src="")
    b = ft.ElevatedButton("Generate", on_click=b_click)
    page.add(t,tb,b)

ft.app(target=main)