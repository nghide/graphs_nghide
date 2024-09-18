from graphs_nghide import sp

def test_dijkstra():
    graph = {0: {1: 4, 7: 8}, 1: {0: 4, 2: 8, 7: 11}}
    dist, path = sp.dijkstra(graph, 0)
    assert dist[1] == 4
    assert path[1] == 0
