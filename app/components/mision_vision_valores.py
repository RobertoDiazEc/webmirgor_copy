import reflex as rx
from app.state import State


def mvv_card(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 bg-cover bg-center",
            style={"backgroundImage": f"url('{item['image']}')"},
        ),
        rx.el.div(class_name="absolute inset-0 bg-black/60"),
        rx.el.div(
            rx.icon(
                tag=item["icon"],
                class_name="h-16 w-16 text-orange-500 mb-6 drop-shadow-lg",
            ),
            rx.el.h3(
                item["title"],
                class_name="text-3xl font-black text-white mb-4 tracking-tight",
            ),
            rx.el.p(
                item["description"],
                class_name="text-base text-gray-200 leading-relaxed max-w-md",
            ),
            class_name="relative z-10 flex flex-col items-center justify-center h-full p-8 text-center",
        ),
        class_name="relative w-full min-h-[400px] flex items-center justify-center overflow-hidden",
    )


def mision_vision_valores() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.foreach(State.mission_vision_values, mvv_card),
            class_name="grid grid-cols-1 md:grid-cols-3",
        ),
        class_name="w-full",
    )