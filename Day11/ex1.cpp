#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <map>

void printVector(std::vector<std::string>& V){
    for(auto v : V){
        std::cout << v << " "; 
    }
    std::cout << std::endl;
}


class Day11{

    public:
        Day11(std::string filename);
        void printMap();
        int solution1();

        std::map<std::string, std::vector<std::string>> mapDevices; 

    private:
        void readInput(std::string filename);
        void solution1Loop(std::string input);
        
        int nPaths;
        std::string begin = "you";
        std::string end = "out";
        std::vector<std::string> chain;


};

Day11::Day11(std::string filename){
    readInput(filename);
}

void Day11::readInput(std::string filename){
    std::ifstream file(filename);

    std::string line, input;
    std::vector<std::string> output;
    
    while(file >> line){
    
        if(input.size() < 1){ // First row
            input = line.substr(0,3);
            continue;
        }
        
        if(line.size() == 4 & output.size() > 0){
            mapDevices[input] = output;
            input = line.substr(0,3);
            output = {};    
        }
        else{
            output.push_back(line);
        }
    }
    mapDevices[input] = output; // Last row
}

void Day11::printMap(){
    for(auto &[input, output]: mapDevices){
        std::cout << input << ": ";
        printVector(output);
    }
}

void Day11::solution1Loop(std::string input){

    chain.push_back(input);

    if(input == end){
        printVector(chain);
        nPaths++;
        chain.pop_back();
        return;
    }
    
    for(std::string& o : mapDevices[input]){
        if(o == begin){
            continue;
        }
        solution1Loop(o);  // Have to be careful with infinity loops perhaps?
    }
    chain.pop_back();
}

int Day11::solution1(){

    nPaths = 0;
    solution1Loop(begin);

    return nPaths;

}


int main(){

    Day11 test("test1.txt");
    //test.printMap();
    std::cout << "Solution test ex1: " << test.solution1() << std::endl;

    Day11 final("input.txt");
    std::cout << "Solution final ex1: " << final.solution1() << std::endl;

    return 1;
}