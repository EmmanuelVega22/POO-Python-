# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:43:44 2024

@author: Emmanuel
"""
import tkinter as tk
from tkinter import messagebox, simpledialog, Menu
import random
import json
from datetime import datetime

class SimonGame:
    
    def __init__(self,app):
        
        self.app = app
        self.app.title('SimonGame')
        self.secuencia = []
        self.secuencia_jugador = []
        self.botones = {}
        self.colores = ["green","red","yellow","blue"]
        app.resizable(width=False, height=False)

        self.ventana() #Crear el tamaño y botones de la ventana
        self.menu()
        self.app.after(1000, self.comenzar_juego)

    
    def comenzar_juego(self):
        self.rondaSiguiente()

    
    def ventana(self):
        

        for color in self.colores:
            
            botonColor = tk.Canvas(self.app,bg=color,width=200, height=200)
            
            if color == 'green':
                
                botonColor.grid(row=0,column=0)
            
            elif color == 'red':
                
                botonColor.grid(row=0,column=1)
            
            elif color == 'yellow':
                
                botonColor.grid(row=1,column=0)
            
            elif color == 'blue':
                
                botonColor.grid(row=1,column=1)

            
            botonColor.bind("<Button-1>", lambda e, col=color: self.apretar_boton(col))
            self.botones[color] = botonColor

            
    def apretar_boton(self, color):
        self.secuencia_jugador.append(color)
        self.iluminar_boton(color)
        if self.secuencia_jugador == self.secuencia[:len(self.secuencia_jugador)]:
            if len(self.secuencia_jugador) == len(self.secuencia):
                self.deshabilitar_botones()
                self.app.after(1000, self.rondaSiguiente)
                #after funciona como un temporizador ejecuta el rondaSiguiente luego de 1000seg o milisegundo
                #para darle tiempo al jugador y ademas ejecutar otra cosas antes
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
        self.app.after(1000 * len(self.secuencia), self.habilitar_botones)


    def habilitar_botones(self):
        for boton in self.botones.values():
            boton.bind("<Button-1>", lambda e, col=boton['bg']: self.apretar_boton(col))

    def game_over(self):
        self.deshabilitar_botones()
        puntaje = len(self.secuencia) - 1
        messagebox.showinfo("Game Over", f"Perdiste! Tu Puntaje: {puntaje}")
        self.app.destroy()
        
        
    def menu(self):
        barraMenu = Menu(self.app)
        self.app.config(menu=barraMenu)
        file_menu = Menu(barraMenu, tearoff=0)
        file_menu.add_command(label="Ver puntajes")#aqui deberia ejecutar un 'command=metodo que muestre los puntajes de un archivo json'
        file_menu.add_separator()#Hace una linea que separa los textos de cada opcion
        file_menu.add_command(label="Salir", command=self.app.destroy)#Cierra la ventana
        barraMenu.add_cascade(label="Archivo", menu=file_menu)

if __name__ == '__main__':
    
    app = tk.Tk()
    SimonGame(app)
    
    app.mainloop()
    
    
    