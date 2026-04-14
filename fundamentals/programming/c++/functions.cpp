#include <iostream>
#include <cmath>
using namespace std;


// User-defined
void greet(){
    cout << "Hello, world!" << endl;
}

int main() {
    
    // built-in function
    double result = sqrt(25.0);
    cout << "Square Root: " << result << endl;

    greet(); // calling user-defined function
    return 0;
}
