from flask import Flask, render_template, request, url_for, redirect, jsonify
from fetch_req import req_castle, req_house, convert_to_int, req_character, req_episode, req_season, req_api
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
res = [""]
req_string = "https://omarko-got-api/"

'''Route to Home Page'''


@app.errorhandler(404)
def page_not_found(error):
    return ('404 NOT FOUND', 404)


@app.route("/home/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def home():
    res[0] = req_castle(119)
    res[0] = json.dumps(res[0], indent=1)
    return render_template('home.html', html_res=res[0])


@app.route("/documentation/", methods=['GET', 'POST'])
def documentation():
    return render_template('documentation.html')


@app.route("/about/", methods=['GET', 'POST'])
def about():
    return render_template('about.html')


'''Route to api page'''


@app.route("/api/", methods=['GET', 'POST'])
def api(data=None, id=None):
    res[0] = req_api()
    return jsonify(res[0])


'''Route to api data'''


@app.route("/castles/", methods=['GET'])
@app.route("/castles/<id>/", methods=['GET'])
def castles(id=None):
    if id != None:
        id = convert_to_int(id)
        if id == 0:
            return ('404 NOT FOUND', 404)

        res[0] = req_castle(id)

        if res[0] == 0:
            return ('404 NOT FOUND', 404)

    else:
        res[0] = req_castle()
        return jsonify(res[0])

    return jsonify(res[0])


'''Route to houses data'''


@app.route("/houses/", methods=['GET'])
@app.route("/houses/<id>/", methods=['GET'])
def houses(id=None):
    if id != None:
        id = convert_to_int(id)
        if id == 0:
            return ('404 NOT FOUND', 404)

        res[0] = req_house(id)

        if res[0] == 0:
            return ('404 NOT FOUND', 404)

    else:
        res[0] = req_house()
        return jsonify(res[0])

    return jsonify(res[0])


@app.route("/characters/", methods=['GET'])
@app.route("/characters/<id>/", methods=['GET'])
def characters(id=None):
    if id != None:
        id = convert_to_int(id)
        if id == 0:
            return ('404 NOT FOUND', 404)

        res[0] = req_character(id)

        if res[0] == 0:
            return ('404 NOT FOUND', 404)

    else:
        res[0] = req_character()
        return jsonify(res[0])

    return jsonify(res[0])


@app.route("/episodes/", methods=['GET'])
@app.route("/episodes/<id>/", methods=['GET'])
def episodes(id=None):
    if id != None:
        id = convert_to_int(id)
        if id == 0:
            return ('404 NOT FOUND', 404)

        res[0] = req_episode(id)

        if res[0] == 0:
            return ('404 NOT FOUND', 404)

    else:
        res[0] = req_episode()
        return jsonify(res[0])

    return jsonify(res[0])


@app.route("/seasons/", methods=['GET'])
@app.route("/seasons/<id>/", methods=['GET'])
def seasons(id=None):
    if id != None:
        id = convert_to_int(id)
        if id == 0:
            return ('404 NOT FOUND', 404)

        res[0] = req_season(id)

        if res[0] == 0:
            return ('404 NOT FOUND', 404)

    else:
        res[0] = req_season()
        return jsonify(res[0])

    return jsonify(res[0])


if __name__ == '__main__':
    app.run(debug=True)
