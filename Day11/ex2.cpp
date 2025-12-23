#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>

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
        int solution2(std::string _begin, std::string _end);

        std::map<std::string, std::vector<std::string>> mapDevices; 

    private:
        void readInput(std::string filename);
        int solution2Loop(std::string& input);
        
        //int nPaths;
        std::string begin;
        std::string end;
        std::vector<std::string> chain;
        int maximumSize = 1e9;
        

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

int Day11::solution2Loop(std::string& input){

    //chain.push_back(input);
    int nPaths = 0;

    if(input == end){
        nPaths++;
        printVector(chain);
        maximumSize = chain.size();
        chain.pop_back();
        return;
    }

    if(chain.size() > maximumSize){
        chain.pop_back();
        return;
    }
    
    for(std::string& o : mapDevices[input]){
        
        if(o == begin){
            continue;
        }
        solution2Loop(o);

    }
    chain.pop_back();

    return nPaths;
}

int Day11::solution2(std::string _begin, std::string _end){

    begin = _begin;
    end = _end;

    int nPaths = solution2Loop(begin);
    
    return nPaths;

}


int main(){

    //Day11 test("test2.txt");
    //std::cout << "Solution test ex2: " << test.solution2() << std::endl;

    Day11 final("input.txt");
    std::cout << "Solution final ex2: " << final.solution2("svr", "fft") << std::endl;

    return 1;
}