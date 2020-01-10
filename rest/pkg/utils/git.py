git = None
try:
    from sh import git
except:
    pass


def get_top_commit(short: bool = True):
    if git:
        try:
            commit = git('rev-parse', '--short', 'HEAD') if short else git('rev-parse', 'HEAD')
            return commit.strip('\n')
        except:
            pass
