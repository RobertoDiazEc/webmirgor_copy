import reflex as rx


class ContactState(rx.State):
    form_data: dict = {}
    form_submitted: bool = False

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print("Form data received:", self.form_data)
        self.form_submitted = True
        yield rx.toast.success("Formulario enviado con éxito!")
        return ContactState.reset_form

    @rx.event
    def reset_form(self):
        self.form_data = {}
        self.form_submitted = False

    @rx.var
    def form_fields_filled(self) -> bool:
        return (
            bool(self.form_data.get("name"))
            and bool(self.form_data.get("email"))
            and bool(self.form_data.get("subject"))
            and bool(self.form_data.get("message"))
        )