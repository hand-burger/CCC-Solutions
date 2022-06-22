#include <iostream>
#include <algorithm> // for sort and min

using namespace std;

int main() {
    int n;
    cin >> n;
    int freq[2001] = {}, height[4001] = {};
    for (int i = 0, l; i < n; i++) {
        cin >> l;
        freq[l]++;
    }
    for (int i = 1; i <= 2000; i++) {
        for (int j = i; j <= 2000; j++) {
            if (i == j) {
                height[i + j] += freq[i] / 2;
            } else {
                height[i + j] += min(freq[i], freq[j]);
            }
        }
    }
    int ans, maxx = 0;
    for (int i = 1; i <= 4000; i++) {
        if (height[i] == maxx) {
            ans++;
        } else if (height[i] > maxx) {
            ans = 1;
            maxx = height[i];
        }
    }
    cout << maxx << " " << ans << endl;
    return 0;
}