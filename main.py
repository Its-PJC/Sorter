import time

import pygame
from Sorter import SorterFeatures as SF
import DiffSorts as ds
if __name__ == '__main__':
    pygame.init()
    w_width = 960
    w_height = 600
    font_size = 35

    # Create display object
    screen = pygame.display.set_mode((w_width, w_height))

    # Create class objects object
    sorter = SF(screen)
    diffsorts = ds.SortType(screen,sorter)

    # Initiate Variables
    shuffled = sorter.arr

    # Set the title
    pygame.display.set_caption('Sorter')

    # Initiate buttons
    sort_butt_smallfont,sort_butt_text = sorter.buttonOnScreen("Sort",font_size)
    sort_t,sort_dim = "Sort",[25, 25, 140, 40]
    rand_butt_smallfont,rand_butt_text = sorter.buttonOnScreen("Randomize",font_size)
    rand_t,rand_dim = "Randomize",[190, 25, 170, 40]
    font_size = 25
    merg_butt_smallfont, merg_butt_text = sorter.buttonOnScreen("Merge Sort",font_size)
    merg_t, merg_dim = "Merge Sort", [w_width-450, 25, 200, 30]
    bubb_butt_smallfont, bubb_butt_text = sorter.buttonOnScreen("Bubble Sort",font_size)
    bubb_t, bubb_dim = "Bubble Sort", [w_width-225, 25, 200, 30]
    slct_butt_smallfont, slct_butt_text = sorter.buttonOnScreen("Selection Sort",font_size)
    slct_t, slct_dim = "Selection Sort", [w_width-450, 70, 200, 30]
    quic_butt_smallfont, quic_butt_text = sorter.buttonOnScreen("Quick Sort",font_size)
    quic_t, quic_dim = "Quick Sort", [w_width-225, 70, 200, 30]


    # Paint screen one time
    pygame.display.flip()
    running = True

    # While loop for the game
    while running:
        # Set the Background
        img = pygame.image.load(sorter.background)
        screen.blit(img, (0, 0))

        # Draw line at bottom
        pygame.draw.line(screen, (255, 255, 255),
                         [25, sorter.w_height - 50],
                         [sorter.w_width - 25, sorter.w_height - 50], 2)

        # Store (x,y) coordinates of mouse cursor
        mouse = pygame.mouse.get_pos()

        # To check all the events listed
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rand_dim[0] <= mouse[0] <= rand_dim[0] + rand_dim[2] and rand_dim[1] <= mouse[1] <= rand_dim[1] + \
                        rand_dim[3]:
                    shuffled = sorter.randomArr()

                if quic_dim[0] <= mouse[0] <= quic_dim[0] + quic_dim[2] and quic_dim[1] <= mouse[1] <= quic_dim[1] + \
                        quic_dim[3]:
                    shuffled = diffsorts.quickSort(shuffled)

                if bubb_dim[0] <= mouse[0] <= bubb_dim[0] + bubb_dim[2] and bubb_dim[1] <= mouse[1] <= bubb_dim[1] + \
                        bubb_dim[3]:
                    shuffled = diffsorts.bubbleSort(shuffled)

                if merg_dim[0] <= mouse[0] <= merg_dim[0] + merg_dim[2] and merg_dim[1] <= mouse[1] <= merg_dim[1] + \
                        merg_dim[3]:
                    shuffled = diffsorts.mergeSort(shuffled)

                if slct_dim[0] <= mouse[0] <= slct_dim[0] + slct_dim[2] and slct_dim[1] <= mouse[1] <= slct_dim[1] + \
                        slct_dim[3]:
                    shuffled = diffsorts.selectionSort(shuffled)

            if event.type == pygame.QUIT:
                running = False

        # Activate buttons
        sorter.activateButtonColor(sort_butt_smallfont,sort_butt_text,mouse, sort_dim, sort_t)
        sorter.activateButtonColor(rand_butt_smallfont,rand_butt_text,mouse, rand_dim, rand_t)
        sorter.activateButtonColor(merg_butt_smallfont, merg_butt_text, mouse, merg_dim, merg_t)
        sorter.activateButtonColor(bubb_butt_smallfont, bubb_butt_text, mouse, bubb_dim, bubb_t)
        sorter.activateButtonColor(slct_butt_smallfont, slct_butt_text, mouse, slct_dim, slct_t)
        sorter.activateButtonColor(quic_butt_smallfont, quic_butt_text, mouse, quic_dim, quic_t)

        sorter.drawLines(shuffled)

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()