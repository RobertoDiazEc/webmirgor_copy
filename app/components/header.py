import reflex as rx
from app.state import State


def nav_item(item: dict) -> rx.Component:
    return rx.el.a(
        item["text"],
        href=item["href"],
        class_name="text-sm font-medium text-gray-100 hover:text-white transition-colors",
    )


def social_icon(item: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=item["icon"], class_name="h-5 w-5"),
        href=item["href"],
        class_name="text-gray-300 hover:text-white transition-colors",
    )


def mobile_nav_item(item: dict) -> rx.Component:
    return rx.el.a(
        item["text"],
        href=item["href"],
        on_click=State.toggle_mobile_menu,
        class_name="text-2xl font-bold text-white hover:text-orange-400 transition-colors py-2 text-center",
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("locate-fixed", class_name="h-4 w-4 mr-2 text-gray-300"),
                rx.el.span(
                    "19th Ave New York, NY 95822, USA",
                    class_name="text-xs text-gray-300",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.foreach(State.socials, social_icon),
                rx.el.div(
                    rx.el.a(
                        "ES",
                        href="#",
                        class_name="text-xs font-bold text-gray-300 hover:text-white transition-colors",
                    ),
                    rx.el.span("|", class_name="text-xs text-gray-400 mx-1"),
                    rx.el.a("EN", href="#", class_name="text-xs font-bold text-white"),
                    class_name="flex items-center",
                ),
                rx.el.button(
                    "Join Now",
                    class_name="bg-white/10 text-white text-xs font-semibold px-4 py-1.5 rounded-md hover:bg-white/20 transition-colors",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="container mx-auto px-4 lg:px-6 py-2 flex justify-between items-center border-b border-white/10",
        ),
        rx.el.div(
            rx.el.a(
                rx.el.h2(
                    "Mirgor",
                    rx.el.span("+", class_name="text-blue-500"),
                    class_name="text-3xl font-bold text-white",
                ),
                href="#",
            ),
            rx.el.nav(
                rx.foreach(State.nav_items, nav_item),
                class_name="hidden md:flex items-center gap-6 lg:gap-8",
            ),
            rx.el.button(
                rx.icon("menu", class_name="h-6 w-6"),
                class_name="md:hidden text-white",
                on_click=State.toggle_mobile_menu,
            ),
            class_name="container mx-auto px-4 lg:px-6 py-4 flex justify-between items-center",
        ),
        rx.cond(
            State.show_mobile_menu,
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("x", class_name="h-8 w-8"),
                        on_click=State.toggle_mobile_menu,
                        class_name="absolute top-8 right-8 text-white",
                    ),
                    rx.el.nav(
                        rx.foreach(State.nav_items, mobile_nav_item),
                        class_name="flex flex-col items-center justify-center h-full gap-6",
                    ),
                    class_name="container mx-auto h-full",
                ),
                class_name="fixed inset-0 bg-black/90 backdrop-blur-md z-50 md:hidden",
            ),
        ),
        class_name="fixed top-0 left-0 right-0 z-20 bg-black/30 backdrop-blur-sm",
    )