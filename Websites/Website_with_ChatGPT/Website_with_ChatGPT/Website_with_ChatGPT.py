import reflex as rx

from Website_with_ChatGPT import style
from Website_with_ChatGPT.State import State


def qa(question: str, answer: str) -> rx.Component:
    # aqui agregamos el estilo de las burbujas y margenes
    # a nuestra web
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )

    #box en un contenedor donde ingresamos 
    #nuestro codigo para modificarlo en bloques qque pueden 
    #anidarse y usarse en conjunto
def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )
    
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input( 
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(chat(), action_bar())


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
