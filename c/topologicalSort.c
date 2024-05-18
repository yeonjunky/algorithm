#include <stdio.h>
#include <stdlib.h>


int dfs(int **graph,int *visited, int *num_edges, int idx, int n){
    visited[idx] = 1;

    for(int i=0;i<n;i++) {
        if(graph[idx][i] && !visited[i]) {
            dfs(graph, visited, num_edges, i, n);
        }
    }

    printf("%d\n", idx);
    return idx;
}

int main(){
    int **graph;
    int *visited;
    int *num_edges;
    int n, v, e;
    // n == number of vertices
    n = 8;


    graph = (int**) malloc(sizeof(int*) * n);
    visited = (int*) calloc(n, sizeof(int));
    num_edges = (int*) calloc(n, sizeof(int));

    for(int i=0;i<n;i++) {
        graph[i] = (int*) calloc(n, sizeof(int));
    }

    graph[0][1] = 1;
    num_edges[1]++;
    graph[0][4] = 1;
    num_edges[4]++;

    graph[1][2] = 1;
    num_edges[2]++;
    graph[1][5] = 1;
    num_edges[5]++;

    graph[2][5] = 1;
    num_edges[5]++;

    graph[4][6] = 1;
    num_edges[6]++;

    graph[5][6] = 1;
    num_edges[6]++;
    graph[5][7] = 1;
    num_edges[7]++;

    printf("graph initialized\n");

    for(int i=0;i<n;i++){
        if(num_edges[i] == 0) {
            dfs(graph, visited, num_edges, i, n);
        }
    }

    for(int i=0;i<n;i++) {
        free(graph[i]);
    }

    free(graph);

    return 0;
}
