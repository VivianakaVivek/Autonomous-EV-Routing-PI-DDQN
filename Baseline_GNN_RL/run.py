import os
import sys
import pickle
import random
from routing import GNNRLAgent

def main():
    map_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'shared_map.pkl')
    if not os.path.exists(map_path):
        print('Shared map not found!')
        return
        
    with open(map_path, 'rb') as f:
        M = pickle.load(f)
    ga = M['graph_a']
    
    non_cs = [n for n, d in ga.nodes(data=True) if not d.get('is_cs')]
    random.seed(42)
    s = random.choice(non_cs)
    d = random.choice([x for x in non_cs if x != s])
    
    print(f'--- Running GNN-RL (SOTA) Simulation ---')
    print(f'Origin: {s} | Destination: {d}')
    
    agent = GNNRLAgent(1, ga, s, d)
    route = agent.compute_route()
    
    print(f'Computed Route: {route}')
    print('Simulation complete.')

if __name__ == '__main__':
    main()
