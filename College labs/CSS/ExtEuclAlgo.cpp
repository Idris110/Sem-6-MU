#include <bits/stdc++.h>
using namespace std;

int main()
{
    int q, r1, r2, r, t1 = 0, t2 = 1, t, tmp;
    int s1 = 1, s2 = 0, s, smp;

    cout<<"Enter two numbers: ";
    cin>>r1 >>r2;

    cout << "\nq\t"<< "r1\t"<< "r2\t"<< "r\t"<< "t1\t"<< "t2\t"<< "t\t"<< "s1\t"<< "s2\t"<< "s\t" << endl;
    cout << "--------------------------------------------------------------------------"<<endl;
    while (r2 > 0)
    {
        q = r1 / r2;
        r = r1 - q * r2;
        cout << q << "\t" << r1 << "\t" << r2 << "\t" << r << "\t";
        r1 = r2;
        r2 = r;

        t = t1 - q * t2;
        cout << t1 << "\t" << t2 << "\t" << t << "\t";
        t1 = t2;
        t2 = t;
        s = s1 - q * s2;

        cout << s1 << "\t" << s2 << "\t" << s << "\t" << endl;
        smp = s1;
        s1 = s2;
        s2 = s;
    }
    cout << "\t" << r1 << "\t" << r2 <<endl<<endl;
    
    return 0;
}