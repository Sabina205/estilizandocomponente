import flet as ft

name = "TextField Básico"

def example(page: ft.Page):
    def button_clicked(e):
        t.value = f"os elementos das caixas de textos são: '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}'."
        t.update()

    def estilo_tb2(e):
        tb2.border_width = int(border_dropdown.value)
        tb2.text_style = ft.TextStyle(size=int(size_dropdown.value), color=color_dropdown.value)
        tb2.update()

    def estilo_tb4(e):
        tb4.border_width = int(border_dropdown.value)
        tb4.text_style = ft.TextStyle(size=int(size_dropdown.value), color=color_dropdown.value)
        tb4.update()

 
    tb1 = ft.TextField(label="Escreva seu priemiro nome", read_only=True, value="Primeiro nome")
    tb2 = ft.TextField(label="Campo de texto editavel", border_width=1, text_style=ft.TextStyle(size=12, color="black"))
    tb3 = ft.TextField(label="Escreva seu sobrenome", read_only=True, value="Sobrenome")
    tb4 = ft.TextField(label="Campo de texto editavel", border_width=1, text_style=ft.TextStyle(size=12, color="black"))

 
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    t = ft.Text()

    color_dropdown = ft.Dropdown(
        label="Cor do texto:",
        options=[
            ft.dropdown.Option("black"),
            ft.dropdown.Option("pink"),
            ft.dropdown.Option("blue"),
        ],
        value="black",
        on_change=lambda e: [estilo_tb2(e), estilo_tb4(e)],
    )

    size_dropdown = ft.Dropdown(
        label="Tamanho do texto:",
        options=[
            ft.dropdown.Option("12"),
            ft.dropdown.Option("16"),
            ft.dropdown.Option("20"),
        ],
        value="12",
        on_change=lambda e: [estilo_tb2(e), estilo_tb4(e)],
    )

    border_dropdown = ft.Dropdown(
        label="Espessura da borda:",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("5"),
        ],
        value="1",
        on_change=lambda e: [estilo_tb2(e), estilo_tb4(e)],
    )

    page.add(
        ft.Column(
            controls=[
                tb1,tb2,tb3,tb4,color_dropdown,size_dropdown,border_dropdown,b,t,
            ]
        )
    )

ft.app(target=example)
