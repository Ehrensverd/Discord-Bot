import db_handler
class BotOperator:
    """Bot operator
     important fucntions that read, insert to database as well as
     process data from both discord and database.

     """

    def __init__(self):
        pass


    def sync_members(self, members):
        """Ensures database data is synced and  up to date with discord members"""
        print('Starting sync_members')
        # Make set of tuples from db with members
        db_members = set(self.get_members())

        # Make set of tuples from list
        disc_members = set()
        for x in members:
            disc_members.add(self.make_member_tuple(x))

        # If both are equal then jobs done!
        if disc_members == db_members:
            print('DB up to date!')
            return

        # Make two sets New users to be inserted, old users to be updated

        # Remove all that are equal
        disc_members.difference_update(db_members)
        new_set = set()
        # Iterate over both sets and insert new users
        for disc_user in disc_members:
            user_id = disc_user[0]
            new_user = True
            for db_user in db_members:
                if db_user[0] == user_id:
                    new_user = False
                    break
            if new_user:
                self.insert_user(disc_user)
                new_set.add(disc_user)

        print('Added', len(new_set), 'users.')

        # Filter newly added users.
        disc_members.difference_update(new_set)

        # Remaining  are users who exist in db but need field updated.
        for user in disc_members:
            self.update_member(user)
        print('Updated', len(disc_members), 'users')
        print('DB has been updated.')


    def insert_user(self, user):
        """Preforms a insert query and tries to write single user to database by id
        Also checks if user is user object or user tuple.
        Query expects tuple
        """
        if type(user) == tuple:
            db_handler.insert_user(user)
        else:
            db_handler.insert_user(self.make_member_tuple(user))

    def update_member(self, member):
        """Changes name and / or discirinator of existing user. does not change ID"""
        if type(member ) == tuple:
            db_handler.update_user(member)
        else:
            db_handler.update_user(self.make_member_tuple(member))

    def get_members(self):
        """Preforms a query and retrieves members as a list"""
        return db_handler.select_all_members()

    def has_member(self, member):
        """Returns true of database has user with matching ID"""
        return db_handler.find_member_id(member.id) != None

    def make_member_tuple(self, member):
        """Takes a use/member object and returns a tuple
        (id, name, discriminator, nick)
        """
        return member.id, member.name, member.discriminator, member.nick

