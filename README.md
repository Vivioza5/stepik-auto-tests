# stepik-auto-tests-course


Small tool for visual testing with python & selenium

To run the layout tests use:

py.test -m --browser=firefox --html=report.html --domain_staging=stepik.org --domain_production=https://stepik.org

You need geckodriver to run on Firefox and chromedriver to run on Google chrome. Put them as the PATH variable on your computer (or just in your working directory).

Enjoy!
