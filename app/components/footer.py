import reflex as rx
from app.state import State


def footer_location_card(location: dict) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            location["country"], class_name="font-bold text-gray-800 mb-3 text-base"
        ),
        rx.foreach(
            location["address_lines"],
            lambda line: rx.el.p(
                line, class_name="text-sm text-gray-600 leading-relaxed"
            ),
        ),
        class_name="w-full",
    )


def footer_link_item(item: dict) -> rx.Component:
    return rx.el.a(
        item["text"],
        href=item["href"],
        class_name="text-sm text-gray-600 hover:text-orange-600 transition-colors",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Innovación para el mundo.",
                        class_name="font-semibold text-gray-800 mb-4",
                    ),
                    rx.el.div(
                        rx.foreach(State.socials, social_icon_footer),
                        class_name="flex items-center gap-4",
                    ),
                    rx.el.p(
                        "© 2024, Grupo Mirgor", class_name="text-xs text-gray-500 mt-8"
                    ),
                    class_name="w-full md:w-1/4 mb-8 md:mb-0",
                ),
                rx.el.div(
                    rx.foreach(State.locations, footer_location_card),
                    class_name="w-full md:w-2/4 grid grid-cols-2 lg:grid-cols-3 gap-8",
                ),
                rx.el.div(
                    rx.foreach(State.footer_links, footer_link_item),
                    class_name="w-full md:w-1/4 flex flex-col items-start md:items-end gap-3",
                ),
                class_name="flex flex-col md:flex-row justify-between gap-8",
            ),
            class_name="container mx-auto px-4 lg:px-6 py-12",
        ),
        class_name="bg-gray-100 border-t border-gray-200",
    )


def social_icon_footer(item: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=item["icon"], class_name="h-6 w-6"),
        href=item["href"],
        class_name="text-gray-500 hover:text-orange-600 transition-colors p-2 bg-gray-200 rounded-full",
    )