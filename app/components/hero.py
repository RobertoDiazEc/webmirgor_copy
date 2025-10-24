import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            class_name="absolute inset-0 bg-cover bg-center bg-no-repeat",
            style={
                "backgroundImage": "url('https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')"
            },
        ),
        rx.el.div(class_name="absolute inset-0 bg-black/50"),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "El grupo | Negocios | Marcas",
                    class_name="text-sm font-medium text-gray-300 mb-4 tracking-wider",
                ),
                rx.el.h1(
                    "En Mirgor nos une un objetivo en común: ser mejores cada día",
                    class_name="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-6 leading-tight",
                ),
                rx.el.p(
                    "Misión, Visión y Valores.",
                    class_name="text-xl text-gray-200 mb-10",
                ),
                rx.el.button(
                    "Conocer más",
                    class_name="bg-blue-600 text-white font-semibold px-8 py-4 rounded-lg hover:bg-blue-700 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-2xl",
                ),
                class_name="max-w-4xl",
            ),
            class_name="relative container mx-auto px-4 lg:px-6 h-full flex items-center justify-start text-left",
        ),
        class_name="relative h-screen min-h-[600px] w-full",
    )