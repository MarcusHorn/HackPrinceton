#!/usr/bin/env python

from flask import Flask, render_template, request

import find_songs


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/video/<number>')
def show_video(number):
    return render_template('display-video.html', video_num=number)


@app.route('/not-found')
def not_found():
    """
    Supposed to be our 404 page.
    """


@app.route('/find-song/')
def get_song_response():
    """
    A call to the restful api rendering songs.

    Meant to be used in the form:
    <domain>/find-song/?search="spam and eggs"
    <domain>/find-song/?search="The Spanish Inquisition"

    Response is a link to the song corresponding to the
    search.
    """
    search = request.args.get('q', '')
    if request.args.get('to_mp3'):
        return  # the video's audio.
    else:
        link = find_songs.find_song(phrase=search)
        return render_template('display-video.html', video_num=link)


if __name__ == '__main__':
    app.run()
