import reflex as rx
from app.states.contact_state import ContactState
from app.state import State


def contact_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            class_name="absolute inset-0 bg-cover bg-center bg-no-repeat",
            style={
                "backgroundImage": "url('https://images.unsplash.com/photo-1554230522-334363673514?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')"
            },
        ),
        rx.el.div(class_name="absolute inset-0 bg-black/60"),
        rx.el.div(
            rx.el.h1(
                "Contáctanos",
                class_name="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-6 leading-tight",
            ),
            rx.el.p(
                "Estamos aquí para ayudarte. Completa el formulario o utiliza nuestros datos de contacto.",
                class_name="text-lg text-gray-200 max-w-2xl text-center",
            ),
            class_name="relative container mx-auto px-4 lg:px-6 h-full flex flex-col items-center justify-center text-center",
        ),
        class_name="relative min-h-[400px] w-full pt-[124px]",
    )


def contact_form() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Envíanos un mensaje", class_name="text-2xl font-bold text-gray-800 mb-6"
        ),
        rx.el.form(
            rx.el.div(
                rx.el.input(
                    placeholder="Nombre completo",
                    name="name",
                    class_name="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500",
                ),
                rx.el.input(
                    placeholder="Email",
                    name="email",
                    type="email",
                    class_name="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4",
            ),
            rx.el.input(
                placeholder="Asunto",
                name="subject",
                class_name="w-full p-3 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500",
            ),
            rx.el.textarea(
                placeholder="Tu mensaje...",
                name="message",
                rows="5",
                class_name="w-full p-3 border border-gray-300 rounded-lg mb-6 focus:outline-none focus:ring-2 focus:ring-orange-500",
            ),
            rx.el.button(
                "Enviar Mensaje",
                type="submit",
                class_name="w-full bg-orange-500 text-white font-semibold py-3 px-6 rounded-lg hover:bg-orange-600 transition-colors duration-300",
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
            class_name="w-full",
        ),
    )


def contact_info() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Información de Contacto",
            class_name="text-2xl font-bold text-gray-800 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("map-pin", class_name="h-6 w-6 text-orange-500 mr-4"),
                    rx.el.div(
                        rx.el.h4(
                            "Nuestras Oficinas",
                            class_name="font-semibold text-gray-700",
                        ),
                        rx.el.p(
                            "19th Ave New York, NY 95822, USA",
                            class_name="text-sm text-gray-600",
                        ),
                    ),
                ),
                class_name="flex items-start mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("phone", class_name="h-6 w-6 text-orange-500 mr-4"),
                    rx.el.div(
                        rx.el.h4("Teléfono", class_name="font-semibold text-gray-700"),
                        rx.el.p(
                            "+1 (555) 123-4567", class_name="text-sm text-gray-600"
                        ),
                    ),
                ),
                class_name="flex items-start mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("mail", class_name="h-6 w-6 text-orange-500 mr-4"),
                    rx.el.div(
                        rx.el.h4("Email", class_name="font-semibold text-gray-700"),
                        rx.el.p(
                            "contacto@mirgor.com", class_name="text-sm text-gray-600"
                        ),
                    ),
                ),
                class_name="flex items-start mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("clock", class_name="h-6 w-6 text-orange-500 mr-4"),
                    rx.el.div(
                        rx.el.h4(
                            "Horarios de Atención",
                            class_name="font-semibold text-gray-700",
                        ),
                        rx.el.p(
                            "Lunes a Viernes: 9:00 AM - 6:00 PM",
                            class_name="text-sm text-gray-600",
                        ),
                    ),
                ),
                class_name="flex items-start",
            ),
        ),
    )


def location_card(location: dict) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            location["country"], class_name="text-xl font-bold text-gray-800 mb-3"
        ),
        rx.foreach(
            location["address_lines"],
            lambda line: rx.el.p(
                line, class_name="text-sm text-gray-600 leading-relaxed mb-1"
            ),
        ),
        class_name="bg-white p-6 rounded-lg border border-gray-200 shadow-sm",
    )


def contact_page_content() -> rx.Component:
    return rx.el.div(
        contact_hero(),
        rx.el.section(
            rx.el.div(
                contact_form(),
                contact_info(),
                class_name="container mx-auto px-4 lg:px-6 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16",
            ),
            class_name="py-12 lg:py-20 bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Nuestras Ubicaciones",
                    class_name="text-3xl font-bold text-gray-800 mb-8 text-center",
                ),
                rx.el.div(
                    rx.foreach(State.locations, location_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
                ),
                class_name="container mx-auto px-4 lg:px-6",
            ),
            class_name="py-12 lg:py-20 bg-white",
        ),
    )