import reflex as rx
from app.state import State
from app.components.header import header
from app.components.hero import hero
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.main(hero(), class_name="pt-[124px]"),
        footer(),
        class_name="font-['Lato'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="orange"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)