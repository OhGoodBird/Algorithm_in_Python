import numpy as np
    
def viterbi(states, obs, start_p, trans_p, emit_p):
    table = np.zeros((len(obs), len(states)))   # shape: Time x State
    path = np.zeros((len(obs)))    # shape: 1 x Time
    
    for idx in range(len(states)):
        table[0][idx] = start_p[states[idx]] * emit_p[states[idx]][obs[0]]
    path[0] = np.argmax(table[0])
        
    #print(table.T)
    for t in range(1, len(obs)):
        for idx_s in range(len(states)):
            max_state = -1
            max_p = -1
            for idx_ss in range(len(states)):
                p = table[t-1][idx_ss] * trans_p[states[idx_ss]][states[idx_s]] * emit_p[states[idx_s]][obs[t]]
                if(p > max_p):
                    max_p = p
                    max_state = idx_ss
            table[t][idx_s] = max_p
            path[t] = np.argmax(table[t])
            
    print(table.T)
    print(path.T)
    
    
def main():
    
    states = ('Healthy', 'Fever')
    observations = ('normal', 'cold', 'dizzy')
    start_probability = {'Healthy': 0.6, 'Fever': 0.4}
    transition_probability = {
        'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
        'Fever' : {'Healthy': 0.4, 'Fever': 0.6},
    }
    emission_probability = {
        'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }
    
    viterbi(states, 
            observations,
            start_probability,
            transition_probability,
            emission_probability)
    
if(__name__ == '__main__'):
    main()
    
