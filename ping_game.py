class PingGame:
    """Ping game where bot randomly prints ping! in discord text chat
        and users gets scored based on how fast they respond with !pong

        An aether_ping event can also be summoned by 5 or more members using the
        !summon_ping command for extra points.
        but beware summoning pings can be dangerous and lead to loss of a user current score

        After a given period(14 days) scores are listed and winners recieve grand prices
    """


    def __init__(self):
        pass

    def initiate_ping_event(self):
        """Initiates a regular ping event"""
        pass
    def score_current_ping_event(self):
        """Listens for user command !pong and calculates score and updates to database"""
        pass

    def summon_aether_ping(self):
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

    def aether_ping(self):
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


    def update_penta_score(self):
        """Subtracts 10% of users score  from failed ping pentagram"""
        pass

    def update_scare_aether_event(self, users):
        """Adds or removes score to users who played the  aether ping game"""
        pass