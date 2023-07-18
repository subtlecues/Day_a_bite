import time

import flet as ft


def main(page: ft.page):
    page.window_width = 500
    page.bgcolor = '#D0F5BE'
    page.title = 'Day-a-bite'
    page.vertical_alignment = "center"

    text = ft.Text(value='building day-a-bite app', color='blue')
    button_text = ft.TextField(label='How should I call you?')
    button_bt = ft.ElevatedButton(text="Say my name!")
    page.add(
        ft.Row(controls=[button_text, button_bt],
               alignment=ft.MainAxisAlignment.SPACE_EVENLY))
    page.add(
        text
    )

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.6)

ft.app(target=main)
