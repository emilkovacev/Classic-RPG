import sys
sys.path.insert(0, "../crpg")

import parser

game = parser.v1("game-2-layout.dl")
game.start()
