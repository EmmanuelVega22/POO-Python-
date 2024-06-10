# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog, Menu,ttk,font
import random
import json
from datetime import datetime

class Jugador:
    def __init__(self, nombre, fecha, hora,puntaje,dificultad):
        self.nombre = nombre
        self.puntaje = puntaje
        self.fecha = fecha
        self.hora = hora
        self.dificultad = dificultad

    def __gt__(self, otro):
        return self.puntaje > otro.puntaje

class GestorJugadores:
    def __init__(self):
        self.lista_jugadores = []

    def cargar_puntajes(self):
        try:
            with open("pysimonpuntajes.json", "r") as file:
                jugadores = json.load(file)
                for jugador in jugadores:
                    nuevoJugador = Jugador(jugador["Nombre"], jugador["Fecha"], jugador["Hora"],jugador["Puntaje"],jugador["Dificultad"])
                    self.lista_jugadores.append(nuevoJugador)
        except FileNotFoundError:
            pass

    def guardar_puntajes(self, jugador):
        self.lista_jugadores.append(jugador)
        GaleriaPuntaje = [{"Nombre": j.nombre, "Fecha": j.fecha, "Hora": j.hora,"Puntaje": j.puntaje ,"Dificultad": j.dificultad} for j in self.lista_jugadores]
        with open("pysimonpuntajes.json", "w") as file:
            json.dump(GaleriaPuntaje, file, indent=4)

    def get_sorted_scores(self):
        return sorted(self.lista_jugadores, reverse=True)
    
class SimonGame:
    
    def __init__(self,app):
        
        self.app = app
        self.app.title('SimonGame')
        self.secuencia = []
        self.secuencia_jugador = []
        self.botones = {}
        self.puntaje=0
        self.colores = ["green","red","yellow","blue"]
        self.dificultad_elegida = ttk.Combobox(self.app, values=['Principiante', 'Experto', 'Super Experto'])
        self.dificultad = None
        self.timer = 0
        self.gestor = GestorJugadores()
        self.gestor.cargar_puntajes()
        self.nombre_jugador = simpledialog.askstring("Nombre del Jugador", "Ingrese su nombre:")
        
        app.resizable(width=False, height=False)
        
        
        self.label_jugador = tk.Label(self.app,text=self.nombre_jugador)
        self.label_jugador.grid(row=0,column=0, padx=5,pady=5)
        
        self.label_puntaje = tk.Label(self.app,text=self.puntaje)
        self.label_puntaje.grid(row=0,column=1,padx=5,pady=5)
        
        self.label_dificultad = tk.Label(self.app,text='Dificultad')
        self.label_dificultad.grid(row=1,column=0,padx=5,pady=5)
        
        self.etiqueta = tk.Label(self.app, text="")
        
        self.dificultad_elegida['state'] = 'readonly'
        self.dificultad_elegida.bind("<<ComboboxSelected>>", self.seleccionar_dificultad)
        self.dificultad_elegida.grid(row=1,column=1,padx=10,pady=10)
        
        
        self.ventana()

        self.menu()
        
        
    def seleccionar_dificultad(self, event):
        self.dificultad = self.dificultad_elegida.get()
        self.ventana()

        self.comenzar_juego()
    
    def comenzar_juego(self):
        self.rondaSiguiente()

    
    def ventana(self):
        
        if self.dificultad == 'Experto':
            
            self.timer = 30
            self.etiqueta.config(text=self.timer)
            self.etiqueta.grid(row=2,column=1,padx=5,pady=5)
            self.actualizar_temporizador()


            
        elif self.dificultad == 'Super Experto':
            
            self.timer = 30
            self.etiqueta.config(text=self.timer)
            self.etiqueta.grid(row=2,column=0,padx=5,pady=5)
            self.actualizar_temporizador()



        
        for color in self.colores:
            
            botonColor = tk.Canvas(self.app,bg=color,width=200, height=200)
            
            if color == 'green':
                
                botonColor.grid(row=3,column=0)
            
            elif color == 'red':
                
                botonColor.grid(row=3,column=1)
            
            elif color == 'yellow':
                
                botonColor.grid(row=4,column=0)
            
            elif color == 'blue':
                
                botonColor.grid(row=4,column=1)


            botonColor.bind("<Button-1>", lambda e, col=color: self.apretar_boton(col))
            self.botones[color] = botonColor

            
    def apretar_boton(self, color):
        self.secuencia_jugador.append(color)
        self.iluminar_boton(color)
        if self.secuencia_jugador == self.secuencia[:len(self.secuencia_jugador)]:
            if len(self.secuencia_jugador) == len(self.secuencia):
                self.deshabilitar_botones()
                self.app.after(1000 , self.rondaSiguiente)
                #after funciona como un temporizador ejecuta el rondaSiguiente luego de 1000seg o milisegundo
                #para darle tiempo al jugador y ademas ejecutar otra cosas antes
                self.puntaje +=1
                self.timer = 30
                self.label_puntaje.config(text=self.puntaje)
        else:
            self.game_over()
        
    
    def iluminar_boton(self, color):
        botonColor = self.botones[color]
        color_original = botonColor['bg']
        botonColor['bg'] = 'white'
        self.app.after(500, lambda: botonColor.config(bg=color_original))

        
    def deshabilitar_botones(self):
        for boton in self.botones.values():
            boton.unbind("<Button-1>")
        
        
    def rondaSiguiente(self):
        self.app.after(1000, self.mostrar_secuencia)
        self.secuencia_jugador = []
        self.secuencia.append(random.choice(self.colores))
        

    def mostrar_secuencia(self):
        for index, color in enumerate(self.secuencia):
            self.app.after(1000 * index, lambda col=color: self.iluminar_boton(col))
        self.app.after( 1000 * len(self.secuencia), self.habilitar_botones)


    def habilitar_botones(self):
        for boton in self.botones.values():
            boton.bind("<Button-1>", lambda e, col=boton['bg']: self.apretar_boton(col))
        
    def game_over(self):
        self.deshabilitar_botones()
        messagebox.showinfo("Game Over", f"Perdiste! Tu Puntaje: {self.puntaje}")
        jugador = Jugador(self.nombre_jugador,datetime.now().strftime("%d/%m/%y"),datetime.now().strftime("%H:%M"),self.puntaje,self.dificultad )
        self.gestor.guardar_puntajes(jugador)
        self.app.destroy()
        
        
    def menu(self):
        barraMenu = Menu(self.app)
        self.app.config(menu=barraMenu)
        file_menu = Menu(barraMenu, tearoff=0)
        file_menu.add_command(label="Ver puntajes", command = self.ver_puntajes)#aqui deberia ejecutar un 'command=metodo que muestre los puntajes de un archivo json'
        file_menu.add_separator()#Hace una linea que separa los textos de cada opcion
        file_menu.add_command(label="Salir", command=self.app.destroy)#Cierra la ventana
        barraMenu.add_cascade(label="Archivo", menu=file_menu)

    
    def ver_puntajes(self):
       
        galeriaPuntaje = Toplevel()
        galeriaPuntaje.resizable(width=False, height=False)
        galeriaPuntaje.title("Ranking de Puntajes")
        puntajes_ordenados = self.gestor.get_sorted_scores()
        label_frame = tk.LabelFrame(galeriaPuntaje,text="Galeria de Puntajes")
        label_frame.grid(padx=10,pady=10)

        label = tk.Label(label_frame,text="Jugador\t\t\tFecha\t\tHora\t\tPuntaje\t\tDificultad\t")
        label.grid(padx=0, pady=0)

        puntaje_text = tk.Text(label_frame,width=70,height=10)
        for j in puntajes_ordenados:
            scores_text = f"{j.nombre}\t\t{j.fecha}\t\t{j.hora}\t\t{j.puntaje}\t{j.dificultad}\n"
            puntaje_text.insert(tk.END, scores_text)
        
        puntaje_text.grid(row=1, column=0, padx=5, pady=5)
        puntaje_text.config(state=tk.DISABLED)
        
        boton_cerrar = tk.Button(galeriaPuntaje,text="Cerrar",command=self.ventana())
        boton_cerrar.grid(row=2,column=0,padx=5,pady=5)
    
    def actualizar_temporizador(self):
        
        self.etiqueta.config(text=f"Tiempo restante:\t\t{self.timer}")
        
        if self.timer == 0:
        
            self.game_over()
        
        else:
            self.timer -= 1
            self.app.after(1000, self.actualizar_temporizador)
        
        
if __name__ == '__main__':
    
    app = tk.Tk()
    SimonGame(app)
    
    app.mainloop()
