from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class AdminPannel(Screen):
    def __init__(self, **kwargs):
        super(AdminPannel, self).__init__(**kwargs)
        self.build_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def build_ui(self):
        self.clear_widgets()
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
        self.layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20], spacing=20)

        # Header
        header = Label(text="Admin Actions", font_size='24sp', color=[0.13, 0.55, 0.13, 1], size_hint=(1, 0.2), bold=True)
        self.layout.add_widget(header)
        
        borrower_list_button = Button(text="Borrower List", color=[1, 1, 1, 1], background_color=(0.6, 0.8, 1, 1), size_hint=(1, 0.2))
        library_list_button = Button(text="Library List", color=[1, 1, 1, 1], background_color=(0.13, 0.55, 0.13, 1), size_hint=(1, 0.2))
        back_button = Button(text="Back", color=[1, 1, 1, 1], background_color=(0.6, 0.8, 1, 1), size_hint=(1, 0.2))

        borrower_list_button.bind(on_press=self.show_borrower_list)
        library_list_button.bind(on_press=self.view_library)
        back_button.bind(on_press=self.go_back)

        self.layout.add_widget(borrower_list_button)
        self.layout.add_widget(library_list_button)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def go_back(self, instance):
        self.manager.current = 'admin_screen'

    def show_borrower_list(self, instance):
        self.manager.current = 'borrower_list_admin'

    def view_library(self, instance):
        self.manager.current = 'admin_library_screen'
