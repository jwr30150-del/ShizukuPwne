from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import subprocess

class ShizukuPwnerApp(App):
    def build(self):
        self.title = "ShizukuPwner"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.header = Label(
            text="[b]ShizukuPwner - Memory & Command Tool[/b]",
            markup=True,
            font_size='20sp',
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.header)
        
        self.output_label = Label(
            text="Status: Ready to execute via Shizuku...",
            font_size='14sp',
            halign='center',
            valign='middle'
        )
        self.output_label.bind(size=self.output_label.setter('text_size'))
        layout.add_widget(self.output_label)
        
        self.command_input = TextInput(
            text="shizuku_command --help",
            multiline=False,
            size_hint_y=None,
            height=45
        )
        layout.add_widget(self.command_input)
        
        exec_btn = Button(
            text="Execute Command",
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        exec_btn.bind(on_press=self.run_command)
        layout.add_widget(exec_btn)
        
        return layout

    def run_command(self, instance):
        cmd = self.command_input.text
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
            output = result.stdout if result.stdout else result.stderr
            self.output_label.text = output if output else "Command executed successfully with no output."
        except Exception as e:
            self.output_label.text = f"Execution Error: {str(e)}"

if __name__ == '__main__':
    ShizukuPwnerApp().run()
