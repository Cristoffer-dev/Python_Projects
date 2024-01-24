# state.py
import reflex as rx
import os
import openai
from Website_with_ChatGPT import openai_env

# Utiliza el nombre de la variable de entorno, no el valor directo
openai.api_key = openai_env.API_KEY

class State(rx.State):

    question: str
    chat_history: list[tuple[str, str]]

    def answer(self):
        # El chatbot ahora tiene algo de inteligencia.
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Agrega la respuesta a medida que el chatbot responde.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Limpia la entrada de la pregunta.
        self.question = ""
        # Hacer yield aquí para limpiar la entrada del frontend antes de continuar.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
                yield
