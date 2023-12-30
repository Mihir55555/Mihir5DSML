# 4.Develop a recommendation system using Flask that suggests content to users based on their preferences.

from flask import Flask, render_template, request

app = Flask(__name__)
songs = {
    1: {'title': 'song 1', 'category': 'Rock'},
    2: {'title': 'song 2', 'category': 'Pop'},
    3: {'title': 'song 3', 'category': 'Classical'},
    4: {'title': 'song 4', 'category': 'Blues'},
    5: {'title': 'song 5', 'category': 'Electronic music'},
}
def recommend_songs(preferred_category):
    recommendations = []
    for song_id, song in songs.items():
        if song['category'] == preferred_category:
            recommendations.append(song)
    return recommendations


@app.route('/')
def home():
    return 'Welcome to the Music Recommendation System!'

@app.route('/select-preferences', methods=['GET', 'POST'])
def select_preferences():
    if request.method == 'POST':
        preferred_category = request.form.get('category')
        recommendations = recommend_songs(preferred_category)
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('preferences.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)