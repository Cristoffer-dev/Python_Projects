# # """Welcome to Reflex!."""

# # from Website_with_ChatGPT import styles

# # # Import all the pages.
# # from Website_with_ChatGPT.pages import *

# # import reflex as rx

# # # Create the app and compile it.
# # app = rx.App(style=styles.base_style)
# # app.compile()


# #crear botones de incremento y decremento
# import reflex as rx
# class State(rx.State):
# #back-end
#     count: int =0
    
#     def increment(self):
#         self.count += 1
        
#     def decrement(self):
#         self.count -= 1
# #front-end
# def index():
#     return rx.hstack(
#         rx.button(
#             "Decrement",
#             color_scheme="gray",
#             border_radius="1em",
#             #back-end implementation using buttons
#             on_click=State.decrement
#         ),
#         rx.heading(State.count,font_size="2em"),
#         rx.button(
#             "Increment",
#             color_scheme="blue",
#             border_radius="1em",
#             #back-end implementation using buttons
#             on_click=State.increment
#         ),
#     )


# app = rx.App()
# app.add_page(index)
# app.compile()
