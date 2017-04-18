How to put a new version on pypi.python.org
===========================================

So that the package maintainer won't have to google it every time.

* http://peterdowns.com/posts/first-time-with-pypi.html

1. git checkout master
2. git pull
3. Update version number in setup.py
4. git commit
5. git push
6. git tag X.X.X -m "vX.X.X"
7. git push --tags
8. python setup.py sdist upload -r pypitest
9. Check that things look right on https://testpypi.python.org/pypi/slacker_log_handler
10. python setup.py sdist upload -r pypi
11. Check that things look right on https://pypi.python.org/pypi/slacker_log_handler
