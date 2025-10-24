import reflex as rx
from app.state import State


def mvv_card(item: dict) -> rx.Component:
    return rx.el.div(
        rx.icon(tag=item["icon"], class_name="h-10 w-10 text-orange-600 mb-4"),
        rx.el.h3(item["title"], class_name="text-xl font-bold text-gray-800 mb-3"),
        rx.el.p(
            item["description"], class_name="text-sm text-gray-600 leading-relaxed"
        ),
        class_name="bg-white p-6 rounded-lg border border-gray-200 shadow-sm text-center flex flex-col items-center",
    )


def mision_vision_valores() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.foreach(State.mission_vision_values, mvv_card),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 lg:px-6",
        ),
        class_name="py-16 md:py-24 bg-gray-50",
    )