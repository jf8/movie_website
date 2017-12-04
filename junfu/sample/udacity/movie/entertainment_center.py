#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''This program uses fresh_tomatoes and media.py to generate a html file
containing a group of movies with posters and trailers.'''


import media
import fresh_tomatoes


#用数据实例化moive对象

iron_man = media.Movie('Iron Man',
                       ('A billionaire industrialist and genius inventor, '
                        'Tony Stark (Robert Downey Jr.), builds an armored '
                        'suit and uses it to combat crime and terrorism.'),
                       ('https://upload.wikimedia.org/wikipedia/en/7/70/'
                        'Ironmanposter.JPG'),
                       'https://www.youtube.com/watch?v=8hYlB38asDY',
                       '2008')


back_to_the_future = media.Movie('Back to the Future',
                                 ('A teenager (Michael J. Foxx) time travels'
                                  ' to the past and gets hit on by his mom.'),
                                 ('https://upload.wikimedia.org/wikipedia/en/'
                                  'd/d2/Back_to_the_Future.jpg'),
                                 'https://www.youtube.com/watch?v=qvsgGtivCgs',
                                 '1985')


tron = media.Movie('Tron',
                   ('Kevin Flynn, computer programmer, finds a way into the'
                    ' machine and has to battle his way out.'),
                   ('https://upload.wikimedia.org/wikipedia/en/1/17/'
                    'Tron_poster.jpg'),
                   'https://www.youtube.com/watch?v=3efV2wqEjEY',
                   '1982')


tron_legacy = media.Movie('Tron: Legacy',
                          ('Years after Sam Flynn\'s father disappeared into'
                           ' the machine, Sam follows in his foot steps.'),
                          ('https://upload.wikimedia.org/wikipedia/en/c/c2/'
                           'Tron_Legacy_poster.jpg'),
                          'https://www.youtube.com/watch?v=L9szn1QQfas',
                          '2010')


space_camp = media.Movie('Space Camp',
                         ('A group of kids get more than they could imagine'
                          ' when they attend space camp.'),
                         ('https://upload.wikimedia.org/wikipedia/en/b/b2/'
                          'Space_camp_-_1986_Poster.png'),
                         'https://www.youtube.com/watch?v=9TDNny6h9nw',
                         '1986')


iron_eagle = media.Movie('Iron Eagle',
                         ('A high school student teams with a Air Force pilot'
                          ' to rescue his father.'),
                         ('https://upload.wikimedia.org/wikipedia/en/0/04/'
                          'Iron_eagle.jpg'),
                         'https://www.youtube.com/watch?v=vSR6sxi1RTo',
                         '1986')

# List of movies to display on page in alphabetical order.
movies = [back_to_the_future,
          iron_eagle,
          iron_man,
          space_camp,
          tron,
          tron_legacy]

#即文件作为脚本直接执行才会被执行，而import到其他脚本中是不会被执行的
if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movies)