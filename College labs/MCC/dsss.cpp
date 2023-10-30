#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> ans;
    vector<int> barker = {1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0};
    cout << "Enter Input String: ";
    string n;
    cin >> n;
    vector<int> encrypt;
    for (int i = 0; i < n.size(); i++)
    {
        for (int j = 0; j < 11; j++)
        {
            encrypt.push_back((n[i] - '0') ^ barker[j]);
        }
    }
    cout << "\nEncrypt signal: ";
    for (auto i : encrypt)
        cout << i;

    string op = "";
    int cnt = 0;
    for (int i = 0; i < encrypt.size(); i = i + 11)
    {
        cnt = 0;
        for (int j = 0; j < 11; j++)
        {
            if (encrypt[i + j] ^ barker[j])
                cnt++;
        }
        op += cnt < 4 ? '0' : '1';
    }
    cout << "\n\nDecrpt signal: ";
    cout << op;
}