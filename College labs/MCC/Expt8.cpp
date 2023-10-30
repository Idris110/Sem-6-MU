#include<bits/stdc++.h>
using namespace std;

int main()
{
    int numCells, numChannels; 
    cout<<"Enter number of cells in the network: ";
    cin>>numCells;

    cout<<"Enter number of available channels in each cell: ";
    cin>>numChannels;

    int cells[numCells][numChannels];

    for (int i = 0; i < numCells; i++) {
        for (int j = 0; j < numChannels; j++) {
            cells[i][j] = (i + j) % numChannels;
        }
    }

    for (int i = 0; i < numCells; i++) {
        cout<<"\nCell " <<i+1 <<":  ";
        for(int j=0; j<numChannels; j++)
            cout<<cells[i][j]<<", ";
    }

    return 0;
}