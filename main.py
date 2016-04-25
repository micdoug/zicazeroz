from graphs import *
from sys import argv

def parse_input(input):
    try:
        file = open(input, 'r')
    except Exception as e:
        print('Couldn\'t open the input file "{}"'.format(input))
        exit()

    nvolunteers, nfriendships = [int(s) for s in file.readline().split(' ')]
    friendships = ListGraph(nvolunteers)
    for i in range(0, nfriendships):
        orig, dest = [int(s) for s in file.readline().split(' ')]
        friendships.add_edge(orig, dest)
        friendships.add_edge(dest, orig)

    nfocuses = int(file.readline())
    focuses_volunteers  = list(range(1, nvolunteers+1))
    focuses = ['f{}'.format(f) for f in range(1, nfocuses+1)]
    focuses_volunteers += focuses
    contributions = ListGraph(focuses_volunteers)

    for i in range(1, nvolunteers+1):
        line = file.readline().strip()
        if len(line) > 0:
            contributions.add_edge(i, ['f{}'.format(int(f)) for f in line.split(' ')])


    return friendships, contributions, focuses


if __name__ == '__main__':

    # Verificar se foram informados os arquivos de entrada e saída
    if len(argv) != 3:
        print('You need to pass the input and output files as parameters')
        exit()

    # Construindo os grafos a partir do arquivo de entrada
    friendships, contributions, focuses = parse_input(argv[1])

    zica = ZicaZeroZ(friendships, contributions, focuses)
    vparams = zica.get_min_volunteers_graph()
    print(vparams)





