// C++ program to find the missing integer 
// in N numbers when N bits are given 
#include <bits/stdc++.h> 
using namespace std; 
  
class BitInteger { 
private: 
    bool* bits; 
  
public: 
    static const int INTEGER_SIZE = 32; 
  
    BitInteger() 
    { 
        bits = new bool[INTEGER_SIZE]; 
    } 
  
    // Constructor to convert an integer 
    // variable into binary format 
    BitInteger(int value) 
    { 
        bits = new bool[INTEGER_SIZE]; 
  
        for (int j = 0; j < INTEGER_SIZE; j++) { 
  
            // The if statement will shift the 
            // original value j times. 
            // So that appropriate (INTEGER_SIZE - 1 -j)th 
            // bits will be either 0/1. 
            //  (INTEGER_SIZE - 1 -j)th bit for all 
            // j = 0 to INTEGER_SIZE-1 corresponds 
            // to  LSB to MSB respectively. 
            if (((value >> j) & 1) == 1) 
                bits[INTEGER_SIZE - 1 - j] = true; 
            else
                bits[INTEGER_SIZE - 1 - j] = false; 
        } 
    } 
    // Constructor to convert a 
    // string into binary format. 
    BitInteger(string str) 
    { 
        int len = str.length(); 
        int x = INTEGER_SIZE - len; 
        bits = new bool[INTEGER_SIZE]; 
  
        // If len = 4. Then x = 32 - 4 = 28. 
        // Hence iterate from 
        // bit 28 to bit 32 and just 
        // replicate the input string. 
        int i = 0; 
  
        for (int j = x; j <= INTEGER_SIZE && i < len; j++, i++) { 
            if (str[i] == '1') 
                bits[j] = true; 
            else
                bits[j] = false; 
        } 
    } 
  
    // this function fetches the kth bit 
    int fetch(int k) 
    { 
        if (bits[k]) 
            return 1; 
  
        return 0; 
    } 
  
    // this function will set a value 
    // of bit indicated by k to given bitValue 
    void set(int k, int bitValue) 
    { 
        if (bitValue == 0) 
            bits[k] = false; 
        else
            bits[k] = true; 
    } 
  
    // convert binary representation to integer 
    int toInt() 
    { 
        int n = 0; 
        for (int i = 0; i < INTEGER_SIZE; i++) { 
            n = n << 1; 
            if (bits[i]) 
                n = n | 1; 
        } 
        return n; 
    } 
}; 
  
// Function to find the missing number 
int findMissingFunc(list<BitInteger>& myList, int column) 
{ 
    // This means that we have processed 
    // the entire 32 bit binary number. 
    if (column < 0) 
        return 0; 
  
    list<BitInteger> oddIndices; 
    list<BitInteger> evenIndices; 
  
    for (BitInteger t : myList) { 
  
        // Initially column = LSB. So 
        // if LSB of the given number is 0, 
        // then the number is even and 
        // hence we add it to evenIndices list. 
        // else if LSB = 0 then add it to oddIndices list. 
        if (t.fetch(column) == 0) 
            evenIndices.push_back(t); 
        else
            oddIndices.push_back(t); 
    } 
  
    // Step 1 and Step 2 of the algorithm. 
    // Here we determine the LSB bit of missing number. 
  
    if (oddIndices.size() >= evenIndices.size()) 
  
        // LSB of the missing number is 0. 
        // Hence it is an even number. 
        // Step 3 and 4 of the algorithm 
        // (discarding all odd numbers) 
        return (findMissingFunc(evenIndices, column - 1)) << 1 | 0; 
  
    else
        // LSB of the missing number is 1. 
        // Hence it is an odd number. 
        // Step 3 and 4 of the algorithm 
        // (discarding all even numbers) 
        return (findMissingFunc(oddIndices, column - 1)) << 1 | 1; 
} 
  
// Function to return the missing integer 
int findMissing(list<BitInteger>& myList) 
{ 
    // Initial call is with given array and LSB. 
    return findMissingFunc(myList, BitInteger::INTEGER_SIZE - 1); 
} 
  
// Driver Code. 
int main() 
{ 
  
    // a corresponds to the input array which 
    // is a list of binary numbers 
    list<BitInteger> a = { BitInteger("0000"), BitInteger("0001"), 
                           BitInteger("0010"), BitInteger("0100"), 
                           BitInteger("0101") }; 
    int missing1 = findMissing(a); 
    cout << missing1 << "\n"; 
  
    return 0; 
} 