from fasthtml.common import *

app,rt = fast_app()

@rt
def index():
    return Titled("Hey you", 
                Body(
                    Div("Let's check out FT Tags from fastcore library")
                )
            )

serve()
