from fasthtml.common import *
app, rt = fast_app()
@rt('/')
def get():
    return Div(
        H1('Welcome to Awesome FastHTML'),
    )
serve()