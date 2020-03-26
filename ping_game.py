import db_handler

"""Ping game where bot randomly prints ping! in discord text chat
    and users gets scored based on how fast they respond with !pong

    An aether_ping event can also be summoned by 5 or more members using the
    !summon_ping command for extra points.
    but beware summoning pings can be dangerous and lead to loss of a user current score

    After a given period(14 days) scores are listed and winners recieve grand prices
"""


def initiate_ping_event():
    """Initiates a regular ping event"""
    pass


def score_ping(member, delta):
    """
    calculates score and updates to database

    Scoring is based on how fast the players can respond to an event.
    The score starts at 1000 points and slopes down to 800 points after 10 seconds,
    then to 600 points after 100 seconds, 400, after 1000 seconds etc.

    Score Equation is: y = m(x-z) + b
    y = score
    m = slope
    x = duration after scoring started and player scored points. timedelta?
    z = the start of the slope.
    b = the max points for each individual slope.

    y = -20 * x + 1000                  if x < 10 sec
    y = -20/9 * (x-10)+ 800             if x < 100 sec
    y = -2/9 * (x-100)+ 600             if x < 1000 sec
    y = -2/90 * (x-1000)+ 400           if x < 10000 sec
    y = -2/900 * (x-10000) + 200        if x < 100000 sec
    """
    if delta < 10:
        db_handler.insert_score((-20) * delta + 1000, member)
        return int((-20) * delta + 1000)
    if delta < 100:
        db_handler.insert_score((-20 / 9) * (delta-10) + 800, member)
        return int((-20 / 9) * (delta-10) + 800)
    if delta < 1000:
        db_handler.insert_score((-2/9) * (delta-100) + 600, member)
    if delta < 10000:
        db_handler.insert_score((-2/90) * (delta-1000) + 400, member)
    if delta < 100000:
        db_handler.insert_score((-2/900) * (delta-10000) + 200, member)



def summon_aether_ping():
    """
    Mini ping game
    Requires 5 or more users to create a
    ping pentagram.

    5 unique Users must write:
    !p1ng
    !p2ng
    !p3ng
    !p4ng
    !p5ng

    in right order withing 2000ms
    for event to start. Each failed attempt removes 10% or all users score

    When a successful ping sequence is given the aether_ping event is triggered
    """
    pass


def aether_ping():
    """ Event game aether ping. sub game of ping game

    Needs to be sucessfully summoned by users.

    Once triggered the bot will wait a random number of seconds to a set max
    and at a random point write aether_ping to the text channel.
    users must respond with !aether_pong
    and only the two fastest will be granted points to their score


    However aether pings are tricky and the bot might be corrupted and
    write aether_p:ing or some other miss spelling.

    if a user writes !aether_pong and no or not the correct bot aether_ping has
    been issued the user has clearly lost concentration during the summoning process
    Users life force is then drain completely and loses all current score points.

    """
    pass


def update_penta_score():
    """Subtracts 10% of users score  from failed ping pentagram"""
    pass


def update_scare_aether_event():
    """Adds or removes score to users who played the  aether ping game"""
    pass
