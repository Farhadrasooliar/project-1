from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


#create the app main class
class SayHello(App):
    def build(self):
        self.windows = GridLayout()
        self.windows.cols = 1
        self.windows.size_hint = (0.6, 0.7)
        self.windows.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #image widget
        self.windows.add_widget(Image(source="app.ico"))
        #label widget
        self.greeting = Label(text="What is Your name: ",
                              font_size=18, color='#118BE4')
        self.windows.add_widget(self.greeting)
        #text input widget
        self.user = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, 0.5 ))
        self.windows.add_widget(self.user)
        #Button widget
        self.btn = Button(text='Get',
                          size_hint=(1, 0.5),
                          bold=True,
                          background_color="#118BE4")
        self.btn.bind(on_press=self.callback)
        self.windows.add_widget(self.btn)

        return self.windows

    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + '!'



if __name__=="__main__":
    SayHello().run()