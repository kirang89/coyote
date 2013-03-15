#Coyote

##Overview
A lame ass search engine written purely for the purpose of understanding the basics of a search engine and of course, for the pleasure of hacking :)

##Installation
* Do the following:
    <pre><code>git clone https://github.com/kirang89/coyote.git
    cd coyote/scripts
    chmod +x setup.sh
    ./setup.sh
    </code></pre>
    
    The ```setup.sh``` file installs **pylibmc** on your system, which is a     dependency for this project. It also sets an alias **search** in your ```bashrc``` file
                                
##Dependencies
* ```pylibmc``` - a memcached client for python

##Running
* I've written a script that runs ```indexer.py``` as a cron job. If you want to do so, run the ```indexer_cron.sh``` script.
* In order to do a search, run the following from the command line

    ``` search <your query here> ```

##Examples

<pre><code>
$search a good website

++++++++++++++
Search Results
++++++++++++++
0. http://www.udacity.com/cs101x/index.html
1. http://www.udacity.com/cs101x/crawling.html

$search blah blah

++++++++++++++
Search Results
++++++++++++++
No results found

</code></pre>
