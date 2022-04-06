from distutils.fancy_getopt import fancy_getopt
import tkinter as tk
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ve 3D')
        self.geometry('500x425')
        self.cvs_figure = tk.Canvas(self, relief = tk.SUNKEN, border = 1, background = 'white',
                                     width = 400, height = 400)
        btn_tam_giac = tk.Button(self, text = 'LOAD PLY', width = 8, command = self.btn_load_ply_click) 
        self.cvs_figure.place(x = 10, y = 10)
        btn_load_ply.place(x = 425, y = 12)
        self.cvs_figure.update()

    def btn_load_ply_click(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        self.PLY = {}
        f= open('D:/thị giác máy/dataset/PLY/cube.ply', 'r')
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = line.split()
        n_vertex = int(line[2])
        self.PLY['n_vertex'] = n_vertex
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        n_face = int(line[2])
        self.PLY['n_face']= n_face
        line = f.readline()
        line = f.readline()
        vetex = []
        for i in range(0,n_vertex):
            line = f.readline()
            line = line.split()
            x= float(line[0])
            y= float(line[1])
            z= float(line[2])
            temp = [ x, y, z]
            vertex.append(temp)
        self.PLY['vertex']=n_vertex
        face = []
        for i in range(0, n_face):
            line = f.readline()
            line = line.split()
            temp = []
        for item in line:
            temp.append(int(item))
            face.append(temp)
        self.PLY['face'] = face
        f.close()
    self.PLY['face'] = face
    vertex_p = []
    for i in range(0, self.PLY['n_vertex']);
        x = scale*self.PLY[vertex'][i][0]
        y = scale*self.PLY[vertex'][i][1]
        z = scale*self.PLY[vertex'][i][2]
        xp = x-L1*z*np.cos(phi)
        yp=
if __name__ == "__main__":
    app = App()
    app.mainloop()
