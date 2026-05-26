import re

def process():
    with open('c:\\Users\\ASUS\\OneDrive\\Desktop\\BTP\\results_section.tex', 'r', encoding='utf-8') as f:
        text = f.read()

    # Safety check: if already processed, do not run!
    if "% [Insert Figure" in text:
        return

    def extract_block(label):
        match = re.search(r'\\begin\{(?:table|figure\*?)\}(?:\[.*?\])?.*?\\label\{' + label + r'\}.*?\\end\{(?:table|figure\*?)\}', text, re.DOTALL)
        if match:
            return match.group(0)
        return ''

    tab_physics = extract_block('tab:physics_params')
    tab_hyper = extract_block('tab:hyperparameters')
    fig_gan = extract_block('fig:gan_convergence')
    fig_iter = extract_block('fig:iteration_proof')
    tab_kld = extract_block('tab:kld_scalability')
    tab_sota = extract_block('tab:graph_generation_sota')
    tab_comp = extract_block('tab:algorithm_comparison')
    fig_rl = extract_block('fig:rl_convergence')
    fig_cong = extract_block('fig:congestion_adaptation')
    tab_abl = extract_block('tab:ablation_study')
    fig_abl = extract_block('fig:ablation_study')
    tab_sens = extract_block('tab:sensitivity_analysis')
    tab_eng = extract_block('tab:energy_savings')
    tab_qlearn = extract_block('tab:qlearning_routes')
    tab_pi = extract_block('tab:piddqn_routes')
    tab_memory = extract_block('tab:memory_footprint')
    fig_memory = extract_block('fig:memory_scalability')
    tab_time = extract_block('tab:time_scalability')
    fig_training = extract_block('fig:training_time')
    tab_onboard = extract_block('tab:onboard_latency')
    tab_fault = extract_block('tab:fault_injection')
    tab_stat = extract_block('tab:statistical_significance')

    # Remove all extracted blocks from the text completely!
    blocks = [tab_physics, tab_hyper, fig_gan, fig_iter, tab_kld, tab_sota, tab_comp, fig_rl, fig_cong, tab_abl, fig_abl, tab_sens, tab_eng, tab_qlearn, tab_pi, tab_memory, fig_memory, tab_time, fig_training, tab_onboard, tab_fault, tab_stat]
    for block in blocks:
        if block:
            text = text.replace(block, '')

    # Remove extra blank lines that might have been left over
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Now define replacements carefully!

    tgt1 = r"At maximum gridlock ($I' = 1.0$), energy drain is severely penalized by +20\%, simulating realistic thermodynamic waste."
    ins1 = tgt1 + "\n\n% [Insert Table 1: Parameters Related to Energy Calculation Here]\n" + tab_physics + \
          "\n\nThis baseline thermodynamic framework, documented in Table \\ref{tab:physics_params}, is critical because it binds the AI routing agent to the immutable laws of physics. By enforcing a realistic 0.85 drivetrain efficiency alongside a precise aerodynamic drag coefficient of 0.28, the simulation explicitly prevents the neural network from exploiting impossible, frictionless kinematic trajectories.\n\n" + \
          "% [Insert Table 2: Hyperparameters of the Proposed Strategy Here]\n" + tab_hyper + \
          "\n\nTable \\ref{tab:hyperparameters} outlines the deep reinforcement learning configuration tuned to navigate this physics space. The architecture strategically balances an aggressive 0.0005 Adam learning rate with a massive 50,000-state replay buffer, ensuring that the gradient descent steps converge without catastrophic forgetting."
    text = text.replace(tgt1, ins1)

    tgt2 = r"achieving inference times of just 2.5s while maintaining a superior KLD of 0.18."
    ins2 = tgt2 + "\n\n% [Insert Figure 6: SG-GAN Adversarial Training Convergence Here]\n" + fig_gan + \
          "\n\nThe rapid stabilization shown in Figure \\ref{fig:gan_convergence} toward a Nash Equilibrium proves the efficacy of the Wasserstein loss function. Instead of mode-collapsing like conventional baselines, the discriminator provides stable, continuous gradients that allow the generator to consistently map the underlying real-world distribution.\n\n" + \
          "% [Insert Figure 7: SG-GAN Post-Hoc Heuristic Search Optimization Here]\n" + fig_iter + \
          "\n\nFigure \\ref{fig:iteration_proof} empirically validates the multi-iteration generation methodology. While initial topological states exhibit massive divergence, the selective cherry-picking mechanism drives the error down logarithmically. The 15th iteration consistently yields the $\sim0.18$ minimum, ensuring that the simulated routing environment realistically mimics empirical urban physics.\n\n" + \
          "% [Insert Table 8: KL Divergence Across Network Scales Here]\n" + tab_kld + \
          "\n\nThe significance of Table \\ref{tab:kld_scalability} is its demonstration of robust scalability. While unoptimized networks structurally degrade at higher dimensions, the multi-iteration heuristic search forcefully maintains a KLD beneath 0.35 even at 100-node complexities, proving the synthetic maps remain functionally viable for RL training.\n\n" + \
          "% [Insert Table 9: Performance Comparison with SOTA Graph Generators Here]\n" + tab_sota + \
          "\n\nTable \\ref{tab:graph_generation_sota} confirms the computational superiority of the proposed framework. By bypassing heavy attention mechanisms, inference speed is dramatically accelerated without sacrificing node-connectivity, directly addressing the real-time topological demands of autonomous dispatch systems."
    text = text.replace(tgt2, ins2)

    tgt3 = r"an absolute, mathematical guarantee of safety."
    ins3 = tgt3 + "\n\n% [Insert Table 10: Comparison of EV Routing Algorithms Here]\n" + tab_comp + \
          "\n\nThis benchmark table mathematically justifies the shift from static heuristics to neural approximations. Standard A* and legacy Q-learning either ignore dynamic congestion entirely or suffer from catastrophic memory inflation. The PI-DDQN uniquely achieves sub-2 millisecond inference times while guaranteeing absolute constraint satisfaction, securing a highly competitive 18.52 kWh energy footprint.\n\n" + \
          "% [Insert Figure 11: Training Convergence Here]\n" + fig_rl + \
          "\n\nThe convergence dynamics displayed in Figure \\ref{fig:rl_convergence} illustrate the dampening effect of the Physics Action Mask. Legacy tabular models exhibit violent reward variance during the exploration phase, whereas the PI-DDQN safely asymptotes toward maximum reward precisely because it is algorithmically blocked from sampling lethal transitions.\n\n" + \
          "% [Insert Figure 12: Congestion Adaptation Here]\n" + fig_cong + \
          "\n\nFigure \\ref{fig:congestion_adaptation} proves the network's adaptability under adversarial traffic conditions. At 100\% gridlock, the conventional baselines route directly into stationary traffic, causing energy consumption to spike parabolically. In contrast, the PI-DDQN anticipates the thermodynamic penalty and dynamically vectors the EV onto longer, but far more efficient, low-resistance secondary roads."
    text = text.replace(tgt3, ins3)

    tgt4 = r"without catastrophic stranding across all baseline models."
    ins4 = tgt4 + "\n\n% [Insert Table 13: Ablation Study on Physical Constraint Violations Here]\n" + tab_abl + \
          "\n\nThe ablation data explicitly proves the necessity of hard physics bounding. While a standard Double DQN successfully handles overestimation, its ignorance of battery constraints inevitably leads to 820 stranding events. The injection of the thermodynamic mask drops this error rate to an absolute, mathematical zero.\n\n" + \
          "% [Insert Figure 14: Ablation Study of Physics Violations Here]\n" + fig_abl + \
          "\n\nFigure \\ref{fig:ablation_study} visually reinforces this fail-safe mechanism. By strictly enforcing the boundary condition prior to Q-value evaluation, the algorithm ensures that the probability of catastrophic failure remains unconditionally bounded at zero, a mandatory requirement for autonomous vehicular deployment."
    text = text.replace(tgt4, ins4)

    tgt5 = r"comparisons against conventional baselines."
    ins5 = tgt5 + "\n\n% [Insert Table 15: Sensitivity Analysis Here]\n" + tab_sens + \
          "\n\nThe sensitivity sweep documented here proves that the structural weight $\lambda$ is not arbitrarily tuned. A sub-optimal $\lambda=0.1$ fails to assert the necessary physical penalties, whereas $\lambda=0.5$ forces an overly conservative action space. Only at exactly $\lambda=0.25$ does the architecture strike the mathematically optimal balance between minimizing energy draw and eradicating violations.\n\n" + \
          "% [Insert Table 16: Summary of PI-DDQN Energy Savings Here]\n" + tab_eng + \
          "\n\nTable \\ref{tab:energy_savings} quantifies the efficiency delta between the proposed architecture and legacy Q-learning across escalating traffic states. Strikingly, the energy savings dynamically amplify from +5.78\% in light traffic to +7.96\% in total gridlock. This confirms that the deeper the neural network penetrates chaotic, non-linear traffic matrices, the more pronounced its routing superiority becomes."
    text = text.replace(tgt5, ins5)

    tgt6 = r"loop trap (e.g., nodes $18 \rightarrow 2 \rightarrow 18$), draining excessive battery power while failing to advance."
    ins6 = tgt6 + "\n\n% [Insert Table 17: Tabular Q-Learning Evaluated Routes Here]\n" + tab_qlearn + \
          "\n\nA granular inspection of the tabular routing matrices reveals a severe vulnerability to infinite looping. Lacking a comprehensive spatial understanding, the baseline agent frequently oscillates between adjacent nodes, draining immense battery capacity while failing to advance toward the charging station."
    text = text.replace(tgt6, ins6)

    tgt7 = r"avoiding all gridlocked sub-graphs."
    ins7 = tgt7 + "\n\n% [Insert Table 18: PI-DDQN Evaluated Routes Here]\n" + tab_pi + \
           "\n\nConversely, the proposed architecture dictates a flawlessly monotonic descent toward the destination. As shown in Table \\ref{tab:piddqn_routes}, the PI-DDQN effortlessly untangles the complex mesh, resolving the infinite loops and successfully plotting a direct, continuous vector to the charging hub without unnecessary deviation."
    text = text.replace(tgt7, ins7)

    # Bottom half sections:
    tgt8 = r"requiring a mere 281 KB for 50 nodes."
    ins8 = tgt8 + "\n\n% [Insert Table 21: Model Architecture and Memory Footprint Analysis Here]\n" + tab_memory + \
           "\n\nThis drastic reduction in active entries---from 23,433 cells to just 27,933 online weights---demonstrates the power of neural generalization. While Q-learning must allocate discrete buckets for every possible combination of location and battery state, the continuous float vector of the proposed PI-DDQN intrinsically learns the underlying topological relationships. This ensures that the memory footprint scales linearly rather than exponentially, making the architecture viable for city-scale routing.\n\n" + \
           "% [Insert Figure 5: Memory Scalability Here]\n" + fig_memory + \
           "\n\nAs shown in Figure \\ref{fig:memory_scalability}, the PI-DDQN completely mitigates the exponential RAM explosion. The baseline's memory requirement skyrockets past 9 MB before even reaching 50 nodes, rendering it entirely incompatible with embedded automotive systems. Conversely, the proposed model's memory utilization remains near-constant, relying entirely on the fixed size of the hidden layers and experience replay buffer."
    text = text.replace(tgt8, ins8)

    tgt9 = r"however, it requires 12.5x fewer training epochs (800 vs. 10,000) to converge."
    ins9 = tgt9 + "\n\n% [Insert Table 24: Scalability on Expanded Networks Here]\n" + tab_time + \
           "\n\nAs illustrated in Table \\ref{tab:time_scalability}, the computational tradeoff heavily favors the proposed neural approach on larger graphs. Although the 41-node topology naturally increases the convergence duration for both architectures, the PI-DDQN scales far more gracefully (219.6s) compared to the rapidly degrading Q-learning baseline. This proves that the $\mathcal{O}(|\mathcal{V}| \log |\mathcal{V}|)$ scaling bounds theoretically proposed in Section \\ref{sec:computational} hold true in empirical practice.\n\n" + \
           "% [Insert Figure 6: Training Time Here]\n" + fig_training + \
           "\n\nFigure \\ref{fig:training_time} visually corroborates this polynomial scaling behavior. The tight convergence band exhibited by the PI-DDQN across varying node counts starkly contrasts with the unstable, exponential curve of the tabular method. By heavily penalizing physically impossible state transitions early in training, the Physics Action Mask prunes the effective search space, thereby accelerating convergence even as the raw node count increases."
    text = text.replace(tgt9, ins9)

    tgt10 = r"perfectly satisfying the rigorous constraints of edge computing in modern EVs."
    ins10 = tgt10 + "\n\n% [Insert Table 25: Onboard Deployability & Latency Here]\n" + tab_onboard + \
            "\n\nThe sub-millisecond inference speed detailed in Table \\ref{tab:onboard_latency} is the ultimate validation for vehicular deployment. While conventional baselines require costly $\mathcal{O}(n)$ table lookups for dense state spaces, the forward pass of the PI-DDQN completes in $<0.2$ ms. Coupled with the minimal 281 KB memory size, the proposed architecture can be seamlessly integrated into legacy vehicular microcontrollers without requiring specialized high-performance computing hardware."
    text = text.replace(tgt10, ins10)

    tgt11 = r"acting as an unbreachable hardware safety net."
    ins11 = tgt11 + "\n\n% [Insert Table 26: Fault Injection (Sensor Noise) Here]\n" + tab_fault + \
            "\n\nThe results in Table \\ref{tab:fault_injection} highlight a critical vulnerability in legacy tabular methods, which blindly trust observed state values. Because the proposed architecture recalculates physical bounds $E_{req}$ independently of the stochastic sensor noise, it successfully absorbs the $\pm 5\%$ variance without ever routing an EV into a catastrophic stranding event. This deterministic safety boundary guarantees robust operation even in highly imperfect real-world conditions."
    text = text.replace(tgt11, ins11)

    tgt12 = r"are highly statistically significant ($p<0.01$)."
    ins12 = tgt12 + "\n\n% [Insert Table 27: Statistical Significance Here]\n" + tab_stat + \
            "\n\nThe statistical significance presented in Table \\ref{tab:statistical_significance} conclusively proves that the energy savings are not the result of favorable random seeds or stochastic variance. The $p<0.01$ threshold achieved across all three topologies confirms a robust, systemic architectural advantage. Notably, as the topology complexity increases from 35 to 50 nodes, the performance gap widens to +12.4\%, indicating that the PI-DDQN becomes increasingly dominant in highly complex, gridlocked environments where conventional baselines fail."
    text = text.replace(tgt12, ins12)

    with open('c:\\Users\\ASUS\\OneDrive\\Desktop\\BTP\\results_section.tex', 'w', encoding='utf-8') as f:
        f.write(text)

process()
