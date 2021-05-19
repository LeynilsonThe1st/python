#include <iostream>

using namespace std;

int main() {
    long long a, b, n;

    cin >> a >> b;
    n = abs(a - b) + 1;
    cout << ((a + b) * n) / 2 << endl;
}
