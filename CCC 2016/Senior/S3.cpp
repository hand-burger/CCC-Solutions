#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

const int maxn = 100000 + 5;
int n, m, xx, a, b, max_d, max_n, ans = 0, ret = 0;
bool pho[maxn];
vector<vi> adj(maxn);

void dfs(int u, int p) {
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            if (pho[v]) {
                pho[u] = true;
            }
        }
    }
}

void dfs(int n, int p, int dis) {
    if (dis > max_d) {
        max_d = dis;
        max_n = n;
    }
    for (int v : adj[n]) {
        if (v != p && pho[v]) {
            dfs(v, n, dis + 1);
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> xx;
        pho[xx] = true;
    }
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    dfs(xx, -1);
    for (int i = 0; i < n; i++) {
        if (pho[i]) {
            ans++;
        }
    }
    dfs(xx, -1, 0);
    dfs(max_n, -1, 0);
    ret += 2 * (ans - 1);
    cout << ret - max_d << "\n";
}