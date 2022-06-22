#include <cstdio>

using namespace std;

bool isValid(int x[100][100], int N) {
	for (int i = 1; i < N; i++) {
		if (x[0][i] < x[0][i-1]) return false;
	}
	for (int i = 0; i < N; i++) {
		for (int j = 1; j < N; j++) {
			if (x[j][i] < x[j-1][i]) return false;
		}
	}
	return true;
}

int main() {
	int N, g[100][100];
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &g[i][j]);
		}
	}
	while (!isValid(g, N)) {
		int t[100][100];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				t[i][j] = g[j][N - i - 1];
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				g[i][j] = t[i][j];
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%d", g[i][j]);
			if (j < N - 1) printf(" ");
			else printf("\n");
		}
	}
}