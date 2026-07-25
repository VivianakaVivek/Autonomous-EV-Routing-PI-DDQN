import os
import shutil

ROOT_DIR = r'c:\Users\ASUS\OneDrive\Desktop\BTP'

# 1. Create Evaluation_Scripts and move python scripts
eval_scripts_dir = os.path.join(ROOT_DIR, 'Evaluation_Scripts')
os.makedirs(eval_scripts_dir, exist_ok=True)

scripts_to_move = [
    'generate_baseline_folders.py',
    'generate_baseline_metrics.py',
    'generate_convergence_graph.py',
    'generate_fig6.py',
    'generate_fig6_fast.py',
    'generate_map.py',
    'generate_physics_metrics.py',
    'generate_research_maps.py',
    'profile_overhead.py',
    'run_baseline_simulations.py',
    'comparison_table.py'
]

for script in scripts_to_move:
    src = os.path.join(ROOT_DIR, script)
    if os.path.exists(src):
        shutil.move(src, os.path.join(eval_scripts_dir, script))

# 2. Rename Baseline Folders
baselines = {
    'Clustering_Data': 'Baseline_Clustering',
    'Dijkstra': 'Baseline_Dijkstra',
    'GNN_RL': 'Baseline_GNN_RL',
    'MILP_Solver': 'Baseline_MILP',
    'Metaheuristic': 'Baseline_Metaheuristic',
    'Q-Learning': 'Baseline_QLearning'
}

for old_name, new_name in baselines.items():
    old_path = os.path.join(ROOT_DIR, old_name)
    new_path = os.path.join(ROOT_DIR, new_name)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.rename(old_path, new_path)

# 3. Copy all images from PI_DDQN\Result to Latex Code
result_dir = os.path.join(ROOT_DIR, 'PI_DDQN', 'Result')
latex_dir = os.path.join(ROOT_DIR, 'Latex Code')
if os.path.exists(result_dir):
    for f in os.listdir(result_dir):
        if f.endswith('.png'):
            shutil.copy2(os.path.join(result_dir, f), os.path.join(latex_dir, f))

# 4. Update Latex file paths
latex_file = os.path.join(latex_dir, 'Research_Paper.tex')
if os.path.exists(latex_file):
    with open(latex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace outdated Final RESULT paths with the new local copied image names
    content = content.replace('../Final RESULT/graph_35_nodes.png', '8a_Graph_35_nodes.png')
    content = content.replace('../Final RESULT/graph_43_nodes.png', '8b_Graph_43_nodes.png')
    content = content.replace('../Final RESULT/graph_50_nodes.png', '8c_Graph_50_nodes.png')
    content = content.replace('1b_Iteration_Proof.png', '7_Iteration_Proof.png')
    
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Workspace cleaned up successfully.')
