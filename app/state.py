import reflex as rx
from typing import TypedDict


class NavItem(TypedDict):
    text: str
    href: str


class Location(TypedDict):
    country: str
    address_lines: list[str]


class FooterLink(TypedDict):
    text: str
    href: str


class MissionVisionValuesItem(TypedDict):
    icon: str
    title: str
    description: str
    image: str


class State(rx.State):
    """The app state."""

    show_mobile_menu: bool = False

    @rx.event
    def toggle_mobile_menu(self):
        self.show_mobile_menu = not self.show_mobile_menu

    mission_vision_values: list[MissionVisionValuesItem] = [
        {
            "icon": "flag",
            "title": "Misión",
            "description": "Generar valor a través de la innovación y la eficiencia en la producción, para ofrecer soluciones tecnológicas que mejoren la vida de las personas y contribuyan al desarrollo sostenible.",
            "image": "https://images.unsplash.com/photo-1554415707-6e8cfc93fe23?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "icon": "eye",
            "title": "Visión",
            "description": "Ser líderes en la industria tecnológica a nivel global, reconocidos por nuestra calidad, compromiso con el cliente y capacidad para anticipar las necesidades del futuro.",
            "image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "icon": "gem",
            "title": "Valores",
            "description": "Nos regimos por la integridad, la excelencia, la colaboración y la pasión por la innovación. Fomentamos un ambiente de respeto y crecimiento para nuestros empleados y socios.",
            "image": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
    ]
    nav_items: list[NavItem] = [
        {"text": "El Grupo", "href": "#"},
        {"text": "Negocios", "href": "#"},
        {"text": "Marcas", "href": "#"},
        {"text": "Países", "href": "#"},
        {"text": "Inversores", "href": "#"},
        {"text": "Empleos", "href": "#"},
        {"text": "Venta Corporativa", "href": "#"},
        {"text": "Contacto", "href": "#"},
    ]
    socials: list[dict[str, str]] = [
        {"icon": "linkedin", "href": "#"},
        {"icon": "instagram", "href": "#"},
        {"icon": "youtube", "href": "#"},
    ]
    locations: list[Location] = [
        {
            "country": "Argentina",
            "address_lines": [
                "Miñones 2177, CABA, Buenos Aires.",
                "Einstein 1111, Río Grande, Tierra del Fuego.",
            ],
        },
        {
            "country": "Uruguay",
            "address_lines": [
                "Avenida Italia 7519, oficina 407, Montevideo.",
                "Tel. +598 95 114 007",
            ],
        },
        {
            "country": "República Dominicana",
            "address_lines": ["Corporativo 2010, Santo Domingo D.N."],
        },
        {
            "country": "Paraguay",
            "address_lines": [
                "Aviadores del Chaco 2581, Torre 2, Oficina 16 C, Asunción."
            ],
        },
        {
            "country": "Ecuador",
            "address_lines": ["Arcos Plaza 2, Samborondón. KM 2 Samborondón"],
        },
        {
            "country": "Panamá",
            "address_lines": [
                "Costa del Este, Avenida La Rotonda, Edificio Bladex, Piso 6."
            ],
        },
    ]
    footer_links: list[FooterLink] = [
        {"text": "Fundación Mirgor", "href": "#"},
        {"text": "Reporte de Sustentabilidad", "href": "#"},
        {"text": "Blog", "href": "#"},
        {"text": "Contacto", "href": "#"},
    ]