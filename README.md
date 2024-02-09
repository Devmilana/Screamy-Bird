# screamy-bird
======================== DESCRIPTION ==========================

Screamy bird is a flappy bird clone which instead of mouseclicks, 
requires the player to shout into a microphone to move the bird up 
and down, through the incoming obstacles.


======================== REQUIREMENTS =========================

pygame
sounddevice
numpy


==================== CHANGING WINDOW SIZE ======================

By default the screen window size is set to flappy bird esque window
size fit for a 1920x1080 screen. The dimensions can be manually changed
in Line 23 and 24.

To always launch in fullscreen, UNCOMMENT OUT the lines of code from
Lines 17 to 20 and COMMENT OUT lines 23 to 26

BE AWARE - Due to the way the game renders the bird and pipes to the 
screen, performance may be impacted when using a larger window. For best 
results, a smaller full window (1536 x 864) or (900 x 1060) is
recommended


================ CHANGING GAMEPLAY DIFFICULTY ==================

Changing scream threshold
Line 140 : if scream_volume > 2:
( Change number. Higher the number, the louder the player has to scream )


Change bird jump height
Line 48 : self.jump = 6
( Change number. Higher the number, the higher the bird jumps )


Changing bird fall speed
Line 49 : self.gravity = 8
( Change number, Higher the number, the faster the bird falls )


Changing pipe width
Line 131 : Pipe = Pipe(85, random.randint(0, int( .... AND
Line 149 : ScreamyBird.Pipe = Pipe(85, random.randint(0, ... AND
Line 211 : Pipe_width = 85

( Change number. Higher the number, the wider the pipe )


Changing pipe scroll speed
Line 212 : Pipe_move = 9
( Change number. Higher the number, faster the pipes will scroll )


================ PLANNED FUTURE UPDATES ==================

Optimised bird and pipe rendering to avoid performance loss

Spawn multiple pipe instances instead of a single set of pipes

Introduce Startup screen

Introduce selectable difficulty system with
    GAME JOURNALIST MODE
    NORMAL
    CHALLENGING
    GODLIKE

Introduce countdown before game starts to play

Introduce sounds for bird dying

Change background based on selected difficulty