from networkx.algorithms import isomorphism
import networkx as nx

# Створюємо графи G1 та G2
G1 = nx.Graph([(1,2), (2,3), (3,4), (4,1)])
G2 = nx.Graph([(1,4), (4,3), (3,2), (2,1)])

# Функція для модифікації графа G2, щоб зробити його ізоморфним до G1
def modify_graph(G1, G2):
    gm = isomorphism.GraphMatcher(G1,G2)
    if not gm.is_isomorphic():
        for permutation in gm.mapping:
            if permutation is not None:
                G2.add_edge(permutation[0], permutation[1])
    return G2

# Перевіряємо на ізоморфізм графи G1 та G2
if isomorphism.GraphMatcher(G1, G2).is_isomorphic():
    print("Графи G1 та G2 ізоморфні")
else:
    print("Графи G1 та G2 неізоморфні")
    G2 = modify_graph(G1, G2)
    print("Модифікований граф G2: ", G2.edges())
