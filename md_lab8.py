import numpy as np
from PIL import Image
import pygame
import random

class Board:
    def __init__(self, image_path="obrazek.bmp"):

        # Wczytanie obrazu
        self.image = Image.open(image_path).convert("RGB")

        # Konwersja obrazu na tablicę numpy
        self.img_array = np.array(self.image)
        self.board_height = self.img_array.shape[0]   #wysokość planszy, czyli liczbę wierszy kwadratów na planszy
        self.board_width = self.img_array.shape[1]   #szerokość planszy, czyli liczbę kolumn kwadratów na planszy

        self.size = 8    # rozmiar małego kwadratu
        #matrix= []
        self.matrix = [[[0,0,0,0,0,0,0,0,0] for x in range(self.board_width)] for y in range(self.board_height)]
        self.number_of_squares = 1000
        self.tick = 0

        # Inicjalizacja pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.board_width * self.size, self.board_height * self.size))
        # wyświetlenie okna gry
        pygame.display.set_caption("LGA")
        self.clock = pygame.time.Clock()        

    def initialize_matrix(self):
        for x in range(20):
            for y in range(self.board_height):
                self.matrix[y][x] = [1, 0, 0, 0, 0, 0, 0, 0, 0]

        self.new_matrix = [[[0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(self.board_width)] for y in range(self.board_height)]

    def rysuj(self):
        temp = np.copy(self.image)
        for x in range(self.board_width):
            for y in range(self.board_height):
                if np.all(self.img_array[x][y] == [0,0,0]):
                    color = [0,0,0]
                else:    
                    color = [255,255,255]
                    
                    suma = 0
                    for i in range(9):
                        suma += self.matrix[x][y][i]
                    if suma == 0:
                        color = [255, 255, 255]    
                    elif suma < 0.1:
                        color = [209, 231, 240]    
                    elif suma < 0.2:
                        color = [187, 223, 237]    
                    elif suma < 0.3:
                        color = [154, 192, 217]    
                    elif suma < 0.4:
                        color = [133, 182, 214]    
                    elif suma < 0.5:
                        color = [102, 164, 204]    
                    elif suma < 0.6:
                        color = [84, 157, 204]    
                    elif suma < 0.7:
                        color = [70, 153, 207]    
                    elif suma < 0.8:
                        color = [48, 146, 209]    
                    elif suma < 0.9:
                        color = [26, 122, 184]    
                    elif suma < 1:
                        color = [18, 114, 176]    
                    elif suma == 1:
                        color = [7, 86, 138]  
                    else:
                        color = [6, 58, 92]                

                pygame.draw.rect(self.screen, color, (y*self.size, x*self.size, self.size, self.size))
                temp[x,y] = color
        img_save =  Image.fromarray(temp)
        img_save.save(f"./gif/frame{self.tick}.bmp")


    def chodzenie(self):

        Direction = {
            0:[0,0],    #srodek
            1:[0,-1],   #gora
            2:[1,0],    #prawo
            3:[0,1],    #dol
            4:[-1,0],   #lewo
            5:[1,-1],   #prawy gorny
            6:[-1,1],   #lewy dolny
            7:[-1,-1],  #lewy gorny
            8:[1,1]     #prawy dolny
        }

        Waga = {
            0:4/9,
            1:1/9,   #gora
            2:1/9,    #prawo
            3:1/9,    #dol
            4:1/9,    #lewo
            5:1/36,
            6:1/36,
            7:1/36,
            8:1/36
        }

        for x in range(self.board_width):
            for y in range(self.board_height):
                if np.all(self.img_array[x][y] != [0,0,0]):
                    ro = 0
                    ro_u_x = 0
                    ro_u_y = 0
                    for i in range(9):
                        ro += self.matrix[x][y][i]
                        ro_u_x += self.matrix[x][y][i]*Direction[i][0]
                        ro_u_y += self.matrix[x][y][i]*Direction[i][1]
                    if ro <= 0.1:
                        u = [0,0]
                    else:
                        u = [ro_u_x/ro,ro_u_y/ro]
                    if u[0] > 0.5:
                        u[0] = 0.5
                    if u[0] < -0.5:
                        u[0] = -0.5
                    if u[1] > 0.5:
                        u[1] = 0.5
                    if u[1] < -0.5:
                        u[1] = -0.5

                    for i in range(9):
                        self.new_matrix[x][y][i] += ro*Waga[i]*(1+3*mnozenie_wektorow(Direction[i],u)+4.5*pow(mnozenie_wektorow(Direction[i],u),2)-1.5*mnozenie_wektorow(u,u))
                        self.matrix[x][y][i] = 0    
                       
    
        for x in range(self.board_width):
            for y in range(self.board_height):
                if np.all(self.img_array[x][y] != [0,0,0]):
                    for i in range(9):
                        if self.new_matrix[x][y][i] > 0:
                            if np.all(self.img_array[(x+Direction[i][1])][(y+Direction[i][0])] == [0,0,0]): 
                                if i == 1:
                                    self.matrix[x][y][3] += self.new_matrix[x][y][i]
                                elif i == 2:
                                    self.matrix[x][y][4] += self.new_matrix[x][y][i]
                                elif i == 3:
                                    self.matrix[x][y][1] += self.new_matrix[x][y][i]
                                elif i == 4:
                                    self.matrix[x][y][2] += self.new_matrix[x][y][i]
                                else:
                                    self.matrix[x][y][(i+1)%4+5] += self.new_matrix[x][y][i]
                            else:  
                                self.matrix[(x + Direction[i][1])][(y + Direction[i][0])][i] += self.new_matrix[x][y][i]
                            self.new_matrix[x][y][i] = 0
             
def mnozenie_wektorow(wektor1, wektor2):
    [x,y] = wektor1
    [x1,y1] = wektor2
    wynik = x * x1 + y * y1
    return wynik
stop = True
if __name__ == "__main__":
 
    board = Board()
    board.initialize_matrix()

    max_ticks = 3000  # Maksymalna liczba iteracji
    run = True

    board.rysuj()
    while run:
        if board.tick < max_ticks:
            board.clock.tick(60)

            if not stop:
                board.chodzenie()
                board.rysuj()        
                board.tick += 1
            pygame.time.delay(1) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed() 
                    if event.key == pygame.K_SPACE:
                        stop = not stop

            pygame.display.flip()
