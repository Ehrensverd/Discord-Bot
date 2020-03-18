import db_handler
class BotOperator:
    """Bot operator
     important fucntions that read, insert to database as well as
     process data from both discord and database.

     """
    pass

    def __init__(self):
        pass


    def sync_members(self, members):
        """Ensures database data is synced and  up to date with discord members"""
        print('Starting sync_members')
        #Get list of tuples from db with members
        db_members = db_handler.select_all_members()
        print('Print each member')

        disc_members = [(k, v.name, int(v.discriminator)) for k, v in members.items()]

        # if both are equal
        if disc_members == db_members:
            return


        # If size missmatch extra member exists either in db or discord_members
        if len(disc_members)!=len(db_members):
            #db can have members that dont exist in discord list, but all
            pass




        print(len(db_members))
        print(len(disc_members))

        print(db_members[0]==disc_members[1])



        #Return true if db sync was performed or not needed, false if db could not be reached or changed
        return

    def insert_user(self, user):
        """Prefors a insert query and tries to write single user to database by id"""
        db_handler.insert_user(user)

    def insert_users(self, users):
        """Similar to insert user, but inserts multiple users."""
        db_handler.insert_users(users)



    def update_user(self, user):
        """Changes name and / or discirinator of existing user. does not change ID"""
        db_handler.update_user(user)

    def retrieve_db_members(self):
        """Preforms a query and retrieves members as a list"""

        return db_handler.members()
