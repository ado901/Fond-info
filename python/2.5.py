import g2d

A = 500
B = 500
distance = 20
g2d.init_canvas((A, B))
dx = 5
dy = 0
x = 20
y = 20


def update():
    global dx, dy, x, y
    g2d.clear_canvas()  # Clear background
    g2d.fill_circle((x, y), 20)  # Draw foreground
    x += dx
    y += dy

    if x >= A - distance:  # angolo in alto a destra
        dx = 0
        dy = 5

    if y >= A - distance:  # angolo in basso a destra
        dx = -5
        dy = 0
    '''
            nei primi due if posso anche inserire gli and come negli ultimi due ottenendo lo stesso risultato. 
            Non l'ho messo semplicemente per ottimizzare il codice
            '''
    if x <= 0 + distance and y >= A - distance:  # angolo in basso a sinistra
        dx = 0
        dy = -5

    if y <= 0 + distance and x <= 0 + distance:  # angolo in alto a sinistra
        dx = 5
        dy = 0


# Blue circle, center=(400, 300), radius=20
g2d.set_color((255, 0, 0))
# circle
g2d.main_loop(update, 1000 // 30)
