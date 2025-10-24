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


class State(rx.State):
    """The app state."""

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