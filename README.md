# screamy-bird
======================== DESCRIPTION ==========================

Screamy Bird is a flappy bird clone that, instead of mouse clicks, 
requires the player to shout into a microphone to move the bird up 
and down through the incoming obstacles.


======================== REQUIREMENTS =========================

pygame
sounddevice
numpy


==================== CHANGING WINDOW SIZE ======================

Run with command: python.exe .\main.py


==================== CHANGING WINDOW SIZE ======================

By default, the screen window size is set to a flappy bird-esque window
size (900 x 1060). This can be manually adjusted.

BE AWARE - Due to the way the game renders the bird and pipes to the 
screen; performance may be impacted when using a larger window. For best 
results, a smaller full window (1536 x 864) or (900 x 1060) is
recommended


==================== CHANGING VOICE INPUT THRESHOLD ======================

Adjust the value at line 134. Raise the threshold value for more screaming.


================ PLANNED FUTURE UPDATES ==================

Optimised bird and pipe rendering to avoid performance loss

Spawn multiple pipe instances instead of a single set of pipes

Introduce Startup screen

Introduce a selectable difficulty system with
    GAME JOURNALIST MODE
    NORMAL
    CHALLENGING
    GODLIKE

Introduce a countdown before the game starts to play

Introduce sounds for bird dying

Change background based on the selected difficulty
