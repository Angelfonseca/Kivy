from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import bcrypt
from kivy.lang import Builder
import sqlite3
from kivy.uix.label import Label


def consulta_usuario(usuario, cursor):
    consulta = "SELECT * FROM usuarios WHERE Usuario = ?"
    cursor.execute(consulta, (usuario,))
    res = cursor.fetchone()
    return res
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
def verificar(usuario, contraseña_prov, cursor):
    user_data = consulta_usuario(usuario, cursor)
    if user_data:
        passwd_hashed = user_data[1]
        ban = bcrypt.checkpw(contraseña_prov.encode('latin-1'), passwd_hashed)
        return ban
    return False
class LoginScreen(Screen):
    def verif(self):
        usuario = self.ids.user.text
        contraseña = self.ids.pwd.text
        if verificar(usuario, contraseña, cursor):
            print("datos correctos")
            self.manager.current = 'main'
        else:
    
            self.user.text = ""
            self.pwd.text = "" 
            print("try again")
class MainScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass
    
class P:
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager() 
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm

Builder.load_file('main.kv')

if __name__ == '__main__':
    MyApp().run()
