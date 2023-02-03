from datetime import datetime
from flask import Flask, render_template
import os, glob

app_f1 = Flask(__name__)


@app_f1.route('/')
def base_page():
    return render_template('base.html')


@app_f1.route('/report')
def built_report():
    onlyfiles = glob.glob('/*/f1 flask/src/files/*')
    with open(onlyfiles[0], 'r') as abb_file:
        abb_dict = {line[:3]: list(line[3:].strip('\n').strip('_').split('_')) for line in abb_file}

    with open(onlyfiles[1], 'r') as end_file:
        end_dict = {line[:3]: line[3:].strip() for line in end_file}

    with open(onlyfiles[2], 'r') as start_file:
        start_dict = {line[:3]: line[3:].strip() for line in start_file}

    time_lap = {}
    format = ('%Y-%m-%d_%H:%M:%S.%f')
    for key in start_dict:
        if key in end_dict:
            start = datetime.strptime(start_dict[key], format)
            end = datetime.strptime(end_dict[key], format)
            r = end - start
            if start > end:
                time_lap[key] = 'DNF'
            else:
                time_lap[key] = str(r)[2:-3]

    time_lap = dict(sorted(time_lap.items(), key=lambda item: item[1]))

    report = {}
    for key, value in time_lap.items():
        if key in abb_dict.keys():
            report[key] = abb_dict[key][0], abb_dict[key][1], value

    return render_template('report.html', report=report)


@app_f1.route('/drivers')
def page_driver(name=None):
    path = os.path.realpath('../links/links.txt')
    full_path = os.path.realpath('..\\files\\abbreviations.txt')
    with open(full_path, 'r') as abb_file:
        abb_dict = {line[:3]: list(line[3:].strip('\n').strip('_').split('_')) for line in abb_file}
    data = abb_dict

    with open(path, 'r') as link_file:
        for k, v in data.items():
            v.append(link_file.readline())

    return render_template('drivers.html', data=data, name=name)


if __name__ == '__main__':
    app_f1.run(debug=True, port=2001)
