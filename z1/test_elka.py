from subprocess import Popen, PIPE


def test_01():
    pr = Popen(f'python3 elka.py', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Не указан аргумент "Количество этажей"' in pr.stderr.readlines()[-1].decode('utf-8')


def test_02():
    pr = Popen('python3 elka.py 12', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Не указан аргумент "Путь к файлу"' in pr.stderr.readlines()[-1].decode('utf-8')


def test_03():
    pr = Popen('python3 elka.py result.txt 12', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Аргумент "Количество этажей" должен быть целым числом' in pr.stderr.readlines()[-1].decode('utf-8')


def test_04():
    pr = Popen('python3 elka.py 0 result.txt', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Аргумент "Количество этажей" должен быть больше нуля' in pr.stderr.readlines()[-1].decode('utf-8')


def test_05():
    pr = Popen('python3 elka.py 12 result.csv', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    assert 'Аргумент "Путь к файлу" должен заканчиваться на ".txt"' in pr.stderr.readlines()[-1].decode('utf-8')


def test_11():
    pr = Popen('python3 elka.py 1 result.txt', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    with open('result.txt', 'r') as fr:
        lines = fr.readlines()
        assert """  W
  *
TTTTT
TTTTT""" == ''.join(lines).rstrip()


def test_12():
    pr = Popen('python3 elka.py 2 result.txt', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    with open('result.txt', 'r') as fr:
        lines = fr.readlines()
        assert """   W
   *
@*****
 TTTTT
 TTTTT""" == ''.join(lines).rstrip()


def test_13():
    pr = Popen('python3 elka.py 3 result.txt', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    with open('result.txt', 'r') as fr:
        lines = fr.readlines()
        assert """    W
    *
 @*****
*********@
  TTTTT
  TTTTT""" == ''.join(lines).rstrip()


def test_14():
    pr = Popen('python3 elka.py 23 result.txt', shell=True, stdout=PIPE, stderr=PIPE)
    pr.wait()
    with open('result.txt', 'r') as fr:
        lines = fr.readlines()
        assert """                                            W
                                            *
                                         @*****
                                        *********@
                                     @*************
                                    *****************@
                                 @*********************
                                *************************@
                             @*****************************
                            *********************************@
                         @*************************************
                        *****************************************@
                     @*********************************************
                    *************************************************@
                 @*****************************************************
                *********************************************************@
             @*************************************************************
            *****************************************************************@
         @*********************************************************************
        *************************************************************************@
     @*****************************************************************************
    *********************************************************************************@
 @*************************************************************************************
*****************************************************************************************@
                                          TTTTT
                                          TTTTT""" == ''.join(lines).rstrip()
