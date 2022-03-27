import matplotlib.pyplot as plt

from Random_gen import RandomWalk

while True:
    iteration_number = input("enter the number of iterations: ")
    rw = RandomWalk(num_points = int(iteration_number)) # sktócenie nazwy class'y + ładuję liczbe iteracji do cslss'y
    rw.fill_walk() # uruchomienie metody fill walk w classie RandomWalk

    plt.style.use('classic') # styl wykresu
    plt.subplots() # funkcja która generuje wykres

    point_numbers = list(range(int(iteration_number))) #pod kolorowanke
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none', s=15) #unkcji scatter() można przekazać listę oddzielnych wartości X i Y; wielkośc kropki s=15; kolorowanka punktów od c=....
    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == 'n':
        break