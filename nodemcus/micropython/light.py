def das_blinken_lights():
    import time, neopixel, machine
    n = 16
    np = neopixel.NeoPixel(machine.Pin(2), n)
    for j in range(255):
        for i in range(n):
            np[i] = (j,0,0)
            np.write()
            time.sleep(0.1)
        for i in range(n):
            np[i] = (0,j,0)
            np.write()
            time.sleep(0.1)
        for i in range(n):
            np[i] = (0,0,j)
            np.write()
            time.sleep(0.1)
        for i in reversed(list(range(n))):
            np[i] = (0,0,0)
            np.write()
        
        
        
def show_time(h,m,s, lumens=255):
    """16x = 12h
        16y = 60ms
    """
    import neopixel, machine, math
    n = 16
    if h > 12:
        h -= 12 # for 24 hours.
    h_pos = math.ceil(n/12*h) - 1 - 8
    m_pos = math.ceil(n/60*m) - 1 - 8
    s_pos = math.ceil(n/60*s) - 1 - 8
    np = neopixel.NeoPixel(machine.Pin(2), n)
    for i in range(n):
        np[i] = (0,0,0)
    np.write()
    np[h_pos] = (lumens,lumens,0)
    np[m_pos] = (0,lumens,lumens)
    np[s_pos] = (lumens,0,lumens)
    np.write()

def test():
    import time
    for h in range(12):
        for m in range(60):
            for s in range(60):
                show_time(h+1,m+1,s+1,lumens=16)
                time.sleep(0.025)
            print("The time is {}:{}".format(h,m))