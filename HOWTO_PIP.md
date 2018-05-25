How to put a new version on pypi.python.org
===========================================

So that the package maintainer won't have to google it every time.

* http://peterdowns.com/posts/first-time-with-pypi.html

1. git checkout master
2. git pull
3. Update version number in setup.py
4. git add setup.py
5. git commit
6. git push
7. git tag X.X.X -m "vX.X.X"
8. git push --tags
9. python setup.py sdist upload -r pypitest
10. Check that things look right on https://test.pypi.org/project/slacker_log_handler/
11. python setup.py sdist upload -r pypi
12. Check that things look right on https://pypi.org/project/slacker-log-handler/
