#include<bits/stdc++.h>

using namespace std;
int main(){
    int i,j,k,n;
    cout<<"Enter the message: ";
    string s;
    getline(cin,s);
    cout<<"\nEnter the key: ";
    string key;
    cin>>key;
    for(i=0;i<s.size();i++){
        if(s[i]==' '){//
            s.erase(s.begin() + i);
            i--;
        }
    }

    vector<vector<char> > a(5,vector<char>(5,' '));
    vector<int> alpha(26,0);
    alpha[9] = 1;//hide j

    vector<char> cleanKey;
    for(int i=0; i<key.size(); i++){
        if(alpha[key[i]-97] == 0){
            cleanKey.push_back(key[i]);
            alpha[key[i]-97]++;
        }
    }
    sort(cleanKey.begin(), cleanKey.end());

    int pt=0, tra=0;
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            if(pt<cleanKey.size())
                a[i][j] = cleanKey[pt++];
            else{
                while(alpha[tra] != 0) tra++;//find next 0
                alpha[tra] ++;
                a[i][j] = (char)(tra+97);
            }
        }
    }

    cout<<endl<<"Key Matrix\n";
    n=5;
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }

    string encr, decr;
    for(i=0;i<s.size()-1;i++){
        if(s[i]==s[i+1])
            s.insert(i+1,"x");
    }

    if(s.size()%2==1)
        s+="x";

    map<char,pair<int,int> > mp2;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            mp2[a[i][j]] = make_pair(i,j);
        }
    }
    
    for(i=0;i<s.size()-1;i+=2){
        int y1 = mp2[s[i]].first;
        int x1 = mp2[s[i]].second;
        int y2 = mp2[s[i+1]].first;
        int x2 = mp2[s[i+1]].second;
        if(y1==y2){
            encr+=a[y1][(x1+1)%5];
            encr+=a[y1][(x2+1)%5];
        }
        else if(x1==x2){
            encr+=a[(y1+1)%5][x1];
            encr+=a[(y2+1)%5][x2];    
        }
        else {
            encr+=a[y1][x2];
            encr+=a[y2][x1];
        }
    }
    cout<<"\nEncrypted Cipher Text :"<<encr<<'\n';

    for(i=0;i<s.size()-1;i+=2){
        int y1 = mp2[encr[i]].first;
        int x1 = mp2[encr[i]].second;
        int y2 = mp2[encr[i+1]].first;
        int x2 = mp2[encr[i+1]].second;
        
        if(y1==y2){
            decr+=a[y1][(x1-1)%5];
            decr+=a[y1][(x2-1)%5];
        }
        else if(x1==x2){
            decr+=a[(y1-1)%5][x1];
            decr+=a[(y2-1)%5][x2];    
        }
        else {
            decr+=a[y1][x2];
            decr+=a[y2][x1];
        }
    }
    cout<<"Decrypted Plain Text :"<<decr<<'\n'<<endl;

    return 0;
}