#include <iostream>

using namespace std;

int main() {
    unsigned int test_cases;

    cin >> test_cases;

    for (unsigned int i = 0; i < test_cases; i++) {
        unsigned int farmers;
        cin >> farmers;

        unsigned long long total = 0;
        for (unsigned int j = 0; j < farmers; j++) {
            unsigned long long size, animals, env_friendly;
            cin >> size >> animals >> env_friendly;

            total += size * env_friendly;
        }

        cout << total << endl;
    }

    return 0;
}