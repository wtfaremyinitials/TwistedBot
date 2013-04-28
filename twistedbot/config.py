
import math

DEBUG = False
WHISPER = False
#To use online login, encryption must also be enabled
ONLINE_LOGIN = False
USE_ENCRYPTION = ONLINE_LOGIN

COMMANDER = "1770749"
COMMANDER = COMMANDER.lower()

USERNAME = "1770749_bot"
PASSWORD = ""

#This is the email address associated with your Mojang account. If you have not migrated your minecraft account to a Mojang account, set this to you minecraft username
EMAIL = ""

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 25565
PROXY_PORT = 25566

LOCALE = 'en_GB'
VIEWDISTANCE = 0  # 0-3 far, normal, short, tiny
DIFFICULTY = 0  # 0-3 peaceful, easy, normal, hard
PROTOCOL_VERSION = 60
CONNECTION_MAX_DELAY = 5
CONNECTION_INITIAL_DELAY = 0.1
KEEP_ALIVE_PERIOD = 300  # that is 6000 ticks

WORLD_HEIGHT = 256
CHUNK_SIDE_LEN = 16

PLAYER_HEIGHT = 1.8
PLAYER_EYELEVEL = 1.62
PLAYER_RADIUS = 0.3
PLAYER_WIDTH = 0.6

MAX_JUMP_HEIGHT = 1.25
MAX_STEP_HEIGHT = 0.5
MAX_WATER_JUMP_HEIGHT = 0.67
MAX_VINE_JUMP_HEIGHT = 0.35

# 0.08 block/tick - drag 0.02 blk/tick (used as final multiply by 0.98)
BLOCK_FALL = 0.08
DRAG = 0.98
SPEED_ON_GROUND = 0.1
SPEED_IN_AIR = 0.02
SPEED_JUMP = 0.42
SPEED_LIQUID_JUMP = 0.04
SPEED_CLIMB = 0.2

TIME_STEP = 0.05

COST_JUMP = 1.1
COST_LADDER = 0.21 / \
    0.15  # common speed on ground / max speed on ladder
COST_FALL = 1.1
COST_DIRECT = 1
COST_DIAGONAL = math.sqrt(2) * COST_DIRECT
PATHFIND_LIMIT = 1000  # roughly in blocks
HORIZONTAL_MOVE_DISTANCE_LIMIT = 2.83

with open ("../../stuff/twistedbotpassword.txt", "r") as file:
    PASSWORD=file.read().replace('\n', '')

with open ("../../stuff/twistedbotemail.txt", "r") as file:
    EMAIL=file.read().replace('\n', '')
