# Importing required packages
import numpy as np

# Defining the function, with the intial vector, decay factors, probability matrix transpose, and iterations
def power_pagerank(mat, x_0, c, rounds):
    # This gets length of each row in the matrix
    size = mat.shape[1]
    # This gets the change added to the modified vector
    delta = (1-c)*((np.array([1]*size, dtype='float64'))/size)
    # This keeps running the dot products and adding delta
    for ind in range(rounds):
        x_0 = np.dot(c, np.dot(mat, x_0)) + delta
    # Returns the final values
    return x_0

# main caller
if __name__ == '__main__':
    # WE know the number of nodes in advance, so I set it as such
    lim = 5
    # Intializes a blank array of 0s
    graph = [[0]*lim for n in range(lim)]
    # updates the graph with connections between nodes
    graph[0][1], graph[1][2], graph[1][3], graph[2][-2], graph[3][0], graph[3][-1], graph[-1][2] = 1, 1, 1, 1, 1, 1, 1
    # Converts the graph to a numpy array to make computations more efficient in the future
    graph = np.array(graph)
    # Creates empty graph with same dimensions as previosu graph
    prob_mat = [[0]*lim for n in range(lim)]
    # Updates the prob_mat with the probabilities of transitions between nodes
    for ind in range(len(graph)):
        den = sum(graph[ind])
        for each in range(len(graph[ind])):
            prob_mat[ind][each] += graph[ind][each]/den
    # Converts the prob_mat to a numpy array to make computations more efficient in the future
    prob_mat = np.array(prob_mat)
    # This gets the list of pagerank values
    vals = list(power_pagerank(prob_mat.T, [1/len(prob_mat)]*len(prob_mat), 0.85, 30))
    # Dictionary to store values based on node number
    cor_vals = {}
    # This populates the dictionary with the values, rounded to 4 digits
    for ind in range(len(vals)):
        cor_vals[ind+1] = round(vals[ind], 4)
    # Finally returns the output in a human readbale form!
    print(f"Corresponding pagerank values for each node:\n{cor_vals}")
