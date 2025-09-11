from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.build_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


    def build_ui(self):
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=[40, 20, 40, 20])

        # Logo Label
        logo_label = Label(text="SOLA Library", font_size='32sp', bold=True, size_hint=(1, 0.3), color=(1, 1, 1, 1))
        layout.add_widget(logo_label)

        # Buttons Layout
        buttons_layout = GridLayout(cols=2, spacing=20, size_hint=(1, 0.2))

        admin_button = Button(text="Admin", font_size='20sp', size_hint=(0.3, 0.2), background_color=(0.13, 0.55, 0.13, 1))
        borrower_button = Button(text="Borrower", font_size='20sp', size_hint=(0.3, 0.2), background_color=(0, 0.6, 0.8, 1))

        # Bind the buttons to navigate to the respective screens
        admin_button.bind(on_press=self.go_to_admin_screen)
        borrower_button.bind(on_press=self.go_to_user_screen)

        buttons_layout.add_widget(admin_button)
        buttons_layout.add_widget(borrower_button)

        layout.add_widget(buttons_layout)

        self.add_widget(layout)

    def go_to_admin_screen(self, instance):
        self.manager.current = 'admin_screen'

    def go_to_user_screen(self, instance):
        self.manager.current = 'user_screen'
