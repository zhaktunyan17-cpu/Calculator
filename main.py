import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex

class AutoFontButton(Button):
    def __init__(self, **kwargs):
        super(AutoFontButton, self).__init__(**kwargs)
        self.bind(size=self.update_font_size)

    def update_font_size(self, *args):
        self.font_size = self.height * 0.3

class CalculatorDisplay(TextInput):
    def __init__(self, **kwargs):
        super(CalculatorDisplay, self).__init__(**kwargs)
        self.bind(size=self.update_font_size)

    def update_font_size(self, *args):
        self.font_size = self.height * 0.40

class CalculatorApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', padding=6, spacing=4)
        
        self.screen = CalculatorDisplay(
            text='', 
            halign='right', 
            multiline=False,
            size_hint=(1, 0.1),
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1)
        )
        root_layout.add_widget(self.screen)
        
        self.buttons_container = BoxLayout(orientation='vertical', spacing=4, size_hint=(1, 0.67))
        rows = [
            ['C', 'CE', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['√', '0', '.', '=']
        ]
        
        for row_keys in rows:
            row_layout = BoxLayout(orientation='horizontal', spacing=2, size_hint=(1, 1))
            for key in row_keys:
                if key == '=':
                    button_bg = '#008D3B'
                    button_fg = '#FFFFFF'
                elif key in ['/', '*', '+', '-', '√', '%', '.', '!']:
                    button_bg = '#212121'
                    button_fg = '#369250'
                elif key in ['C', 'CE']:
                    button_bg = '#212121'
                    button_fg = '#FF5722'
                elif key in ['x²', 'x³', 'π']:
                    button_bg = '#212121'
                    button_fg = '#467C91'
                else:
                    button_bg = '#212121'
                    button_fg = '#ffffff'
                
                btn = AutoFontButton(
                    text=key,
                    background_normal='',
                    background_color=get_color_from_hex(button_bg),
                    color=get_color_from_hex(button_fg)
                )
                btn.bind(on_press=lambda instance, k=key: self.press(k))
                row_layout.add_widget(btn)
            self.buttons_container.add_widget(row_layout)
            
        root_layout.add_widget(self.buttons_container)
        
        self.adv_toggle_btn = AutoFontButton(
            text='Other functions',
            size_hint=(1, 0.1),
            background_normal='',
            background_color=get_color_from_hex('#212121'),
            color=get_color_from_hex('#467C91')
        )
        self.adv_toggle_btn.bind(on_press=self.toggle_advanced)
        root_layout.add_widget(self.adv_toggle_btn)
        
        self.adv_container = BoxLayout(orientation='vertical', spacing=4, size_hint=(1, 0.1))
        self.advanced_visible = False
        
        adv_row_layout = BoxLayout(orientation='horizontal', spacing=4, size_hint=(1, 1))
        adv_keys = ['x²', 'x³', 'π', 'sin', '!']
        for adv_key in adv_keys:
            btn = AutoFontButton(
                text=adv_key,
                background_normal='',
                background_color=get_color_from_hex('#212121'),
                color=get_color_from_hex('#467C91')
            )
            btn.bind(on_press=lambda instance, k=adv_key: self.press(k))
            adv_row_layout.add_widget(btn)
        self.adv_container.add_widget(adv_row_layout)
        
        self.root_layout_ref = root_layout
        return root_layout

    def toggle_advanced(self, instance):
        if self.advanced_visible:
            if self.adv_container in self.root_layout_ref.children:
                self.root_layout_ref.remove_widget(self.adv_container)
            self.advanced_visible = False
            self.adv_toggle_btn.text = 'Other functions'
        else:
            self.root_layout_ref.add_widget(self.adv_container)
            self.advanced_visible = True
            self.adv_toggle_btn.text = 'Hide functions'

    def press(self, key):
        current_text = self.screen.text
        if key == '=':
            try:
                x = eval(current_text)
                self.screen.text = str(x)
            except Exception:
                self.screen.text = " ERROR "
        elif key == 'C':
            self.screen.text = ""
        elif key == 'CE':
            if len(current_text) > 0:
                self.screen.text = current_text[:-1]
        elif key == '√':
            try:
                x = float(current_text)
                self.screen.text = str(math.sqrt(x))
            except Exception:
                self.screen.text = " ERROR "
        elif key == '%':
            try:
                x = float(current_text)
                self.screen.text = str(x / 100)
            except Exception:
                self.screen.text = "ERROR"
        elif key == 'x²':
            try:
                x = float(current_text)
                self.screen.text = str(x * x)
            except Exception:
                self.screen.text = "ERROR"
        elif key == 'x³':
            try:
                x = float(current_text)
                self.screen.text = str(x * x * x)
            except Exception:
                self.screen.text = "ERROR"
        elif key == 'π':
            self.screen.text += str(math.pi)
        elif key == 'sin':
            try:
                x = float(current_text)
                self.screen.text = str(math.sin(math.radians(x)))
            except Exception:
                self.screen.text = " ERROR "
        elif key == '!':
            try:
                val = eval(current_text)
                x = int(val)
                self.screen.text = str(math.factorial(x))
            except Exception:
                self.screen.text = "ERROR"
        else:
            self.screen.text += key

if __name__ == '__main__':
    CalculatorApp().run()