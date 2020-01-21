import instaloader

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER) # (load session created w/
                               #  `instaloader -l USERNAME`)


for post in L.get_hashtag_posts('cat'):
    # post is an instance of instaloader.Post
    L.download_post(post, target='#cat')
