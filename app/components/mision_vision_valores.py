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
            rx.el.div(
                rx.foreach(
                    State.mission_vision_values,
                    lambda item, index: rx.el.div(
                        mvv_card(item),
                        class_name="w-full flex-shrink-0",
                        id=f"mvv-section-{index}",
                    ),
                ),
                class_name="flex transition-transform duration-500 ease-in-out",
                style={"transform": f"translateX(-{State.current_mvv_index * 100}%)"},
            ),
            class_name="relative w-full overflow-hidden",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon(tag="arrow-left", class_name="h-6 w-6"),
                on_click=State.prev_mvv,
                class_name="bg-white/20 text-white p-3 rounded-full hover:bg-white/30 transition-colors",
            ),
            rx.el.div(
                rx.foreach(
                    State.mission_vision_values,
                    lambda item, index: rx.el.button(
                        on_click=lambda: State.set_mvv_index(index),
                        class_name=rx.cond(
                            State.current_mvv_index == index,
                            "w-3 h-3 bg-orange-500 rounded-full transition-all duration-300",
                            "w-3 h-3 bg-white/50 rounded-full hover:bg-white/75 transition-all duration-300",
                        ),
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.button(
                rx.icon(tag="arrow-right", class_name="h-6 w-6"),
                on_click=State.next_mvv,
                class_name="bg-white/20 text-white p-3 rounded-full hover:bg-white/30 transition-colors",
            ),
            class_name="absolute bottom-8 left-1/2 -translate-x-1/2 z-20 flex items-center gap-6",
        ),
        class_name="w-full relative",
    )