from fasthtml.common import *

app,rt = fast_app()

@rt
def index():
    return Titled("Simple", Body(
        Div("Starting out...")
    ))

serve()
