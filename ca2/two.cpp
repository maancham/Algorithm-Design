#include <limits>
#include <iostream>
#include <vector>

using namespace std;


int minimum_cost = numeric_limits<int>::max();


int cost(int inp,int a,int c,int g,int t) {
    if (inp == 'A')
        return a;
    else if (inp == 'C')
        return c;
    else if (inp == 'G')
        return g;
    else
        return t;
}



int main() {
    string chaman,asadi;
    int a,c,g,t;
    int h,hadi,key;
    cin >> chaman >> asadi;
    cin >> a >> c >> g >> t;
    for (int i=0; i<chaman.size(); i++) {
        hadi = i;
        h = 0;
        key = 0;
        while (h < asadi.size()) {
            if((hadi < chaman.size()) && (chaman[hadi] == asadi[h]))
                hadi++;
            else
                key += cost(asadi[h], a, c, g, t);
            h++;
        }
        if (key < minimum_cost)
            minimum_cost = key;
    }
    cout << minimum_cost << endl;
}


