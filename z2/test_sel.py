from subprocess import Popen, PIPE
import csv


def test_01():
    pr = Popen(f'python3 main.py', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Не указан путь в выходному файлу' in pr.stderr.readlines()[-1].decode('utf-8')


def test_02():
    pr = Popen('python3 main.py result.txt', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Путь в выходному файлу должен заканчиваться на ".csv"' in pr.stderr.readlines()[-1].decode('utf-8')


def test_11():
    pr = Popen('python3 main.py result.csv', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    with open('result.csv') as fr:
        csv_reader = csv.reader(fr, delimiter=';')
        for line in csv_reader:
            assert ['Country', 'CompanyName', 'FullAddress'] == line
            break
